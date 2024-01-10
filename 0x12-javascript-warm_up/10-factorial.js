#!/usr/bin/node
// a script that computes and prints a factorial
function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 0) {
    return (1);
  }
  return a * factorial(a - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
