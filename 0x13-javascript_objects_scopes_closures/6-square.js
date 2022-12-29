#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c === 'C') {
        console.log('C'.repeat(this.size));
      } else {
        console.log('X'.repeat(this.size));
      }
    }
  }
};
