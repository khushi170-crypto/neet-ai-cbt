from graph.state import ExamState


def validate_exam(state: ExamState) -> ExamState:
    df = state["df"]
    rules = state["rules"]

    subjects = ["Physics", "Chemistry", "Botany", "Zoology"]

    for subject in subjects:
        count = len(df[df["Subject"] == subject])

        if count < rules[subject]:
            raise ValueError(
                f"Not enough questions in {subject}. Required: {rules[subject]}, Available: {count}"
            )

    return state