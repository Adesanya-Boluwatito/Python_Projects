from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:




    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        self.window.config(pady=20, padx=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(14))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, columnspan=2, pady=50)

        self.image_1 = PhotoImage(file="images/false.png")
        self.button_1 = Button(image=self.image_1, highlightthickness=0, command=self.wrong)
        self.button_1.grid(row=2, column=0)

        self.image_2 = PhotoImage(file="images/true.png")
        self.button_2 = Button(image=self.image_2, highlightthickness=0, command=self.right)
        self.button_2.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.button_2.config(state="disabled")
            self.button_1.config(state="disabled")

    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


