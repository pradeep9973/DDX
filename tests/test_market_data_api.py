from src.data_pull.market_data_api import get_candles_from_to

a = get_candles_from_to('s', 'MSFT', '2023-02-03', '2023-02-04', 'D')
print(a)