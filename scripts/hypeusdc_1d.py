import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fetch_utils import fetch_ohlcv, add_indicators, save_to_csv


def main():
    df = fetch_ohlcv("HYPE", "1d")
    if df.empty:
        print("No data returned for 1d interval")
        return
    df = add_indicators(df)
    save_to_csv(df, "output/hypeusdc_1d.csv")


if __name__ == "__main__":
    main()
