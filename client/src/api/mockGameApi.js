import delay from './delay';

// This file mocks a web API by working with the hard-coded data below.
// It uses setTimeout to simulate the delay of an AJAX call.
// All calls return promises.
const games = [
  {
    game_id: 1,
    game_type: "Football",
    game_name: "Gabe's Football Game",
    game_day: "January 2",
    startTime: "6:20",
    location: "Haifa",
    user: "GabeR"
  },
  {
    game_id: 2,
    game_type: "Basketball",
    game_name: "Community Basketball game in Florentin",
    game_day: "January 2",
    start_time: "18:30",
    location: "Tel Aviv",
    user: "ITC"
  }
];

function replaceAll(str, find, replace) {
  return str.replace(new RegExp(find, 'g'), replace);
}

//This would be performed on the server in a real app. Just stubbing in.
const generateId = (course) => {
  return replaceAll(course.title, ' ', '-');
};

class GameApi {
  static getAllGames() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(Object.assign([], games));
      }, delay);
    });
  }

  // static saveGame(game) {
  //   game = Object.assign({}, game); // to avoid manipulating object passed in.
  //   return new Promise((resolve, reject) => {
  //     setTimeout(() => {
  //       // Simulate server-side validation
  //       const minCourseTitleLength = 1;
  //       if (game.title.length < minCourseTitleLength) {
  //         reject(`Title must be at least ${minCourseTitleLength} characters.`);
  //       }

  //       if (course.id) {
  //         const existingCourseIndex = courses.findIndex(a => a.id == course.id);
  //         courses.splice(existingCourseIndex, 1, course);
  //       } else {
  //         //Just simulating creation here.
  //         //The server would generate ids and watchHref's for new courses in a real app.
  //         //Cloning so copy returned is passed by value rather than by reference.
  //         course.id = generateId(course);
  //         course.watchHref = `http://www.pluralsight.com/courses/${course.id}`;
  //         courses.push(course);
  //       }

  //       resolve(course);
  //     }, delay);
  //   });
  // }

  // static deleteGame(gameId) {
  //   return new Promise((resolve, reject) => {
  //     setTimeout(() => {
  //       const indexOfCourseToDelete = games.findIndex(course => {
  //         return game.gameId == courseId;
  //       });
  //       courses.splice(indexOfCourseToDelete, 1);
  //       resolve();
  //     }, delay);
  //   });
  // }
}

export default GameApi;
