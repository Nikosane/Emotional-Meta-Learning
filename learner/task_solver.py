from .base_learner import BaseLearner

class TaskSolver(BaseLearner):
    def __init__(self, strategy_controller):
        super().__init__()
        self.strategy_controller = strategy_controller
        self.state = None

    def observe(self, state):
        self.state = state

    def act(self):
        strategy = self.strategy_controller.select_strategy()
        return strategy(self.state)

    def learn(self, feedback):
        self.strategy_controller.update_emotions(feedback)
