import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import Tk, Label, Button, Entry, messagebox, StringVar, Radiobutton

def fetch_stock_data(ticker_symbol, period='1y'):
    stock_data = yf.download(ticker_symbol, period=period)
    return stock_data

def animate(i, data, lines):
    for line, dataframe in zip(lines, data):
        line.set_data(dataframe.index[:i], dataframe['Close'][:i])
    return lines

def visualize_stock_data(dataframes, title, plot_type='line'):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.grid(True)

    lines = []
    for dataframe in dataframes:
        if plot_type == 'line':
            line, = ax.plot_date(dataframe.index, dataframe['Close'], '-')
            lines.append(line)
        elif plot_type == 'bar':
            ax.bar(dataframe.index, dataframe['Close'])

    if plot_type == 'line':
        ani = FuncAnimation(fig, animate, frames=len(dataframes[0]), fargs=(dataframes, lines), repeat=False)
    plt.show()

def fetch_and_plot():
    ticker_symbol = ticker_entry.get()
    try:
        stock_data = fetch_stock_data(ticker_symbol)
        visualize_stock_data([stock_data], f"Stock Visualization for {ticker_symbol}", chart_type_var.get())
    except:
        messagebox.showerror("Error", "Failed to fetch data. Ensure the ticker symbol is valid.")

def compare_stocks():
    ticker1 = ticker_entry1.get()
    ticker2 = ticker_entry2.get()
    if not ticker1 or not ticker2:
        messagebox.showerror("Error", "Please enter ticker symbols for comparison.")
        return

    try:
        stock_data1 = fetch_stock_data(ticker1)
        stock_data2 = fetch_stock_data(ticker2)
        visualize_stock_data([stock_data1, stock_data2], f"{ticker1} vs {ticker2}", chart_type_var.get())
    except:
        messagebox.showerror("Error", "Failed to fetch data. Ensure the ticker symbols are valid.")

# GUI setup
app = Tk()
app.title("Stock Visualizer")

# Colors and Styles
bg_color = "#2C3E50"
text_color = "#ECF0F1"
button_color = "#2980B9"
app.configure(bg=bg_color)

label1 = Label(app, text="Enter First Stock Ticker:", fg=text_color, bg=bg_color)
label1.pack(padx=20, pady=5)
ticker_entry1 = Entry(app, bg=text_color, fg=bg_color)
ticker_entry1.pack(padx=20, pady=5)

label2 = Label(app, text="Enter Second Stock Ticker:", fg=text_color, bg=bg_color)
label2.pack(padx=20, pady=5)
ticker_entry2 = Entry(app, bg=text_color, fg=bg_color)
ticker_entry2.pack(padx=20, pady=5)

# Radiobuttons for chart type
chart_type_var = StringVar()
chart_type_var.set("line")
line_rb = Radiobutton(app, text="Line Chart", variable=chart_type_var, value="line", bg=bg_color, fg=text_color)
line_rb.pack(pady=5)
bar_rb = Radiobutton(app, text="Bar Chart", variable=chart_type_var, value="bar", bg=bg_color, fg=text_color)
bar_rb.pack(pady=5)

compare_button = Button(app, text="Compare", command=compare_stocks, bg=button_color, fg=text_color)
compare_button.pack(padx=20, pady=20)

app.mainloop()