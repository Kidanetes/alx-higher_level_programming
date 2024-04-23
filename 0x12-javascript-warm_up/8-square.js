#!/usr/bin/node
const arr = process.argv;
let i = 0;
if (arr[2] === undefined || isNaN(Number(arr[2]))) {
  console.log('Missing size');
} else {
  const x = Number(arr[2]);
  while (i < x) {
    let str1 = '';
    let j = 0;
    while (j < x) {
      str1 += 'X';
      j++;
    } console.log(str1);
    i++;
  }
}
