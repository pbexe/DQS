class Result:
    def __init__(self, result, student):
        self.__result = result
        self.__student = student

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value


class Overall_Results:
    def __init__(self, results):
        self.__results = results

    @property
    def results(self):
        return self.__results

    @results.setter
    def results(self, value):
        self.__results = value

    def generate_average(self, school, year_group):
        total = 0
        sum_ = 0
        for result in self.__results:
            if result.student.school == school and result.student.year_group == year_group:
                total += result.result
                sum_ += 1
        return total / sum
