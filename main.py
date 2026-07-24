from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config.rules import NEET_RULES
from graph.builder import graph_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUBJECTS = ["Physics", "Chemistry", "Botany", "Zoology"]
MARKS_CORRECT = 4
MARKS_WRONG = -1

# In-memory storage for prototype
latest_exam: Optional[dict] = None
latest_result: Optional[dict] = None


class SubmitExamRequest(BaseModel):
    candidate_name: str = "Student"
    answers: Dict[str, str]


@app.get("/")
def home():
    return {
        "message": "NEET AI Backend Running"
    }


@app.post("/generate-exam")
def generate_exam():
    global latest_exam

    initial_state = {
        "csv_path": "data/questions.csv",
        "df": None,
        "rules": NEET_RULES,
        "selected_questions": {},
        "exam": {},
    }

    result = graph_app.invoke(initial_state)
    latest_exam = result["exam"]

    return {
        "status": "success",
        "exam": latest_exam,
    }


def _collect_questions(exam: dict) -> list:
    """Flatten all exam questions from every subject and section."""
    questions = []

    for subject in SUBJECTS:
        subject_data = exam.get(subject, {})

        for section_name in ["Section_A", "Section_B"]:
            for question in subject_data.get(section_name, []):
                questions.append({
                    "question_id": question["QuestionID"],
                    "subject": subject,
                    "section": section_name,
                    "correct_answer": question["CorrectAnswer"],
                })

    return questions


def _calculate_result(exam: dict, answers: dict, candidate_name: str) -> dict:
    questions = _collect_questions(exam)

    correct = 0
    wrong = 0
    unattempted = 0
    score = 0

    subject_analysis = {
        subject: {
            "correct": 0,
            "wrong": 0,
            "unattempted": 0,
            "score": 0,
            "total_questions": 0,
        }
        for subject in SUBJECTS
    }

    for question in questions:
        question_id = question["question_id"]
        subject = question["subject"]
        correct_answer = question["correct_answer"].upper()

        subject_analysis[subject]["total_questions"] += 1

        student_answer = answers.get(question_id)

        if not student_answer:
            unattempted += 1
            subject_analysis[subject]["unattempted"] += 1
            continue

        student_answer = student_answer.upper()

        if student_answer == correct_answer:
            correct += 1
            score += MARKS_CORRECT
            subject_analysis[subject]["correct"] += 1
            subject_analysis[subject]["score"] += MARKS_CORRECT
        else:
            wrong += 1
            score += MARKS_WRONG
            subject_analysis[subject]["wrong"] += 1
            subject_analysis[subject]["score"] += MARKS_WRONG

    total_questions = len(questions)

    return {
        "candidate_name": candidate_name,
        "total_questions": total_questions,
        "attempted": correct + wrong,
        "correct": correct,
        "wrong": wrong,
        "unattempted": unattempted,
        "score": score,
        "max_score": total_questions * MARKS_CORRECT,
        "subject_wise_analysis": subject_analysis,
    }


@app.post("/submit-exam")
def submit_exam(payload: SubmitExamRequest):
    global latest_result

    if latest_exam is None:
        raise HTTPException(
            status_code=400,
            detail="No exam found. Call POST /generate-exam first.",
        )

    latest_result = _calculate_result(
        exam=latest_exam,
        answers=payload.answers,
        candidate_name=payload.candidate_name,
    )

    return {
        "status": "success",
        "result": latest_result,
    }


@app.get("/result")
def get_result():
    if latest_result is None:
        raise HTTPException(
            status_code=404,
            detail="No result found. Submit an exam first using POST /submit-exam.",
        )

    return latest_result
