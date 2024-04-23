#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    const con1 = w === undefined || isNaN(Number(w)) || w <= 0;
    const cond2 = h === undefined || isNaN(Number(h)) || h <= 0;
    if (!con1 && !cond2) {
      this.width = w; this.height = h;
    }
  }

  print () {
    if (this.width !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let str1 = '';
        for (let j = 0; j < this.width; j++) {
          str1 += 'X';
        } console.log(str1);
      }
    }
  }

  rotate () {
    if (this.width !== undefined) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  double () {
    if (this.width !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
module.exports = Rectangle;
