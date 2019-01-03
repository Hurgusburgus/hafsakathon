import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import GameList from './GameList';
import {browserHistory} from 'react-router';

class GamesPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.redirectToAddCoursePage = this.redirectToAddCoursePage.bind(this);
  }

  courseRow(game, index) {
    return <div key={index}>{game.name}</div>;
  }

  redirectToAddCoursePage() {
    browserHistory.push('/course');
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
    games: state.games
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(GamesPage);
