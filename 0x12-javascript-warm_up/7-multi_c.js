#!/usr/bin/node

const [, , arg] = process.argv;

if (isNaN(parseInt(arg, 10))) console.log('Missing number of occurrences');

if (!isNaN(parseInt(arg))) {
  for (let i = 0; i < arg; i++) {
    if (arg < 0) {
      break;
    } else {
      console.log('C is fun');
    }
  }
}
