#!/usr/bin/node
// An array of integer arguments being passed
// to the function to return the second biggest argument.
function secondbig (args) {
  if (args.length <= 1) {
    return (0);
  }
  for (let i = 0; i < args.length - 1; i++) {
    for (let j = 0; j < args.length - i - 1; j++) {
      let templarge = 0;
      if (args[j] < args[j + 1]) {
        templarge = args[j + 1];
        args[j + 1] = args[j];
        args[j] = templarge;
      }
    }
  }
  return (args[1]);
}
const numsArray = process.argv.slice(2).map(Number);
console.log(secondbig(numsArray));
