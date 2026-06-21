def topic_accuracy(questions, answers):
    total = len(questions)
    correct = 0

    for item in questions:
        q = item["question"]

        qid = q.id
        user_ans = answers.get(qid)

        if user_ans is not None and norm(q.correct_option) == norm(user_ans):
            correct += 1

    return (correct / total) * 100 if total else 0


def norm(x):
    return str(x).strip().lower() if x is not None else ""