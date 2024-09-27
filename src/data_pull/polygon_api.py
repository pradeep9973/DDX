import requests
from config.api_keys import POLYGON_API_KEY

BASE_URL = "https://api.polygon.io/v2"
#https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey=*

def fetch_stock_data(symbol, api_key=POLYGON_API_KEY):
    url = f"{BASE_URL}/aggs/ticker/{symbol}/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_market_data(symbol, api_key=POLYGON_API_KEY):
    url = f"{BASE_URL}/aggs/ticker/{symbol}/prev?apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

