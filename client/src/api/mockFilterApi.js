import delay from './delay';

// This file mocks a web API by working with the hard-coded data below.
// It uses setTimeout to simulate the delay of an AJAX call.
// All calls return promises.
const locations = [
  {
    value: 'tlv',
    label: 'Tel Aviv'
  },
  {
    value: 'ha',
    label: 'Haifa'
  }
];

const game_types = [
  {
    value: 'fb', 
    label: 'Football'
  }, 
  {
    value: 'bb', 
    label: 'Basketball'
  }
];

class FiltersApi {
  
  static getAllLocations() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(Object.assign([], locations));
      }, delay);
    });
  }

  static getAllGameTypes() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(Object.assign([], game_types));
      }, delay);
    });
  }
  
}

export default FiltersApi;
