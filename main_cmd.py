import os
import pickle

from classes.quiz import Quiz
from classes.save import Save
from classes.admin import Admin
from classes.result import Overall_Results, Result
from classes.answer import Picture_Answer, Text_Answer
from classes.school import School, Student, Year_Group
from classes.question import Picture_Question, Text_Question

LOAD_FILE = "data.quiz"


def save_data(save_file):
    pickle.dump(save_file, open(LOAD_FILE, "wb"))


def main():
    # If there is a load file
    if os.path.exists(LOAD_FILE):
        # Load it
        save = pickle.load(open(LOAD_FILE, "rb"))
    else:
        # Otherwise create a new save object and make a new save file for it
        save = Save()
        pickle.dump(save, open(LOAD_FILE, "wb"))

    setup(save)


def setup(save):
    school = None
    year = None
    category = None
    print("\nConfig menu")
    print("===========")
    print("To return to this menu, please close the program and then reopen\n")
    while 1:
        print("\nCurrent config:")
        if school:
            print("School:     " + school.name)
        else:
            print("School:     Not Selected")
        if year:
            print("Year-group: " + year.year)
        else:
            print("Year-group: Not Selected")
        if category:
            print("Category:   " + category)
        else:
            print("Category:   Not Selected")
        choice = print_menu("Please choose an option", ["Start Quiz", "Set School", "Add School", "Set Year-group", "Add Year-group", "Set Category", "Edit Questions"])

        if choice == 0:
            if school and year and category:
                pass # Start quiz
        elif choice == 1:
            if save.schools:
                school_choice = print_menu("Please choose a school", [school.name for school in save.schools])
                school = save.schools[school_choice]
            else:
                print("There are currently no schools to pick from. Please add a school to continue")
        elif choice == 2:
            name = input("Please enter the school's name: ")
            school_ = School()
            school_.name = name
            if save.schools:
                save.schools = save.schools + school_
            else:
                save.schools = [school_]
        elif choice == 3:
            if school:
                if school.year_groups:
                    yeargroup_choice = print_menu("Please choose a year-group", [year.year for year in school.year_groups])
                    year = school.year_groups[yeargroup_choice]
                else:
                    print("There are currently no year-groups to pick from with your current choice of school. Please add a yeargroup to continue")
            else:
                print("Please set a school before setting a year-group")
        elif choice == 4:
            if save.schools:
                year_school_choice = print_menu("Please select a school to add a year-group to:", [school.name for school in save.schools])
                school_to_add_year_to = save.schools[year_school_choice]
                name = input("Please enter the year-group name: ")
                year_ = Year_Group(name)
                if school_to_add_year_to.year_groups:
                    school_to_add_year_to.year_groups = school_to_add_year_to.year_groups + year_
                else:
                    school_to_add_year_to.year_groups = [year_]
            else:
                print("Please add a school before adding a year-group")
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        save_data(save)


def print_menu(statement, options):
    """Presents the user with a choice of options and allows the user to pick one

    Arguments:
        statement {str} -- The description of the choice
        options {list} -- The possible options the user can pick

    Returns:
        int -- The index of the option the user picked from the options
    """

    print(statement)
    for i, option in enumerate(options, 1):
        print(str(i) + ". " + option)
    while 1:
        try:
            value = int(input("Please choose an option: "))
            if 0 < value <= len(options):
                return value - 1
            print("Invalid input")
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
