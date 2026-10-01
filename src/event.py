class Event:
    def __init__(self, name, location, time, duration, goal):
        self.name = name
        self.location = location
        self.time = time
        self.duration = duration
        self.goal = goal

    def completed(self):
        pass