#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;
request(args[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    let j = 0;
    let list1;
    for (let i = 0; i < obj.results.length; i++) {
      list1 = obj.results[i].characters;
      for (let k = 0; k < list1.length; k++) {
        if (list1[k].endsWith('people/18/')) {
          j = j + 1;
        }
      }
    }
    console.log(j);
  }
});
