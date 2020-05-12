import React, { Component } from "react";
import { Link } from "react-router-dom";

class Header extends Component {
  state = {
    current_user: this.props.current_user,
  };

  navbar() {
    if (this.state.current_user.is_anonymous) {
      return this.forGuests();
    } else if (this.state.current_user.position) {
      return this.forManagers();
    } else {
      return this.forCrew();
    }
  }

  forManagers() {
    return (
      <div>
        <li className="nav-item">
          <a className="nav-link" href="{{url_for('edit_worker')}}">
            Edit Worker
          </a>
        </li>
        <li className="nav-item dropdown">
          <a
            className="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            Schedule
          </a>
          <div className="dropdown-menu" aria-labelledby="navbarDropdown">
            <a className="dropdown-item" href="#">
              Add Schedule
            </a>
            <a className="dropdown-item" href="#">
              Edit Schedule
            </a>
          </div>
        </li>
      </div>
    );
  }
  forGuests() {
    return (
      <div>
        <li className="nav-item">
          <a className="nav-link" href="{{url_for('register')}}">
            Register
          </a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="{{url_for('login')}}">
            Login
          </a>
        </li>
      </div>
    );
  }

  forCrew() {
    return (
      <div>
        <li className="nav-item" id="bob">
          {/*this needs work
                    <a className = 'nav-link' href="{{url_for('user', username = current_user.username)}}">{{current_user.username}}</a>*/}
          Profile
        </li>
        <li className="nav-item" id="bobby">
          <a className="nav-link" href="{{url_for('logout')}}">
            Logout
          </a>
        </li>
      </div>
    );
  }

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light mr-3">
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <a className="nav-link" href="{{url_for('home')}}">
                Home <span class="sr-only">(current)</span>
              </a>
            </li>
            {this.navbar()}
            {console.log(this.current_user)}
          </ul>
        </div>
      </nav>
    );
  }
}
export default Header;
