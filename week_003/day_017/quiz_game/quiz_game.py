from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_list = list(map(lambda q: Question(q), question_data["results"]))

quiz_brain = QuizBrain(question_list)

while True:
    status = quiz_brain.next_question()

    if status == "end":
        break
