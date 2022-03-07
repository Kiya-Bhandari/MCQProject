import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import PrivateRoutes from "./auth/helper/PrivateRoutes";
import Home from "./core/Home";
import TakeTest from "./core/TakeTest";
import History from "./core/History";
import Quiz from "./core/Quiz";
import Result from "./core/Result";
import Signup from "./user/Signup";
import Signin from "./user/Signin";

const Routes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/signup" component={Signup} />
        <Route exact path="/signin" component={Signin} />
        <PrivateRoutes exact path="/taketest" component={TakeTest} />
        <PrivateRoutes exact path="/history" component={History} />
        <PrivateRoutes exact path="/taketest/:quiz_id" component={Quiz} />

        <PrivateRoutes exact path="/result" component={Result} />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;
