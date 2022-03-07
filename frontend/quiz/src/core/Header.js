import React from "react";
import { signout, isAuthenticated } from "../auth/helper";
import { Link, withRouter } from "react-router-dom";

const Header = ({ history }) => {
  return (
    <header>
      <div className="container-fluid">
        <div className="row">
          <div className="col-lg-2 col-md-2 col-sm-2">
            <h6> MCQ TEST</h6>
          </div>
          {isAuthenticated() && (
            <React.Fragment>
              <div className="col-lg-9 col-md-2 col-sm-2">
                <p className="reg"></p>
              </div>

              <div className="col-lg-1 col-md-2 col-sm-2">
                <p
                  className="sign"
                  onClick={() => {
                    signout(() => {
                      history.push("/");
                    });
                  }}
                >
                  Sign Out
                </p>
              </div>
            </React.Fragment>
          )}
          {!isAuthenticated() && (
            <React.Fragment>
              <div className="col-lg-9">
                <Link to="/signup" className="reg">
                  Register
                </Link>
              </div>
              <div className="col-lg-1">
                <Link to="/signin" className="sign">
                  Sign In
                </Link>
              </div>
            </React.Fragment>
          )}
        </div>
      </div>
    </header>
  );
};

export default withRouter(Header);
