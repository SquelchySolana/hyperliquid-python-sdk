import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import time
from typing import List

import pandas as pd
import numpy as np
import ta
from hyperliquid.info import Info


def interval_to_millis(interval: str) -> int:
    unit = interval[-1]
    value = int(interval[:-1])
    if unit == 'm':
        return value * 60 * 1000
    if unit == 'h':
        return value * 60 * 60 * 1000
    if unit == 'd':
        return value * 24 * 60 * 60 * 1000
    raise ValueError(f"Unsupported interval: {interval}")


def fetch_ohlcv(symbol: str, interval: str, limit: int = 500) -> pd.DataFrame:
    info = Info(skip_ws=True)
    end = int(time.time() * 1000)
    interval_ms = interval_to_millis(interval)
    start = end - interval_ms * limit
    data = info.candles_snapshot(symbol, interval, start, end)
    df = pd.DataFrame(data)
    if df.empty:
        return df
    df['t'] = pd.to_datetime(df['t'], unit='ms')
    df = df.rename(columns={'o': 'open', 'h': 'high', 'l': 'low', 'c': 'close', 'v': 'volume'})
    df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
    return df


def supertrend(df: pd.DataFrame, period: int = 10, multiplier: float = 3.0) -> pd.Series:
    hl2 = (df['high'] + df['low']) / 2
    atr = ta.volatility.average_true_range(df['high'], df['low'], df['close'], window=period, fillna=True)
    upperband = hl2 + multiplier * atr
    lowerband = hl2 - multiplier * atr
    final_ub = upperband.copy()
    final_lb = lowerband.copy()
    for i in range(1, len(df)):
        final_ub[i] = upperband[i] if df['close'][i-1] <= final_ub[i-1] else max(upperband[i], final_ub[i-1])
        final_lb[i] = lowerband[i] if df['close'][i-1] >= final_lb[i-1] else min(lowerband[i], final_lb[i-1])
    st = pd.Series(np.nan, index=df.index)
    in_uptrend = True
    for i in range(1, len(df)):
        if in_uptrend:
            if df['close'][i] < final_lb[i-1]:
                in_uptrend = False
                st[i] = final_ub[i]
            else:
                st[i] = final_lb[i]
        else:
            if df['close'][i] > final_ub[i-1]:
                in_uptrend = True
                st[i] = final_lb[i]
            else:
                st[i] = final_ub[i]
    return st


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df['EMA_9'] = ta.trend.EMAIndicator(df['close'], window=9).ema_indicator()
    df['EMA_21'] = ta.trend.EMAIndicator(df['close'], window=21).ema_indicator()
    df['EMA_50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()

    bb = ta.volatility.BollingerBands(df['close'])
    df['BB_Middle'] = bb.bollinger_mavg()
    df['BB_Upper'] = bb.bollinger_hband()
    df['BB_Lower'] = bb.bollinger_lband()

    df['VWAP'] = ta.volume.VolumeWeightedAveragePrice(
        df['high'], df['low'], df['close'], df['volume']
    ).volume_weighted_average_price()

    df['Supertrend'] = supertrend(df)

    df['Volume_MA'] = df['volume'].rolling(window=20).mean()

    df['RSI_14'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    macd = ta.trend.MACD(df['close'], window_fast=12, window_slow=26, window_sign=9)
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()
    df['MACD_hist'] = macd.macd_diff()

    df['Stoch_RSI'] = ta.momentum.StochRSIIndicator(df['close']).stochrsi()

    df['ATR_12'] = ta.volatility.AverageTrueRange(
        df['high'], df['low'], df['close'], window=12
    ).average_true_range()

    df['OBV'] = ta.volume.OnBalanceVolumeIndicator(df['close'], df['volume']).on_balance_volume()

    high = df['high'].max()
    low = df['low'].min()
    diff = high - low
    levels = {
        'Fib_0': high,
        'Fib_236': high - diff * 0.236,
        'Fib_382': high - diff * 0.382,
        'Fib_5': high - diff * 0.5,
        'Fib_618': high - diff * 0.618,
        'Fib_786': high - diff * 0.786,
        'Fib_1': low,
    }
    for k, v in levels.items():
        df[k] = v

    # VPVR is not available in ta library. A specialized library would be needed.
    return df


def save_to_csv(df: pd.DataFrame, filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

