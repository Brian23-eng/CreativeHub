$(function() {
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 10) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});


$(document).ready(function() {
        $('form').submit(function(event) {
                event.preventDefault()

                form = $('form')



                $.ajax({
                        'url': '/ajax/subscribe/',
                        'type': 'POST',
                        'data': form.serialize(),
                        'dataType': 'json',
                        'success': function(data) {
                            alert(data['success'])
                        },
                    }) // End of submit event

                $('#id_your_name').val('')
                $("#id_email").val('')
            }) // End of submit event

    }) // End of document ready function