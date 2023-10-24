#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const [, , URL, file] = process.argv;

request(URL, { json: true }, (_, data) => {
  fs.writeFile(file, data.body, 'utf8', err => {
    if (err) console.log(err);
  });
});
