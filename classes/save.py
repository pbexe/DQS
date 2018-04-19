class Save:
    def __init__(self):
        self.__result = None
        self.__schools = None
        self.__results = None

    @property
    def results(self):
        return self.__results

    @results.setter
    def results(self, value):
        self.__results = value

    @property
    def schools(self):
        return self.__schools

    @schools.setter
    def schools(self, value):
        self.__schools = value

    @property
    def questions(self):
        return self.__questions

    @questions.setter
    def questions(self, value):
        self.__questions = value
