#!/usr/bin/node

function factorial(arg) {
  return isNaN(parseInt(arg, 10))
    ? 1
    : arg === 0 || arg === 1
      ? 1
      : arg < 0
        ? 1
        : parseInt(arg, 10) * factorial(parseInt(arg, 10) - 1);
};

console.log(factorial(process.argv[2]));
