#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  reversed_list = [];
  for (i; i >= 0; i--) {
    reversed_list.push(list[i]);
  }
  return reversed_list;
};
