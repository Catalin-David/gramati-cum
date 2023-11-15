from question import Question
from answer import Answer
from database import initialise_database
import random

def display_menu():
    print("0. Exit")
    print("1. Take a quiz")
    print("2. List all questions and their correct answers")
    print("3. Filter questions based on word")
    
def take_quiz(quiz_size, questions):
    score = 0
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.answers)

    for i in range(quiz_size):
        question = questions[i]
        print(question.question + "\n")
        j=0
        options="abcd"
        for answer in question.answers:
            print(options[j] + ". " + answer.answer)
            j += 1
        
        choice = input("Your answer: ")
        answer_chosen = options.find(choice)
        if answer_chosen >= 0:
            if question.answers[answer_chosen].id == question.correct:
                score = score + 1
                print("Correct\n")
            else:
                print("Not correct\n")
    return score
        

def filter_questions(contains, questions):
    filtered_list = []
    for question in questions:
        if  question.question.find(contains) != -1:
            filtered_list.append(question)
    return filtered_list

running = True
quiz_size = 3
questions = initialise_database()
while running:
    display_menu()
    option = int(input("Choose option: "))
    if option == 1:
        score = take_quiz(quiz_size, questions)

        print("Your score: " + str(score) + " out of " + str(quiz_size)) 

    elif option == 2:
        for question in questions:
            print(question)

    elif option == 3:
        contains = input("Filter by: ")
        found_questions = filter_questions(contains, questions)
        for question in found_questions:
            print(question)
        
    elif option == 0:
        running = False
