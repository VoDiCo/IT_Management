import React, { Component } from "react";
import { render } from "react-dom";
import '../../static/css/index.css'
import HomePage from "./HomePage";
import Dashboard from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);