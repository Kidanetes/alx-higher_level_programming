#!/usr/bin/node
const arr = process.argv;
console.log(factorial(Number(arr[2])));

function factorial (num) {
  if (num === undefined || isNaN(num) || num === 0) {
    return (1);
  } return num * factorial(num - 1);
}
