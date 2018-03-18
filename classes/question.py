class Question:
    def __init__(self):
        self.__question_text = None

    @property
    def question_text(self):
        return self.__question_text

    @question_text.setter
    def question_text(self, value):
        self.__question_text = value


class Picture_Question(Question):
    def __init__(self):
        super.__init__()
        self.__correct_answer = None
        self.__incorrect_answers = []

    @property
    def correct_answer(self):
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, value):
        self.__correct_answer = value

    @property
    def incorrect_answers(self):
        return self.__incorrect_answers

    @incorrect_answers.setter
    def incorrect_answers(self, value):
        self.__incorrect_answers = value


class Text_Question(Question):
    def __init__(self):
        super.__init__()
        self.__correct_answer = None
        self.__incorrect_answers = []

    @property
    def correct_answer(self):
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, value):
        self.__correct_answer = value

    @property
    def incorrect_answers(self):
        return self.__incorrect_answers

    @incorrect_answers.setter
    def incorrect_answers(self, value):
        self.__incorrect_answers = value
