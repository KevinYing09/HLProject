from member import Member
from event import Event


class Organization:
    def __init__(self, purpose):
        self.members = []
        self.events = []
        self.purpose = purpose

    def status(self):
        pass