# 📈 YTD Stock Performance Comparison: TSLA vs META
# Author: Fodé Abass Camara
# Description: Download YTD price data and compare cumulative returns

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# === Parameters ===
tickers = ['TSLA', 'META']
today = pd.to_datetime('2025-05-19')  # You can set this to pd.to_datetime("today") for dynamic date
start_date = pd.to_datetime(f'{today.year}-01-01')

# === Download historical data from Yahoo Finance ===
print("📥 Downloading data...")
data = yf.download(tickers, start=start_date, end=today)

# === Calculate YTD Cumulative Returns ===
data['TSLA YTD Return'] = data['Close']['TSLA'].pct_change().add(1).cumprod().sub(1)
data['META YTD Return'] = data['Close']['META'].pct_change().add(1).cumprod().sub(1)

# === Plot the cumulative returns ===
plt.figure(figsize=(10, 6))
data[['TSLA YTD Return', 'META YTD Return']].plot()
plt.title('TSLA vs META – Year-To-Date (YTD) Cumulative Return')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.legend()
plt.tight_layout()

# === Save the plot ===
plt.savefig('stock_gains.png')
print("✅ Plot saved as 'stock_gains.png'")

