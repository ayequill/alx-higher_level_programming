#!/usr/bin/node
/**
 * Finds the second largest number
 * @param {Array} args
 * @returns {Array}
 */

const findSecondLargestNumber = (args) =>
  args.slice(2).map(Number).sort((a, b) => b - a)[1];

if (process.argv.length === 2 || process.argv.length < 4) {
  console.log(0);
} else {
  console.log(findSecondLargestNumber(process.argv));
}
