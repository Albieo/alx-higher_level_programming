#!/usr/bin/node
const fs = require('fs');

function readFileContent (filePath) {
  fs.writeFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

const filePath = process.argv[2];
readFileContent(filePath);
