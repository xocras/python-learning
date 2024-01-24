from question_model import Question
from data import question_data

question_bank = map(lambda q: Question(q), question_data)

