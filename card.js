$(function() {
    var uname = $("#github-card").html();
    call_github_api(uname);

    function call_github_api(uname) {
        var url = "https://api.github.com/users/" + uname;
        console.log(url);
        $.getJSON({
            url: url,
            success: function(data) {
                jdata = JSON.stringify(data);
                draw_card(data);
                //$("#github-card").html(jdata);
            }
        });
    }

    function draw_card(data) {
        var card = $("#github-card");
        card.width(300).height(100);
        card.css("border", "solid 1px black");
        card.css("border-radius", "5px");
        card.css("padding", 10);
        var img = $("<img />", {
            src: data['avatar_url']
        });
        img.css("max-width", 102);
        img.css("max-height", 102);
        img.css("border-radius", "5px");
        card.append(img);
    }
});
