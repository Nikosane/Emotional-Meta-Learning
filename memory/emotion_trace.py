class EmotionTrace:
    def __init__(self):
        self.history = []

    def log(self, emotion_name, intensity, timestamp):
        self.history.append({
            "emotion": emotion_name,
            "intensity": intensity,
            "timestamp": timestamp
        })

    def get_history(self):
        return self.history

    def get_recent(self, n=10):
        return self.history[-n:]
