import React from 'react';
import { Route, IndexRoute } from 'react-router';
import App from './components/App';
import HomePage from './components/home/HomePage';
import AboutPage from './components/about/AboutPage';
import GamesPage from './components/course/GamesPage';
import GamePage from './components/course/GamePage';
import ManageGamePage from './components/course/ManageGamePage'; //eslint-disable-line import/no-named-as-default

export default (
  <Route path="/" component={App}>
    <IndexRoute component={HomePage} />
    <Route path="games" component={GamesPage} />
    <Route path="course" component={ManageGamePage} />
    <Route path="game/:id" component={GamePage} />
    <Route path="course/:id" component={ManageGamePage} />
    <Route path="about" component={AboutPage} />
  </Route>
);
