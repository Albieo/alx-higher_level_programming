#!/usr/bin/node
const request = require('request');

function countCompletedTasks (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`code: ${response.statusCode}`);
      return;
    }

    const completed = {};
    const tasks = JSON.parse(body);

    tasks.forEach((task) => {
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    });

    console.log(completed);
  });
}

const url = process.argv[2];
countCompletedTasks(url);
