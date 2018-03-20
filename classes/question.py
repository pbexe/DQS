class Question:
    def __init__(self, text):
        self.__question_text = text

    @property
    def question_text(self):
        return self.__question_text

    @question_text.setter
    def question_text(self, value):
        self.__question_text = value


class Picture_Question(Question):
    def __init__(self, correct, incorrect):
        super.__init__()
        self.__correct_answer = correct
        self.__incorrect_answers = incorrect

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
    def __init__(self, correct, incorrect):
        super.__init__()
        self.__correct_answer = correct
        self.__incorrect_answers = incorrect

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
