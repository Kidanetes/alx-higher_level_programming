#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const keys in dict) {
  newDict[dict[keys]] = [];
} for (const keys in dict) {
  newDict[dict[keys]].push(keys);
} console.log(newDict);
