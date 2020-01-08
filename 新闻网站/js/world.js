$(function () {
    $.getJSON("../../php/getData_world.php",function (data) {
        console.log(data);
        var $rows = $('.rows');
        data = data.data;
        $.each(data,function (key,val) {
            var $image = "<img src='"+val.image+"'>";   //某些图片存在问题，显示404错误，无碍。
            var $h3_title = "<h3>"+val.title+"</h3>";
            var $time = "<p class='time'>"+val.publishDate+"</p>";
            var $source = "<p class='source'>"+val.source+"</p>";
            var $col = "<div class='col-md-4'><a href='son.html?id="+key+"'style='text-decoration: none;'>"+$image+$h3_title+$time+$source+"</a></div>";
            $rows.append($col);
            // $(".rows img").trigger("create");        //若是新创建的节点丢失样式，可用此命令触发节点初始化设置
        });
    })
    // $("img").css({"width":"50%"});      //只能影响html中已经存在的节点
});