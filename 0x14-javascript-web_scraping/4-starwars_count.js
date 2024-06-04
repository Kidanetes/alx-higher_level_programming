#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;

request(args[2], function (err, response, body) {
  if (err) {
    
  } else {
    const obj = JSON.parse(body);
    let j = 0;
    for (let i = 0; i < obj.results.length; i++) {
      if (obj.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        j = j + 1;
      }
    }
    console.log(j);
  }
});
