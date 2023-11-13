#!/usr/bin/node
exports.add = function (a, b) {
    if (a == undefined || b == undefined) {
        return (NaN);
    } else {
        return (parseInt(a) + parseInt(b));
    };
};