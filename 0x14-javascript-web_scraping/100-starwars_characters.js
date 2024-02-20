#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Check if a Movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID.');
  process.exit(1);
}

// Define the URL with the provided Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error if an error occurred during the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const movie = JSON.parse(body);
      // Print all characters of the movie
      movie.characters.forEach(character => {
        request.get(character, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            } else {
              console.error(`Failed to retrieve character information. Status code: ${charResponse.statusCode}`);
            }
          }
        });
      });
    } else {
      // Print an error message if the response status code is not 200
      console.error(`Failed to retrieve movie information. Status code: ${response.statusCode}`);
    }
  }
});
