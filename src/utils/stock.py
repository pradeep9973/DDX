"""
This module contains the Stock class, which represents a stock.

"""

import yfinance as yf
from datetime import datetime, timedelta
from src.data_pull.market_data_api import fetch_stock_data
class Stock:
    def __init__(self, ticker):
        self.ticker = ticker        # Stock ticker symbol
        self.name = None            # Company name
        self.industry = None        # Industry sector
        self.sector = None          # Industry sector

# yahoo finance
    def load_yfinance(self):
        """Get the stock data from Yahoo Finance."""
        self.yf = yf.Ticker(self.ticker)

    def get_info(self):
        """get the info from yahoo finance"""
        return self.yf.info
    
    def get_price_history_yf(self, interval="1d", period="5y"):
        """Get the daily price history from Yahoo Finance.
        Returns:
            DataFrame: The daily price history
        Inputs:
            interval (str): The interval of the data (1d, 1wk, 1mo)
            period (str): The period of the data (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        """
        if not hasattr(self, "yf"):
            self.load_yfinance()
        if interval == "1m":
            period = "7d"
            return self.yf.history(interval="1d", period=period)
        return self.yf.history(interval=interval, period=period)
    
    def get_price_history(self, interval="D", period="1Y", from_=None, to=None):
        """
        Returns:
            DataFrame: Stock price history
        Inputs:
            interval (str): 
                Minutely Resolutions: (minutely, 1, 3, 5, 15, 30, 45, ...)
                Hourly Resolutions: (hourly, H, 1H, 2H, ...)
                Daily Resolutions: (daily, D, 1D, 2D, ...)
                Weekly Resolutions: (weekly, W, 1W, 2W, ...)
                Monthly Resolutions: (monthly, M, 1M, 2M, ...)
                Yearly Resolutions:(yearly, Y, 1Y, 2Y, ...)
            Set period to None if you want to get the data from a particular time interval
        """
        def year_to_date():
            """Calculates the number of days from the start of the year to the current date."""
            return (datetime.now() - datetime(datetime.now().year, 1, 1)).days

        period_map = {"Y": 365, "W": 7, "D": 1, "YTD": year_to_date()}

        def separate_int_string(period):
            """Separates the numeric and alphabetic parts of the period string."""
            num = ''.join(filter(str.isdigit, period)) or '1'
            unit = ''.join(filter(str.isalpha, period))
            return int(num), unit

        def get_period_days(period):
            """Converts a period string to the number of days."""
            num, unit = separate_int_string(period)
            return num * period_map[unit]
        if from_ is not None:
            period = None
        if period is not None:
            to = datetime.now().date()
            from_ = to - timedelta(days=get_period_days(period))

        else:
            to = datetime.strptime(to, '%Y-%m-%d').date() if to else datetime.now().date()
            from_ = datetime.strptime(from_, '%Y-%m-%d').date() if from_ else to - timedelta(days=365)

        return fetch_stock_data(self.ticker, resolution=interval, from_=str(from_), to=str(to), limit=50000)
    
    def generate_rolling_windows(self, window_size=60):
        """
        Generate a list of DataFrames, each containing a rolling window of data.
        
        Args:
        data (pd.DataFrame): The original DataFrame.
        window_size (int): The size of each window.
        
        Returns:
        List[pd.DataFrame]: A list of DataFrames, each containing a rolling window of data.
        """
        data = self.get_price_history_yf()
        rolling_windows = []
        for start in range(len(data) - window_size + 1):
            end = start + window_size
            rolling_windows.append(data.iloc[start:end])
        return rolling_windows

                

    def __str__(self):
        """Return a string representation of the stock."""
        return f"{self.name} ({self.ticker}) - Price: {self.price}, Volume: {self.volume}, Market Cap: {self.market_cap}"

# Example usage:
if __name__ == "__main__":
    pass


# class stock_snapshot: it will give a snapshot of a particular window of the stock data, but will have other details as well, it will also have methods to calculate parameters like moving average and other which are helpful for building alphas 

class stock_snapshot:
    def __init__(self, ticker, price_data, ancillary_info = None ):
        self.ticker = ticker
        self.price_data = price_data
        self.ancillary_info = ancillary_info


    def __str__(self):
        """Return a string representation of the stock price data."""
        return f"Stock Data: {self.symbol}, Info: {self.ancillary_info}"



