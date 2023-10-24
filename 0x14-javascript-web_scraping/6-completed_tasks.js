#!/usr/bin/node
const request = require('request');

const [, , URL] = process.argv;

request(URL, { json: true }, (_, data) => {
  const completeObj = data.body.filter(todo => todo.completed);
  const obj = {};

  completeObj.forEach(user => {
    if (obj[user.userId]) obj[user.userId]++;
    else obj[user.userId] = 1;
  });
  console.log(obj);
});
