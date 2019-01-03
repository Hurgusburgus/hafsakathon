import React, {PropTypes} from 'react';
import {Link} from 'react-router';

const GameListRow = ({game}) => {
  // <td><a href={game.watchHref} target="_blank">Watch</a></td>
  // <Link to={'/course/' + course.id}>{course.title}</Link>
  return (
    <tr>
      <td>{game.game_type}</td>
      <td>{game.user}</td>
      <td>{game.location}</td>
      <td>{game.game_name}</td>
      <td>{game.game_day} {game.start_day}</td>
      <td> <button type="button" className="btn btn-default">Join Game</button></td>
    </tr>
  );
};

GameListRow.propTypes = {
  game: PropTypes.object.isRequired
};

export default GameListRow;
