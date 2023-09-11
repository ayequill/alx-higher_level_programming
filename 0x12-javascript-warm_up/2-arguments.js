#!/usr/bin/node

/**
 * Prints a message depending of the number of arguments passed
 * @returns {string}
 */

const printArgv = () => {
  const argsLen = process.argv.length;

  if (argsLen) {
    if (argsLen < 3) {
      return 'No argument';
    } else if (argsLen === 3) {
      return 'Argument found';
    }
    return 'Arguments found';
  }
};

console.log(printArgv());
