#!/usr/bin/node
if (process.argv.length === 2) {
    console.log('Not a number');
} else {
    number = process.argv[2];
    if (Number.isInteger(parseInt(number))) {
        console.log('My number: %s', Math.floor(number));
    } else {
        console.log('Not a number');
    }
}
