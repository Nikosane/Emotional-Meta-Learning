from emotions import Frustration, Curiosity, Boredom
import random

class StrategyController:
    def __init__(self):
        self.frustration = Frustration()
        self.curiosity = Curiosity()
        self.boredom = Boredom()

        # Predefined strategies
        self.strategies = {
            "default": self.default_strategy,
            "explore": self.explore_strategy,
            "radical": self.radical_strategy
        }
        self.current_strategy = "default"

    def update_emotions(self, feedback):
        score = feedback.get("score", 0)
        state = feedback.get("state")

        f = self.frustration.evaluate(score)
        c = self.curiosity.evaluate(state)
        b = self.boredom.evaluate(state)

        if f > 0.7:
            self.current_strategy = "radical"
        elif c > 0.5:
            self.current_strategy = "explore"
        elif b > 0.6:
            self.current_strategy = random.choice(["explore", "radical"])
        else:
            self.current_strategy = "default"

    def select_strategy(self):
        return self.strategies[self.current_strategy]

    def default_strategy(self, state):
        return f"Performing default action on {state}"

    def explore_strategy(self, state):
        return f"Exploring around {state}"

    def radical_strategy(self, state):
        return f"Trying radical change from {state}"
