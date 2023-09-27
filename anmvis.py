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

# Tkinter functions
def fetch_and_plot():
    ticker_symbol = ticker_entry.get()
    stock_data = fetch_stock_data(ticker_symbol)
    add_rolling_average(stock_data)
    visualize_stock_data(stock_data, f"Stock Visualization for {ticker_symbol}")

# GUI setup
app = Tk()
app.title("Stock Visualizer")

# Colors and Styles
bg_color = "#2C3E50"
text_color = "#ECF0F1"
button_color = "#2980B9"
app.configure(bg=bg_color)

label = Label(app, text="Enter Stock Ticker:", fg=text_color, bg=bg_color)
label.pack(padx=20, pady=5)

ticker_entry = Entry(app, bg=text_color, fg=bg_color)
ticker_entry.pack(padx=20, pady=5)

submit_button = Button(app, text="Fetch & Visualize", command=fetch_and_plot, bg=button_color, fg=text_color)
submit_button.pack(padx=20, pady=20)

app.mainloop()