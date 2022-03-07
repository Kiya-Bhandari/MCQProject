import React, { useEffect, useState } from "react";
import Base from "./Base";

import { history } from "./helper/coreapicalls";

const History = () => {
  const [historData, setHistoryData] = useState([]);
  useEffect(() => {
    console.log("history");
    getHistory();
  }, []);

  const getHistory = () => {
    history()
      .then((data) => {
        setHistoryData(data.history_data);
      })
      .catch((e) => console.log(e));
  };
  const showHistory = () => {
    return (
      <div className="table-sec">
        <table className="table table-bordered">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Test Name</th>
              <th scope="col">Date Taken</th>
              <th scope="col">Marks</th>
            </tr>
          </thead>

          <tbody>
            {historData.map((data, index) => (
              <tr key={index}>
                <th scope="row">{index + 1}</th>
                <td>
                  {data.quiz.topic},{data.quiz.difficulty}
                </td>
                <td>{data.created}</td>
                <td>
                  {data.score}/{data.quiz.number_of_questions}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  return <Base>{showHistory()}</Base>;
};

export default History;
