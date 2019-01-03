import React from 'react';
import TextInput from '../common/TextInput';
import SelectInput from '../common/SelectInput';

const UserForm = ({user, locations, onSave, onChange, saving}) => {
  return (
    <form>
      <h1>Register: </h1>

      <TextInput
        name="username"
        label="Username"
        value={user.username}s
        onChange={onChange}/>

      <TextInput
        name="first_name"
        label="First Name"
        value={user.first_name}
        onChange={onChange}/>

      <TextInput
        name="last_name"
        label="Last Name"
        value={user.last_name}
        onChange={onChange}/>

      <input
        name="birth"
        type="date"
        label="Birthdate"
        value={user.birth}
        onChange={onChange}/>

      <label for="sex"><b> Sex (M/F/N) </b></label>
      <select name="sex">
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="N" selected>Non-binary // Prefer to not answer</option>
      </select>
        
      <SelectInput
        name="location"
        label="Location"
        value={user.location}
        defaultOption="tag"
        options={locations}
        onChange={onChange}/>

      <input
        name="phone"
        type="number"
        label="Phone Number"
        value={user.phone}
        onChange={onChange}/>

      <TextInput
        name="email"
        label="Email"
        value={user.email}
        onChange={onChange}/>

      <input
        name="pass"
        type="password"
        label="Password"
        value={user.pass}
        onChange={onChange}/>

      <TextInput
        name="description"
        label="Description"
        value={user.description}
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

UserForm.propTypes = {
  user: React.PropTypes.object.isRequired,
  locations: React.PropTypes.array.isRequired,
  onSave: React.PropTypes.func.isRequired,
  onChange: React.PropTypes.func.isRequired,
  saving: React.PropTypes.bool,
  errors: React.PropTypes.object
};

export default UserForm;
