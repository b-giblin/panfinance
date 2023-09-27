import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import Tk, Label, Button, Entry

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

def fetch_and_plot():
    ticker_symbol = ticker_entry1.get()
    stock_data = fetch_stock_data(ticker_symbol)
    add_rolling_average(stock_data)
    visualize_stock_data(stock_data, f"Stock Visualization for {ticker_symbol}")

def fetch_and_compare():
    ticker1, ticker2 = ticker_entry1.get(), ticker_entry2.get()
    stock_data1 = fetch_stock_data(ticker1)
    stock_data2 = fetch_stock_data(ticker2)
    compare_stock_data(stock_data1, stock_data2, f"Comparison of {ticker1} vs {ticker2}")

def compare_stock_data(dataframe1, dataframe2, title):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_xlim(min(dataframe1.index[0], dataframe2.index[0]), max(dataframe1.index[-1], dataframe2.index[-1]))
    ax.set_ylim(min(dataframe1['Close'].min(), dataframe2['Close'].min()), max(dataframe1['Close'].max(), dataframe2['Close'].max()))
    ax.grid(True)
    ax.plot(dataframe1.index, dataframe1['Close'], label=f'{ticker_entry1.get()} Closing Price', linestyle='--')
    ax.plot(dataframe2.index, dataframe2['Close'], label=f'{ticker_entry2.get()} Closing Price', linestyle='-.')
    ax.legend()
    plt.show()

# GUI setup
app = Tk()
app.title("Stock Visualizer")

# Colors and Styles
bg_color = "#2C3E50"
text_color = "#ECF0F1"
button_color = "#2980B9"
app.configure(bg=bg_color)

# Additional Entry for First Ticker
label1 = Label(app, text="Enter First Ticker:", fg=text_color, bg=bg_color)
label1.pack(padx=20, pady=5)

ticker_entry1 = Entry(app, bg=text_color, fg=bg_color)
ticker_entry1.pack(padx=20, pady=5)

# Additional Entry for Second Ticker
label2 = Label(app, text="Enter Second Ticker:", fg=text_color, bg=bg_color)
label2.pack(padx=20, pady=5)

ticker_entry2 = Entry(app, bg=text_color, fg=bg_color)
ticker_entry2.pack(padx=20, pady=5)

submit_button = Button(app, text="Fetch & Visualize", command=fetch_and_plot, bg=button_color, fg=text_color)
submit_button.pack(padx=20, pady=20)

compare_button = Button(app, text="Compare", command=fetch_and_compare, bg=button_color, fg=text_color)
compare_button.pack(padx=20, pady=20)

app.mainloop()