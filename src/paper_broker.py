class PaperBroker:
    def __init__(self):
        self.positions = {}
        self.trades = []
        self.total_pnl = 0.0

    def open_position(self, symbol, quantity, price):
        if symbol in self.positions:
            self.positions[symbol] += quantity
        else:
            self.positions[symbol] = quantity
        self.trades.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price})

    def close_position(self, symbol, quantity, price):
        if symbol in self.positions and self.positions[symbol] >= quantity:
            self.positions[symbol] -= quantity
            if self.positions[symbol] == 0:
                del self.positions[symbol]
            pnl = (price - self.get_average_price(symbol)) * quantity
            self.total_pnl += pnl
            self.trades.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price, 'pnl': pnl})
        else:
            raise ValueError("Not enough shares to close the position.")

    def get_average_price(self, symbol):
        total_cost = sum(trade['price'] * trade['quantity'] for trade in self.trades if trade['symbol'] == symbol and trade['type'] == 'buy')
        total_qty = sum(trade['quantity'] for trade in self.trades if trade['symbol'] == symbol and trade['type'] == 'buy')
        return total_cost / total_qty if total_qty > 0 else 0

    def get_performance_statistics(self):
        total_trades = len(self.trades)
        avg_pnl = self.total_pnl / total_trades if total_trades > 0 else 0
        return {'total_pnl': self.total_pnl, 'total_trades': total_trades, 'avg_pnl': avg_pnl}
