import React from 'react';
import {Link} from 'react-router';

class HomePage extends React.Component {
  render() {
    return (
      <div className="jumbotron">
        <h1>Recess</h1>
        <p>An app to get off your phone</p>
        <Link to="games" className="btn btn-primary btn-lg">Play</Link>
      </div>
    );
  }
}

export default HomePage;
