import React, {PropTypes} from 'react';
import GameListRow from './GameListRow';

const GameList = ({games}) => {
  console.log(games)
  return (
    <table className="table">
      <thead>
      <tr>
        <th>What</th>
        <th>Who</th>
        <th>Where</th>
        <th>Description</th>
        <th>When</th>
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
