const API_BASE = "http://127.0.0.1:8000";

export async function generateExam() {
  const response = await fetch(`${API_BASE}/generate-exam`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error("Failed to generate exam");
  }

  return response.json();
}

export async function submitExam(candidateName, answers) {
  const response = await fetch(`${API_BASE}/submit-exam`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      candidate_name: candidateName,
      answers,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to submit exam");
  }

  return response.json();
}

export async function getResult() {
  const response = await fetch(`${API_BASE}/result`);

  if (!response.ok) {
    throw new Error("Failed to fetch result");
  }

  return response.json();
}

export function flattenExam(exam) {
  const subjects = ["Physics", "Chemistry", "Botany", "Zoology"];
  const questions = [];

  subjects.forEach((subject) => {
    if (!exam[subject]) {
      return;
    }

    ["Section_A", "Section_B"].forEach((section) => {
      exam[subject][section].forEach((question) => {
        questions.push({
          ...question,
          subject,
          section,
        });
      });
    });
  });

  return questions;
}
