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
        ).reset_index(drop=True)

        # Number of questions required for this subject
        total_questions = rules[subject]

        # Prototype: All questions in Section A
        section_a_count = total_questions
        section_b_count = 0

        section_a = shuffled.iloc[:section_a_count]
        section_b = shuffled.iloc[
            section_a_count:
            section_a_count + section_b_count
        ]

        selected_questions[subject] = {
            "Section_A": section_a.fillna("").to_dict(orient="records"),
            "Section_B": section_b.fillna("").to_dict(orient="records")
        }

    state["selected_questions"] = selected_questions

    return state