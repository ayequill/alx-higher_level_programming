#!/usr/bin/node
const request = require('request');

const [, , id] = process.argv;

const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(URL, (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters

  characters.forEach((url) => {
    request(url, (_, res, body) => {
        const charData = JSON.parse(body)
        console.log(charData.name);
    });
  });
});
