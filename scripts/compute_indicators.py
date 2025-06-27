import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import time
import pandas as pd
import pandas_ta as ta
from hyperliquid.info import Info

INTERVAL_TO_MS = {
    "5m": 5 * 60 * 1000,
    "1h": 60 * 60 * 1000,
    "4h": 4 * 60 * 60 * 1000,
    "1d": 24 * 60 * 1000,
}


def fetch_ohlcv(symbol: str, interval: str, limit: int = 1000) -> pd.DataFrame:
    """Fetch OHLCV data from Hyperliquid."""
    if interval not in INTERVAL_TO_MS:
        raise ValueError(f"Unsupported interval {interval}")
    end_ms = int(time.time() * 1000)
    start_ms = end_ms - INTERVAL_TO_MS[interval] * limit
    info = Info(skip_ws=True)
    data = info.candles_snapshot(symbol, interval, start_ms, end_ms)
    if not data:
        raise RuntimeError("No data returned from API")
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["t"], unit="ms")
    df = df[["timestamp", "o", "h", "l", "c", "v"]]
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
    df.set_index("timestamp", inplace=True)
    return df


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate technical indicators and append them to the DataFrame."""
    df["EMA_9"] = ta.ema(df["close"], length=9)
    df["EMA_21"] = ta.ema(df["close"], length=21)
    df["EMA_50"] = ta.ema(df["close"], length=50)

    bb = ta.bbands(df["close"], length=20)
    df = pd.concat([df, bb], axis=1)

    df["VWAP"] = ta.vwap(df["high"], df["low"], df["close"], df["volume"])
    st = ta.supertrend(df["high"], df["low"], df["close"])
    df = pd.concat([df, st], axis=1)

    df["Volume_MA"] = df["volume"].rolling(20).mean()
    df["RSI_14"] = ta.rsi(df["close"], length=14)
    macd = ta.macd(df["close"], fast=12, slow=26, signal=9)
    df = pd.concat([df, macd], axis=1)

    stoch = ta.stochrsi(df["close"])
    df = pd.concat([df, stoch], axis=1)

    df["ATR_12"] = ta.atr(df["high"], df["low"], df["close"], length=12)
    df["OBV"] = ta.obv(df["close"], df["volume"])

    return df


def add_fibonacci_levels(df: pd.DataFrame) -> pd.DataFrame:
    """Add Fibonacci retracement level columns based on the data range."""
    high = df["high"].max()
    low = df["low"].min()
    diff = high - low
    levels = {
        "Fib_0": high,
        "Fib_0.236": high - diff * 0.236,
        "Fib_0.382": high - diff * 0.382,
        "Fib_0.5": high - diff * 0.5,
        "Fib_0.618": high - diff * 0.618,
        "Fib_0.786": high - diff * 0.786,
        "Fib_1": low,
    }
    for name, value in levels.items():
        df[name] = value
    return df


def run(symbol: str, interval: str, limit: int = 1000, output_dir: str = "output") -> str:
    df = fetch_ohlcv(symbol, interval, limit)
    df = add_indicators(df)
    df = add_fibonacci_levels(df)

    os.makedirs(output_dir, exist_ok=True)
    filename = f"{symbol.lower().replace('/', '')}_{interval}.csv"
    path = os.path.join(output_dir, filename)
    df.reset_index().to_csv(path, index=False)
    return path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch OHLCV data and compute indicators")
    parser.add_argument("symbol", help="Symbol name e.g. HYPE")
    parser.add_argument("interval", choices=list(INTERVAL_TO_MS.keys()), help="Interval")
    parser.add_argument("--limit", type=int, default=1000, help="Number of candles")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()

    out_path = run(args.symbol, args.interval, args.limit, args.output)
    print(f"Saved {out_path}")
