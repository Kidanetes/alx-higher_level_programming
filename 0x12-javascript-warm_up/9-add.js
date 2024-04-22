#!/usr/bin/node
const arr = process.argv;
if (arr[2] === undefined || arr[3] === undefined) {
  console.log('NaN');
} else if (isNaN(Number(arr[2])) || isNaN(Number(arr[3]))) {
  console.log('NaN');
} else {
  console.log(Number(arr[2]) + Number(arr[3]));
}
