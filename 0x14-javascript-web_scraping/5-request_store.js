#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both URL and file path are provided
if (!url || !filePath) {
  console.error('Please provide a URL and a file path.');
  process.exit(1);
}

// Make a GET request to the provided URL
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error if an error occurred during the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Write the body response to the specified file in UTF-8 encoding
      fs.writeFileSync(filePath, body, 'utf-8');
      console.log(`${url} has been successfully downloaded and stored in ${filePath}.`);
    } else {
      // Print an error message if the response status code is not 200
      console.error(`Failed to retrieve the webpage. Status code: ${response.statusCode}`);
    }
  }
});
