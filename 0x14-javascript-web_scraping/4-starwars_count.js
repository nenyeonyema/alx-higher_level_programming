#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');

// Get the API URL of the Star Wars API from the command line argument
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Please provide the API URL of the Star Wars API.');
  process.exit(1);
}

// Character ID of Wedge Antilles
const characterId = '18';

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if an error occurred during the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const films = JSON.parse(body).results;
      // Count the number of movies where Wedge Antilles is present
      const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
      // Print the count
      console.log(count);
    }
  }
});
