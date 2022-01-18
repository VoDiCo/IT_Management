import React, { Component } from "react";
import {Button} from "@mui/material";
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <>
        <Button variant="contained">Contained</Button>
      </>
    );
  }
}