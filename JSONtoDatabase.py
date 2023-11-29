from answer import Answer
from question import Question
import json

def load_questions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['questions']


def create_answers(answer_data):
    # answers=[]
    # for answer_text in answer_data:
    #     ans= Answer[answer_text]
    #     answers.append(ans)
    # return answers
     return [Answer(answer_text) for answer_text in answer_data]


def create_question(question_data):
    answers = create_answers(question_data['answers'])
    correct_answer = question_data['correct_answer']

    for answer in answers:
        if answer.answer == correct_answer:
            CorrectId=answer.id

    question = Question(
        question_data['question'],
        answers,
        CorrectId
    )
    return question

def initialise_database():
    questions=[]
    json_file_path = 'Questions.json'  # Replace with the actual file path
    questions_data = load_questions_from_json(json_file_path)

    for question_data in questions_data:
        question_instance = create_question(question_data)
        questions.append(question_instance)
    return questions
