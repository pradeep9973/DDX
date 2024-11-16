import pandas as pd

class TradingSystem:
    def __init__(self):
        self.order_book = pd.DataFrame(columns=['symbol', 'order_type', 'quantity', 'price', 'status','portfolio_networth'])
        self.portfolio = pd.DataFrame(columns=['symbol', 'quantity', 'average_price', "last_traded_price"])
        self.cash = 1000000  # Starting cash balance

    def execute_order(self, symbol, order_type, quantity, price):
        # Check if there is enough cash for buy order
        if order_type == 'buy' and self.cash < quantity * price:
            print("Not enough cash to execute the order")
            return

        # Update order book
        order = {'symbol': symbol, 'order_type': order_type, 'quantity': quantity, 'price': price, 'status': 'executed', 'portfolio_networth': self.get_portfolio_networth()}
        # self.order_book = self.order_book.append(order, ignore_index=True)
        self.order_book = pd.concat([self.order_book, pd.DataFrame(order, index=[0])], ignore_index=True)

        # Update portfolio
        if order_type == 'buy':
            self.cash -= quantity * price
            if symbol in self.portfolio['symbol'].values:
                self.portfolio.loc[self.portfolio['symbol'] == symbol, 'quantity'] += quantity
                total_cost = self.portfolio.loc[self.portfolio['symbol'] == symbol, 'average_price'] * (self.portfolio.loc[self.portfolio['symbol'] == symbol, 'quantity'] - quantity) + quantity * price
                self.portfolio.loc[self.portfolio['symbol'] == symbol, 'average_price'] = total_cost / self.portfolio.loc[self.portfolio['symbol'] == symbol, 'quantity']
                self.portfolio.loc[self.portfolio['symbol'] == symbol, 'last_traded_price'] = price
            else:
                # self.portfolio = self.portfolio.append({'symbol': symbol, 'quantity': quantity, 'average_price': price}, ignore_index=True)
                # use pd.concat instead of append
                self.portfolio = pd.concat([self.portfolio, pd.DataFrame({'symbol': symbol, 'quantity': quantity, 'average_price': price, 'last_traded_price': price}, index=[0])], ignore_index=True)
        elif order_type == 'sell':
            if symbol in self.portfolio['symbol'].values and self.portfolio.loc[self.portfolio['symbol'] == symbol, 'quantity'].values[0] >= quantity:
                self.cash += quantity * price
                self.portfolio.loc[self.portfolio['symbol'] == symbol, 'quantity'] -= quantity
                self.portfolio.loc[self.portfolio['symbol'] == symbol, 'last_traded_price'] = price
                if self.portfolio.loc[self.portfolio['symbol'] == symbol, 'quantity'].values[0] == 0:
                    self.portfolio = self.portfolio[self.portfolio['symbol'] != symbol]
            else:
                print("Not enough shares to execute the sell order")
                return

    def get_portfolio_value(self):
        # return self.cash + sum(self.portfolio['quantity'] * self.portfolio['last_traded_price'])
        return self.cash + sum(self.portfolio['quantity'] * self.portfolio['average_price'])

    def get_portfolio_networth(self):
        return self.cash + sum(self.portfolio['quantity'] * self.portfolio['last_traded_price'])


    def __str__(self):
        return f"Order Book:\n{self.order_book}\n\nPortfolio:\n{self.portfolio}\n\nCash: {self.cash}\n\nTotal Portfolio Value: {self.get_portfolio_value()}"

# Example usage:
# if __name__ == "__main__":
#     ts = TradingSystem()
#     ts.execute_order('AAPL', 'buy', 10, 150)
#     ts.execute_order('AAPL', 'sell', 5, 155)
#     print(ts)