#!/usr/bin/node
const request = require('request');

const [, , URL] = process.argv;
const film = 'https://swapi-api.alx-tools.com/api/people/18/';

request(URL, { json: true }, (_, data) => {
  console.log(data.body.results.filter(mov => {
    return mov.characters.includes(film);
  }).length);
});
