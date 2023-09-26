import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""Fetch stock data using yfinance"""
def fetch_stock_data(ticker_symbol, period='1y'):
  stock_data = yf.download(ticker_symbol, period=period) 
  return stock_data

def add_rolling_average(dataframe, window=7): #add rolling average to dataframe
  dataframe['Rollingavg'] = dataframe['Close'].rolling(window = window).mean()


def visualize_stock_data(dataframe, title):
  plt.figure(figsize=(14, 7))
  plt.plot(dataframe['Close'], label='Actual Closing Price', linestyle='--')
  plt.title(title)
  plt.xlabel("Date")
  plt.ylabel("Price")
  plt.legend()
  plt.grid(True)
  plt.show()


def main():
  ticker = input("Enter the stock ticker symbol (e.g. GOOGL for Google): ")
  data = fetch_stock_data(ticker)
  add_rolling_average(data)
  visualize_stock_data(data, title=f"{ticker} Stock Data with 7 day rolling average")


if __name__ == "__main__":
  main()