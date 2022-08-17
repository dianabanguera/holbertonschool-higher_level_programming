#!/usr/bin/node
const square = require('./4-rectangle');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
