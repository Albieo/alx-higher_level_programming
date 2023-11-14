#!/usr/bin/node
exports.esrever = function (list) {
  reversed_list = [];
  for (let i = list.length - 1; i > -1; i--) {
    reversed_list.push(list[i]);
  }
  return reversed_list;
};
