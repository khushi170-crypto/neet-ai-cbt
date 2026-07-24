"""One-time script to create sample questions.csv for the prototype."""

import csv
import os

SUBJECTS = ["Physics", "Chemistry", "Botany", "Zoology"]
QUESTIONS_PER_SUBJECT = 95  # 60 Section A + 30 Section B + buffer

rows = []
question_id = 1

for subject in SUBJECTS:
    for i in range(1, QUESTIONS_PER_SUBJECT + 1):
        rows.append({
            "QuestionID": f"Q{question_id:04d}",
            "Subject": subject,
            "Chapter": f"Chapter {(i % 10) + 1}",
            "Difficulty": ["Easy", "Medium", "Hard"][i % 3],
            "Question": f"{subject} question {i}: What is the correct answer?",
            "OptionA": f"Option A for {subject} Q{i}",
            "OptionB": f"Option B for {subject} Q{i}",
            "OptionC": f"Option C for {subject} Q{i}",
            "OptionD": f"Option D for {subject} Q{i}",
            "CorrectAnswer": ["A", "B", "C", "D"][i % 4],
        })
        question_id += 1

output_path = os.path.join(os.path.dirname(__file__), "..", "data", "questions.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {len(rows)} questions at {output_path}")
