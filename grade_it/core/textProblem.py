class TextProblem:
    handled_types = ["text"]
    def __init__(self, specs):
        self.text = specs['text']
        self.ans = specs['ans']

    def problem(self):
        return self.text
    def answer(self):
        return self.ans