import uuid

class Answer:
    
    def __init__(self, answer):
            self.__id = uuid.uuid4()
            self.__answer = answer

    @property
    def id(self):
            return self.__id

    @property
    def answer(self):
            return self.__answer
    
    @answer.setter
    def answer(self, answer):
            self.__answer=answer

    @property
    def correct(self):    
        return self.__correct

    def __str__(self):
        return self.answer + "\n"