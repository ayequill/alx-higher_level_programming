#!/usr/bin/node
const fs = require('fs');

const [, , file, content] = process.argv;

fs.writeFile(file, content, 'utf8', (err) => {
  if (err) console.log(err);
});
