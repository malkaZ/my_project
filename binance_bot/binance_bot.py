import numpy as np
import talib
from binance.client import Client

# Replace with your actual keys
api_key = 'CHm6Hto05kuU72hl5c4hhYkW9pKjGx9CyWq6WkSNaW2f2HCZbrSmiQx5RVUshaua'  # Replace with your API key
secret_key = 'irdF8ZgrR8oE68TsU146BMcxOkUxmWXiOI2UnXPnDR8RHTZzuvxTSENZkdo9pxJi'  # Replace with your Secret key

# Create a Binance client
client = Client(api_key, secret_key)

# Example function to get historical prices and calculate RSI
def get_rsi(symbol, interval='1d', lookback=14):
    # Get historical price data
    klines = client.get_historical_klines(symbol, interval, f"{lookback} days ago UTC")
    close_prices = np.array([float(kline[4]) for kline in klines])  # Closing prices

    # Calculate RSI
    rsi = talib.RSI(close_prices, timeperiod=lookback)
    return rsi

# Example usage
if __name__ == "__main__":
    symbol = 'BTCUSDT'
    rsi = get_rsi(symbol)
    print(f"RSI for {symbol}: {rsi[-1]}")

