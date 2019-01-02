import FilterApi from '../api/mockFilterApi';
import * as types from './actionTypes';
import {beginAjaxCall} from './ajaxStatusActions';

export function loadLocationsSuccess(authors) {
  return {type: types.LOAD_LOCATIONS_SUCCESS, authors};
}

export function loadGameTypesSuccess(authors) {
  return {type: types.LOAD_GAME_TYPES_SUCCESS, authors};
}

export function loadLocations() {
  return function(dispatch){
    dispatch(beginAjaxCall());
    return FilterApi.getAllLocations().then(locations => {
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
      dispatch(loadGameTypesSuccess(game_types));
    }).catch(error => {
      throw(error);
    });
  };
}
