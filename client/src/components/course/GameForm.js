import React from 'react';
import TextInput from '../common/TextInput';
import SelectInput from '../common/SelectInput';

const GameForm = ({game, locations, game_types, onSave, onChange, saving, errors}) => {
  return (
    <form>
      <h1>Create Game</h1>
      <SelectInput
        name="game_type"
        label="Game Type"
        value={game.game_type}
        options={game_types}
        onChange={onChange}/>

      <TextInput
        name="game_name"
        label="Game Name"
        value={game.game_name}
        onChange={onChange}/>

      <label for="date">Date of Game</label>
      <input
        name="date"
        type="date"
        label="date"
        value={game.date}
        onChange={onChange}        />

      <label for="time">Start Time: </label>  
      <input
        name="time"
        type="time"
        label="Start Time"
        value={game.time}
        onChange={onChange}/>

      <br/>

      <SelectInput
        name="location"
        label="Location"
        value={game.location}
        options={locations}
        onChange={onChange}/>

      <label for="min_players">Min Players</label>
      <input
        name="min_players"
        type="number"
        label="Minimum Number of Players"
        value={game.min_players}
        onChange={onChange} />

      <label for="max_players">Max Players</label>
      <input
        name="max_players"
        type="number"
        label="Maximum Number of Players"
        value={game.max_players}
        onChange={onChange}/>

      <br/>
      <label for="num_teams">Number of Teams</label>
      <input
        name="num_teams"
        type="number"
        label="Number of Teams"
        value={game.num_teams}
        onChange={onChange}/>

      <br/>
      <input
        type="submit"
        disabled={saving}
        value={saving ? 'Saving...' : 'Save'}
        className="btn btn-primary"
        onClick={onSave}/>
    </form>
  );
};

GameForm.propTypes = {
  game: React.PropTypes.object.isRequired,
  locations: React.PropTypes.array,
  game_types: React.PropTypes.array,
  onSave: React.PropTypes.func.isRequired,
  onChange: React.PropTypes.func.isRequired,
  saving: React.PropTypes.bool,
  errors: React.PropTypes.object
};

export default GameForm;
