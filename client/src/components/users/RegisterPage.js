import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as gameActions from '../../actions/gameActions';
import UserForm from './CreateUser';
import {authorsFormattedForDropdown} from '../../selectors/selectors';
import toastr from 'toastr';

const locations = [
                   {value: 'Tel-Aviv', label: 'Tel Aviv'}, 
                   {value: 'Netanya', label: 'Netanya'},
                   {value: 'Haifa', label: 'Haifa'},
                   {value: 'Jerusalem', label: 'Jerusalem'},
                   {value: 'Jaffa', label: 'Jaffa'},
                   ]

export class RegisterPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    const user = {
        username: "", 
        first_name:"", 
        last_name: "", 
        birth: "",
        sex: "", 
        location:"", 
        phone: "",
        email: "", 
        pass: "", 
        description: ""
    }
    this.state = {
      user: Object.assign({}, user),
      errors: {},
      saving: false
    };
    this.saveGame = this.saveGame.bind(this);
  }

  userFormIsValid() {
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

    if (!this.userFormIsValid()) {
      return;
    }

    this.setState({saving: true});

    this.redirect();
  }

  redirect() {
    this.setState({saving: false});
    toastr.success('User registered!');
    this.context.router.push('/games');
  }

  updateFormState(event) {
    const field = event.target.name;
    let user = Object.assign({}, this.state.user);
    user[field] = event.target.value;
    return this.setState({user: user});
  }

  render() {
    return (
      <UserForm
        locations={locations}
        onSave={this.saveGame}
        user={this.state.user}
        onChange={this.updateFormState}
        errors={this.state.errors}
        saving={this.state.saving}
      />
    );
  }
}

RegisterPage.propTypes = {
  actions: PropTypes.object.isRequired
};

//Pull in the React Router context so router is available on this.context.router.
RegisterPage.contextTypes = {
  router: PropTypes.object
};


function mapStateToProps(state, ownProps) {
  return {}
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(gameActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(RegisterPage);
