import React from "react";

const Result = (props) => {
  return (
    <div className="container">
      <h3>{props.responseData.message}</h3>
      <h3>{props.responseData.score}</h3>
    </div>
  );
};
export default Result;
