import React, {PropTypes} from 'react';
import {Link} from 'react-router';

const GameListRow = ({game, joinGameFunc}) => {
  // <td><a href={game.watchHref} target="_blank">Watch</a></td>
  // <Link to={'/course/' + course.id}>{course.title}</Link>
  return (
    <tr style={{backgroundColor: game.joined ? "#66FF66" : "#FFF"}}>
      <td>{game.game_type}</td>
      {/* <td>{game.user}</td> */}
      <td>{game.location}</td>
      <td><Link to={'/game/' + game.id_game}>{game.game_name}</Link></td>
      <td>{game.game_day} </td>
      <td>{game.start_time}</td>
      <td> <input type="submit"
               value= {game.joined ? "Joined!" : "Join Game"}
               className="btn btn-primary"
               onClick={joinGameFunc}
               disabled={game.joined}/></td>
    </tr>
  );
};

GameListRow.propTypes = {
  game: PropTypes.object.isRequired
};

export default GameListRow;
