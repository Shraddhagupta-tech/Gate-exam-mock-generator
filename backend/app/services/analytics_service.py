from app.models.question_option import QuestionOption
from app.models.question import Question
from app.models.mock_questions import MockQuestion
from app.database.db_connection import sessionlocal
db = sessionlocal()

def evaluate(questions, answers,mock_id):
    score = 0

    # fast lookup for user answers
    answer_map = {a['question_id']: a for a in answers}

    for item in questions:
        q = item['question']
        qid = q.id
        if qid not in answer_map:
            continue
        user_ans = answer_map[qid]
        # fetch marks
        mockquestion = db.query(MockQuestion).filter(
            MockQuestion.question_id == qid ,MockQuestion.mocktest_id==mock_id
        ).one()

        # -------------------------
        # MCQ / MSQ
        # -------------------------
        if 'selected_option_ids' in user_ans:
            correct_options = db.query(QuestionOption).filter(
                QuestionOption.question_id == qid,
                QuestionOption.is_correct == True
            ).all()
            correct_ids = sorted([opt.id for opt in correct_options])
            user_ids = sorted(user_ans['selected_option_ids'])
            if user_ids == correct_ids:
                score += mockquestion.marks
        # -------------------------
        # NAT
        # -------------------------
        elif 'numerical_answer' in user_ans:
            correct_q = db.query(Question).filter(
                Question.id == qid
            ).one()
            user_value = float(user_ans['numerical_answer'])
            correct_value = float(correct_q.correct_answer_value)
            tolerance = float(correct_q.answer_tolerance)
            if abs(user_value - correct_value) <= tolerance:
                score += mockquestion.marks

    return score
