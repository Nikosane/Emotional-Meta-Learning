import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        timestamp = datetime.datetime.now().isoformat()
        entry = f"[{timestamp}] {message}"
        self.logs.append(entry)
        print(entry)

    def get_logs(self):
        return self.logs
