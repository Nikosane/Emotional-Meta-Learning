# 🧠 Emotional Meta-Learning

Train deep learning models that don't just solve tasks—but adapt how they learn based on simulated emotional feedback like **frustration**, **curiosity**, and **boredom**.

---

## 🚀 Motivation

Most machine learning models optimize for performance alone. But humans learn differently—we adjust **how** we learn based on emotional cues:

* We get **frustrated** when stuck.
* We feel **bored** when things get repetitive.
* We become **curious** when encountering something new.

**Emotional Meta-Learning** brings this flexibility to AI.

---

## 🧠 Simulated Emotions

| Emotion         | Trigger Condition                           | Effect on Learning                              |
| --------------- | ------------------------------------------- | ----------------------------------------------- |
| **Frustration** | Stuck on same error/loss too long           | Aggressive exploration, retry with new strategy |
| **Curiosity**   | Encountering new, unknown states or inputs  | Encourages exploration, deeper analysis         |
| **Boredom**     | Repeating the same inputs/actions over time | Penalizes repetitive strategy, injects noise    |

Each emotion produces a scalar intensity signal ∈ \[0, 1].

---

## 🧬 Architecture

### 1. Task

Agent is given a toy task (e.g., multi-armed bandit, maze, etc.)

### 2. Emotional Evaluation

After each step:

* `Frustration`, `Curiosity`, and `Boredom` levels are calculated
* Stored in `emotion_trace.json`

### 3. Strategy Controller

Learner adapts:

* Exploration rate
* Learning rate
* Optimizer
* Loss weighting

### 4. Memory

Past emotion-task relationships stored for future strategy recall.

---

## 🛠️ Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Training Loop

```bash
python main.py
```

### 3. Configuration

All key parameters (emotion thresholds, task complexity, etc.) are stored in:

```
config/config.yaml
```

---

## 🌊 Example Use-Cases

* **Meta-RL**: Agents that change learning strategies dynamically.
* **AI Tutoring Systems**: Systems that simulate emotions to guide user interaction.
* **Neuroscience-Inspired AI**: Explore cognitive dynamics under simulated emotions.

---

## 🧪 Sample Emotion Trace

```json
{
  "step": 1002,
  "frustration": 0.74,
  "curiosity": 0.32,
  "boredom": 0.12,
  "strategy": "explore_randomly"
}
```

---

## 🔍 Future Extensions

* Train on real-world tasks (e.g., robotics, text generation).
* Add more affective states (e.g., fear, confidence).
* Integrate emotional decay or emotion-to-memory encoding.

---

## 📄 License

MIT License



emg commit1
emg commit2
emg commit3