import React, {PropTypes} from 'react';
import GameListRow from './GameListRow';

const GameList = ({games}) => {
  console.log(games)
  return (
    <table className="table">
      <thead>
      <tr>
        <th>Game Type</th>
        <th>Creator</th>
        <th>Location</th>
        <th>Description</th>
<<<<<<< HEAD
        <th>When</th>
        <th></th>
=======
        <th>Start Time</th>
>>>>>>> 244c96f578bb4d017c5ecdea748d3ca9bfde5316
      </tr>
      </thead>
      <tbody>
      {games.map(game =>
        <GameListRow key={game.id_game} game={game}/>
      )};
      </tbody>
    </table>
  );
};

GameList.propTypes = {
  games: PropTypes.array.isRequired
};

export default GameList;
