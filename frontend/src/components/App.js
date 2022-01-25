import React, { Component } from "react";
import { render } from "react-dom";
import PersistentDrawerLeft from "./Drawer";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <PersistentDrawerLeft/>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);