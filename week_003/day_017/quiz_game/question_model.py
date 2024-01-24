class Question:
    def __init__(self, data):
        self.text = data.get("text")
        self.answer = data.get("answer")
