import React, {PropTypes} from 'react';
import GameListRow from './GameListRow';

const UserList = ({users, joinGameFunc}) => {
  console.log(games)
  return (
    <table className="table">
      <thead>
      <tr>
        <th>Username</th>
        <th></th>
      </tr>
      </thead>
      <tbody>
      {users.map(user =>
        <tr>
            <td>{user.username}</td>
        </tr>
      )};
      </tbody>
    </table>
  );
};

GameList.propTypes = {
  games: PropTypes.array.isRequired
};

export default GameList;