#!/usr/bin/node

const [, , num1, num2] = process.argv;

const add = (a, b) => {
  return a + b;
};

console.log(add(parseInt(num1, 10), parseInt(num2, 10)));
