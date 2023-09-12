#!/usr/bin/node

function addMeMaybe (value, func) {
  value = value + 1;
  return func(value);
}

exports.addMeMaybe = addMeMaybe;
