import React from 'react';
import TextInput from '../common/TextInput';
import SelectInput from '../common/SelectInput';

const GameForm = ({game, locations, game_types, onSave, onChange, saving, errors}) => {
  return (
    <form>
      <h1>Manage Course</h1>
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

      <input
        name="date"
        type="date"
        label="Date"
        value={game.date}
        onChange={onChange}/>
        
      <input
        name="time"
        type="time"
        label="Start Time"
        value={game.time}
        onChange={onChange}/>

      <SelectInput
        name="location"
        label="Location"
        value={game.location}
        defaultOption="tag"
        options={locations}
        onChange={onChange}/>

      <input
        name="min_players"
        type="number"
        label="Minimum Number of Players"
        value={game.min_players}
        onChange={onChange}/>

      <input
        name="max_players"
        type="number"
        label="Maximum Number of Players"
        value={game.max_players}
        onChange={onChange}/>

      <input
        name="num_teams"
        type="number"
        label="Number of Teams"
        value={game.num_teams}
        onChange={onChange}/>

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
