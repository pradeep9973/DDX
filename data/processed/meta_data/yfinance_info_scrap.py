import yfinance as yf
import pandas as pd

def fetch_ticker_info(start, end, input_file="../../raw/List_of_companies/TSX_list.csv", output_file="meta_data_TSX.csv"):
    # Read the ticker list CSV
    nyse_data = pd.read_csv(input_file)
    
    # Ensure ticker symbols are in a column named 'Ticker'
    tickers = nyse_data['Symbol'].tolist()[start:end]

    all_ticker_info = []
    
    for ticker in tickers:
        try:
            ticker = ticker.replace(".", "-")
            ticker = ticker + ".TO"
            stock = yf.Ticker(ticker)
            info = stock.info
            info['Ticker'] = ticker  # Add the ticker symbol to the info dictionary
            all_ticker_info.append(info)
            print(f"Fetched data for {ticker}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    # Convert the list of dictionaries to a DataFrame
    df_info = pd.DataFrame(all_ticker_info)

    # Append to the existing meta_data.csv file or create a new one if it doesn't exist
    try:
        existing_data = pd.read_csv(output_file)
        updated_data = pd.concat([existing_data, df_info], ignore_index=True)
        updated_data.to_csv(output_file, index=False)
    except FileNotFoundError:
        df_info.to_csv(output_file, index=False)

if __name__ == "__main__":
    print("This script fetches information about a range of tickers from Yahoo Finance.")
    # Ask the user for the range of tickers to process
    start_num = int(input("Enter the start number: "))
    end_num = int(input("Enter the end number: "))

    # Fetch and store the ticker info for the specified range
    fetch_ticker_info(start_num, end_num)
