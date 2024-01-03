#!/usr/bin/node
const request = require('request');

function countMoviesWithWedge (url) {
  const id = 18;
  const characterUrl = `https://swapi-api.alx-tools.com/api/people/${id}/`;
  let count = 0;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`code: ${response.statusCode}`);
      return;
    }

    JSON.parse(body).results.forEach((film) => {
      if (film.characters.includes(characterUrl)) {
        count++;
      }
    });

    console.log(count);
  });
}

const url = process.argv[2];
countMoviesWithWedge(url);
