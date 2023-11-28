import uuid

class Question:
    
    def __init__(self, question, answers, correct):
            self.__id = uuid.uuid4()
            self.__question = question
            self.__answers = answers
            self.__correct = correct #the id of the correct answer

    @property
    def id(self):
            return self.__id

    @property
    def question(self):
            return self.__question
    
    @question.setter
    def question(self, question):
            self.__question=question

    @property
    def answers(self):
        return self.__answers

    @answers.setter
    def answers(self, answers):
        self.__answers = answers

    @property
    def correct(self):    
        return self.__correct
    
    @correct.setter
    def correct(self, corret):
            self.__correct=corret

    def get_correct_answer(self):
        for answer in self.answers:
            if answer.id == self.correct:
                return answer.answer
        return "Correct answer not found"  # Add this line to provide a default value

    def __str__(self):
        result = "Intrebare: " + self.question + "\nRaspunsuri:\n"
        for answer in self.answers:
              result = result + answer.answer + "\n"
        result = result + "Correct: " + self.get_correct_answer() + "\n"
        return result