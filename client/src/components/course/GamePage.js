import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import UserList from './UserList';
import {browserHistory} from 'react-router';
import axios from 'axios'

class GamePage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      users: [],
      game: Object.assign({}, props.game)
    };
    this.redirectToGamesPage = this.redirectToGamesPage.bind(this);
    this.getUsers = this.getUsers.bind(this);

  }
  componentWillReceiveProps(nextProps) {
    if (this.props.game.id_game != nextProps.game.id_game) {
      this.setState({game: Object.assign({}, nextProps.game)});
    }
    this.getUsers(nextProps.game.id_game);
}

  getUsers(game_id) {
      axios.get(`http://localhost:8000/get_users_for_game/` + game_id ).then(response => {
        const users = response.data;
        this.setState({users})
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

  render() {
    const users = this.state.users;

    return (
      <div>
        <h1>{"Users in game " + this.state.game.game_name }</h1>
        <input type="submit"
               value="Back to games list"
               className="btn btn-primary"
               onClick={this.redirectToGamesPage}/>
        <UserList users={users}/>
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
  let game = {id: '', 
              game_type: '', 
              game_name: '',
              date: '', 
              time: '', 
              location: '', 
              min_players: '',
              max_players: '',
              num_teams: ''
            };

  if (gameId && state.games.length > 0) {
    game = getGameById(state.games, gameId);
  }

  return {  
    game: game
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(GamePage);