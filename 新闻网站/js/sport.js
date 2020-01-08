$(function () {
    $.getJSON("../../php/getData_sport.php",function (data) {
        console.log(data);
        var $rows = $('.rows');
        data = data.data;
        $.each(data,function (key,val) {
            var $image = "<img src='"+val.image+"'>";
            var $h3_title = "<h3>"+val.title+"</h3>";
            var $time = "<p class='time'>"+val.publishDate+"</p>";
            var $source = "<p class='source'>"+val.source+"</p>";
            var $col = "<div class='col-md-4'><a href='son.html?id="+key+"'style='text-decoration: none;'>"+$image+$h3_title+$time+$source+"</a></div>";
            $rows.append($col);
        });
    })
});