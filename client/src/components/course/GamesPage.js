import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import GameList from './GameList';
import {browserHistory} from 'react-router';
import toastr from 'toastr';

class GamesPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.redirectToAddCoursePage = this.redirectToAddCoursePage.bind(this);
    this.joinGame = this.joinGame.bind(this);
  }

  courseRow(game, index) {
    return <div key={index}>{game.name}</div>;
  }

  redirectToAddCoursePage() {
    browserHistory.push('/course');
  }

  joinGame(game) {
    
      debugger;
      const joined_game = game;
      joined_game.joined = true;
      let games = this.state.games.map(ex_game => {
        if(ex_game.id_game == joined_game.id_game){
          return joined_game;
        } else {
          return ex_game;
        }
      });
      
      toastr.success("Joined Game in " + game.location + " on " + game.game_day);
      return this.setState({games});
  }

  render() {
    const {games} = this.props;

    return (
      <div>
        <h1>Games</h1>
        <input type="submit"
               value="Add Game"
               className="btn btn-primary"
               onClick={this.redirectToAddCoursePage}/>
        <GameList games={games} joinGameFunc={this.joinGame}/>
      </div>
    );
  }
}

GamesPage.propTypes = {
  games: PropTypes.array.isRequired,
  actions: PropTypes.object.isRequired
};

function mapStateToProps(state, ownProps) {
  return {
    games: state.games.map(game => {
      game.joined = false;
      return game;
    })
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(GamesPage);
