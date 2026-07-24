function QuestionPalette({
  questions,
  currentIndex,
  answers,
  visited,
  markedForReview,
  onQuestionClick,
}) {
  function getStatus(index) {
    const questionId = questions[index].QuestionID;
    const isVisited = visited.has(index);
    const isAnswered = Boolean(answers[questionId]);
    const isMarked = markedForReview.has(questionId);

    if (isAnswered && isMarked) {
      return "answered-review";
    }
    if (isMarked) {
      return "review";
    }
    if (isAnswered) {
      return "answered";
    }
    if (isVisited) {
      return "not-answered";
    }
    return "not-visited";
  }

  return (
    <aside className="question-palette">
      <h3>Question Palette</h3>

      <div className="palette-legend">
        <span className="legend not-visited">Not Visited</span>
        <span className="legend not-answered">Not Answered</span>
        <span className="legend answered">Answered</span>
        <span className="legend review">Mark for Review</span>
        <span className="legend answered-review">Answered + Review</span>
      </div>

      <div className="palette-grid">
        {questions.map((question, index) => (
          <button
            key={question.QuestionID}
            className={`palette-item ${getStatus(index)} ${
              index === currentIndex ? "active" : ""
            }`}
            onClick={() => onQuestionClick(index)}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </aside>
  );
}

export default QuestionPalette;
