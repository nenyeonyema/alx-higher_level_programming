#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Check if a movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

// Define the URL with the provided movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error if an error occurred during the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const movie = JSON.parse(body);
      // Print the title of the movie
      console.log(movie.title);
    } else {
      // Print an error message if the response status code is not 200
      console.error(`Failed to retrieve movie information. Status code: ${response.statusCode}`);
    }
  }
});
