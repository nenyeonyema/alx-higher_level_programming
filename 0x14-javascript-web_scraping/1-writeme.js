#!/usr/bin/node
// a script that writes a string to a file.

const fs = require('fs');

// Get the file path and the string to write
// from the command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if both file path and string to write are provided
if (!filePath || !stringToWrite) {
  console.error('Please provide a file path and a string to write.');
  process.exit(1);
}

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred while writing
    console.error(err);
  }
});
