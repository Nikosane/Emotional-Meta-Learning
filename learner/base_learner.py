class BaseLearner:
    def __init__(self):
        pass

    def observe(self, state):
        raise NotImplementedError

    def act(self):
        raise NotImplementedError

    def learn(self, feedback):
        raise NotImplementedError
