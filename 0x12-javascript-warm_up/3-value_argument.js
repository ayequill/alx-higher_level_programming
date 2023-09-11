#!/usr/bin/node

/**
 * Prints the first arg passed
 * @returns {string}
 */

const printArg = () => {
  const argsLen = process.argv.length;

  if (argsLen) {
    if (argsLen < 3) {
      return 'No argument';
    }
    return process.argv[2];
  }
};

console.log(printArg());
