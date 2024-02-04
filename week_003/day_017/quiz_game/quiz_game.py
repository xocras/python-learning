from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_list = [Question(question) for question in question_data["results"]]

quiz_brain = QuizBrain(question_list)

while True:
    status = quiz_brain.next_question()

    if status == "end":
        break
