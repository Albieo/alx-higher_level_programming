#!/usr/bin/node
const fs = require('fs');
const request = require('request');

function storeInFile (url, file) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`code: ${response.statusCode}`);
      return;
    }

    const writeStream = fs.createWriteStream(file);
    writeStream.write(body);
    writeStream.end();
  });
}

const url = process.argv[2];
const file = process.argv[3];
storeInFile(url, file);
