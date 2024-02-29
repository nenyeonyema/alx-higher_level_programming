// A script that updates the text of the <header>
// element to New Header!!! when the user clicks on DIV#update_header
// Using query selector
/*
 * document.addEventListener('DOMContentLoaded', function() {
 *     updateHeader = document.queryselector('#update_header');
 *     updateHeader.addEventListener('click', function() {
 *         const header = document.querySelector('header');
 *         header.textContent = 'New Header!!!';
 *     });
 * });
 */
$(document).ready(function() {
	$('#update_header').click(function() {
		$('header').text('New Header!!!');
	});
});
