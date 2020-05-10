import React from "react";
import { List, Header } from "semantic-ui-react";

const Users = ({ users }) => (
  <List>
    {users.map((user) => {
      return (
        <List.Item key={user.username}>
          <Header> {user.first_name} </Header>
        </List.Item>
      );
    })}
  </List>
);

export default Users;
