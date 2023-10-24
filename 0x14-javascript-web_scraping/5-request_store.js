#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const [, , URL, file] = process.argv;

request(URL, (_, res, body) => {
  fs.writeFile(file, body, 'utf8', err => {
    if (err) console.log(err);
  });
});
