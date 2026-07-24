from graph.state import ExamState


def generate_subject_questions(state: ExamState) -> ExamState:
    df = state["df"]
    rules = state["rules"]

    selected_questions = {}

    subjects = ["Physics", "Chemistry", "Botany", "Zoology"]

    for subject in subjects:
        subject_df = df[df["Subject"] == subject]

        shuffled = subject_df.sample(
            frac=1,
            random_state=rules["Random_State"]
        )

        section_a = shuffled.iloc[:60]
        section_b = shuffled.iloc[60:90]

        selected_questions[subject] = {
            "Section_A": section_a.to_dict(orient="records"),
            "Section_B": section_b.to_dict(orient="records")
        }

    state["selected_questions"] = selected_questions

    return state