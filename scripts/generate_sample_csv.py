"""Create NEET-style sample questions.csv for prototype."""

import csv
import os
import random


SUBJECTS = {
    "Physics": [
        ("Mechanics", "Newton's second law relates force, mass and acceleration."),
        ("Current Electricity", "Ohm's law describes the relation between voltage, current and resistance."),
        ("Optics", "Convex lenses are used for image formation."),
        ("Thermodynamics", "Heat transfer occurs due to temperature difference."),
    ],
    "Chemistry": [
        ("Atomic Structure", "Atomic number represents the number of protons."),
        ("Chemical Bonding", "Ionic bonds involve transfer of electrons."),
        ("Thermodynamics", "Enthalpy represents heat content of a system."),
        ("Organic Chemistry", "Carbon forms stable covalent bonds."),
    ],
    "Botany": [
        ("Cell Biology", "Cell is the basic structural unit of life."),
        ("Plant Physiology", "Photosynthesis occurs inside chloroplasts."),
        ("Genetics", "DNA carries hereditary information."),
        ("Ecology", "Plants act as primary producers."),
    ],
    "Zoology": [
        ("Human Physiology", "The heart pumps blood throughout the body."),
        ("Animal Kingdom", "Chordates possess a notochord."),
        ("Evolution", "Natural selection explains evolutionary changes."),
        ("Biology", "Enzymes work as biological catalysts."),
    ]
}


QUESTIONS_PER_SUBJECT = 45

rows = []
question_id = 1


for subject, chapters in SUBJECTS.items():

    for i in range(1, QUESTIONS_PER_SUBJECT + 1):

        chapter, concept = random.choice(chapters)

        options = [
            "It is the correct scientific explanation",
            "It is not scientifically correct",
            "It is partially correct",
            "None of these"
        ]

        rows.append({
            "QuestionID": f"Q{question_id:04d}",
            "Subject": subject,
            "Chapter": chapter,
            "Difficulty": random.choice(
                ["Easy", "Medium", "Hard"]
            ),
            "Question": (
                f"NEET {subject} Q{i}: {concept} "
                "Choose the correct option."
            ),
            "OptionA": options[0],
            "OptionB": options[1],
            "OptionC": options[2],
            "OptionD": options[3],
            "CorrectAnswer": random.choice(
                ["A", "B", "C", "D"]
            ),
        })

        question_id += 1


output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "questions.csv"
)

os.makedirs(
    os.path.dirname(output_path),
    exist_ok=True
)


with open(
    output_path,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print(f"Created {len(rows)} NEET-style questions at {output_path}")