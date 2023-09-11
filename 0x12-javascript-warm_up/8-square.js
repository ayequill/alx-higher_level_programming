#!/usr/bin/node

const drawSquare = (arg) => {
  if (isNaN(parseInt(arg))) console.log('Missing size');

  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
};

drawSquare(process.argv[2]);
