import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def fetch_stock_data(ticker_symbol, period='1y'):
    stock_data = yf.download(ticker_symbol, period=period) 
    return stock_data

def add_rolling_average(dataframe, window=7):
    dataframe['Rollingavg'] = dataframe['Close'].rolling(window=window).mean()

def animate(i, data, line):
    line.set_data(data.index[:i], data['Close'][:i])
    return line,

def visualize_stock_data(dataframe, title):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_xlim(dataframe.index[0], dataframe.index[-1])
    ax.set_ylim(dataframe['Close'].min(), dataframe['Close'].max())
    ax.grid(True)
    line, = ax.plot_date([], [], '-', label='Actual Closing Price', linestyle='--')
    ax.legend()

    ani = FuncAnimation(fig, animate, frames=len(dataframe), fargs=(dataframe, line), repeat=False)
    plt.show()

def main():
    ticker = input("Enter the stock ticker symbol (e.g. GOOGL for Google): ")
    data = fetch_stock_data(ticker)
    add_rolling_average(data)
    visualize_stock_data(data, title=f"{ticker} Stock Data with 7-day rolling average")

if __name__ == "__main__":
    main()