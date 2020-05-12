import React from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";
import Users from "./components/Users";
import Header from "./components/Header2";

class App extends React.Component {
  state = { users: [], current_user: {} };

  componentDidMount() {
    fetch("/users").then((response) =>
      response.json().then((data) => {
        this.addUsers(data.users);
        this.set_current_user(data.current_user);
      })
    );
    fetch("/getUrl", { method: "PUT", body: "login" }).then((response) =>
      response.json().then((data) => {
        console.log(data.url);
      })
    );
  }

  addUsers = (users) => {
    this.setState({ users: users });
  };

  set_current_user = (current_user) => {
    this.setState({ current_user: current_user });
  };

  render() {
    return (
      <Router>
        <div className="App">
          {/*<Header current_user={this.state.current_user} />*/}
          <Users users={this.state.users} />
          <h1>{this.state.current_user.first_name}</h1>
        </div>
      </Router>
    );
  }
}

export default App;
