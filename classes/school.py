class School:
    def __init__(self):
        self.__name = None
        self.__year_groups = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def year_groups(self):
        return self.__year_groups

    @year_groups.setter
    def year_groups(self, value):
        self.__year_groups = value


class Year_Group:
    def __init__(self, year):
        self.__year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value


class Student:
    def __init__(self, school, year_group):
        self.__school = school
        self.__year_group = year_group

    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, value):
        self.__school = value

    @property
    def year_group(self):
        return self.__year_group

    @year_group.setter
    def year_group(self, value):
        self.__year_group = value
