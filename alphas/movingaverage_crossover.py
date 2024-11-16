from alphas.alpha import Alpha
import pandas as pd

class MovingAverageCrossoverAlpha(Alpha):
    def calculate_indicator(self):
        # Calculate the 10-day and 50-day moving averages
        short_window = 10
        long_window = 50
        
        short_avg = self.stock_snapshot.price_data['Close'].rolling(window=short_window).mean().iloc[-1]
        long_avg = self.stock_snapshot.price_data['Close'].rolling(window=long_window).mean().iloc[-1]
        
        return short_avg, long_avg

    def generate_signal(self):
        short_avg, long_avg = self.calculate_indicator()
        
        if short_avg > long_avg:
            return "buy"
        elif short_avg < long_avg:
            return "sell"
        return None

# class MeanReversionAlpha(Alpha):
#     def calculate_indicator(self):
#         # Example: Calculate the z-score for mean reversion strategy
#         mean_price = sum(self.stock.data) / len(self.stock.data)
#         current_price = self.stock.data[self.stock.current_day - 1]
#         threshold = self.params.get("z_threshold", 2)
#         return (current_price - mean_price) / mean_price, threshold

#     def generate_signal(self):
#         z_score, threshold = self.calculate_indicator()
        
#         if z_score > threshold:
#             return "sell"
#         elif z_score < -threshold:
#             return "buy"
#         return None