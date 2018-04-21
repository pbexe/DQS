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

    school, year, category = setup(save)

    print("Starting quiz with", school, year, category)


def setup(save):
    """The method run at startup to allow configuration of the quiz

    Arguments:
        save {Save} -- An object that holds all the data for the quiz so that everything can be quickly saved

    Returns:
        tuple -- The school and yeargroup of the person answering the quiz, and the
    """

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
        print()

        if choice == 0:
            if school and year and category:
                return school, year, category
            else:
                print("Please ensure you have entered a school, year and category")

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
            if save.questions:
                q = []
                for question in save.questions:
                    q.append(question.question_category)
                q = list(set(q))
                cat = print_menu("Please select a category", q)
                category = q[cat]
            else:
                print("Please add questions before selecting a category")

        elif choice == 6:
            save.questions = question_editor(save.questions)

        save_data(save)


def question_editor(questions):
    if questions:
        pass
    else:
        questions = []
    while 1:
        choice = print_menu("Would you like to:", ["Add a question", "Delete a question", "Quit the question editor"])
        if choice == 0:
            text = input("Please enter the question: ")
            correct = input("Please enter the correct answer: ")
            incorrect = [input("Please enter an incorrect answer: ") for i in range(0,3)]
            cat = input("Please enter a category: ")
            questions.append(Text_Question(text, correct, incorrect, cat))
        elif choice == 1:
            if len(questions) > 0:
                choice = print_menu("Please select a question to delete:", [q.question_text for q in questions])
                del questions[choice]
            else:
                print("There are no questions to delete")
        else:
            return questions


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
