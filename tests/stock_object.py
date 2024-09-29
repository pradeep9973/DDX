import sys
import os

# Add the parent directory to the system path to allow importing from src.utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the stock module from src.utils
import src.utils.stock as stock

# Create a Stock object for TSLA
tsla = stock.Stock("TSLA")

# Load stock data using yfinance
tsla.load_yfinance()

# Print stock information
print(tsla.get_info())

# Print stock price history using yfinance
print(tsla.get_price_history_yf())

# Print stock price history with a specific interval and period
print("Market_data_api-YTD")
print(tsla.get_price_history(interval="1", period="YTD"))

print("Market_data_api-3min")
print(tsla.get_price_history(interval="3", from_="2024-02-03", to="2024-09-09"))