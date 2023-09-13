#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

Object.entries(dict).map(([userID, occurrence]) => {
  newDict[occurrence] = newDict[occurrence] || [];
  newDict[occurrence].push(userID);
  return newDict;
});

console.log(newDict);
