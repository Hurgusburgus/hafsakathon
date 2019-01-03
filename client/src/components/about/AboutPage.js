import React from 'react';

class AboutPage extends React.Component {
  render() {
    return (
      <div>
        <h1>About Recess</h1>
        <p>Recess was built for the Israel Tech Challenge Hackathon</p>
        <p>Team: Gabe Rimmon, Guy Ginton, Oren Chikli, Shay Weinstein, Smadar Danon </p>
        <p>Front end uses React, Redux, React Router and a variety of other helpful libraries.</p>
        <p>Back end uses Python.</p>
        <p>There are two versions of back end: Local using SQLite and Public using DB4Free.net.</p>
      </div>
    );
  }
}

export default AboutPage;
