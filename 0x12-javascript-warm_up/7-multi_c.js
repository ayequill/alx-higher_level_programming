#!/usr/bin/node

const [, , arg] = process.argv;
if (arg < 0) {
  // Do nothing
} else {
  console.log(
    isNaN(parseInt(arg, 10))
      ? 'Missing number of occurrences'
      : 'C is fun\n'.repeat(arg)
  );
}
