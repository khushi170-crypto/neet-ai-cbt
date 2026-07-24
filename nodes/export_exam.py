import json
import os

from graph.state import ExamState


def export_exam(state: ExamState) -> ExamState:
    os.makedirs("output", exist_ok=True)

    with open(
        "output/exam.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            state["exam"],
            file,
            indent=4,
            ensure_ascii=False
        )

    return state