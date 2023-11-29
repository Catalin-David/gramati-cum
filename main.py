from question import Question
from answer import Answer
from JSONtoDatabase import initialise_database
import random
import csv
import os
from student import Student, initialise_students

def display_menu_student():
    print("0. Exit")
    print("1. Take a quiz")

def display_menu_prof():
    print("")
    print("0. Exit")
    print("1. List all questions and their correct answers")
    print("2. Filter questions based on word")
    print("3. List students")
    print("4. List scores for a student")

def add_quiz_score(name, score):
    file_path = "quiz_scores.csv"

    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file doesn't exist, create it and add the entry
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'score'])  # Header
            writer.writerow([name, score])
    else:
        # If the file exists, append the entry
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, score])

def take_quiz(quiz_size, questions):
    score = 0
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.answers)

    for i in range(quiz_size):
        question = questions[i]
        print(str(i+1)+' '+question.question )
        j=0
        options="abcd"
        for answer in question.answers:
            print(options[j] + ". " + answer.answer)
            j += 1

        chosen_answer = -1
        while chosen_answer < 0:
            choice = input("Raspunsul tau: ")
            chosen_answer = options.find(choice)
            if chosen_answer < 0:
                print("Alege o varianta valida")

        if chosen_answer >= 0:
            if question.answers[chosen_answer].id == question.correct:
                score = score + 1
                print("Corect\n")
            else:
                print("Gresit\n")
    return score
        

def filter_questions(contains, questions):
    filtered_list = []
    for question in questions:
        if  question.question.find(contains) != -1:
            filtered_list.append(question)
    return filtered_list

quiz_size = 3
questions = initialise_database()

mode = input("prof/stud: ")
while mode != "exit":
    running = True
    
    if mode == "stud":
        name = input("name: ")
        while running:
            display_menu_student()
            option = int(input("Choose option: "))
            if option == 1:
                score = take_quiz(quiz_size, questions)
                add_quiz_score(name, score)
                print("Your score: " + str(score) + " out of " + str(quiz_size)) 
                
            elif option == 0:
                running = False

            else:
                print("Valoarea selectata nu e in lista")

    elif mode == "prof":
        students = initialise_students()
        while running:
            display_menu_prof()
            option = int(input("Choose option: "))
            if option == 1:
                for question in questions:
                    print(question)

            elif option == 2:
                contains = input("Filter by: ")
                found_questions = filter_questions(contains, questions)
                for question in found_questions:
                    print(question)

            elif option == 3:
                for student in students:
                    print(student)

            elif option == 4:
                name = input("name: ")
                for student in students:
                    if name == student.name:
                        print(student.scores)

            elif option == 0:
                running = False

            else:
                print("Valoarea selectata nu e in lista")
    mode = input("prof/stud: ")