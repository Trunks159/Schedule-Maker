import React from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";
import Users from "./components/Users";

class App extends React.Component {
  state = { users: [] };

  componentDidMount() {
    fetch("/users").then((response) =>
      response.json().then((data) => {
        this.addUsers(data.users);
      })
    );
  }

  addUsers = (users) => {
    this.setState({ users: users });
  };

  render() {
    return (
      <Router>
        <div className="App">
          <Users users={this.state.users} />
        </div>
      </Router>
    );
  }
}

export default App;
