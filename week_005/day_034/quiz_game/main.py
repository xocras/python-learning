import requests

from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

VIDEO_GAMES = 15

settings = {
    'amount': 10,
    'category': VIDEO_GAMES,
    'difficulty': 'easy',
    'type': 'boolean'
}

response = requests.get("https://opentdb.com/api.php", settings)

response.raise_for_status()

question_list = [Question(question) for question in response.json()["results"]]

quiz_brain = QuizBrain(question_list)

quiz_ui = QuizInterface(quiz_brain)
