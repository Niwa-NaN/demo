<?php
require "数据获取模拟/response.class.json.php";    //引入返回信息类
//获取全部提交的数据 $_POST
//打印数据
//print_r($_POST);
//print_r($_GET);

$id = $_GET['id'];


//链接数据库
$link = mysqli_connect('localhost','root','root','php导入专用');
//访问表
$world = mysqli_query($link,"select * from t_news_copy where newsId= $id");
//设置编码格式
mysqli_query($link,'set name utf8');

//准备返回数据
$code = 200;
$message = "信息请求成功";
$data = array(
    "name" => "腾讯新闻爬取",
    "time"  => time(),

);

//$i=0;
//匹配数据
$row = mysqli_fetch_assoc($world);
//获取新闻id
$newsId = $row['newsId'];

//获取标题
$title = $row["title"];
$data[$newsId]['title']=$title;

//获取新闻发布时间
$publishDate = $row["publishDate"];
$data[$newsId]['publishDate'] = $publishDate;

//获取新闻来源
$source = $row["author"];
$data[$newsId]['source'] = $source;

//获取新闻内容
$content = $row['content'];
$data[$newsId]['content'] = $content;


//echo $newsId;
//    //获取新闻图片
//    $image = $row["imageName"];
//    $data[$newsId]['image'] = $image;

//实例化response类
$response = new Response;

//返回数据
echo $response -> json($code,$message,$data);
?>

