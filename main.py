from question_model import Question
from data import question_data
from quiz_brain import *
from time import *
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.question_number != len(quiz.questions_list):
    quiz.nextquestion()

print(f"Congratulations! You managed to guess {quiz.points} answers out of {len(quiz.questions_list)} questions!")
sleep(10)
