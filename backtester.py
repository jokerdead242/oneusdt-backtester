import argparse
import pandas as pd
import matplotlib.pyplot as plt
from utils import simple_sma_strategy

def main():
    parser = argparse.ArgumentParser(description="ONE/USDT Backtester")
    parser.add_argument("--csv", type=str, required=True, help="CSV file with candles")
    parser.add_argument("--strategy", type=str, default="sma", help="Strategy type (sma)")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df.set_index('open_time', inplace=True)

    if args.strategy == "sma":
        results = simple_sma_strategy(df)
    else:
        raise ValueError("Unknown strategy")

    print(results.tail())

    plt.figure(figsize=(10,5))
    plt.plot(df['close'], label="Price")
    plt.plot(df['sma_fast'], label="SMA Fast")
    plt.plot(df['sma_slow'], label="SMA Slow")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
