import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import Base from "../core/Base";
import { signin, authenticate, isAuthenticated } from "../auth/helper";

const Signin = () => {
  const [values, setValues] = useState({
    username: "fenil",
    password: "fenil@123",
    error: false,
    success: false,
    loading: false,
    didRedirect: false,
  });

  const { username, password, error, loading } = values;

  const handleChange = (name) => (event) => {
    setValues({ ...values, error: false, [name]: event.target.value });
  };

  const onSubmit = (event) => {
    event.preventDefault();
    setValues({
      ...values,
      error: false,
      loading: true,
    });
    signin({ username, password })
      .then((data) => {
        // console.log("data:",data)
        if (data.token) {
          authenticate(data, () => {
            console.log("token added");
            setValues({
              ...values,
              didRedirect: true,
              success: true,
            });
          });
        } else {
          setValues({
            ...values,
            error: true,
            loading: false,
            success: false,
          });
        }
      })
      .catch((e) => console.log(e));
  };

  const performRedirect = () => {
    if (isAuthenticated()) {
      return <Redirect to="/taketest" />;
    }
  };

  const performLoading = () => {
    return loading && <h3>Loading...</h3>;
  };

  const errorMessage = () => {
    return (
      <div style={{ display: error ? "" : "none", textAlign: "center" }}>
        <h3>Check all fields again.</h3>
      </div>
    );
  };

  const signInForm = () => {
    return (
      <div className="row ">
        <div className="col-lg-3 col-md-3 col-sm-2"></div>
        <div className="col-lg-6 col-md-6 col-sm-7 login-sec">
          <form>
            <div className="form-group">
              <div className="col-lg-12 input-design">
                <input
                  type="text"
                  name="username"
                  className="form-control"
                  value={username}
                  onChange={handleChange("username")}
                  placeholder="Enter Username"
                />
              </div>

              <div className="col-lg-12 input-design">
                <input
                  type="password"
                  name="password"
                  className="form-control"
                  value={password}
                  onChange={handleChange("password")}
                  placeholder="Password"
                />
              </div>

              <div className="col-lg-12 input-design">
                <center>
                  <input
                    type="submit"
                    className="sub-btn"
                    value="Login"
                    onClick={onSubmit}
                  />
                </center>
              </div>
            </div>
          </form>
        </div>
        <div className="col-lg-3 col-md-3 col-sm-2"></div>
      </div>
    );
  };
  return (
    <Base>
      {performLoading()}
      {signInForm()}

      {errorMessage()}
      {performRedirect()}
    </Base>
  );
};

export default Signin;
