class BaseEmotion:
    def __init__(self):
        self.intensity = 0.0

    def evaluate(self, **kwargs):
        """
        Override this method to calculate emotion intensity based on input.
        """
        raise NotImplementedError

    def get_intensity(self):
        return self.intensity
