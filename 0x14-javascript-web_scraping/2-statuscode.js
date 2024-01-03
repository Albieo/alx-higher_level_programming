#!/usr/bin/node
const request = require('request');

function getRequestStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}

const url = process.argv[2];
getRequestStatusCode(url);
