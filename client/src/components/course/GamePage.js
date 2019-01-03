import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import GameList from './GameList';
import {browserHistory} from 'react-router';
import axios from 'axios'

class GamePage extends React.Component {
  constructor(props, context) {
    super(props, context);
    const game_id = props.game_id
    this.state = {
      game_id,
      game: Object.assign({}, props.game)
    };
    this.redirectToGamesPage = this.redirectToGamesPage.bind(this);

  }

  componentDidMount() {
      axios.get(`http://localhost:8000/games/all`, ).then(response => {
        this.users = response.data;
        }).catch(error => {
            throw(error);
        })
  }

  courseRow(game, index) {
    return <div key={index}>{game.name}</div>;
  }

  redirectToGamesPage() {
    browserHistory.push('/games');
  }

  joinGame(game_id) {
    return function() {
      debugger;
      browserHistory.push('/game/' + game_id)
    }
  }

  render() {
    const {games} = this.props;

    return (
      <div>
        <h1>Games</h1>
        <input type="submit"
               value="Back to games list"
               className="btn btn-primary"
               onClick={this.redirectToGamesPage}/>
        <GameList games={games} joinGameFunc={this.joinGame}/>
      </div>
    );
  }
}

GamePage.propTypes = {
  game: PropTypes.array.isRequired,
  actions: PropTypes.object.isRequired
};

function getGameById(games, id) {
  const game = games.filter(game => game.id_game == id);
  if (game) return game[0]; //since filter returns an array, have to grab the first.
  return null;
}

function mapStateToProps(state, ownProps) {
  const gameId = ownProps.params.id;
  
  if (gameId && state.games.length > 0) {
    game = getGameById(state.games, gameId);
  }

  return {
    game_id: gameId,  
    game: state.games
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(GamePage);