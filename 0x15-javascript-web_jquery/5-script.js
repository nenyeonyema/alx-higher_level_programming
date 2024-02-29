// A JavaScript script that adds a <li> element to a
// list when the user clicks on the tag DIV#add_item:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
// Using  a query selector
/*
 * document.addEventListener('DOMContentLoader', function() {
 *     const addItem = document.querySelector('#add_item');
 *     addItem.addEventListener('click', function() {
 *         const newListElement = document.createElement('li');
 *         newListElement.textContent = 'Item';
 *         document.querySelector('ul.my_list').appendChild('newListElement');
 *     });
 * });
 */
// Uisng JQuery
$(document).ready(function() {
	$('#add_item').click(function() {
		$('<li>Item</li>').appendTo('ul.my_list');
	});
});
