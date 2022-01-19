import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import TemporaryDrawer from "./SideBar";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
      <div>
        <TemporaryDrawer/>
      </div>
      <div>
        <HomePage/>
      </div>
          </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);