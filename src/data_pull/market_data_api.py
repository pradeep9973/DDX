# Add API KEY to the Token Header or import from a .py file
# Get A Series of Historical Option Quotes from the API

# Example usage:
# get_options_quote_from('IBM', '2023-02-10', 'C', '140', '2023-01-01')

import requests
import pandas as pd
import numpy as np
import io
import json
from datetime import datetime, timedelta
from config.api_keys import MARKET_DATA_API_KEY

class api_token:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.API_KEY}'
        }

api_key = api_token(MARKET_DATA_API_KEY)
headers = api_key.headers

"""
# Authentication

# Your token
token = MARKET_DATA_API_KEY #'your_token_here'

# The API endpoint for retrieving stock quotes for SPY
url = 'https://api.marketdata.app/v1/stocks/quotes/SPY/'

# Setting up the headers for authentication
headers = {
    'Accept': 'application/json', # The format of the response csv or json
    'Authorization': f'Bearer {token}'
}

# Making the GET request to the API
response = requests.get(url, headers=headers)

# Checking if the request was successful
if response. status_code in (200, 203):
    # Parsing the JSON response
    data = response.json()
    print(data)
else:
    print(f'Failed to retrieve data: {response.status_code}')

""" 



""" 
PARAMETERS
File Format : /candles/daily/AAPL?format=json # csv or json
Time format : 
    /candles/daily/AAPL?dateformat=timestamp
    /candles/daily/AAPL?dateformat=unix
    /candles/daily/AAPL?dateformat=spreadsheet
    Keep the default format as unix
Limit : 
    Default Limit: 10,000
    Maximum Limit: 50,000
    /candles/daily/AAPL?limit=10 

"""
# subtract 5 years from the current date
# from_ = str(datetime.now().date() - timedelta(days=5*365))


def fetch_stock_data(symbol, limit = 10000, resolution = "D", from_ = None, to = None, exchange = None, country = None): 
    #Candles
    # Set default values for 'from_' and 'to' if not provided
    if from_ is None:
        from_ = str((datetime.now().date() - timedelta(days=0.9*365)))
    if to is None:
        to = str(datetime.now().date())

    file_format = 'json' # csv or json

    URL = f"https://api.marketdata.app/v1/stocks/candles/{resolution}/{symbol}?from={from_}&to={to}&limit={limit}&format={file_format}"

    # if country is not None:
    #     URL = URL + f"&country={country}"
    # if exchange is not None:
    #     URL = URL + f"&exchange={exchange}"
    
    """
    Required Parameters

    resolution:string
        The duration of each candle.

            Minutely Resolutions: (minutely, 1, 3, 5, 15, 30, 45, ...)
            Hourly Resolutions: (hourly, H, 1H, 2H, ...)
            Daily Resolutions: (daily, D, 1D, 2D, ...)
            Weekly Resolutions: (weekly, W, 1W, 2W, ...)
            Monthly Resolutions: (monthly, M, 1M, 2M, ...)
            Yearly Resolutions:(yearly, Y, 1Y, 2Y, ...)

    symbol:string

        The company's ticker symbol.

    from date

        The leftmost candle on a chart (inclusive). If you use countback, to is not required. Accepted timestamp inputs: ISO 8601, unix, spreadsheet.

    to date

        The rightmost candle on a chart (inclusive). Accepted timestamp inputs: ISO 8601, unix, spreadsheet.

    countback number

        Will fetch a number of candles before (to the left of) to. If you use from, countback is not required.

    """
   
    # response = requests.request("GET", url)
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data for {symbol}")
        print(response.text)
        return None
    df = pd.read_json(response.text)
    df.rename(columns={'t': 'datetime', 'o': 'open','h':'high', 'l':'low','c':'close', 'v': 'volume'}, inplace=True)
    df['datetime'] = pd.to_datetime(df['datetime'], unit='s')
    return df.drop(columns=['s'])
    # print(response.text)
    # url = f"https://api.marketdata.app/v1/candles/daily/{symbol}?format=json&limit={limit}&dateformat={dateformat}"
    

if __name__ == "__main__": 
    pass
    # symbol = "TSLA"  # Example stock symbol
    # data = fetch_stock_data(symbol, resolution="3", limit=50000, from_="2024-02-03",to="2024-09-09")
    # print(data)
    # print("Stock Data:", data)
    # print(data)
    # print(data['results'])
    # print(data['results'][0]['datetime'])
    # print(data['results'][0]['open'])
    # print(data['results'][0]['high'])
    # print(data['results'][0]['low'])
    # print(data['results'][0]['close'])
    # print(data['results'][0]['volume


