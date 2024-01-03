#!/usr/bin/node
const request = require('request');

function countMoviesWithWedge (url) {
  const id = 18;
  const characterUrl = `https://swapi-api.alx-tools.com/api/people/${id}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`code: ${response.statusCode}`);
      return;
    }

    const filmData = JSON.parse(body).results;
    let count = 0;

    filmData.forEach(film => {
      if (film.characters.includes(characterUrl)) {
        count++;
      }
    });

    console.log(count);
  });
}

const url = process.argv[2];
countMoviesWithWedge(url);
