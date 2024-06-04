#!/usr/bin/node
const fs = require('fs')
const request = require('request');
const process = require('process');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, async function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let obj = JSON.parse(body);
    let dict1 = {}
    let count = 0;
    const list1 = obj.characters;
    for (let i = 0; i < list1.length; i++) {
      request(list1[i], function(err, response, body) {
        obj = JSON.parse(body);
        dict1[i + ''] = obj.name;
	count++;
	if (count === list1.length) {
          for (let j = 0; j < count; j++) {
            console.log(dict1['' + j]);
	  }
	}
	
  });
  }
}
});

