#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;
request(args[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    const dict1 = {};
    let j;
    for (let i = 0; i < obj.length; i++) {
      j = '' + obj[i].userId;
      if (j in dict1) {
        if (obj[i].completed === true) {
          dict1[j]++;
        }
      } else {
        if (obj[i].completed === true) {
          dict1[j] = 1;
        } else {
          dict1[j] = 0;
        }
      }
    }
    console.log(dict1);
  }
});
