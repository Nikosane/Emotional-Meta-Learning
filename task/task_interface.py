
class TaskInterface:
    def reset(self):
        """
        Reset the task environment to initial state.
        """
        raise NotImplementedError

    def step(self, action):
        """
        Apply an action and return the new state and feedback.
        Should return: (state, feedback_dict)
        """
        raise NotImplementedError
