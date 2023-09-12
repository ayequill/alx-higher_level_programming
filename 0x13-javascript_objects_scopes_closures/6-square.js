#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) return this.print();
    for (let i = 0; i < this.height; i++) console.log('C'.repeat(this.width));
  }
}

module.exports = Square;
