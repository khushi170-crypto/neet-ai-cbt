import Timer from "./Timer";

function Header({ candidateName, onSubmit, secondsLeft }) {
  return (
    <header className="exam-header">
      <div className="header-left">
        <h1>NEET AI Exam</h1>
        <p>Candidate: {candidateName}</p>
      </div>

      <Timer secondsLeft={secondsLeft} />

      <button className="submit-exam-btn" onClick={onSubmit}>
        Submit Exam
      </button>
    </header>
  );
}

export default Header;
