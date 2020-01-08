<?php
require "response.class.json.php";    //引入返回信息类

//链接数据库
$link = mysqli_connect('localhost','root','root','php导入专用');
//访问表
$world = mysqli_query($link,'select * from t_news_copy where typeId="1"');
//设置编码格式
mysqli_query($link,'set name utf8');

//准备返回数据
$code = 200;
$message = "信息请求成功";
$data = array(
    "name" => "腾讯新闻爬取",
    "time"  => "20191204",

);

//匹配数据
while($row = mysqli_fetch_assoc($world)){
    $title = $row["title"];
    $data['title'][]=$title;
}

//实例化response类
$response = new Response;

//返回数据
echo $response -> json($code,$message,$data);
?>