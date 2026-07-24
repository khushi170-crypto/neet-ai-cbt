from ai.watsonx_model import analyze_exam
from graph.state import ExamState


def assemble_exam(state: ExamState) -> ExamState:
    selected_questions = state["selected_questions"]

    exam = {
        "Physics": selected_questions["Physics"],
        "Chemistry": selected_questions["Chemistry"],
        "Botany": selected_questions["Botany"],
        "Zoology": selected_questions["Zoology"],
    }

    exam["ai_analysis"] = analyze_exam(exam)

    state["exam"] = exam

    return state