from question_model import Question
from data import question_data
from trivia_brain import TriviaBrain
import random

print("Welcome to Trivia!")
size = int(input("How many questions would you like? (Max: 50): "))
print('\n')

question_bank = []
while len(question_bank) < size:
    question = random.choice(question_data)
    if question not in question_bank:
        question_bank.append(question)

trivia_questions_final = []
for data in question_bank:
    question_text = data['question']
    question_answer = data['correct_answer']
    new_question = Question(question_text, question_answer)
    trivia_questions_final.append(new_question)

quiz = TriviaBrain(trivia_questions_final)

while quiz.still_has_questions():
    quiz.next_question()
    print('\n')

print("Congratulations! You've completed all questions.")
print(f"Your final score was: {quiz.score}/{quiz.q_num}")
