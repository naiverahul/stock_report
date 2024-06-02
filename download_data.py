import os
import yfinance as yf

# Create the data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Download historical data for Nvidia
apple = yf.download("NVDA", start="2015-12-01", end="2024-05-10")

# Save to CSV
apple.to_csv('data/historical_data.csv')
