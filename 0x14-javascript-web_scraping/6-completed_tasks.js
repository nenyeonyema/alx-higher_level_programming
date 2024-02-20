#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const request = require('request');

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Please provide the API URL.');
  process.exit(1);
}

// Make a GET request to the provided API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if an error occurred during the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const todos = JSON.parse(body);
      // Create an object to store the number of completed tasks by user id
      const completedTasksByUser = {};

      // Loop through the todos to count completed tasks by user id
      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      // Print the number of completed tasks by user id
      console.log(completedTasksByUser);
    }
  }
});
