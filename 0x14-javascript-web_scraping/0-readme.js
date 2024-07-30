#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const args = process.argv;
fs.readFile(args[2], function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
