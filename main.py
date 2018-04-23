import os
import xlsxwriter
import time
import pickle
import random
import numpy as np
import matplotlib.pyplot as plt

from classes.quiz import Quiz
from classes.save import Save
from classes.result import Overall_Results, Result
from classes.answer import Picture_Answer, Text_Answer, Answer
from classes.school import School, Student, Year_Group
from classes.question import Picture_Question, Text_Question

LOAD_FILE = "data.quiz"


def clear_screen():
    """Clears the screen
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def save_data(save_file):
    """Saves the quiz data to a file

    Arguments:
        save_file {Save} -- A save object containing all of the quiz's data
    """

    # Uses pickle to dump the object into a byte array and then into a file
    pickle.dump(save_file, open(LOAD_FILE, "wb"))


def main():
    """The main function that is run when the file is run
    """

    # If there is a load file
    if os.path.exists(LOAD_FILE):
        # Load it
        save = pickle.load(open(LOAD_FILE, "rb"))
    else:
        # Otherwise create a new save object and make a new save file for it
        save = Save()
        pickle.dump(save, open(LOAD_FILE, "wb"))

    clear_screen()
    category = setup(save)

    clear_screen()
    quiz(category, save)


def quiz(category, save):
    """Allows the user to complete the quiz

    Arguments:
        school {School} -- The school that the quiz is currently set up for
        year {Year_Group} -- The year-group that the quiz is currently set up
        for
        category {str} -- The category that the questions shall be for
        save {Save} -- The save file that shall be saved to disk
    """

    while 1:
        school = None
        year = None
        if save.schools:
            school_choice = print_menu("Please choose a school", [
                                        school.name for school in save.schools])
            school = save.schools[school_choice]
        else:
            print("There are currently no schools to pick from. Please add a school to continue")
            break
        if school:
            if school.year_groups:
                yeargroup_choice = print_menu(
                    "Please choose a year-group", [year.year for year in school.year_groups])
                year = school.year_groups[yeargroup_choice]
            else:
                print(
                    "There are currently no year-groups to pick from with your current choice of school. Please add a yeargroup to continue")
        else:
            print("Please set a school before setting a year-group")
        questions = []
        for question in save.questions:
            if question.question_category == category:
                questions.append(question)
        if len(questions) < 10:
            print("There are not enough questions for a quiz in this category")
            break
        else:
            questions = random.sample(questions, 10)
        student = Student(school, year)
        random.shuffle(questions)
        answers = []
        for question in questions:
            print()
            index = random.randint(0, 3)
            options = list(question.incorrect_answers)
            options.insert(index, question.correct_answer)
            choice = print_menu(question.question_text, options)
            clear_screen()
            if choice == index:
                answers.append((question, Answer(True)))
                print("\nCorrect!")
            else:
                answers.append((question, Answer(False)))
                print("\nIncorrect...")
                print("The correct answer is:", question.correct_answer)
        result = Result(answers, student)
        if save.results:
            save.results = save.results + [result]
        else:
            save.results = [result]
        print()
        print("Congratulations! You scored: " + str(len(
            [answer for answer in answers if answer[1].correct is True]
            )) + "/" + str(len(answers)))
        print()
        save_data(save)
        time.sleep(5)
        clear_screen()


def setup(save):
    """The method run at startup to allow configuration of the quiz

    Arguments:
        save {Save} -- An object that holds all the data for the quiz so that
        everything can be quickly saved

    Returns:
        tuple -- The school and yeargroup of the person answering the quiz,
        and the
    """

    category = None

    print("Config menu")
    print("===========")
    print("To return to this menu, please close the program and then reopen\n")

    while 1:
        print("\nCurrent config:")
        if category:
            print("Category:   " + category)
        else:
            print("Category:   Not Selected")
        choice = print_menu("Please choose an option",
                            ["Start Quiz",
                             "Add School",
                             "Add Year-group",
                             "Set Category",
                             "Edit Questions",
                             "View Statistics"])
        print()
        clear_screen()

        if choice == 0:
            if category:
                return category
            else:
                print("Please ensure you have entered a category")

        elif choice == 1:
            name = input("Please enter the school's name: ")
            school_ = School()
            school_.name = name

            if save.schools:
                save.schools = save.schools + [school_]
            else:
                save.schools = [school_]

        elif choice == 2:
            if save.schools:
                year_school_choice = print_menu("Please select a school to add a year-group to:", [school.name for school in save.schools])
                school_to_add_year_to = save.schools[year_school_choice]
                name = input("Please enter the year-group name: ")
                year_ = Year_Group(name)

                if school_to_add_year_to.year_groups:
                    school_to_add_year_to.year_groups = school_to_add_year_to.year_groups + [year_]
                else:
                    school_to_add_year_to.year_groups = [year_]
            else:
                print("Please add a school before adding a year-group")

        elif choice == 3:
            if save.questions:
                q = []
                for question in save.questions:
                    q.append(question.question_category)
                q = list(set(q))
                cat = print_menu("Please select a category", q)
                category = q[cat]
            else:
                print("Please add questions before selecting a category")

        elif choice == 4:
            save.questions = question_editor(save.questions)

        elif choice == 5:
            show_stats(save)

        save_data(save)


def show_stats(save):
    """Displays and exports statistics

    Arguments:
        save {Save} -- Contains all application data
    """

    while 1:
        choice = print_menu("What would you like to do?", ["Compare year-groups from a school", "Compare schools", "Export to Excel", "Quit stats viewer"])
        if choice == 0:
            years = {}
            if save.schools:
                school_choice = print_menu("Please select a school:", [school.name for school in save.schools])
                school = save.schools[school_choice]
                if school.year_groups:
                    for year_group in school.year_groups:
                        years[year_group.year] = []
                    for year in years:
                        if save.results:
                            for result in save.results:
                                if result.student.school == school and result.student.year_group.year == year:
                                    answers = result.result
                                    years[year].append(len(
                                        [answer for answer in answers if answer[1].correct is True]
                                    ))
                            year_names = []
                            year_averages = []
                            for year in years:
                                years[year] = sum(years[year])/len(years[year])
                                year_names.append(year)
                                year_averages.append(years[year])
                            index = np.arange(len(year_names))
                            plt.bar(index, year_averages)
                            plt.xlabel('Year-groups')
                            plt.ylabel('Average Score')
                            plt.xticks(index, year_names)
                            plt.title('Averages for year-groups in ' + school.name)
                            plt.show()
                        else:
                            print("Please complete at least one quiz")

                else:
                    print("This school has no year-groups")
            else:
                print("There are no schools to display")
        elif choice == 1:
            school_results = {}
            if save.schools:
                for school in save.schools:
                    if save.results:
                        for result in save.results:
                            if result.student.school.name == school.name:
                                if school.name in school_results:
                                    school_results[school.name].append(len(
                                        [answer for answer in result.result if answer[1].correct is True]
                                    ))
                                else:
                                    school_results[school.name] = [(len(
                                        [answer for answer in result.result if answer[1].correct is True]
                                    ))]
                school_names = []
                school_averages = []
                for school in school_results:
                    school_results[school] = sum(school_results[school])/len(school_results[school])
                    school_names.append(school)
                    school_averages.append(school_results[school])
                index = np.arange(len(school_names))
                plt.bar(index, school_averages)
                plt.xlabel('Schools')
                plt.ylabel('Average Score')
                plt.xticks(index, school_names)
                plt.title('Averages for schools')
                plt.show()


            else:
                print("There are no schools to compare")
        elif choice == 2:
            workbook = xlsxwriter.Workbook('data.xlsx')
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})
            worksheet.write('A1', 'School', bold)
            worksheet.write('B1', 'Year', bold)
            worksheet.write('C1', 'Category', bold)
            worksheet.write('D1', 'Result', bold)
            row = 1
            col = 0
            if save.results:
                for result in save.results:
                    worksheet.write(row, col, result.student.school.name)
                    worksheet.write(row, col + 1, result.student.year_group.year)
                    worksheet.write(row, col + 2, result.result[0][0].question_category)
                    worksheet.write(row, col + 3, str(len([answer for answer in result.result if answer[1].correct is True])))
                    row += 1
                workbook.close()
                print("Data successfully exported to data.xlsx")
            else:
                print("There is no data to export")

        elif choice == 3:
            return

def question_editor(questions):
    """Creates an easy interface to edit the questions with

    Arguments:
        questions {list} -- The questions to edit

    Returns:
        list -- The edited questions
    """

    if questions:
        pass
    else:
        questions = []
    while 1:
        choice = print_menu("Would you like to:", ["Add a question", "Delete a question", "Quit the question editor"])
        if choice == 0:
            text = input("Please enter the question: ")
            correct = input("Please enter the correct answer: ")
            incorrect = [input("Please enter an incorrect answer: ") for i in range(0, 3)]
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
