$(document).on("click", ".result", function (event) {
    // prevent the click
    event.preventDefault();

    // get the result pk from the link id
    var result_pk = $(this).attr("id");

    // send the ajax request to the view
    $.ajax({
        url: '/result/' + result_pk + '/',
        data: {},
        dataType: 'json',
        success: function (data) {
            console.log("good");
            // replace the result details
            $("#last_result_date_created").text(data.date_created);
            $("#last_result_latency").text(data.latency);
            $("#last_result_packet_loss").text(data.packet_loss);
            $("#last_result_content").text(data.content);
        }
    });
});
