import React, { useEffect, useState } from "react";
import Base from "./Base";
import Result from "./Result";
import { questions, submitData } from "./helper/quizquestionsapicall";
import Timer from "./Timer";

const markStyle = {
  float: "right",
  fontSize: "15px",
  paddingTop: "10px",
  fontWeight: "bold",
};
const Quiz = (props) => {
  const [topic, setTopic] = useState("");
  const [quizTime, setquizTime] = useState("");
  const [quizData, setQuizData] = useState([]);
  const [currentSlide, setCurrentSlide] = useState(0);
  const [responseData, setresponseData] = useState([]);

  useEffect(() => {
    const getQuestions = () => {
      questions(props.match.params.quiz_id)
        .then((data) => {
          // console.log(data.data);
          setQuizData(data.data);
          setquizTime(data.time);
          setTopic(data.topic);
        })
        .catch((e) => console.log(e));
    };
    getQuestions();
  }, [props.match.params.quiz_id]);

  const showSlide = (n) => {
    // console.log('slides')
    const slides = document.querySelectorAll(".slide");

    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");
    const submitButton = document.getElementById("submit");

    slides[currentSlide].classList.remove("active-slide");
    slides[n].classList.add("active-slide");
    setCurrentSlide(n);

    if (currentSlide === 0) {
      previousButton.style.display = "none";
    } else {
      previousButton.style.display = "inline-block";
    }
    if (currentSlide === slides.length - 1) {
      nextButton.style.display = "none";
      submitButton.style.display = "inline-block";
    } else {
      nextButton.style.display = "inline-block";
      submitButton.style.display = "none";
    }
  };

  const showNextSlide = () => {
    showSlide(currentSlide + 1);
  };

  const showPreviousSlide = () => {
    showSlide(currentSlide - 1);
  };

  const setshowSlide = () => {
    const time = setTimeout(() => {
      showSlide(currentSlide);
    }, 310);
    return () => clearTimeout(time);
  };

  const buildQuiz = () => {
    let output = [];
    quizData.forEach((data, index) => {
      output.push(
        <div key={index}>
          <div className="slide">
            <div className="question">
              {data.question}
              <span style={markStyle}>{data.marks} Marks</span>
            </div>
            <div className="answers">
              {(() => {
                let answers = [];
                for (let i = 0; i < data.answers.length; i++) {
                  answers.push(
                    <div>
                      <label>
                        <input
                          type="radio"
                          className="ans"
                          id={data.question}
                          name={data.question}
                          value={data.answers[i]}
                        />
                        {data.answers[i]}
                      </label>
                    </div>
                  );
                }
                return answers;
              })()}
            </div>
          </div>
        </div>
      );
    });
    // console.log("output:",output)
    return output;
  };
  const sendData = () => {
    const elements = [...document.getElementsByClassName("ans")];
    const data = {};

    elements.forEach((e1) => {
      if (e1.checked) data[e1.name] = e1.value;
      else {
        if (!data[e1.name]) data[e1.name] = null;
      }
    });

    submitData(props.match.params.quiz_id, data)
      .then((data) => {
        // console.log("data : ", data);
        document.getElementById("quiz-form").style.display = "none";
        setresponseData(data);
      })
      .catch((e) => console.log(e));
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    sendData();
  };
  const displayTimer = () => {
    return <Timer topic={topic} quizTime={quizTime} sendData={sendData} />;
  };
  const displayQuiz = () => {
    return (
      <React.Fragment>
        {quizTime && displayTimer()}
        <form id="quiz-form" className="quiz-container" onSubmit={handleSubmit}>
          <div className="row">
            <div className="col-lg-12 col-md-12">
              {buildQuiz()}
              {setshowSlide()}
            </div>
            <div id="quiz-button" className="col-lg-12 col-md-12">
              <button
                type="button"
                className="sub-btn"
                id="previous"
                onClick={showPreviousSlide}
              >
                Previous Question
              </button>
              <button
                type="button"
                className="sub-btn"
                id="next"
                onClick={showNextSlide}
              >
                Next Question
              </button>
              <button type="submit" className="sub-btn" id="submit">
                Submit Quiz
              </button>
            </div>
          </div>
        </form>
      </React.Fragment>
    );
  };
  const displayResult = () => {
    return <Result responseData={responseData} />;
  };
  return (
    <Base>
      {displayQuiz()}
      {responseData && displayResult()}
    </Base>
  );
};

export default Quiz;
