class Question:
    def __init__(self, text, category):
        self.__question_text = text
        self.__question_category = category

    @property
    def question_text(self):
        return self.__question_text

    @question_text.setter
    def question_text(self, value):
        self.__question_text = value

    @property
    def question_category(self):
        return self.__question_category

    @question_category.setter
    def question_category(self, value):
        self.__question_category = value


class Picture_Question(Question):
    def __init__(self, text, correct, incorrect):
        super.__init__(text)
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
    def __init__(self, text, correct, incorrect):
        super.__init__(text)
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
