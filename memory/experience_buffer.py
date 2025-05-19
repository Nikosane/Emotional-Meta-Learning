
from collections import deque

class ExperienceBuffer:
    def __init__(self, capacity=1000):
        self.buffer = deque(maxlen=capacity)

    def add(self, experience):
        self.buffer.append(experience)

    def sample(self, batch_size):
        batch_size = min(batch_size, len(self.buffer))
        return list(self.buffer)[-batch_size:]

    def __len__(self):
        return len(self.buffer)
