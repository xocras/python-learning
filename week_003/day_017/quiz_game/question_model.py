class Question:
    def __init__(self, data):
        self.text = data.get("question").replace("&quot;", "\"")
        self.answer = data.get("correct_answer")
