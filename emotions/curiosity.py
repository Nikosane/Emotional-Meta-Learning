from .base_emotion import BaseEmotion

class Curiosity(BaseEmotion):
    def __init__(self):
        super().__init__()
        self.visited_states = set()

    def evaluate(self, state):
        state_key = str(state)
        if state_key not in self.visited_states:
            self.visited_states.add(state_key)
            self.intensity = 1.0  # high curiosity for novel states
        else:
            self.intensity = 0.0
        return self.intensity
