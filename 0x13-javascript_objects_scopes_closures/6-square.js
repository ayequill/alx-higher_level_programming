#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) console.log(c.repeat(this.width));
    } else {
      return this.print();
    }
  }
}

module.exports = Square;
