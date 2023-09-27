import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk

"""Fetch stock data using yfinance"""
def fetch_stock_data(ticker_symbol, period='1y'):
    stock_data = yf.download(ticker_symbol, period=period) 
    return stock_data

def add_rolling_average(dataframe, window=7):
    dataframe['Rollingavg'] = dataframe['Close'].rolling(window=window).mean()

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
    def fetch_and_visualize():
        ticker = ticker_entry.get()
        data = fetch_stock_data(ticker)
        add_rolling_average(data)
        visualize_stock_data(data, title=f"{ticker} Stock Data with 7 day rolling average")

    # Create the tkinter window
    window = tk.Tk()
    window.title("Stock Data Visualization")

    # Set tkinter window background color
    window.configure(bg="#2C3E50")

    #Set tkinter button background color
    button_color = "#355E3B"
    #set tkinter text color
    text_color = "#ECF0F1"

    # Create widgets (labels, entry, button)
    ticker_label = tk.Label(window, text="Enter the stock ticker symbol (e.g. GOOGL for Google): ")
    ticker_entry = tk.Entry(window)
    visualize_button = tk.Button(window, text="Visualize", command=fetch_and_visualize, bg=button_color, fg=text_color)

    # Grid layout for widgets
    ticker_label.grid(row=0, column=0)
    ticker_entry.grid(row=0, column=1)
    visualize_button.grid(row=1, column=0, columnspan=2)

    # Run the tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()