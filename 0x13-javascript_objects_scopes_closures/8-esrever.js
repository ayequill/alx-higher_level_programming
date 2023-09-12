#!/usr/bin/node

exports.esrever = function (list) {
  return list.map((item, index, array) => array[array.length - 1 - index]);
};
