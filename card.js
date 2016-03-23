$(function() {
  if ($("#card.twitter").length) { create_twitter_card(); }
  if ($("#card.github").length) { create_github_card(); }
  if ($("#card.yelp").length) { create_yelp_card(); }

  function create_github_card() {
    uname = $("#card.github").html();
    var url = "https://api.github.com/users/" + uname;
    $.getJSON({
      url: url,
      success: function(data) {
        var github = prepare_obj(
          data['avatar_url'],
          data['name'],
          data['login'],
          'rgb(64,120,192)',
          false,
          '',
          '',
          data['public_repos'],
          'Repositories',
          122,
          true,
          'https://shrouded-oasis-42259.herokuapp.com',
          data['login'],
          '',
          'Streak',
          186,
          false,
          '',
          '',
          data['followers'],
          'Followers',
          250,
          0.1,
          'http://packlnd.github.io/github.ico'
        );
        draw_card($("#card.github"), github);
      }
    });
  }

  function draw_card(card, data) {
    card.html("");
    card
      .width(300)
      .height(100)
      .css("font-family", "Helvetica, arial, nimbussansl, liberationsans, freesans, clean, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'")
      .css("background-color", "#EEE")
      .css("border", "solid 1px #D3D3D3")
      .css("border-radius", "3px")
      .css("position", "relative")
      .css("z-index", -2)
      .css("padding", 10);
    var img = $("<img />", {src: data['img']})
      .css("position", "absolute")
      .css("top", 10)
      .css("left", 10)
      .css("max-width", 102)
      .css("max-height", 102);
    var name = $("<h2>")
      .css("position", "absolute")
      .html(shorten_if_long(data['name']))
      .css("color", "rgb(51,51,51)")
      .css("margin", 0)
      .css("top", 10)
      .css("left", 122);
    var uname = $("<p>")
      .css("position", "absolute")
      .html(data['uname'])
      .css("top", 38)
      .css("left", 122)
      .css("margin",0)
      .css("font-size","14px")
      .css("color", "#666");
    $.each(data['stats']['items'], function(i,v) {
      if (v['from_server']) {
        fetch_from_server(card, v, data['stats']['color']);
      } else {
        var div = create_stats_div(card, v['number'], v['text'], data['stats']['color'], v['left']);
        card.append(div);
      }
    });
    var ico = $("<img/>", {
        src : data['icon']['img']
      })
      .css("position", "absolute")
      .css("top", 5)
      .css("right", 5)
      .css("opacity", data['icon']['opacity'])
      .css("z-index", -1);
    card
      .append(img)
      .append(name)
      .append(uname)
      .append(ico);
  }

  function create_stats_div(card, number, text, color, left) {
    var container = $("<div>")
      .css("top",65)
      .css('left',left)
      .width(64)
      .css("position","absolute");
    var num = $("<h3>")
      .html(number)
      .css("color", color)
      .css("text-align", "center")
      .css("margin", "auto 0");
    var txt = $("<p>")
      .html(text)
      .css("margin",0)
      .css("color", "rgb(118,118,118")
      .css("text-align", "center")
      .css("font-size", "10px");
    container
      .append(num)
      .append(txt);
    return container;
  }

  function shorten_if_long(name) {
    if (name.length <= 14)
      return name;
    return name.slice(0,14) + "...";
  }

  function fetch_from_server(card, item, color) {
    $.get({
      url: item['url'],
      data: {'uname': item['data']},
      success: function(obj) {
        var div = create_stats_div(card, obj['data'],item['text'], color, item['left']);
        card.append(div);
      }
    });
  }

  function prepare_obj(
      img,nm,unm,clr,
      fs1,u1,d1,n1,t1,l1,
      fs2,u2,d2,n2,t2,l2,
      fs3,u3,d3,n3,t3,l3,
      io,ii) {
    return {
      'img': img,
      'name': nm,
      'uname': unm,
      'stats': {
        'color': clr,
        'items': [{
          'from_server': fs1,
          'url': u1,
          'data': d1,
          'number': n1,
          'text': t1,
          'left': l1
        },{
          'from_server': fs2,
          'url': u2,
          'data': d2,
          'number': n2,
          'text': t2,
          'left': l2
        },{
          'from_server': fs3,
          'url': u3,
          'data': d3,
          'number': n3,
          'text': t3,
          'left': l3
        }]
      },
      'icon': {
        'opacity': io,
        'img': ii
      }
    };
  }
});
