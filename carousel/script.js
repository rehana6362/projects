let slideImages = document.querySelectorAll('img');
let next = document.querySelector('.next');
let prev = document.querySelector('.prev');
let dots = document.querySelectorAll('.dot');

let counter = 0;

// Next button functionality
next.addEventListener('click', slideNext);
function slideNext() {
    slideImages[counter].style.animation = 'next1 0.5s ease-in forwards';
    
    if (counter >= slideImages.length - 1) {
        counter = 0;
    } else {
        counter++;
    }
    
    slideImages[counter].style.animation = 'next2 0.5s ease-in forwards';
    updateIndicators();
}

// Previous button functionality
prev.addEventListener('click', slidePrev);
function slidePrev() {
    slideImages[counter].style.animation = 'prev1 0.5s ease-in forwards';
    
    if (counter === 0) {
        counter = slideImages.length - 1;
    } else {
        counter--;
    }
    
    slideImages[counter].style.animation = 'prev2 0.5s ease-in forwards';
    updateIndicators();
}

// Update the dot indicators
function updateIndicators() {
    dots.forEach(dot => dot.classList.remove('active'));
    dots[counter].classList.add('active');
}

// Add click event for each dot
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => switchImage(index));
});

// Switch to the selected image when a dot is clicked
function switchImage(imageIndex) {
    if (imageIndex > counter) {
        slideImages[counter].style.animation = 'next1 0.5s ease-in forwards';
    } else if (imageIndex < counter) {
        slideImages[counter].style.animation = 'prev1 0.5s ease-in forwards';
    }
    
    counter = imageIndex;
    slideImages[counter].style.animation = imageIndex > counter ? 'next2 0.5s ease-in forwards' : 'prev2 0.5s ease-in forwards';
    updateIndicators();
}

// Auto slide functionality
let autoSlideInterval = setInterval(slideNext, 3000); // Change every 3 seconds

// Pause auto-slide when hovering over the slider
const container = document.querySelector('.slider-container');
container.addEventListener('mouseover', () => clearInterval(autoSlideInterval));

// Resume auto-slide when not hovering
container.addEventListener('mouseout', () => {
    autoSlideInterval = setInterval(slideNext, 3000);
});
