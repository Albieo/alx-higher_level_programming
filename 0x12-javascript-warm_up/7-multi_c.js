#!/usr/bin/node
/*
    Write a script that prints x times “C is fun”
    
    -> Where x is the first argument of the script
    -> If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    -> You must use console.log(...) to print all output
    -> You are not allowed to use var
    -> You can use only one console.log
    -> You must use a loop (while, for, etc.)
*/


if (process.argv.length <= 2) {
    console.log("Missing number of occurrences")
}

number = parseInt(process.argv[2])

while (number > 0) {
    console.log("C is fun")
    number -= 1
}