import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

ticket = "TSLA"
data = yf.download(ticket,start='2020-01-01', end="2025-01-01") #Gets the ticket data from Jan 01, 2020 to Jan 01, 2025

data["MA20"] = data["Close"].rolling(window=20).mean() #This creates a new column named MA20 holding the mean value from the previous 20 days
data["MA50"] = data["Close"].rolling(window=50).mean() #This creates a new column named MA50 holding the mean value from the previous 50 days



data["signal"] = data["MA20"] > data["MA50"] #Creates a column named SIGNAL that hold the boolean values when MA20 is greater (Above) than MA50
data['cross_over'] = data['signal'].ne(data['signal'].shift())

bullish = data[(data["cross_over"]) & (data['signal'] == True)] # MA20 crosses Above the MA50
bearish = data[(data["cross_over"]) & (data['signal'] == False)] # MA20 crosses Bellow the MA50


# print(data.index)

plt.figure(figsize=(12,6))
sns.lineplot(data=data, x=data.index, y=data["MA20"], label='20-Day MA')
sns.lineplot(data=data, x=data.index, y=data["MA50"], label='50-Day MA')
plt.scatter(bullish.index, bullish["MA20"], color='green', label='Bullish Cross-Over', s=80, zorder=5)
plt.scatter(bearish.index, bearish["MA20"], color='red', label='Bearish Cross-Over', s=80, zorder=5)
plt.title(f'{ticket} Stock Price & Moving Average with Cross-Over')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# data["Daily Return"] = data["Close"].pct_change()
# print("Average daily return", round(data["Daily Return"].mean(), 4))
# print("Volatility: ", round(data["Daily Return"].std(), 4))










# print(data.columns)

# data["Date"] = pd.to_datetime(data["Date"])
# data = data.set_index("Date")
# print(data.head)
# print(data.tail())
# print(data.loc["2023-07-01":"2023-10-31",["MA20","MA50"]])
# df = data.loc["2023-07-01":"2023-10-31",["MA20","MA50"]]

# df["signal"] = df["MA20"] > df["MA50"]
# df['cross_over'] = df['signal'].ne(df['signal'].shift())

# bullish = df[(df["cross_over"]) & (df['signal'] == True)] # MA20 crosses Above the MA50
# bearish = df[(df["cross_over"]) & (df['signal'] == False)] # MA20 crosses Bellow the MA50

# print(data.info())
# print(data.head())