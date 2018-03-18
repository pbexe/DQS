import tkinter as tk
from tkinter import font as tkfont

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

        self.frames = {}
        start = StartPage(parent=container, controller=self)
        self.frames['start'] = start
        start.grid(row=0, column=0, sticky="nsew")

        # for F in (StartPage, PageOne, PageTwo):
        #     page_name = F.__name__
        #     frame = F(parent=container, controller=self)
        #     self.frames[page_name] = frame

        #     # put all of the pages in the same location;
        #     # the one on the top of the stacking order
        #     # will be the one that is visible.
        #     frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("start")

    def start_quiz(self):
        """Starts the quiz
        """

        print("Quiz starting")

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


class Question(tk.Frame):
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
