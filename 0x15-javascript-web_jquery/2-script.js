// A script that updates the text color of the <header>
// element to red (#FF0000) when the user clicks on the tag DIV#red_header
// Using document.querySelector
/*
  document.addEventListener('DOMContentLoaded', function() {
       const redHeader = document.querySelector('#red_header');
       redHeader.addEventListener('click', function() {
           const header = document.querySelector('header');
           header.style.color = '#FF0000';
       });
  });
*/
$(document).ready(function() {
	$('#red_header').click(function() {
		$('header').css('color', '#FF0000');
	});
});
