import React from 'react';
import TextInput from '../common/TextInput';
import SelectInput from '../common/SelectInput';

const GameForm = ({game, locations, game_types, onSave, onChange, saving, errors}) => {
  return (
    <form id="create_game_form">
      <h1 id="create_game_header">Create Game</h1>
      <SelectInput
        name="game_type"
        label="Game Type"
        class="custom-select"
        value={game.game_type}
        options={game_types}
        onChange={onChange}/>

      <TextInput
        name="game_name"
        label="Game Name"
        value={game.game_name}
        onChange={onChange}/>

      <div class="row row-space">
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
      </div>
      <br/>

      <SelectInput
        name="location"
        label="Location"
        value={game.location}
        options={locations}
        onChange={onChange}/>

      <br/> <br/>

      <div class="row row-space">
        <label for="min_players">Min Players</label>
        <input
          name="min_players"
          type="number"
          class="quantity"
          label="Minimum Number of Players"
          value={game.min_players}
          onChange={onChange} />

        <label for="max_players">Max Players</label>
        <input
          name="max_players"
          type="number"
          class="quantity"
          label="Maximum Number of Players"
          value={game.max_players}
          onChange={onChange}/>

        <br/>

        <label for="num_teams">Number of Teams</label>
        <input
          name="num_teams"
          type="number"
          class="quantity"
          label="Number of Teams"
          value={game.num_teams}
          onChange={onChange}/>
        </div>
      <br/> <br/>

      <TextInput
        name="description"
        label="Custom Description"
        value={game.description}
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
