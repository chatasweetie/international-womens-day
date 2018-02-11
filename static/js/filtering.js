var $mediaElements = $('.card-block');

$('.filter_link').click(function(e){
    e.preventDefault();
    
    var filterVal = $(this).data('filter');
    $mediaElements.filter('.' + filterVal).toggleClass("schedule-session-highlight");
});

var $sessionElements = $('.schedule-talks');

$('.filter_link').click(function(e){
    e.preventDefault();

    var filterVal = $(this).data('filter');
    $sessionElements.filter('.' + filterVal).toggleClass("schedule-session-highlight");
});

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        document.getElementById("topBtn").style.display = "block";
    } else {
        document.getElementById("topBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}