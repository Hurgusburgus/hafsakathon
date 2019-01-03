import FilterApi from '../api/mockFilterApi';
import * as types from './actionTypes';
import {beginAjaxCall} from './ajaxStatusActions';

export function loadLocationsSuccess(locations) {
  return {type: types.LOAD_LOCATIONS_SUCCESS, locations};
}

export function loadGameTypesSuccess(game_types) {
  return {type: types.LOAD_GAME_TYPES_SUCCESS, game_types};
}

export function loadLocations() {
  return function(dispatch){
    dispatch(beginAjaxCall());
    return FilterApi.getAllLocations().then(locations => {
      console.log(locations);
      dispatch(loadLocationsSuccess(locations));
    }).catch(error => {
      throw(error);
    });
  };
}

export function loadGameTypes() {
  return function(dispatch){
    dispatch(beginAjaxCall());
    return FilterApi.getAllGameTypes().then(game_types => {
      console.log(game_types);
      dispatch(loadGameTypesSuccess(game_types));
    }).catch(error => {
      throw(error);
    });
  };
}
