import React from 'react';

class AboutPage extends React.Component {
  render() {
    return (
      <div>
        <h1>About Recess</h1>
        <p>Recess was built for the Israel Tech Challenge Hackathon.</p>
        <p>We intended to tackle three issues facing community: Tech Addiction, Social Isolation and Fitness.</p> 
        <br/>
        <h1>The Team</h1>
        <p>Developers: Gabe Rimmon, Guy Ginton, Oren Chikli, Shay Weinstein, Smadar Danon.</p>
        <p>Front lead: Gabe Rimmon, Guy Ginton.</p>
        <p>Back lead: Oren Chikli, Shay Weinstein, Smadar Danon.</p>
        <p>Google analytics: Shay Weinstein</p>
        <br/>
        <h1>Tech Specs</h1>
        <p>Front end uses React, Redux, React Router and a variety of other helpful libraries.</p>
        <p>Back end uses Python and requires Yarn, Node.js and NPM to run.</p>
        <p>Analytics are provided through Google Tag Manager, Google Analytics, Google Data Studio</p>
        <p>The Recess demo uses SQLite. A public version uses DB4Free.net.</p>
      </div>
    );
  }
}

export default AboutPage;
