$(document).ready(function() {
  $("button").click(function(e) {
    that = $(this)
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: likeArticleURL,
        data: {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        success: function($xhr) {
            $('#total_like').html('')
            $('#total_like').html($xhr)
        },
        error: function($xhr) {
            error = $xhr.responseJSON.error
            $('#like_error').removeClass('d-none').fadeIn('slow')
            $('#like_error').html(error)
            setTimeout(function() {
                $('#like_error').addClass('d-none');
                $('#like_error').html('')
            }, 2000);
        }
    });
  });
});