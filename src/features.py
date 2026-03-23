import pandas as pd
import numpy as np

class FeatureEngine:
    def __init__(self, data):
        # Expecting data as a DataFrame with a DateTime index
        self.data = data

    def calculate_rsi(self, period=14):
        delta = self.data['Close'].diff()  
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        return self.data['RSI']

    def calculate_macd(self, short_window=12, long_window=26, signal_window=9):
        short_ema = self.data['Close'].ewm(span=short_window, adjust=False).mean()
        long_ema = self.data['Close'].ewm(span=long_window, adjust=False).mean()
        self.data['MACD'] = short_ema - long_ema
        self.data['MACD_Signal'] = self.data['MACD'].ewm(span=signal_window, adjust=False).mean()
        return self.data[['MACD', 'MACD_Signal']]

    def calculate_bollinger_bands(self, period=20, num_std=2):
        rolling_mean = self.data['Close'].rolling(window=period).mean()
        rolling_std = self.data['Close'].rolling(window=period).std()
        self.data['Bollinger_Upper'] = rolling_mean + (rolling_std * num_std)
        self.data['Bollinger_Lower'] = rolling_mean - (rolling_std * num_std)
        return self.data[['Bollinger_Upper', 'Bollinger_Lower']]

    def calculate_returns(self):
        self.data['Returns'] = self.data['Close'].pct_change()
        return self.data['Returns']
    
    def calculate_volatility(self, period=30):
        self.data['Volatility'] = self.data['Returns'].rolling(window=period).std() * np.sqrt(period)
        return self.data['Volatility']

    def calculate_volume_ratios(self):
        self.data['Volume_Ratio'] = self.data['Volume'] / self.data['Volume'].rolling(window=20).mean()
        return self.data['Volume_Ratio']
