$( document ).ready(function() {
});

$(window).scroll(function() {
    var startPx = $(window).scrollTop();
    startPx >= 50 ? $(".normal-nav").addClass("sticky-nav") :  $(".normal-nav").removeClass("sticky-nav");
});

