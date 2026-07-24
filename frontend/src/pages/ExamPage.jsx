import { useEffect, useMemo, useRef, useState } from "react";
import Header from "../components/Header";
import QuestionPanel from "../components/QuestionPanel";
import Options from "../components/Options";
import QuestionPalette from "../components/QuestionPalette";
import NavigationButtons from "../components/NavigationButtons";
import { flattenExam, submitExam } from "../services/api";

const EXAM_DURATION_SECONDS = 180 * 60;

function ExamPage({ exam, candidateName, onSubmitSuccess }) {
  const questions = useMemo(() => flattenExam(exam), [exam]);

  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [visited, setVisited] = useState(new Set([0]));
  const [markedForReview, setMarkedForReview] = useState(new Set());
  const [secondsLeft, setSecondsLeft] = useState(EXAM_DURATION_SECONDS);
  const [submitting, setSubmitting] = useState(false);

  const answersRef = useRef(answers);
  answersRef.current = answers;

  const currentQuestion = questions[currentIndex];

  useEffect(() => {
    const timerId = setInterval(() => {
      setSecondsLeft((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);

    return () => clearInterval(timerId);
  }, []);

  useEffect(() => {
    if (secondsLeft === 0 && !submitting) {
      handleSubmitExam(true);
    }
  }, [secondsLeft, submitting]);

  function markVisited(index) {
    setVisited((prev) => new Set(prev).add(index));
  }

  function handleSelectAnswer(option) {
    const questionId = currentQuestion.QuestionID;
    setAnswers((prev) => ({
      ...prev,
      [questionId]: option,
    }));
  }

  function handlePrevious() {
    if (currentIndex > 0) {
      const newIndex = currentIndex - 1;
      setCurrentIndex(newIndex);
      markVisited(newIndex);
    }
  }

  function handleSaveNext() {
    if (currentIndex < questions.length - 1) {
      const newIndex = currentIndex + 1;
      setCurrentIndex(newIndex);
      markVisited(newIndex);
    }
  }

  function handleMarkReview() {
    const questionId = currentQuestion.QuestionID;
    setMarkedForReview((prev) => new Set(prev).add(questionId));
  }

  function handleClearResponse() {
    const questionId = currentQuestion.QuestionID;
    setAnswers((prev) => {
      const updated = { ...prev };
      delete updated[questionId];
      return updated;
    });
  }

  function handlePaletteClick(index) {
    setCurrentIndex(index);
    markVisited(index);
  }

  async function handleSubmitExam(autoSubmit = false) {
    const confirmSubmit = autoSubmit
      ? true
      : window.confirm("Are you sure you want to submit the exam?");

    if (!confirmSubmit || submitting) {
      return;
    }

    setSubmitting(true);

    try {
      const response = await submitExam(candidateName, answersRef.current);
      onSubmitSuccess(response.result);
    } catch (error) {
      alert("Submit failed. Please check backend connection.");
      setSubmitting(false);
    }
  }

  return (
    <div className="exam-page">
      <Header
        candidateName={candidateName}
        secondsLeft={secondsLeft}
        onSubmit={() => handleSubmitExam(false)}
      />

      <div className="exam-body">
        <main className="exam-main">
          <QuestionPanel
            question={currentQuestion}
            questionNumber={currentIndex + 1}
          />
          <Options
            question={currentQuestion}
            selectedAnswer={answers[currentQuestion.QuestionID]}
            onSelect={handleSelectAnswer}
          />

          <NavigationButtons
            onPrevious={handlePrevious}
            onSaveNext={handleSaveNext}
            onMarkReview={handleMarkReview}
            onClear={handleClearResponse}
            disablePrevious={currentIndex === 0}
            disableNext={currentIndex === questions.length - 1}
          />
        </main>

        <QuestionPalette
          questions={questions}
          currentIndex={currentIndex}
          answers={answers}
          visited={visited}
          markedForReview={markedForReview}
          onQuestionClick={handlePaletteClick}
        />
      </div>
    </div>
  );
}

export default ExamPage;
