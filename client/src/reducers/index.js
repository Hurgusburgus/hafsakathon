import {combineReducers} from 'redux';
import games from './courseReducer';
import filters from './filterReducer'
import ajaxCallsInProgress from './ajaxStatusReducer';

const rootReducer = combineReducers({
  games,
  filters,
  ajaxCallsInProgress
});

export default rootReducer;
