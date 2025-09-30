# fintech_starter.py
"""
FinTech starter:
 - Fetch historical prices for a ticker (stock or crypto like BTC-USD)
 - Compute simple moving averages (20 & 50)
 - Save a PNG plot (plot_<TICKER>_YYYYmmdd_HHMMSS.png)
Usage: python fintech_starter.py
"""

import sys
from datetime import datetime

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data(ticker: str, period: str = "6mo"):
    try:
        df = yf.download(ticker, period=period, progress=False)
        if df.empty:
            return None
        return df
    except Exception as e:
        print("Error fetching data:", e)
        return None


def compute_sma(df: pd.DataFrame, windows=(20, 50)) -> pd.DataFrame:
    for w in windows:
        df[f"SMA_{w}"] = df["Close"].rolling(window=w).mean()
    return df


def plot_and_save(df: pd.DataFrame, ticker: str) -> str:
    plt.figure(figsize=(10, 6))
    df["Close"].plot(label="Close", linewidth=1)
    if "SMA_20" in df.columns:
        df["SMA_20"].plot(label="SMA 20", linewidth=1)
    if "SMA_50" in df.columns:
        df["SMA_50"].plot(label="SMA 50", linewidth=1)

    plt.title(f"{ticker} — Close & SMAs")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)

    fname = f"plot_{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.tight_layout()
    plt.savefig(fname)   # always save so Codespaces/Headless works
    try:
        plt.show()       # will work locally if a display is available
    except Exception:
        pass

    print(f"Saved plot to: {fname}")
    return fname


def main():
    print("FinTech Starter — fetch prices & plot basic indicators.")
    ticker = input("Enter ticker (e.g. AAPL or BTC-USD): ").strip().upper()
    if not ticker:
        print("Ticker required.")
        sys.exit(1)
    period = input("Period (default 6mo, examples: 1mo, 6mo, 1y): ").strip() or "6mo"

    df = fetch_data(ticker, period=period)
    if df is None:
        print("No data found for:", ticker)
        sys.exit(1)

    df = compute_sma(df)
    print("\nLatest rows:\n", df[["Close", "SMA_20", "SMA_50"]].tail())
    plot_and_save(df, ticker)


if __name__ == "__main__":
    main()
