function NavigationButtons({
  onPrevious,
  onSaveNext,
  onMarkReview,
  onClear,
  disablePrevious,
  disableNext,
}) {
  return (
    <div className="nav-buttons">
      <button onClick={onPrevious} disabled={disablePrevious}>
        Previous
      </button>
      <button onClick={onSaveNext} disabled={disableNext}>
        Save &amp; Next
      </button>
      <button onClick={onMarkReview}>Mark for Review</button>
      <button onClick={onClear}>Clear Response</button>
    </div>
  );
}

export default NavigationButtons;
