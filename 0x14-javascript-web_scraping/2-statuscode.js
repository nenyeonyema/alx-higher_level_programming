#!/usr/bin/node
// a script that display the status code of a GET request.

const request = require('request');

// Get the URL to request from the command line arguments
const url = process.argv[2];

// Check if a URL is provided
if (!url) {
  console.error('Please provide a URL.');
  process.exit(1);
}

// Make a GET request to the provided URL
request.get(url, (error, response) => {
  if (error) {
    // Print the error if an error occurred during the request
    console.error(error);
  } else {
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
