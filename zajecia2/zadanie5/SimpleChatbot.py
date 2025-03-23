class SimpleChatbot:
    def __init__(self, questions):
        self.questions = questions

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            question = self.questions[self.index]
            self.index += 1
            return question
        except IndexError:
            raise StopIteration()
