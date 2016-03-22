$(function() {
    var sname = $("#twitter-card").html();
    $.get({
        url: "https://shrouded-oasis-42259.herokuapp.com/twitter",
        data: {'screen_name': sname},
        success: function(data) {
            console.log(data);
            draw_card(data);
        }
    });

    function draw_card(data) {
        var card = $("#twitter-card")
            .width(300).height(100)
            .css("font-family", "Helvetica, arial, nimbussansl, liberationsans, freesans, clean, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'")
            .css("background-color", '#'+data['profile_background_color'])
            .css("border", "solid 1px #D3D3D3")
            .css("border-radius", "3px")
            .css("position", "relative")
            .css("z-index", -2)
            .css("padding", 10);
        var img = $("<img />", {
                src: data['profile_image_url'].replace('_normal','')
            })
            .css("position", "absolute")
            .css("top", 10)
            .css("left", 10)
            .css("max-width", 102)
            .css("max-height", 102);
        var name = $("<h2>")
            .css("position", "absolute")
            .html(data['name'])
            .css("color", "rgb(51,51,51)")
            .css("margin", 0)
            .css("top", 10)
            .css("left", 122);
        var uname = $("<p>")
            .css("position", "absolute")
            .html('@' + data['screen_name'])
            .css("top", 38)
            .css("left", 122)
            .css("margin",0)
            .css("font-size","14px")
            .css("color", "#666");
        var tweets = create_stats_div(
                data['statuses_count'],
                "Tweets")
            .css("left", 122)
            .css("color", "#"+data['profile_link_color']);
        var ico = $("<img/>", {
            src : "http://packlnd.github.io/twitter.ico"
            })
            .css("position", "absolute")
            .css("top", 5)
            .css("right", 5)
            .css("opacity", 0.1)
            .css("z-index", -1);
        card.html(img)
            .append(name)
            .append(uname)
            .append(tweets)
            .append(ico);
    }

    function create_stats_div(n, s) {
        var container = $("<div>")
            .css("top",65)
            .width(64)
            .css("position","absolute");
        var num = $("<h3>")
            .html(n)
            //.css("color", "rgb(64,120,192)")
            .css("text-align", "center")
            .css("margin", "auto 0");
        var txt = $("<p>")
            .html(s)
            .css("margin",0)
            .css("color", "rgb(118,118,118")
            .css("text-align", "center")
            .css("font-size", "10px");
        container
            .append(num)
            .append(txt);
        return container;
    }
});
