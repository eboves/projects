import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

ticket = "TSLA"
data = yf.download(ticket,start='2020-01-01', end="2025-01-01")

data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()



# print("MA 20: ", data["MA20"])


print(data.head())

# print(data.index)

plt.figure(figsize=(12,6))
sns.lineplot(data=data, x=data.index, y=data["MA20"], label='20-Day MA')
sns.lineplot(data=data, x=data.index, y=data["MA50"], label='50-Day MA')
plt.title(f'{ticket} Stock Price & Moving Average')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

data["Daily Return"] = data["Close"].pct_change()
print("Average daily return", round(data["Daily Return"].mean(), 4))
print("Volatility: ", round(data["Daily Return"].std(), 4))

# print(data.info())
# print(data.head())