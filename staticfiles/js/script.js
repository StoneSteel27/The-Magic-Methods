$( document ).ready(function() {
});

$(window).scroll(function() {
    var startPx = $(window).scrollTop();
    startPx >= 50 ? $(".normal-nav").addClass("sticky-nav") :  $(".normal-nav").removeClass("sticky-nav");
});

// COUNTER
var initial = 0;
$(window).scroll(function() {
    var msTop = $('#accomplished-counter').offset().top - window.innerHeight;
    if (initial == 0 && $(window).scrollTop() > msTop) {
        $('.accomplished-counter-value').each(function() {
            var $this = $(this),
                countData = $this.attr('counter');
            $({
                countNo: $this.text()
            }).animate({
                    countNo: countData
                },
 
                {
                    easing: 'linear',
                    duration: 2300,
                    step: function() {
                        $this.text(Math.floor(this.countNo));
                    },
                    complete: function() {
                        $this.text(this.countNo);
                    }
 
                });
        });
        initial = 1;
    }
});