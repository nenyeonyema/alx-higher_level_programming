// A script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// Using querySelector
/*
 * document.addEventListener('DOMContentLoaded', function() {
  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      const characterDiv = document.querySelector('#character');
      characterDiv.textContent = data.name;
    })
    .catch(error => console.error('Error fetching character:', error));
});
*/
// Using JQuery
$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    $('#character').text(data.name);
  });
});
