import {combineReducers} from 'redux';
import games from './courseReducer';
import authors from './authorReducer';
import ajaxCallsInProgress from './ajaxStatusReducer';

const rootReducer = combineReducers({
  games,
  authors,
  ajaxCallsInProgress
});

export default rootReducer;
