#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    const con1 = w === undefined || isNaN(Number(w)) || w <= 0;
    const cond2 = h === undefined || isNaN(Number(h)) || h <= 0;
    if (!con1 && !cond2) {
      this.width = w; this.height = h;
    }
  } 
  print() {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let str1 = '';
	for (let j = 0; j < this.width; j++) {
	  str1 += 'X';
	} console.log(str1);
      }
    }
  }
}
module.exports = Rectangle;
