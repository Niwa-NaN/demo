<?php
require "response.class.json.php";    //引入返回信息类
//获取全部提交的数据 $_POST
//打印数据
//print_r($_POST);
//print_r($_GET);
$id = $_GET['id'];
echo $id;

echo "<a href='getData.php?id= $id '>将参数传递到getData.php 页面</a>";

//3.判断跳转
$realUrl = 'demoB.html';
//echo "<script>location.href = '$realUrl'</script>";

?>

