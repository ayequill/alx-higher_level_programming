#!/usr/bin/node

const [, , arg] = process.argv;
const parsedArg = parseInt(arg, 10);

console.log(isNaN(parsedArg) ? 'Not a number' : `My number: ${parsedArg}`);
