// A script that toggles the class of the <header>
// element when the user clicks on the tag DIV#toggle_header
// Using query Selector
/*
 * document.addEventListener('DOMContentLoaded', function() {
  const toggleHeader = document.querySelector('#toggle_header');
  toggleHeader.addEventListener('click', function() {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
*/
// Using JQuery
$(document).ready(function() {
  $('#toggle_header').click(function() {
    $('header').toggleClass('red green');
  });
});
