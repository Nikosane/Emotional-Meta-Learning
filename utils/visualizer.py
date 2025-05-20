import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        self.emotion_log = []

    def log_emotion(self, emotion_name, intensity):
        self.emotion_log.append((emotion_name, intensity))

    def plot_emotions(self):
        if not self.emotion_log:
            print("No emotion data to plot.")
            return

        names = [e[0] for e in self.emotion_log]
        intensities = [e[1] for e in self.emotion_log]
        x = list(range(len(self.emotion_log)))

        plt.figure(figsize=(10, 5))
        plt.plot(x, intensities, label='Intensity')
        for i, name in enumerate(names):
            plt.text(i, intensities[i], name, fontsize=8, rotation=45)
        plt.title("Emotion Intensity Over Time")
        plt.xlabel("Steps")
        plt.ylabel("Intensity")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
