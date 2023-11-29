import uuid
import csv
from collections import defaultdict

class Student:
    def __init__(self, name, scores):
        self.__name = name
        self.__scores = scores

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self):
        self.__scores = True

    def average_score(self):
        if len(self.__scores) > 0:
            return sum(self.__scores) / len(self.__scores)
        else:
            return 0

    def __str__(self):
        return "name: " + self.name + ", average score: " + str(self.average_score())
    
def initialise_students():
    result_dict = defaultdict(list)

    with open('quiz_scores.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header

        for row in csv_reader:
            name, score = row
            result_dict[name].append(int(score))

    student_list = []
    for name, scores in result_dict.items():
        student_list.append(Student(name, scores))

    return student_list
