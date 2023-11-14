#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
        c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let line = '';
      for (let j = 0; j < this.size; j++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
