#!/usr/bin/node
const request = require('request');

const [, , id] = process.argv;

const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(URL, { json: true }, (err, data) => {
  if (err) console.log(err);
  data.body.characters.forEach(char => {
    request(char, { json: true }, (_, x) => console.log(x.body.name));
  });
});
