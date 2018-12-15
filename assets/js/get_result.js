$(document).on("click", ".result", function (event) {
    // prevent the click
    event.preventDefault();

    // get the result pk from the link id
    var result_pk = $(this).attr("id");

    // send the ajax request to the view
    $.ajax({
        url: '/result/' + result_pk + '/',
        data: {},
        success: function (data) {
            // replace the result details
            $("#last_result").html(data);
        }
    });
});
