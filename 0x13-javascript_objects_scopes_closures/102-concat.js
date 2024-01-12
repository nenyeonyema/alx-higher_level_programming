#!/usr/bin/node

const fs = require('fs');

// Get file paths from command line arguments
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destFilePath = process.argv[4];

// Read the content of fileA
fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) {
    console.error('Error reading file A:', err);
    return;
  }

  // Read the content of fileB
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) {
      console.error('Error reading file B:', err);
      return;
    }

    // Concatenate the contents of fileA and fileB
    const concatenatedContent = dataA.trim() + dataB.trim();

    // Write the concatenated content to the destination file
    fs.writeFile(destFilePath, concatenatedContent, (err) => {
      if (err) {
        console.error('Error writing to destination file:', err);
        return;
      }
      console.log(`Concatenated files ${fileAPath} and ${fileBPath} into ${destFilePath}`);
    });
  });
});
