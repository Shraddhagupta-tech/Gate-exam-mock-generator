import os
import json

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

QUESTION_BANK_PATH = os.path.join(BASE_DIR, "question_bank")


def load_all_questions():
    all_questions = []

    # loop over folders: gate_cse, gate_da
    for folder in os.listdir(QUESTION_BANK_PATH):
        folder_path = os.path.join(QUESTION_BANK_PATH, folder)

        # skip if not a folder
        if not os.path.isdir(folder_path):
            continue

        # loop over json files inside folder
        for file in os.listdir(folder_path):
            if file.endswith(".json"):
                file_path = os.path.join(folder_path, file)

                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                        questions = data.get("question_bank", [])
                    
                        if isinstance(questions, list):
                            all_questions.extend(questions)
                        else:
                            print(f"⚠️ Invalid format in {file_path}")

                except Exception as e:
                    print(f"Error in file : {file_path}")
                    print(e)

    return all_questions


def get_questions_by_concept(concept_id: int):
    questions = load_all_questions()

    return [q for q in questions if q.get("concept_id") == concept_id]

print(load_all_questions())