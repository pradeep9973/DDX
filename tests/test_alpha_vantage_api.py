import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.data_pull.alpha_vantage_api import fetch_daily_stock_data, fetch_intraday_stock_data


def test_fetch_stock_data():
    symbol = "AAPL"  # Example stock symbol
    data = fetch_daily_stock_data(symbol)
    assert data is not None, "No data returned"
    assert "results" in data, "No results in response"
    return data
    # print("Stock Data:", data)


def test_fetch_stock_data():
    symbol = "AAPL"  # Example stock symbol
    data = fetch_daily_stock_data(symbol)
    assert data is not None, "No data returned"
    assert "results" in data, "No results in response"
    print("Stock Data:", data)

if __name__ == "__main__":
    test_fetch_stock_data()
#    test_fetch_market_data()

