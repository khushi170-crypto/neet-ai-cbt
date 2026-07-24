from langgraph.graph import StateGraph, START, END

from graph.state import ExamState

from nodes.load_csv import load_csv
from nodes.validate_exam import validate_exam
from nodes.generate_subject_questions import generate_subject_questions
from nodes.assemble_exam import assemble_exam
from nodes.export_exam import export_exam


builder = StateGraph(ExamState)

builder.add_node("load_csv", load_csv)
builder.add_node("validate_exam", validate_exam)
builder.add_node(
    "generate_subject_questions",
    generate_subject_questions
)
builder.add_node("assemble_exam", assemble_exam)
builder.add_node("export_exam", export_exam)

builder.add_edge(START, "load_csv")
builder.add_edge("load_csv", "validate_exam")
builder.add_edge(
    "validate_exam",
    "generate_subject_questions"
)
builder.add_edge(
    "generate_subject_questions",
    "assemble_exam"
)
builder.add_edge("assemble_exam", "export_exam")
builder.add_edge("export_exam", END)

graph_app = builder.compile()