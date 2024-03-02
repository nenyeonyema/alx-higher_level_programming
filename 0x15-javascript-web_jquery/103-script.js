/*
 * Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
The translation of “Hello” must be displayed in the HTML tag DIV#hello
*/

// Using document.querySelector

/*
 * document.addEventListener('DOMContentLoaded', function() {
  const btnTranslate = document.querySelector('#btn_translate');
  const languageCodeInput = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  btnTranslate.addEventListener('click', fetchTranslation);
  languageCodeInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = languageCodeInput.value;
    fetch(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => console.error('Error fetching translation:', error));
  }
});
*/

// Using jquery
$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
