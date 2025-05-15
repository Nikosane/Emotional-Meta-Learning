from .base_emotion import BaseEmotion

class Frustration(BaseEmotion):
    def __init__(self, threshold=5):
        super().__init__()
        self.threshold = threshold
        self.no_improvement_count = 0
        self.last_score = None

    def evaluate(self, current_score):
        if self.last_score is None:
            self.last_score = current_score
            self.intensity = 0.0
        elif current_score <= self.last_score:
            self.no_improvement_count += 1
        else:
            self.no_improvement_count = 0
        
        self.intensity = min(1.0, self.no_improvement_count / self.threshold)
        self.last_score = current_score
        return self.intensity
