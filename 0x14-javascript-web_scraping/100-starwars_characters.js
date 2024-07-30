#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let obj = JSON.parse(body);
    const list1 = obj.characters;
    for (let i = 0; i < list1.length; i++) {
      request(list1[i], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          obj = JSON.parse(body);
          console.log(obj.name);
        }
      });
    }
  }
});
