from trading.trading_system import TradingSystem
from alphas.alpha import Alpha
from alphas.movingaverage_crossover import MovingAverageCrossoverAlpha
from src.utils.stock import Stock, stock_snapshot
import matplotlib.pyplot as plt

# we are building a backtester that will test the performance of a trading strategy

# class BackTest will take the following parameters:
# 1. stock: Stock object
# 2. alpha: Alpha object
# 3. stock_snapshot: stock_snapshot object
# 4. trading_system: TradingSystem object
# it will use the rolling windows method of stock to make stock_snapshots, 
# and then use the alpha object to calculate the indicator and generate the signal
# then it will use the trading_system object to execute the trades
# it will have a method to calculate the performance of the strategy

class BackTest:
    def __init__(self, stock, alpha, trading_system):
        self.stock = stock
        self.alpha = alpha
        self.trading_system = trading_system
        self.rolling_windows = self.stock.generate_rolling_windows()
        self.stock_snapshots = [stock_snapshot(stock.ticker, window) for window in self.rolling_windows]
        self.buy = 0 
        self.sell = 0

    def run_backtest(self):
        signal = None
        for snapshot in self.stock_snapshots:
            self.alpha.stock_snapshot = snapshot
            old_signal = signal
            signal = self.alpha.generate_signal()
            if signal == 'buy':
                self.buy += 1
                trade_amount = 100
                self.trading_system.execute_order(self.stock.ticker,signal,trade_amount,snapshot.price_data['Close'].iloc[-1])
            elif signal == 'sell':
                self.sell += 1
                trade_amount = 300
                self.trading_system.execute_order(self.stock.ticker,signal,trade_amount,snapshot.price_data['Close'].iloc[-1])
            # if signal != old_signal:
                # self.trading_system.execute_order(self.stock.ticker,signal,100,snapshot.price_data['Close'].iloc[-1])
            # print the order
            print(  f"Order: {signal} {trade_amount} shares of {self.stock.ticker} at {snapshot.price_data['Close'].iloc[-1]}")
        return #signals
    
    def calculate_performance(self):
        print(f"Number of buy signals: {self.buy}, Number of sell signals: {self.sell}")
        return self.trading_system.get_portfolio_networth()
    
    def plot_performance(self):
        plt.plot(self.trading_system.order_book['portfolio_networth'])
        plt.show()
        return

    def __str__(self) -> str:
        return f"BackTest for {self.stock.ticker} using {self.alpha.__class__.__name__} strategy"

