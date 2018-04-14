class School:
    def __init__(self, name, year_group):
        self.__name = name
        self.__year_group = year_group

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def year_group(self):
        return self.__year_group

    @year_group.setter
    def year_group(self, value):
        self.__year_group = value


class Year_Group:
    def __init__(self, year):
        self.__year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value
