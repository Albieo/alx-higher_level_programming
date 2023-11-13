#!/usr/bin/node
/*
    Write a script that prints two arguments passed to it, in the following format: “ is ”
    
    -> You must use console.log(...) to print all output
    -> You are not allowed to use var
*/


const first = process.argv[2]
const second = process.argv[3]

console.log(first," is ", second)