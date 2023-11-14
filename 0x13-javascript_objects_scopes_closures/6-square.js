#!/usr/bin/node
const FirstSquare = require('./5-square');

class Square extends FirstSquare {
  constructor (size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
        c = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
