$(function () {
    //获取？后的字符串
    var url = location.search;
    // console.log(url);
    var id = url.split("=")[1];
    // $('#showBar').append(id);
    console.log(id);
    $.getJSON("../../php/getData.php?id="+id,function (data) {
        console.log(data);
        var $showbar = $('#showBar');
        data = data.data;
        var $title = "<h1>"+data[id].title+"</h1>";
        var $time = "<p>"+data[id].publishDate+"</p>";
        var $source = "<p>"+data[id].source+"</p>";
        var $content = "<div class='content'>"+data[id].content+"</div>";
        var $col = "<div class='col-md-4'>"+$title+$time+$source+"</div>";
        $showbar.append($col);
        $showbar.append($content);
        console.log(data[id].title);
    })
})