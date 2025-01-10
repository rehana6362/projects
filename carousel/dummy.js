let slideIndex = 0;
const slides = document.querySelectorAll('.carousel-slide img');
const dots = document.querySelectorAll('.dot');
const next = document.querySelector('.next');
const prev = document.querySelector('.prev');

showSlide(slideIndex);

// Next button click
next.addEventListener('click', () => {
    moveSlide(1);
});

// Previous button click
prev.addEventListener('click', () => {
    moveSlide(-1);
});

function moveSlide(n) {
    showSlide(slideIndex += n);
}

// Display the slide based on index
function showSlide(n) {
    if (n >= slides.length) slideIndex = 0;
    if (n < 0) slideIndex = slides.length - 1;

    slides.forEach((slide, index) => {
        slide.style.display = (index === slideIndex) ? 'block' : 'none';
    });

    dots.forEach(dot => dot.classList.remove('active'));
    dots[slideIndex].classList.add('active');
}

// Click on dots
function currentSlide(n) {
    showSlide(slideIndex = n);
}

// Auto-slide functionality
let autoSlide = setInterval(() => {
    moveSlide(1);
}, 3000);

// Pause auto-slide on hover
document.querySelector('.carousel-container').addEventListener('mouseover', () => {
    clearInterval(autoSlide);
});

// Resume auto-slide on mouseout
document.querySelector('.carousel-container').addEventListener('mouseout', () => {
    autoSlide = setInterval(() => {
        moveSlide(1);
    }, 3000);
});
