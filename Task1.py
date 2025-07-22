import requests
import matplotlib.pyplot as plt

# Replace with your Alpha Vantage API key
API_KEY = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'  
symbol = 'CODTECH IT SOLUTIONS on BSE'  #  Codtech It Solutions on BSE

# Alpha Vantage URL for daily time series data
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'

# API call
response = requests.get(url)
data = response.json()

# Check if data is available
if "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]

    # Sort dates and get the last 30
    dates = sorted(time_series.keys())[-30:]
    closing_prices = [float(time_series[date]['4. close']) for date in dates]

    # Plot using matplotlib
    plt.figure(figsize=(12, 6))
    plt.plot(dates, closing_prices, color='green', marker='o', linestyle='-', label='Close Price')
    plt.title('CODTECH IT SOLUTIONS – Daily Closing Prices (Last 30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print("❌ Error: Unable to fetch data. Please check your API key or request limit.")
