class SignalEngine:
    def __init__(self, model):
        self.model = model

    def generate_signal(self, data):
        predictions, confidence_scores = self.model.predict(data)
        signals = []

        for prediction, confidence in zip(predictions, confidence_scores):
            if confidence < 0.6:
                signals.append('hold')
            elif prediction == 1:
                signals.append('buy')
            else:
                signals.append('sell')

        return signals

# Example usage:
# model = SomeTrainedModel()
# engine = SignalEngine(model)
# signals = engine.generate_signal(your_data)
