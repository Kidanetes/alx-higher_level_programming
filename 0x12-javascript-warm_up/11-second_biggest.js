#!/usr/bin/node
const arr = process.argv;
let j = 2;
for (j = 2; j < arr.length; j++) {
  arr[j] = Number(arr[j]);
} if (arr.length === 2 || arr.length === 3) {
  console.log(0);
} else {
  let max; let max2; let i = 4;
  if (arr[2] >= arr[3]) {
    max = arr[2]; max2 = arr[3];
  } else {
    max = arr[3]; max2 = arr[2];
  } while (i < arr.length) {
    if (arr[i] > max) {
      max2 = max; max = arr[i];
    } else if (arr[i] >= max2) {
      max2 = arr[i];
    } i++;
  }
  console.log(max2);
}
