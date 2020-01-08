$(function () {
    console.log("是否运行");
    var $ul = $('#nav>ul').children();
    console.log($ul.length);
    $('li').click(function () {
        // console.log(this.innerHTML);
        $(this).addClass('active')
            .siblings().removeClass('active');
        // return false;
    })
})