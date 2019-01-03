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
    return axios.get(`http://localhost:8000/games/all`, ).then(response => {
    // return GameApi.getAllGames().then(games => {s
      dispatch(loadGamesSuccess(response.data));
    }).catch(error => {
      throw(error);
    });
  };
}

export function saveGame(game) {
   return function (dispatch, getState) {
     dispatch(beginAjaxCall());
     debugger;
     var bodyFormData = new FormData();
     bodyFormData.set("game_type", game.game_type);
     bodyFormData.set("game_name", game.game_name);
     bodyFormData.set("game_day", game.date);
     bodyFormData.set("start_time", game.time);
     bodyFormData.set("location", game.location);
     bodyFormData.set("min_players", game.min_players);
     bodyFormData.set("max_players", game.max_players);
     bodyFormData.set("num_teams" ,game.num_teams);
     return axios({method: 'POST',
                        url: 'http://localhost:8000/games', 
                        data: bodyFormData,
                        config: { headers: {'Content-Type': 'multipart/form-data' }}
                        }).then(game => {
       game.id ? dispatch(updateGameSuccess(game)) :
         dispatch(createGameSuccess(game));
     }).catch(error => {
       dispatch(ajaxCallError(error));
       throw(error);
     });
   };
}
