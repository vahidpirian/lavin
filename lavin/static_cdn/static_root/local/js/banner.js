jQuery(document).ready(function($) {

let index = 0;
const slides = $('.lavin-slide');
const prev = $('.prev').first();
const next = $('.next').first();

function changeSlide() {
    for(let i=0; i < slides.length; i++) {
        slides[i].classList.remove("active")
    }
    slides[index].classList.add('active');
}

prev.click(function() {
    if(index == 0) {
        index = slides.length - 1;
    }
    else {
        index--;
    }
    changeSlide();
});

next.click(function() {
    if (index == slides.length - 1) {
        index = 0;
    } else {
        index++;
    }
    changeSlide();
});

});