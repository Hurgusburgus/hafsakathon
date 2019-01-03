import React, {PropTypes} from 'react';
import {Link} from 'react-router';

const GameListRow = ({game, joinGameFunc}) => {
  // <td><a href={game.watchHref} target="_blank">Watch</a></td>
  // <Link to={'/course/' + course.id}>{course.title}</Link>
  return (
    <tr>
      <td>{game.game_type}</td>
      {/* <td>{game.user}</td> */}
      <td>{game.location}</td>
      <td><Link to={'/game/' + game.id_game}>{game.game_name}</Link></td>
      <td>{game.game_day} </td>
      <td>{game.start_time}</td>
      <td> <input type="submit"
               value="Join Game"
               className="btn btn-primary"
               onClick={joinGameFunc}/></td>
    </tr>
  );
};

GameListRow.propTypes = {
  game: PropTypes.object.isRequired
};

export default GameListRow;
