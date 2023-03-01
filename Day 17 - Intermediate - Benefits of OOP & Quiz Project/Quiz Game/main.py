from question_model import Question
from data import complete_data
# from data2 import question_data as question_data2
from quiz_brain import QuizBrain


question_bank = [ ]

# my solution:
# for item in range(len(question_data)):
#     question_text = (question_data[item]['text'])
#     question_answer = (question_data[item]['answer'])
#     question_bank.append(Question(question_text, question_answer))


# tutor solution:
# Final challenge - adding additional data
for question in complete_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print (question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")