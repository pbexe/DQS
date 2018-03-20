import os
import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

from classes.quiz import Quiz
from classes.admin import Admin
from classes.result import Overall_Results, Result
from classes.answer import Picture_Answer, Text_Answer
from classes.school import School, Student, Year_Group
from classes.question import Picture_Question, Text_Question

# Frame switcher based off of code retreived from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter


class App(tk.Tk):
    """The main app class

    Args:
        tk (obj): The tkinter class that the app inherits from
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.state('zoomed')
        self.frames = {}
        self.questions = []
        start = StartPage(parent=container, controller=self)
        self.frames['start'] = start
        start.grid(row=0, column=0, sticky="nsew")

        editor = Editor(parent=container, controller=self)
        self.frames['editor'] = editor
        editor.grid(row=0, column=0, sticky="nsew")

        self.show_frame("start")

        self.LOAD_FILE = "data.quiz"
        if os.path.exists(self.LOAD_FILE):
            pickle.load(open(self.LOAD_FILE, "rb"))
        else:
            query = messagebox.askyesno("No file", "There is no quiz file. Would you like to create a new one?")
            if query == True:
                self.show_frame("editor")
            else:
                self.destroy()


    def start_quiz(self):
        """Starts the quiz
        """

        print("Quiz starting")

        quiz = Quiz()

    def show_frame(self, page_name):
        """Changes which page is being displayed

        Args:
            page_name (str): The key of the page that is going to be displayed
        """

        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    """The starting page of the program

    Args:
        tk (obj): Tkinter frame object
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        start_button = tk.Button(self, text="Begin Quiz",
                                 command=lambda: controller.start_quiz())
        start_button.pack()


class Editor(tk.Frame):
    """The question editor

    Args:
        tk (obj): Tkinter frame object
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Editor",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        for question in controller.questions:
            pass  # write each question


class QuestionView(tk.Frame):
    """The page that a question is displayed on

    Args:
        tk (obj): Tkinter frame object
    """

    def __init__(self, parent, controller, question, type, *args):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
