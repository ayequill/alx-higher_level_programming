#!/usr/bin/node

/**
 * Prints the first arg passed
 * @returns {string}
 */

const printArg = () => {
  let count = 0;

  process.argv.forEach((_) => (count += 1));

  if (count < 3) {
    return 'No argument';
  }
  return process.argv[2];
};

console.log(printArg());
