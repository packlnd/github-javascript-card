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
        var card = $("#github-card");
        card.width(300).height(100);
        card.css("font-family", "Helvetica, arial, nimbussansl, liberationsans, freesans, clean, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'");
        card.css("position", "absolute");
        card.css("border", "solid 1px #D3D3D3");
        card.css("border-radius", "3px");
        card.css("padding", 10);
        var img = $("<img />", {
            src: data['avatar_url']
        });
        img.css("max-width", 102);
        img.css("max-height", 102);
        card.html(img);
        var name = $("<h2>");
        name.css("position", "absolute");
        name.html(data['name']);
        name.css("color", "rgb(51,51,51)");
        name.css("margin", 0);
        name.css("top", 10);
        name.css("left", 122);
        card.append(name);
        var repos = $("<h3>");
        repos.html(data['public_repos']);
        repos.css("position", "absolute");
        repos.css("color", "rgb(64,120,192)");
        repos.css("bottom", 10);
        repos.css("margin", 0);
        repos.css("left", 122);
        card.append(repos);
        var repoText = $("<p>");
        repoText.html("Repositories");
        repoText.css("color", "rgb(118,118,118");
        card.append(repoText);
    }
});
