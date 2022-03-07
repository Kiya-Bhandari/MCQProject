import React, { useState } from "react";
import Base from "../core/Base";
import { signup } from "../auth/helper";

const Signup = () => {
  const [values, setValues] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    password2: "",
    error: "",
    success: false,
  });

  const {
    username,
    first_name,
    last_name,
    email,
    password,
    password2,
    error,
    success,
  } = values;

  const handleChange = (name) => (event) => {
    setValues({ ...values, error: false, [name]: event.target.value });
  };

  const onSubmit = (event) => {
    event.preventDefault();
    setValues({ ...values, error: false });
    signup({ username, first_name, last_name, email, password, password2 })
      .then((data) => {
        console.log("data : ", data);
        if (data.username === username) {
          setValues({
            ...values,
            username: "",
            first_name: "",
            last_name: "",
            email: "",
            password: "",
            password2: "",
            error: "",
            success: true,
          });
        } else {
          setValues({
            ...values,
            error: true,
            success: false,
          });
        }
      })
      .catch((e) => console.log(e));
  };

  const successMessage = () => {
    return (
      <div style={{ display: success ? "" : "none", textAlign: "center" }}>
        <h3>New user created successfully.</h3>
      </div>
    );
  };
  const errorMessage = () => {
    return (
      <div style={{ display: error ? "" : "none", textAlign: "center" }}>
        <h3>Check all fields again.</h3>
      </div>
    );
  };
  const signUpForm = () => {
    return (
      <div className="row">
        <div className="col-lg-3"></div>
        <div className="col-lg-6 registration-sec">
          <form>
            <div className="form-group">
              <div className="col-lg-12 input-design">
                <input
                  type="text"
                  name="first_name"
                  className="form-control"
                  value={first_name}
                  onChange={handleChange("first_name")}
                  placeholder="First Name"
                />
              </div>
              <div className="col-lg-12 input-design">
                <input
                  type="text"
                  name="last_name"
                  className="form-control"
                  value={last_name}
                  onChange={handleChange("last_name")}
                  placeholder="Last Name"
                />
              </div>
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
                  type="email"
                  name="email"
                  className="form-control"
                  value={email}
                  onChange={handleChange("email")}
                  placeholder="Email"
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
                <input
                  type="password"
                  name="password2"
                  class="form-control"
                  value={password2}
                  onChange={handleChange("password2")}
                  placeholder="Confirm Password"
                />
              </div>
              <div className="col-lg-12 input-design">
                <center>
                  <input
                    type="submit"
                    className="sub-btn"
                    value="Register"
                    onClick={onSubmit}
                  />
                </center>
              </div>
            </div>
          </form>
        </div>
        <div className="col-lg-3"></div>
      </div>
    );
  };
  return (
    <Base>
      {signUpForm()}
      {successMessage()}
      {errorMessage()}
    </Base>
  );
};

export default Signup;
