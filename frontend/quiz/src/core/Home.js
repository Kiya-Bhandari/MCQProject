import React from "react";
import Base from "./Base";

export default function Home() {
  return (
    <Base>
      <div className="container-fluid">
        <div className="row">
          <div className="col-lg-2 col-md-2"></div>
          <div className="col-lg-8 col-md-8 welcome">
            <p>Welcome to MCQ Test</p>
          </div>
          <div className="col-lg-2 col-md-2"></div>
        </div>
      </div>
    </Base>
  );
}
