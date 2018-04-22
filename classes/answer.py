class Answer:
    """Base class for all types of answer
    """

    def __init__(self, correct):
        """Constructor for `Answer`

        Arguments:
            correct {boolean} -- Whether the answer is correct or not
        """

        self.__correct = correct

    @property
    def correct(self):
        """Returns whether or not the answer is correct

        Returns:
            boolean -- Whether the answer is correct or not
        """

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
        self.__answer_image = value


class Text_Answer(Answer):
    def __init__(self, correct, text):
        self.__answer_text = text

    @property
    def answer_text(self):
        return self.__answer_text

    @answer_text.setter
    def answer_text(self, value):
        self.__answer_text = value
