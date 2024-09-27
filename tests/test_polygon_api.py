
from src.data_pull.polygon_api import fetch_stock_data, fetch_market_data


# tests/test_polygon_api.py

from src.data_pull.polygon_api import fetch_stock_data, fetch_market_data

def test_fetch_stock_data():
    symbol = "AAPL"  # Example stock symbol
    data = fetch_stock_data(symbol)
    assert data is not None, "No data returned"
    assert "results" in data, "No results in response"
    print("Stock Data:", data)

def test_fetch_market_data():
    symbol = "AAPL"
    data = fetch_market_data(symbol)
    assert data is not None, "No data returned"
    assert "results" in data, "No results in response"
    print("Market Data:", data)

if __name__ == "__main__":
    test_fetch_stock_data()
#    test_fetch_market_data()

