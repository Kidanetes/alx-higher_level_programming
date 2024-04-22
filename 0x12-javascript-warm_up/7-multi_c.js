#!/usr/bin/node
const arr = process.argv;
let i = 0;
if (arr[2] === undefined || isNaN(Number(arr[2]))) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(arr[2]);
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
