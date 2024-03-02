// A script that script that fetches and lists the
// title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json

// Using dpcument.queryselector
/*
 * document.addEventListener('DOMContentLoaded', function() {
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      const listMovies = document.querySelector('#list_movies');
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => console.error('Error fetching movies:', error));
});
*/

// Using JQuery
$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;
    const listMovies = $('#list_movies');
    $.each(movies, function(index, movie) {
      $('<li>').text(movie.title).appendTo(listMovies);
    });
  });
});

