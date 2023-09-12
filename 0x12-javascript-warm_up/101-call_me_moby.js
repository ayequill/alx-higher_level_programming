#!/usr/bin/node

/**
 * Description
 * @param {Number} n
 * @param {Function} moby
 * @returns {null}
 */
function callMeMoby (n, moby) {
  if (n <= 0) return;
  moby();
  callMeMoby(n - 1, moby);
}

exports.callMeMoby = callMeMoby;
