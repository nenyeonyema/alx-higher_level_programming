/*
 * A script  script that adds, removes and clears LI elements from a list when the user clicks:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
When the user clicks on DIV#add_item: a new element is added to the list
When the user clicks on DIV#remove_item: the last element is removed from the list
When the user clicks on DIV#clear_list: all elements of the list are removed
*/

// Using document.querySelector
/*
 * document.addEventListener('DOMContentLoaded', function() {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  removeItem.addEventListener('click', function() {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearList.addEventListener('click', function() {
    myList.innerHTML = '';
  });
});
*/

// Using jquery
$(document).ready(function() {
  $('#add_item').click(function() {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
