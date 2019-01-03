import React, {PropTypes} from 'react';
import GameListRow from './GameListRow';

const UserList = ({users}) => {
  console.log(users)
  return (
    <table className="table">
      <thead>
      <tr>
        <th>Username</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Birth date</th>
        <th>Sex</th> 
        <th>City</th> 
        <th>Phone</th>
        <th>Email</th>
      </tr>
      </thead>
      <tbody>
      {users.map(user =>
        <tr>
            <td>{user.username}</td>
            <td>{user.firstname}</td>
            <td>{user.lastname}</td>
            <td>{user.birth}</td>
            <td>{user.sex}</td> 
            <td>{user.city}</td> 
            <td>{user.phone}</td>
            <td>{user.email}</td>
        </tr>
      )}
      </tbody>
    </table>
  );
};

UserList.propTypes = {
  users: PropTypes.array.isRequired
};

export default UserList;