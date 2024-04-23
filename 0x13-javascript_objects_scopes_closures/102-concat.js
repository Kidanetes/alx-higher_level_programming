#!/usr/bin/node
const arr = process.argv;
const fs = require('fs');
const s1 = fs.readFileSync('./' + arr[2]);
const s2 = fs.readFileSync('./' + arr[3]);
const s3 = s1 + s2;
fs.writeFileSync('./' + arr[4], s3);
