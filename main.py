import yaml
from learner.task_solver import TaskSolver
from learner.strategy_controller import StrategyController
from tasks.toy_task import ToyTask
from emotions.frustration import Frustration
from emotions.curiosity import Curiosity
from utils.logger import Logger
from utils.visualizer import Visualizer
from memory.experience_buffer import ExperienceBuffer
from memory.emotion_trace import EmotionTrace

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Initialize components
task = ToyTask()
frustration = Frustration(threshold=config["frustration_threshold"])
curiosity = Curiosity()
logger = Logger()
visualizer = Visualizer()
experience_buffer = ExperienceBuffer()
emotion_trace = EmotionTrace()

strategy_controller = StrategyController([frustration, curiosity])
learner = TaskSolver(strategy_controller)

# Training loop
state = task.reset()
for step in range(config["max_steps"]):
    action = learner.act(state)
    new_state, feedback = task.step(action)

    # Log experience
    experience_buffer.add((state, action, new_state, feedback))

    # Evaluate emotions
    frust_intensity = frustration.evaluate(feedback["score"])
    curio_intensity = curiosity.evaluate(new_state)

    # Log emotions
    emotion_trace.log("frustration", frust_intensity, step)
    emotion_trace.log("curiosity", curio_intensity, step)
    visualizer.log_emotion("frustration", frust_intensity)
    visualizer.log_emotion("curiosity", curio_intensity)

    logger.log(f"Step {step}: Action={action}, State={new_state}, Score={feedback['score']}, Frustration={frust_intensity:.2f}, Curiosity={curio_intensity:.2f}")

    state = new_state

# Visualize emotion trends
visualizer.plot_emotions()
