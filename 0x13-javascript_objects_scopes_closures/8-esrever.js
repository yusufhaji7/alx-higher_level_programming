#!/usr/bin/node
exports.esrever = function (list) {
  const emptyList = [];
  for (let i = 0; i < list.length; i++) {
    emptyList[i] = list[list.length - i - 1];
  }
  return (emptyList);
};
