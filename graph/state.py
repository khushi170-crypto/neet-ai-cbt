from typing import TypedDict
import pandas as pd


class ExamState(TypedDict):
    csv_path: str
    df: pd.DataFrame
    rules: dict
    selected_questions: dict
    exam: dict