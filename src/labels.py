class LabelGenerator:
    def __init__(self, threshold):
        self.threshold = threshold

    def generate_label(self, forward_price_return):
        if forward_price_return > self.threshold:
            return 'buy'
        elif forward_price_return < -self.threshold:
            return 'sell'
        else:
            return 'hold'
