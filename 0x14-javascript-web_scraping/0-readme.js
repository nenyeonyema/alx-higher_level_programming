#!/usr/bin/node
// a script that reads and prints the content of a file

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Check if a file path is provided
if (!filePath) {
  console.error('Please provide a file path.');
  process.exit(1);
}

// Read the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred during reading
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
