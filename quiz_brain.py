class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.questions_list = qlist
        self.points = 0

    def nextquestion(self):
        question = self.questions_list[self.question_number]
        k = input(f"Q.{self.question_number + 1}: {question.text}. (True\False)?")
        self.question_number += 1
        self.checkquestion(k,question.answer)

    def checkquestion(self, k,question):
        if question == k.capitalize():
            self.points += 1
            print("\n"+rf"Right answer! Your right guesses are {self.points}\{self.question_number} ")
        else:
            print("\n"+rf"Wrong answer! Your right guesses are {self.points}\{self.question_number} ")
        print(f"The correct answer was {question}")
        