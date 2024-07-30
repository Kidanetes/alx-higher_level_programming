#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;
const url = args[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const fs = require('fs');
    fs.writeFile(args[3], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
