from random import shuffle


class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_index = 0
        self.question_list = question_list

        # Randomize order
        shuffle(self.question_list)

    def check_answer(self, answer):
        result = self.question_list[self.question_index].answer[0].lower() == answer[0]

        print("Correct!" if result else "Wrong!")

        self.score += 1 if result else 0

        return result

    def end_game(self):
        print(f"\nFinal Score: {self.score}/{self.question_index}")
        print("\nGoodbye!")
        return "end"

    def next_question(self):

        if self.question_index == len(self.question_list):
            print("\nYou've reached the end. There are no more questions.")
            return self.end_game()

        answer = input(f"\nQ.{self.question_index + 1}:"
                       f" {self.question_list[self.question_index].text}"
                       f" (True/False):\n\n").lower()

        if answer == "end":
            return self.end_game()

        self.check_answer(answer)

        self.question_index += 1


