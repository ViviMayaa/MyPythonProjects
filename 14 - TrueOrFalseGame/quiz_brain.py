class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.points = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)? ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_question_answer):
        if user_answer == current_question_answer:
            print("You got it right!")
            self.points += 1
        else:
            print("You got it wrong!")
        print(f"You've got {self.points}/{self.question_number}!\n")

    def final_points(self):
        print(f"You've completed the quiz! \nYou got {self.points}/{self.question_number}")
