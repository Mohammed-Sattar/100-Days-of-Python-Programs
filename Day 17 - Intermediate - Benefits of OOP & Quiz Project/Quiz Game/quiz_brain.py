class QuizBrain:
    from question_model import Question

    def __init__(self, question_list):
        """Initializes an object that accepts the question_bank list as an argument and initializes the question number to 0."""
        self.question_number = 0
        # get_question = question_bank[self.question_number]
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

        # more efficient solution:

        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False), or type 'end' to quit: ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        elif user_answer == "End":
            # return False
            self.question_number = len(self.question_list)
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} \n\n")