from user import User


class Member(User):
    def __init__(self, login, organization, position):
        super().__init__(login)
        self.organization = organization
        self.position = position

    def createEvent(self, name, time):
        pass

    def answerQuestion(self, answer):
        pass
