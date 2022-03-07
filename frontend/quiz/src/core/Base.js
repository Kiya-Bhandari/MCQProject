import React from "react";
import Header from "./Header";
import { Link } from "react-router-dom";

const Base = ({ children }) => {
  return (
    <React.Fragment>
      <Header />

      <div className="container-fluid">
        <div className="row">
          <div className="col-lg-2 col-md-2 sidebar">
            <Link to="/taketest" className="sidebar-text">
              <h6>Take Test</h6>
            </Link>
            <Link to="/history" className="history">
              <h6>History</h6>
            </Link>
          </div>
          <div className="col-lg-10 col-md-10 main-sec">{children}</div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Base;
