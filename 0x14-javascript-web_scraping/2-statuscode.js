#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;
request(args[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
