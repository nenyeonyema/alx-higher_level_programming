// A script that adds the class red to the <header>
// element when the user clicks on the tag DIV#red_header
// Using document.querySelector
/*
 * document.addEventListener('DOMContentLoaded', function() {
 *     const redHeader = document.querySelector('#red_header');
 *     redHeader.addEventListener('click', function() {
 *         const header = document.querySelector('header');
 *         header.classList.add('red');
 *     });
 * });
 */
$(document).ready(function() {
	$('#red_header').click(function() {
		$('header').addClass('red');
	});
});
