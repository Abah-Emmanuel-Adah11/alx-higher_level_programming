#!/usr/bin/node

/* Defining the class Square */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  /* constructor call super constructor */
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
