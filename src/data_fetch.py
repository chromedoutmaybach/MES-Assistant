import pandas as pd
import os

class DataFetcher:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.data = None

    def fetch_data(self, symbol, start_date, end_date):
        # Pseudocode for fetching data
        # Replace with actual data fetching logic
        self.data = self._simulate_data_fetch(symbol, start_date, end_date)
        self.save_to_csv(symbol)

    def _simulate_data_fetch(self, symbol, start_date, end_date):
        # Simulated data generation for the sake of example
        dates = pd.date_range(start=start_date, end=end_date, freq='B')
        return pd.DataFrame({
            'Date': dates,
            'Open': [100 + i for i in range(len(dates))],
            'High': [102 + i for i in range(len(dates))],
            'Low': [98 + i for i in range(len(dates))],
            'Close': [101 + i for i in range(len(dates))],
            'Volume': [1000 + i * 10 for i in range(len(dates))]
        }).set_index('Date')

    def save_to_csv(self, symbol):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        csv_path = os.path.join(self.data_folder, f'{symbol}_data.csv')
        self.data.to_csv(csv_path)

    def load_from_csv(self, symbol):
        csv_path = os.path.join(self.data_folder, f'{symbol}_data.csv')
        if os.path.exists(csv_path):
            self.data = pd.read_csv(csv_path, index_col='Date', parse_dates=True)
        else:
            raise FileNotFoundError(f"CSV file for {symbol} does not exist.")
