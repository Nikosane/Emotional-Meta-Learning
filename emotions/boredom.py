from .base_emotion import BaseEmotion
from collections import deque

class Boredom(BaseEmotion):
    def __init__(self, window_size=10, repetition_threshold=0.8):
        super().__init__()
        self.window_size = window_size
        self.repetition_threshold = repetition_threshold
        self.recent_states = deque(maxlen=window_size)

    def evaluate(self, state):
        state_key = str(state)
        self.recent_states.append(state_key)

        if len(self.recent_states) < self.window_size:
            self.intensity = 0.0
        else:
            most_common = max(set(self.recent_states), key=self.recent_states.count)
            freq = self.recent_states.count(most_common) / self.window_size
            self.intensity = min(1.0, max(0.0, freq - self.repetition_threshold))

        return self.intensity
