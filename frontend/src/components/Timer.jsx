function Timer({ secondsLeft }) {
  const hours = String(Math.floor(secondsLeft / 3600)).padStart(2, "0");
  const minutes = String(Math.floor((secondsLeft % 3600) / 60)).padStart(2, "0");
  const seconds = String(secondsLeft % 60).padStart(2, "0");

  return (
    <div className="timer-box">
      <span>Time Left</span>
      <strong>
        {hours}:{minutes}:{seconds}
      </strong>
    </div>
  );
}

export default Timer;
