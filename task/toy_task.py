
from .task_interface import TaskInterface
import random

class ToyTask(TaskInterface):
    def __init__(self):
        self.state = 0
        self.goal = 10

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == "Performing default action on 0":
            self.state += 1
        elif action.startswith("Exploring"):
            self.state += random.choice([-1, 1, 2])
        elif action.startswith("Trying radical"):
            self.state += random.choice([-3, 3])

        reward = -abs(self.goal - self.state)
        feedback = {"score": reward, "state": self.state}
        return self.state, feedback
