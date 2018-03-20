class Quiz:
    def __init__(self):
        self.__questions = []
        self.__student = None

    @property
    def questions(self):
        return self.__questions

    @questions.setter
    def questions(self, value):
        self.__questions = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value
