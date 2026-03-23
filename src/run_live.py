import time
import random  # Simulated data fetching

class LiveTrader:
    def __init__(self, trading_mode='paper'):
        self.trading_mode = trading_mode
        self.position = 0  # Current position in trading

    def fetch_latest_data(self):
        # Simulate fetching the latest market data
        return random.uniform(100, 200)  # Random price for demonstration

    def generate_signal(self, latest_price):
        # Basic signal generation logic (to be improved)
        if latest_price > 150:
            return "sell"
        elif latest_price < 130:
            return "buy"
        return "hold"

    def execute_trade(self, signal):
        # Simulated trade execution
        if self.trading_mode == 'live':
            print(f"Executing {signal} trade in live mode.")
        else:
            print(f"Executing {signal} trade in paper mode.")

    def start_trading(self, interval=10):
        while True:
            latest_price = self.fetch_latest_data()
            signal = self.generate_signal(latest_price)
            self.execute_trade(signal)
            time.sleep(interval)  # Pause for the specified interval

if __name__ == "__main__":
    trader = LiveTrader(trading_mode='paper')
    trader.start_trading(interval=10)  # Fetch data and trade every 10 seconds
