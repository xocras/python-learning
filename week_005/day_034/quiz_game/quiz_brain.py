from random import shuffle


class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_index = 0
        self.question_list = question_list

        # Randomize order
        shuffle(self.question_list)

    def check_answer(self, answer):
        result = self.question_list[self.question_index].answer == answer

        if result:
            self.score += 1

        self.question_index += 1

        return result

    def next_question(self):
        if self.question_index == len(self.question_list):
            return f"\nFinal Score: {self.score}/{self.question_index}"
        else:
            return f"\nQ.{self.question_index + 1}: {self.question_list[self.question_index].text}"
