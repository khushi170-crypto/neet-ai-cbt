import { useState } from "react";
import ExamPage from "./pages/ExamPage";
import ResultPage from "./pages/ResultPage";
import { generateExam } from "./services/api";
import "./App.css";

function App() {
  const [screen, setScreen] = useState("start");
  const [examData, setExamData] = useState(null);
  const [resultData, setResultData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const candidateName = "Student";

  async function handleStartExam() {
    setLoading(true);
    setError("");

    try {
      const data = await generateExam();
      setExamData(data.exam);
      setScreen("exam");
    } catch (err) {
      setError("Could not start exam. Backend check karo.");
    } finally {
      setLoading(false);
    }
  }

  function handleExamSubmit(result) {
    setResultData(result);
    setScreen("result");
  }

  if (screen === "exam" && examData) {
    return (
      <ExamPage
        exam={examData}
        candidateName={candidateName}
        onSubmitSuccess={handleExamSubmit}
      />
    );
  }

  if (screen === "result" && resultData) {
    return (
      <ResultPage
        result={resultData}
        onRestart={() => {
          setScreen("start");
          setExamData(null);
          setResultData(null);
        }}
      />
    );
  }

  return (
    <div className="start-screen">
      <div className="start-card">
        <h1>NEET AI CBT Exam</h1>
        <p>Computer Based Test Prototype</p>

        {error && <p className="error-text">{error}</p>}

        <button onClick={handleStartExam} disabled={loading}>
          {loading ? "Generating Exam..." : "Start Exam"}
        </button>
      </div>
    </div>
  );
}

export default App;