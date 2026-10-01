from user import User


class Volunteer(User):
    def __init__(self, login, availableTimes):
        super.__init__(login)
        self.availableTimes = availableTimes

    def signUp(self, event):
        pass

    def askQuestion(self, question, organization):
        pass