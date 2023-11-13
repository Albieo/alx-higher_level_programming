#!/usr/bin/node
if (process.argv.length <= 2) {
    console.log('Missing size');
} else if (Number.isInteger((parseInt(process.argv[2]))) == false) {
    console.log('Missing size');
} else {
    const size = parseInt(process.argv[2]);
    for (let i = 0; i < size; i++) {
        let line = '';
        for (let j = 0; j < size; j++) {
            line += 'X';
        }
        console.log(line);
    }
}
