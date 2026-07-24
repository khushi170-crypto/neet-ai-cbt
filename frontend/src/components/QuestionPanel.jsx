function QuestionPanel({ question, questionNumber }) {
  if (!question) {
    return null;
  }

  return (
    <section className="question-panel">
      <div className="question-meta">
        <span>Q. {questionNumber}</span>
        <span>{question.Subject}</span>
        <span>{question.Chapter}</span>
        <span className={`difficulty ${question.Difficulty.toLowerCase()}`}>
          {question.Difficulty}
        </span>
        <span>{question.section.replace("_", " ")}</span>
      </div>

      <p className="question-text">{question.Question}</p>
    </section>
  );
}

export default QuestionPanel;
