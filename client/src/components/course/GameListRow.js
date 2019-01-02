import React, {PropTypes} from 'react';
import {Link} from 'react-router';

const GameListRow = ({game}) => {
  // <td><a href={game.watchHref} target="_blank">Watch</a></td>
  // <Link to={'/course/' + course.id}>{course.title}</Link>
  return (
    <tr>
      <td>{game.gameType}</td>
      <td>{game.user}</td>
      <td>{game.location}</td>
      <td>{game.gameName}</td>
      <td>{game.date} {game.startTime}</td>
    </tr>
  );
};

GameListRow.propTypes = {
  game: PropTypes.object.isRequired
};

export default GameListRow;
