import * as types from './actionTypes';
import GameApi from '../api/mockGameApi';
import axios from 'axios';
import {beginAjaxCall, ajaxCallError} from './ajaxStatusActions';

export function loadGamesSuccess(games) {
  return { type: types.LOAD_GAMES_SUCCESS, games};
}

export function createGameSuccess(game) {
  return {type: types.CREATE_GAME_SUCCESS, game};
}

export function updateGameSuccess(game) {
  return {type: types.UPDATE_GAME_SUCCESS, game};
}

export function loadGames() {
  return function(dispatch) {
    dispatch(beginAjaxCall());
    return axios.get(`http://localhost:8000/games/all`).then(games => {
      console.log(games)
    // return GameApi.getAllGames().then(games => {
      dispatch(loadGamesSuccess(games));
    }).catch(error => {
      throw(error);
    });
  };
}

// export function saveCourse(game) {
//   return function (dispatch, getState) {
//     dispatch(beginAjaxCall());
//     return GameApi.saveGame(game).then(game => {
//       game.id ? dispatch(updateGameSuccess(game)) :
//         dispatch(createGameSuccess(game));
//     }).catch(error => {
//       dispatch(ajaxCallError(error));
//       throw(error);
//     });
//   };
//}
