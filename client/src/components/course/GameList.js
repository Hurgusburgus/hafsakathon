import React, {PropTypes} from 'react';
import GameListRow from './GameListRow';

const GameList = ({games, joinGameFunc}) => {
  console.log(games)
  return (
    <table className="table">
      <thead>
      <tr>
        <th>Game Type</th>
        {/* <th>Creator</th> */}
        <th>Location</th>
        <th>Description</th>
        <th>Date</th>
        <th>Start Time</th>
        <th></th>
      </tr>
      </thead>
      <tbody>
      {games.map(game =>
        <GameListRow key={game.id_game} game={game} joinGameFunc={() => {return joinGameFunc(game)}}/>
      )};
      </tbody>
    </table>
  );
};

GameList.propTypes = {
  games: PropTypes.array.isRequired
};

export default GameList;
