// Get the search input and the loader element
const searchInput = document.querySelector('input[name="query"]');
const loader = document.querySelector('#loader');

// Show the loader when the search query is submitted
searchInput.addEventListener('input', function() {
  loader.style.display = 'block';
});

// Hide the loader when the search results are loaded
window.addEventListener('load', function() {
  loader.style.display = 'none';
});


// Get the cards element
const cards = document.querySelector('.cards');

// Hide the cards by default
cards.style.display = 'flex';





//////

// Initialize page count
let page = 1;

// Listen to scroll event
window.addEventListener('scroll', function() {
  // Check if user has scrolled to the bottom
  if (window.innerHeight + window.pageYOffset >= document.body.offsetHeight) {
    // Show loader/spinner
    const loader = document.getElementById('loaader');
    loader.style.display = 'block';

    // Make AJAX request to load more cards
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/load-cards?page=' + page);
    xhr.onload = function() {
      // Hide loader/spinner
      loader.style.display = 'none';

      // Append new card elements to container
      const response = xhr.response;
      const cardContainer = document.getElementsByClassName('cards')[0];
      cardContainer.innerHTML += response;

      // Remove hidden attribute from new card elements
      const newCards = cardContainer.querySelectorAll('.card.hidden');
      for (let i = 0; i < newCards.length; i++) {
        newCards[i].classList.remove('hidden');
      }

      // Increment page
      page += 1;
    };
    xhr.send();
  }
});

///but it is not working correctly i want ot to know
//the number of counts as user is scrolling once it 
/// reaches the 20th one it triggers the animation