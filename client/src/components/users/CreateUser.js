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

      <label for="birth">Birthdate</label>
      <input
        name="birth"
        type="date"
        label="Birthdate"
        value={user.birth}
        onChange={onChange}/>

      <br/> <br/>

      <label for="sex"><b> Sex (M/F/N) </b></label>
      <select name="sex">
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="N" selected>Non-binary // NA</option>
      </select>
        
      <br/> <br/>
      
      <SelectInput
        name="location"
        label="Location"
        value={user.location}
        options={locations}
        onChange={onChange}/>

      <label for="phone">Phone Number</label>
      <input
        name="phone"
        type="number"
        label="Phone Number"
        value={user.phone}
        onChange={onChange}/>

      <br/> <br/>

      <label for="email">Email</label>
      <input 
        name="email"
        label="Email"
        type="email"
        value={user.email}
        onChange={onChange}/>

      <label for="pass">Password</label>
      <input
        name="pass"
        type="password"
        label="Password"
        value={user.pass}
        onChange={onChange}/>

      <br/> <br/>

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
