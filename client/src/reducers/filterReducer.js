import * as types from '../actions/actionTypes';
import initialState from './initialState';

function locationReducer(state = initialState.locations, action) {
  switch (action.type) {
    case types.LOAD_LOCATIONS_SUCCESS:
      return action.locations;

    default:
      return state;
  }
}
function gameTypeReducer(state = initialState.game_types, action) {
    switch (action.type) {
      case types.LOAD_GAME_TYPES_SUCCESS:
        return action.game_types;
  
      default:
        return state;
    }
}

export default {locationReducer, gameTypeReducer}
