import json
import os
import random

BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../data/question_bank")
)


def load_questions(exam="gate_cse"):
    exam_path = os.path.join(BASE_PATH, exam)

    all_questions = []
    question_id = 1

    for file_name in os.listdir(exam_path):

        if file_name.endswith(".json"):

            file_path = os.path.join(exam_path, file_name)

            with open(file_path, "r") as f:
                data = json.load(f)

            questions = data["question_bank"]

            for q in questions:

                q["id"] = question_id
                question_id += 1

                q["subject"] = file_name.replace(".json", "")

                all_questions.append(q)

    return all_questions

def create_mock(exam="gate_cse"):
    questions = load_questions(exam)

    selected = random.sample(
        questions,
        min(5, len(questions))
    )

    return {
        "title": f"{exam} mock",
        "questions": selected
    }