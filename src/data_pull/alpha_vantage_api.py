import requests
from config.api_keys import ALPHA_VANTAGE_API_KEY

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
BASE_URL = 'https://www.alphavantage.co/query?'
#function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=demo'
#r = requests.get(url)
#data = r.json()


#data
def fetch_intraday_stock_data(symbol, interval = '1min', api_key=ALPHA_VANTAGE_API_KEY):
    func = 'TIME_SERIES_INTRADAY'
    outputsize = 'full' # compact, full
    datatype = 'csv' # json, csv
    url = f"{BASE_URL}function={func}&symbol={symbol}&interval={interval}&outputsize={outputsize}&datatype={datatype}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def fetch_daily_stock_data(symbol, api_key=ALPHA_VANTAGE_API_KEY):
    func = 'TIME_SERIES_DAILY'
    outputsize = 'full' # compact, full
    datatype = 'json' # json, csv
    url = f"{BASE_URL}function={func}&symbol={symbol}&outputsize={outputsize}&datatype={datatype}&apikey={api_key}"
    response = requests.get(url)
    return response.json()  

#####CSV
# df = pd.read_csv(csv_data)
# from io import StringIO
# csv_data = StringIO(response.text)
#csv_data = StringIO(response.text)


#####JSON
# response = requests.get(url)
# # Parse the response and extract the data
# data = response.json()
# stock_data = data['Time Series (Daily)']
# # Convert the data to a pandas DataFrame
# df=pd.DataFrame(stock_data).T
# df.index.name = 'Date'

#ticker search

def fetch_symbol_search_data(keywords, api_key=ALPHA_VANTAGE_API_KEY):
    func = 'SYMBOL_SEARCH'
    url = f"https://www.alphavantage.co/query?function={func}&keywords={keywords}&apikey={api_key}"
    response = requests.get(url)
    return response.json()





