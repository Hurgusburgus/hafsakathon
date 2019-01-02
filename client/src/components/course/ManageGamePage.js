import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import GameForm from './GameForm';
import {authorsFormattedForDropdown} from '../../selectors/selectors';
import toastr from 'toastr';

export class ManageGamePage extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      game: Object.assign({}, props.game),
      errors: {},
      saving: false
    };

    this.updateGameState = this.updateGameState.bind(this);
    this.saveGame = this.saveGame.bind(this);
  }

  componentWillReceiveProps(nextProps) {
    if (this.props.game.id_game != nextProps.game.id_game) {
      this.setState({game: Object.assign({}, nextProps.game)});
    }
  }

  updateGameState(event) {
    const field = event.target.name;
    let game = Object.assign({}, this.state.game);
    game[field] = event.target.value;
    return this.setState({game: game});
  }

  gameFormIsValid() {
    let formIsValid = true;
    let errors = {};

    if (this.state.game.title.length < 5) {
      errors.title = 'Title must be at least 5 characters.';
      formIsValid = false;
    }

    this.setState({errors: errors});
    return formIsValid;
  }


  saveGame(event) {
    event.preventDefault();

    if (!this.gameFormIsValid()) {
      return;
    }

    this.setState({saving: true});

    this.props.actions.saveGame(this.state.game)
      .then(() => this.redirect())
      .catch(error => {
        toastr.error(error);
        this.setState({saving: false});
      });
  }

  redirect() {
    this.setState({saving: false});
    toastr.success('Game saved');
    this.context.router.push('/games');
  }

  render() {
    return (
      <GameForm
        allAuthors={this.props.authors}
        onChange={this.updateGameState}
        onSave={this.saveGame}
        game={this.state.game}
        errors={this.state.errors}
        saving={this.state.saving}
      />
    );
  }
}

ManageGamePage.propTypes = {
  game: PropTypes.object.isRequired,
  authors: PropTypes.array.isRequired,
  actions: PropTypes.object.isRequired
};

//Pull in the React Router context so router is available on this.context.router.
ManageGamePage.contextTypes = {
  router: PropTypes.object
};

function getGameById(games, id) {
  const game = games.filter(game => game.id_game == id);
  if (game) return game[0]; //since filter returns an array, have to grab the first.
  return null;
}

function mapStateToProps(state, ownProps) {
  const gameId = ownProps.params.id;

  let game = {id: '', watchHref: '', title: '', authorId: '', length: '', category: ''};

  if (gameId && state.games.length > 0) {
    game = getCourseById(state.games, courseId);
  }

  return {
    game: game,
    authors: authorsFormattedForDropdown(state.authors)
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ManageGamePage);
