#!/usr/bin/node
const Squaree = require('./5-square');
class Square extends Squaree {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      if (this.width !== undefined) {
        const size = this.width;
        for (let i = 0; i < size; i++) {
          let str1 = '';
          for (let j = 0; j < size; j++) {
            str1 += c;
          }
          console.log(str1);
        }
      }
    }
  }
}
module.exports = Square;
