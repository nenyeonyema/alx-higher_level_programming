// A script that script that fetches from
// https://hellosalut.stefanbohacek.dev/?lang=fr and displays the
// value of hello from that fetch in the HTML tag DIV#hello.

// Using document.querySelector
/*
 * document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloDiv = document.querySelector('#hello');
      helloDiv.textContent = data.hello;
    })
    .catch(error => console.error('Error fetching translation:', error));
});
*/

// Jquery
$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
  });
});
