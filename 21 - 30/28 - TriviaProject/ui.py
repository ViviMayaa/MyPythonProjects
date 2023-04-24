from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # has to tell what type its expects (classQuizBrain) so it can autocomplete and find the methods
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_layout = Label()
        self.score_layout.config(text=f'Score: {self.score}', bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_layout.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(bg='white', height=250, width=300)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Hi",
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'))

        self.canvas.grid(column=0, row=1, columnspan=2)

        mark_yes_image = PhotoImage(file="images/true.png")
        mark_yes = Button(image=mark_yes_image, highlightthickness=0, command=self.score_layout_yes)
        mark_yes.grid(column=0, row=2)

        mark_no_image = PhotoImage(file="images/false.png")
        mark_no = Button(image=mark_no_image, highlightthickness=0, command=self.score_layout_no)
        mark_no.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def score_layout_yes(self):
        if self.quiz.check_answer_yes():
            self.score += 1
            self.score_layout.config(text=f'Score: {self.score}')
            self.got_it_right()
        else:
            self.got_it_wrong()

    def score_layout_no(self):
        if self.quiz.check_answer_no():
            self.score += 1
            self.score_layout.config(text=f'Score: {self.score}')
            self.got_it_right()
        else:
            self.got_it_wrong()

    def get_next_question(self):
        self.canvas.config(bg='white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def got_it_right(self):
        self.canvas.config(bg='green')
        self.window.after(1000, self.get_next_question)

    def got_it_wrong(self):
        self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

