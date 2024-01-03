#!/usr/bin/node
const request = require('request');

function getStarWarsTitle (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`code: ${response.statusCode}`);
      return;
    }
    console.log(JSON.parse(body).title);
  });
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
getStarWarsTitle(url);
