#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    const con1 = w === undefined || isNaN(Number(w)) || w <= 0;
    const cond2 = h === undefined || isNaN(Number(h)) || h <= 0;
    if (!con1 && !cond2) {
      this.width = w; this.height = h;
    }
  }
}
module.exports = Rectangle;
