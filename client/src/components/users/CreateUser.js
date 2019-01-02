import React from 'react';
import TextInput from '../common/TextInput';
import SelectInput from '../common/SelectInput';

const CourseForm = ({game, locations, onSave, onChange, saving}) => {
  return (
    <form>
      <h1>Register: </h1>

      <TextInput
        name="username"
        label="Username"
        value={game.username}
        onChange={onChange}/>

      <TextInput
        name="first_name"
        label="First Name"
        value={game.first_name}
        onChange={onChange}/>

      <TextInput
        name="last_name"
        label="Last Name"
        value={game.last_name}
        onChange={onChange}/>

      <input
        name="birth"
        type="date"
        label="Birthdate"
        value={game.birth}
        onChange={onChange}/>

      <label for="sex"><b> Sex (M/F/N) </b></label>
      <select name="sex">
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="N" selected>Non-binary // Prefer to not answer</option>
      </select>
        
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
        name="phone"
        type="number"
        label="Phone Number"
        value={game.phone}
        onChange={onChange}/>

      <TextInput
        name="email"
        label="Email"
        value={game.email}
        onChange={onChange}/>

      <input
        name="pass"
        type="password"
        label="Password"
        value={game.pass}
        onChange={onChange}/>

      <TextInput
        name="description"
        label="Description"
        value={game.description}
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

CourseForm.propTypes = {
  course: React.PropTypes.object.isRequired,
  allAuthors: React.PropTypes.array,
  onSave: React.PropTypes.func.isRequired,
  onChange: React.PropTypes.func.isRequired,
  saving: React.PropTypes.bool,
  errors: React.PropTypes.object
};

export default CourseForm;
