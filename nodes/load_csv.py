import pandas as pd

from graph.state import ExamState


def load_csv(state: ExamState) -> ExamState:
    state["df"] = pd.read_csv(state["csv_path"])
    return state