class Answer:
    def __init__(self, correct):
        self.__correct = correct

    @property
    def correct(self):
        return self.__correct

    @correct.setter
    def correct(self, value):
        self.correct = value


class Picture_Answer(Answer):
    def __init__(self, correct, image):
        self.__answer_image = image

    @property
    def answer_image(self):
        return self.__answer_image

    @answer_image.setter
    def answer_image(self, value):
        self.answer_image = value


class Text_Answer(Answer):
    def __init__(self, correct, text):
        self.__answer_text = text

    @property
    def answer_text(self):
        return self.__answer_text

    @answer_text.setter
    def answer_text(self, value):
        self.answer_text = value
