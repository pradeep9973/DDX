from abc import ABC, abstractmethod

class Alpha(ABC):
    def __init__(self, stock_snapshot=None, params=None):
        self.stock_snapshot = stock_snapshot
        self.params = params  # Dictionary for flexible parameterization
    
    @abstractmethod
    def calculate_indicator(self):
        """Defines mathematical logic for the strategy"""
        pass
    
    @abstractmethod
    def generate_signal(self):
        """Uses the indicator to generate buy/sell signals"""
        pass


