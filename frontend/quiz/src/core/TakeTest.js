import React, { useState, useEffect } from "react";
import Base from "./Base";
import { testlist } from "./helper/coreapicalls";
import { Redirect } from "react-router-dom";

const TakeTest = () => {
  const [testData, setTestData] = useState([]);
  const [values, setValues] = useState({
    take: false,
    start: false,
    quiz_id: "",
    topic: "",
  });

  const { take, quiz_id, start } = values;

  useEffect(() => {
    getTestList();
  }, []);

  const getTestList = () => {
    testlist()
      .then((data) => {
        setTestData(data.testLists);
      })
      .catch((e) => console.log(e));
  };
  const startText = () => {
    // console.log("startttt");
    return (
      <div>
        <div className="row">
          <div className="col-lg-12 col-md-12">
            <div id="start-test">
              You are about start a test. Please click Start button to start the
              test session.
              <br></br>
              <button
                type="button"
                id="startBtn"
                onClick={() =>
                  setValues({ ...values, start: true, take: false })
                }
              >
                Start
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  };
  const startQuiz = () => {
    return <Redirect to={"/taketest/" + quiz_id} />;
  };
  const taketest = () => {
    return (
      <div className="table-sec">
        <table className="table table-bordered">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Test Name</th>
              <th scope="col">Date Created</th>
              <th scope="col">Date Expires</th>
              <th scope="col">View Questions</th>
            </tr>
          </thead>

          <tbody>
            {testData.map((data, index) => (
              <tr key={index}>
                <th scope="row">{index + 1}</th>
                <td>
                  {data.topic.topic},{data.topic.difficulty}
                </td>
                <td>{data.created}</td>
                <td>{data.expired}</td>
                <td>
                  <button
                    type="button"
                    className="sub-btn takeBtn"
                    onClick={() => {
                      setValues({
                        ...values,
                        take: true,
                        quiz_id: data.topic.id,
                        topic: data.topic.topic,
                      });
                      document.getElementsByClassName(
                        "table"
                      )[0].style.display = "none";
                    }}
                  >
                    Take
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  return (
    <React.Fragment>
      <Base>
        {taketest()}
        {take && startText()}
        {start && startQuiz()}
      </Base>
    </React.Fragment>
  );
};

export default TakeTest;
