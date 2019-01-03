import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import GameForm from './GameForm';
import {authorsFormattedForDropdown} from '../../selectors/selectors';
import toastr from 'toastr';

const game_types = [{value: "basketball", label: "Basketball"}, 
                   {value: "dodgeball", label: "Dodgeball"}, 
                   {value: "frisbee", label: "Frisbee"}, 
                   {value: "gridiron", label: "Gridiron"}, 
                   {value: "hide_and_seek", label: "Hide and Seek"}, 
                   {value: "hockey", label: "Hockey"},
                   {value: "running", label: "Running"}, 
                   {value: "soccer", label: "Soccer"}, 
                   {value: "table_tennis", label: "Table Tennis"}, 
                   {value: "tennis", label: "Tennis"}, 
                   {value: "volleyball", label: "Volleyball"},
                   {value: "other", label: "Other"}]

const locations = [
                   {value: 'Tel-Aviv', label: 'Tel Aviv'}, 
                   {value: 'Netanya', label: 'Netanya'},
                   {value: 'Haifa', label: 'Haifa'},
                   {value: 'Jerusalem', label: 'Jerusalem'},
                   {value: 'Jaffa', label: 'Jaffa'},
                   ]

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

    // if (this.state.game.title.length < 5) {
    //   errors.title = 'Title must be at least 5 characters.';
    //   formIsValid = false;
    // }

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
        locations={locations}
        game_types={game_types}
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
  // locations: PropTypes.array.isRequired,
  // game_types: PropTypes.array.isRequired,
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
    game: game,
    locations: state.locations,
    game_types: state.game_types
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ManageGamePage);
