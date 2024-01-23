from question import Question
from answer import Answer
from JSONtoDatabase import initialise_database
import random
import tkinter as tk
from tkinter import font as tkFont
from tkinter import simpledialog, messagebox
import csv
import os
import json
import random
from question import Question
from answer import Answer
from JSONtoDatabase import initialise_database_again

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Application")
        self.geometry("500x400")  # Larger window size

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, ProfessorModeFrame, StudentModeFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light blue')
        self.controller = controller
        title_font = tkFont.Font(family='Helvetica', size=18, weight='bold')

        tk.Label(self, text="Main Menu", font=title_font, bg='light blue').pack(pady=20)
        tk.Button(self, text="Professor Mode", command=lambda: controller.show_frame(ProfessorModeFrame)).pack(pady=10)
        tk.Button(self, text="Student Mode", command=lambda: controller.show_frame(StudentModeFrame)).pack(pady=10)

class ProfessorModeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light green')
        tk.Label(self, text="Professor Functionalities Here", bg='light green').pack(pady=20)
        tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu)).pack()


class StudentModeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='light yellow')
        self.controller = controller

        self.student_name = None
        self.questions = initialise_database_again()
        random.shuffle(self.questions)
        for q in self.questions:
            random.shuffle(q.answers)
        self.total_questions = 5 #len(self.questions)
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self, text="", bg='light yellow')
        self.question_label.pack(pady=(20, 10))

        self.start_quiz_button = tk.Button(self, text="Start Quiz", command=self.prompt_name_and_start_quiz)
        self.start_quiz_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        self.back_button.pack(pady=10)

        self.option_buttons = []

    def prompt_name_and_start_quiz(self):
        if not self.student_name:
            self.student_name = simpledialog.askstring("Name", "Enter your name", parent=self)
        if self.student_name:
            self.start_quiz_button.pack_forget()

        for _ in range(4):  # Assuming 4 options per question
            btn = tk.Button(self, text="", command=lambda value=_: self.check_answer(value))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(self, text="", bg='light yellow')
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.show_question()
        
    def show_question(self):
        if self.current_question_index < self.total_questions:
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.question)
            for i, btn in enumerate(self.option_buttons):
                btn.config(text=question.answers[i].answer, state='normal', relief=tk.RAISED)
        else:
            self.record_score()
            messagebox.showinfo("Quiz Complete", f"Your score: {self.score}")
            self.questions = initialise_database_again()
            random.shuffle(self.questions)
            for q in self.questions:
                random.shuffle(q.answers)
            self.total_questions = 5 #len(self.questions)
            self.current_question_index = 0
            self.score = 0
            self.controller.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == StudentModeFrame:
            frame.prompt_name_and_start_quiz()

    def check_answer(self, selected_option_index):
        question = self.questions[self.current_question_index]
        correct_index = [i for i, ans in enumerate(question.answers) if ans.answer == question.get_correct_answer()][0]
        
        for i, btn in enumerate(self.option_buttons):
            if i == correct_index:
                btn.config(relief=tk.GROOVE, highlightbackground="green", highlightcolor="green", highlightthickness=2)
            if i == selected_option_index:
                if i != correct_index:
                    btn.config(relief=tk.GROOVE, highlightbackground="red", highlightcolor="red", highlightthickness=2)

        if question.answers[selected_option_index].answer == question.get_correct_answer():
            self.score += 1
            self.feedback_label.config(text="Correct!")
        else:
            self.feedback_label.config(text="Wrong answer.")
        for btn in self.option_buttons:
            btn.config(state='disabled')

    def next_question(self):
        self.current_question_index += 1
        self.feedback_label.config(text="")
        self.show_question()

    def record_score(self):
        file_exists = os.path.isfile('quiz_scores.csv')
        with open('quiz_scores.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['name', 'score'])  # Header
            writer.writerow([self.student_name, self.score])

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
