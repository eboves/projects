import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import customtkinter as ctk



def button_callback():
    # print(f"You entered: {entry.get()}")
    data = yf.download(entry.get(),start='2020-01-01', end="2025-01-01") #Gets the ticket data from Jan 01, 2020 to Jan 01, 2025
    data["MA20"] = data["Close"].rolling(window=20).mean() #This creates a new column named MA20 holding the mean value from the previous 20 days
    data["MA50"] = data["Close"].rolling(window=50).mean() #This creates a new column named MA50 holding the mean value from the previous 50 days

    data["signal"] = data["MA20"] > data["MA50"] #Creates a column named SIGNAL that hold the boolean values when MA20 is greater (Above) than MA50
    data['cross_over'] = data['signal'].ne(data['signal'].shift())

    bullish = data[(data["cross_over"]) & (data['signal'] == True)] # MA20 crosses Above the MA50
    bearish = data[(data["cross_over"]) & (data['signal'] == False)] # MA20 crosses Bellow the MA50

    plt.figure(figsize=(12,6))
    sns.lineplot(data=data, x=data.index, y=data["MA20"], label='20-Day MA')
    sns.lineplot(data=data, x=data.index, y=data["MA50"], label='50-Day MA')
    plt.scatter(bullish.index, bullish["MA20"], color='green', label='Bullish Cross-Over', s=80, zorder=5)
    plt.scatter(bearish.index, bearish["MA20"], color='red', label='Bearish Cross-Over', s=80, zorder=5)
    plt.title(f'{entry.get()} Stock Price & Moving Average with Cross-Over')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

app = ctk.CTk()
app.title("My App")
app.geometry("400x150")

entry = ctk.CTkEntry(master=app, placeholder_text="Enter Ticket: TSLA")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.pack(pady=5)

app.mainloop()
