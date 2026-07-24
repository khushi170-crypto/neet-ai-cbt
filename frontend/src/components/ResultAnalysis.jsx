function ResultAnalysis({ result }) {
  const subjects = Object.keys(result.subject_wise_analysis || {});

  return (
    <div className="result-analysis">
      <div className="result-summary">
        <div className="summary-card">
          <span>Score</span>
          <strong>{result.score}</strong>
        </div>
        <div className="summary-card">
          <span>Correct</span>
          <strong>{result.correct}</strong>
        </div>
        <div className="summary-card">
          <span>Wrong</span>
          <strong>{result.wrong}</strong>
        </div>
        <div className="summary-card">
          <span>Unattempted</span>
          <strong>{result.unattempted}</strong>
        </div>
      </div>

      <h3>Subject-wise Performance</h3>
      <div className="subject-table">
        <div className="subject-row subject-header">
          <span>Subject</span>
          <span>Correct</span>
          <span>Wrong</span>
          <span>Unattempted</span>
          <span>Score</span>
        </div>

        {subjects.map((subject) => {
          const stats = result.subject_wise_analysis[subject];
          return (
            <div key={subject} className="subject-row">
              <span>{subject}</span>
              <span>{stats.correct}</span>
              <span>{stats.wrong}</span>
              <span>{stats.unattempted}</span>
              <span>{stats.score}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default ResultAnalysis;
