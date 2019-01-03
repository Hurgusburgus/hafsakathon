import {combineReducers} from 'redux';
import games from './courseReducer';
import {locationReducer, gameTypeReducer} from './filterReducer';
import ajaxCallsInProgress from './ajaxStatusReducer';

const rootReducer = combineReducers({
  games,
  locationReducer,
  gameTypeReducer,
  ajaxCallsInProgress
});

export default rootReducer;
