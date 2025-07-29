import "react";
import { useState } from "react";

export function MCQChallenge({ challenge, showExplanation = false }) {
  const [selectedOption, setSelectedOption] = useState(null);
  const [shouldShowExplanation, setShouldShowExplanation] =
    useState(showExplanation);

  const options =
    typeof challenge.options === "string"
      ? JSON.parse(challenge.options)
      : challenge.options;

  const handleOptionSelect = (index) => {
    if (selectedOption !== null) return;
    setSelectedOption(index);
    setShouldShowExplanation(true);
  };

  // when user choose this option (correct/incorrect)
  const getOptionClass = (index) => {
    if (selectedOption === null) return "option";

    if (index === challenge.correct_answer_id) {
      return "option correct";
    }
    if (selectedOption === index && index !== challenge.correct_answer_id) {
      return "option incorrect";
    }
    return "option";
  };
  return <></>;
}
