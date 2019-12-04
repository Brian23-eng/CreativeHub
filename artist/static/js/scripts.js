$(function() {
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 10) {
            $('.navbar').removeClass('active');
        } else {
            $('.navbar').addClass('active');
        }
    });
});