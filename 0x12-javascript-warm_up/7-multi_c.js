#!/usr/bin/node
if (process.argv.length <= 2) {
    console.log('Missing number of occurrences');
} else {
    number = parseInt(process.argv[2]);
    while (number > 0) {
        console.log('C is fun');
        number -= 1;
    }
}
