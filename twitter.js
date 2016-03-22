$(function() {
    var sname = $("#twitter-card").html();
    $.get({
        //url: "https://shrouded-oasis-42259.herokuapp.com/twitter",
        url: "http://localhost:5000/twitter",
        data: {'screen_name': sname},
        success: function(data) {
            $("#twitter-card").html(data);
        }
    });
});
