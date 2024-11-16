import yfinance as yf
import pandas as pd
import numpy as np

# Step 1: Load historical data for a specific stock
ticker = 'SPY'  # S&P 500 ETF for example
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
data['Close'].plot(title=f"Closing Prices for {ticker}")

# Step 2: Calculate momentum over a 20-day window
momentum_period = 20
data['Momentum'] = data['Close'].pct_change(momentum_period) * 100

# Step 3: Define entry and exit thresholds
entry_threshold = 5  # Buy when momentum exceeds 5%
exit_threshold = 2    # Sell when momentum falls below 3%

# Step 4: Generate buy/sell signals
data['Signal'] = np.where(data['Momentum'] > entry_threshold, 1, 0)
data['Signal'] = np.where(data['Momentum'] < exit_threshold, -1, data['Signal'])

# Step 5: Implement trading logic
data['Position'] = data['Signal'].replace(to_replace=0, method='ffill')  # Hold position based on last signal
data['Returns'] = data['Close'].pct_change() * data['Position'].shift()

# Step 6: Calculate cumulative returns and analyze performance
data['Cumulative_Returns'] = (1 + data['Returns']).cumprod()
final_return = data['Cumulative_Returns'].iloc[-1] - 1

print(f"Final Cumulative Return of the Strategy: {final_return * 100:.2f}%")
data['Cumulative_Returns'].plot(title='Cumulative Returns of the Momentum Strategy')

# Optional: Print performance metrics
winning_trades = data[data['Returns'] > 0].shape[0]
losing_trades = data[data['Returns'] < 0].shape[0]
win_rate = winning_trades / (winning_trades + losing_trades)

print(f"Win Rate: {win_rate * 100:.2f}%")
print(f"Number of Winning Trades: {winning_trades}")
print(f"Number of Losing Trades: {losing_trades}")
