import os

from dotenv import load_dotenv

load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY", "")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID", "")
IBM_URL = os.getenv("IBM_URL", "")
MODEL_ID = os.getenv("MODEL_ID", "ibm/granite-3-3-8b-instruct")

PLACEHOLDER_VALUES = {"YOUR_API_KEY", "YOUR_PROJECT_ID", "YOUR_IBM_URL", ""}


def is_watsonx_available() -> bool:
    """Return True only when real IBM credentials exist in .env."""
    return all(
        value not in PLACEHOLDER_VALUES
        for value in [IBM_API_KEY, IBM_PROJECT_ID, IBM_URL]
    )


def _get_watsonx_llm():
    """Create Watsonx LLM client. Returns None if credentials are missing."""
    if not is_watsonx_available():
        return None

    try:
        from langchain_ibm import WatsonxLLM

        return WatsonxLLM(
            model_id=MODEL_ID,
            url=IBM_URL,
            apikey=IBM_API_KEY,
            project_id=IBM_PROJECT_ID,
            params={
                "max_new_tokens": 300,
                "temperature": 0.3,
            },
        )
    except Exception:
        return None


def ask_ai(prompt: str) -> dict:
    """
    Send a prompt to IBM Granite.
    Falls back to a simple local response if AI is unavailable.
    """
    llm = _get_watsonx_llm()

    if llm is None:
        return {
            "source": "fallback",
            "response": (
                "AI is offline. Using rule-based exam generation. "
                "Add valid IBM credentials in .env to enable Watsonx analysis."
            ),
        }

    try:
        response = llm.invoke(prompt)
        return {
            "source": "watsonx",
            "response": str(response).strip(),
        }
    except Exception as error:
        return {
            "source": "fallback",
            "response": f"AI call failed ({error}). Exam generated without AI analysis.",
        }


def analyze_exam(exam: dict) -> dict:
    """
    Analyze the assembled exam.
    Uses Watsonx when available, otherwise returns basic stats.
    """
    stats = _build_exam_stats(exam)

    if not is_watsonx_available():
        return {
            "mode": "fallback",
            "summary": _fallback_summary(stats),
            "stats": stats,
        }

    prompt = f"""
You are a NEET exam analyst.

Analyze this exam summary and give 3 short bullet points:
- subject balance
- difficulty spread
- one tip for students

Exam stats:
{stats}
"""

    ai_result = ask_ai(prompt)

    return {
        "mode": ai_result["source"],
        "summary": ai_result["response"],
        "stats": stats,
    }


def _build_exam_stats(exam: dict) -> dict:
    """Count questions and difficulty levels per subject."""
    stats = {}

    for subject, sections in exam.items():
        if subject == "ai_analysis":
            continue

        all_questions = sections["Section_A"] + sections["Section_B"]
        difficulty_count = {}

        for question in all_questions:
            level = question.get("Difficulty", "Unknown")
            difficulty_count[level] = difficulty_count.get(level, 0) + 1

        stats[subject] = {
            "total_questions": len(all_questions),
            "section_a": len(sections["Section_A"]),
            "section_b": len(sections["Section_B"]),
            "difficulty": difficulty_count,
        }

    return stats


def _fallback_summary(stats: dict) -> str:
    """Simple summary when IBM Watsonx is not configured."""
    lines = ["Exam generated successfully using rule-based selection (seed=42)."]

    for subject, info in stats.items():
        lines.append(
            f"- {subject}: {info['total_questions']} questions "
            f"({info['section_a']} in Section A, {info['section_b']} in Section B)"
        )

    lines.append("Tip: Configure IBM Watsonx in .env for AI-powered exam analysis.")
    return "\n".join(lines)
