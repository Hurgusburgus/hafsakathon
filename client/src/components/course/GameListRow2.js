import React, {PropTypes} from 'react';
import {Link} from 'react-router';

const GameListRow = ({game}) => {
  // <td><a href={game.watchHref} target="_blank">Watch</a></td>
  // <Link to={'/course/' + course.id}>{course.title}</Link>
  return (
    <div>
      <div>{game.gameType}</div>
      <div>{game.user}</div>
      <div>{game.location}</div>
      <div>{game.gameName}</div>
      <div>{game.date + ' ' + game.startTime}</div>
    </div>
  );
};

GameListRow.propTypes = {
  game: PropTypes.object.isRequired
};

export default GameListRow;
