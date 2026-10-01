class User:
    def __init__(self, login):
        self.login = login
        self.related_events = []
        self.hours = 0

    def logHours(self):
        pass