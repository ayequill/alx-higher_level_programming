#!/usr/bin/node

const factorial = (arg) => {
  return isNaN(parseInt(arg, 10))
    ? 1
    : arg === 0 || arg === 1
      ? 1
      : arg < 0
        ? 1
        : parseInt(arg) * factorial(parseInt(arg) - 1);
};

console.log(factorial(process.argv[2]));
