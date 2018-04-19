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


def main():
    # If there is a load file
    if False:  #os.path.exists(LOAD_FILE):
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
    print("===========\n")
    while 1:
        print("Current config:")
        if school:
            print("School:     " + school.name)
        else:
            print("School:     Not Selected")
        if year:
            print("Year-group: " + school.yeargroup)
        else:
            print("Year-group: Not Selected")
        if category:
            print("Category:   " + category)
        else:
            print("Category:   Not Selected")
        print("To return to this menu, please close the program and then reopen\n")
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
            school = School()
            school.name = name
            if save.schools:
                save.schools = save.schools + school
            else:
                save.schools = [school]
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass

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
