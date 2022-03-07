import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowCircleLeft } from "@fortawesome/free-solid-svg-icons";

const Timer = (props) => {
  const [quizTime, setquizTime] = useState(props.quizTime);
  useEffect(() => {
    // console.log(props.quizTime);
    // sactivateTimer(quizTime);
  }, []);

  const activateTimer = (time) => {
    if (time.toString().length < 2) setquizTime("0" + time + ":00");
    else setquizTime(time + ":00");
    let minutes = time - 1;
    let seconds = 60;
    let displaySeconds;
    let displayMinutes;
    const timer = setInterval(() => {
      seconds--;
      if (seconds < 0) {
        seconds = 59;
        minutes--;
      }
      if (minutes.toString().length < 2) displayMinutes = "0" + minutes;
      else displayMinutes = minutes;
      if (seconds.toString().length < 2) displaySeconds = "0" + seconds;
      else displaySeconds = seconds;
      if (minutes === 0 && seconds === 0) {
        setquizTime("00:00");
        setTimeout(() => {
          clearInterval(timer);
          alert("Time over");
          props.sendData();
        }, 500);
      }
      setquizTime(displayMinutes + ":" + displaySeconds);
    }, 1000);
  };
  const displayContent = () => {
    return (
      <div className="container">
        <div className="row">
          <div className="col-lg-2">
            <a href="/taketest">
              <FontAwesomeIcon
                icon={faArrowCircleLeft}
                size="2x"
                className="back"
              />
            </a>
          </div>
          <div className="col-lg-8 topic">
            <b> {props.topic}</b>
          </div>
          <div className="col-lg-2 text-right">
            <b className="timer">{quizTime}</b>
          </div>
        </div>
      </div>
    );
  };
  return <React.Fragment> {displayContent()}</React.Fragment>;
};
export default Timer;
