$(function() {
    var uname = $("#github-card").html();
    $("#github-card").html("");
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
        var card = $("#github-card")
            .width(300).height(100)
            .css("font-family", "Helvetica, arial, nimbussansl, liberationsans, freesans, clean, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'")
            .css("position", "absolute")
            .css("border", "solid 1px #D3D3D3")
            .css("border-radius", "3px")
            .css("padding", 10);
        var img = $("<img />", {src: data['avatar_url']})
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
            .html(data['login'])
            .css("top", 38)
            .css("left", 122)
            .css("margin",0)
            .css("font-size","14px")
            .css("color", "#666");
        var repo = create_stats_div(
                data['public_repos'],
                "Repositories")
            .css("left", 122);
        var followers = create_stats_div(
                data['followers'],
                "Followers")
            .css("left", 250);
        $.get({
            url: "https://shrouded-oasis-42259.herokuapp.com/github_streak",
            data: {uname: data['login']},
            success: function(st_len) {
                console.log(st_len);
                var streak = create_stats_div(st_len,"Streak")
                    .css("left", 186);
                card.append(streak);
            }
        });
        card.html(img)
            .append(name)
            .append(uname)
            .append(repo)
            .append(followers);
    }

    function create_stats_div(n, s) {
        var container = $("<div>")
            .css("top",65)
            .width(64)
            .css("position","absolute");
        var num = $("<h3>")
            .html(n)
            .css("color", "rgb(64,120,192)")
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
