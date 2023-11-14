#!/usr/bin/node
exports.esrever = function (list) {
  reversed_list = [];
  for (element of list) {
    reversed_list += element;
  }
  return (reversed_list);
}
