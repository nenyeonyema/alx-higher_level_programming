#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (a && b) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}
