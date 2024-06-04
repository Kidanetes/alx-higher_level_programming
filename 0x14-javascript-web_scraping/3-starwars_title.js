#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
}
);
