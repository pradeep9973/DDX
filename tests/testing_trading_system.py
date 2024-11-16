
from src.utils.stock import Stock, stock_snapshot
from trading.trading_system import TradingSystem
from alphas.alpha import Alpha
from alphas.movingaverage_crossover import MovingAverageCrossoverAlpha
from trading.backtester import BackTest

tsla = Stock('TSLA')

ts = TradingSystem()
tsla_ma = MovingAverageCrossoverAlpha()
bt = BackTest(tsla, tsla_ma, ts)

bt.run_backtest()
print(bt.calculate_performance())
bt.plot_performance()

