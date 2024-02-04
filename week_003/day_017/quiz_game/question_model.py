import html


class Question:
    def __init__(self, data):
        self.text = html.unescape(data.get("question"))
        self.answer = html.unescape(data.get("correct_answer"))