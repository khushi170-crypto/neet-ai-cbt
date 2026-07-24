const OPTION_KEYS = ["A", "B", "C", "D"];

function Options({ question, selectedAnswer, onSelect }) {
  if (!question) {
    return null;
  }

  return (
    <div className="options-list">
      {OPTION_KEYS.map((key) => (
        <label key={key} className="option-item">
          <input
            type="radio"
            name={question.QuestionID}
            value={key}
            checked={selectedAnswer === key}
            onChange={() => onSelect(key)}
          />
          <span className="option-label">{key}</span>
          <span>{question[`Option${key}`]}</span>
        </label>
      ))}
    </div>
  );
}

export default Options;
