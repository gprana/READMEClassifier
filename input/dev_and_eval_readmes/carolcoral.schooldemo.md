# schooldemo
网站页面视图文件：

index.php（网站首页）<br>
说明：本页面为网站首页展示，为进入网站的门户页面。该页面内容主要包括网站整体框架——导航和主体。该页面包含了网站的导航栏、网站功能说明、网站更新说明、网站公告、网站底部栏。

aboutschool.php（学院简介）<br>
说明：该页面为二级导航链接，页面主要内容为介绍学院成立时间等基本信息。

tese.php（学院特色）<br>
说明：该页面为学院特色介绍页面，主要介绍学院办学特色和教学特色等。

jiangjin.php（奖、助学金）<br>
说明：该页面主要介绍学院奖学金、助学金的成立历史和获奖条件等。

contact.php（留言）<br>
说明：该页面为留言页面。主要为有意愿报名的同学活家长提供咨询平台等，若留言无法解决问题可跳转至jiuye.php页面根据页面提供的信息电话咨询。
该页面后台操作页面为actioncontact.php文件。
该页面功能主要实现代码为：
```
switch($_GET["action"]){
		case "add": //添加
			//1. 获取添加信息
			$UserN 	= $_POST["UserName"];
			$Email = $_POST["Email"];
			$Subject = $_POST["Subject"];
			$Body 	= $_POST["Body"];
			$addtime = time();
			//2. 验证()省略
			if(empty($Email)){
				die("邮箱不能为空 !");
			}
			//3. 拼装sql语句，并执行添加
			$sql = "insert into contact values(null,'{$UserName}','{$Email}','{$Subject}','{$Body}','{$addtime}')";
			//echo $sql;
			$res=mysql_query($sql,$link);
			
			$count = mysql_affected_rows();
			//6. 判断并输出结果
			if($count>0){
				echo "<script>alert('发表成功 !')</script>";
				echo "<script>window.location.href='showcontact.php'</script>";
			}
			else{
				//echo ".$sql()";
				echo "<script>alert('发表失败 !')</script>".$sql();
				echo "<script>window.location.href='contact.php'</script>";
			}
			break;
}
```

showcontact.php（留言展示）<br>
说明：该页面为留言展示页面，目前只展示最新发布信息的前28条信息。设置展示信息功能代码为：
```
<?php
            error_reporting(0);//关闭php警告功能
            include("dbconfig.php");
            $conn = mysql_connect("localhost","root","");
            mysql_select_db("studentsN",$conn);
            // mysql_query("set names gbk_chinese_ci");
            $Conn = mysqli_connect(HOST,USER,PASS,DBNAME) or die("Error " . mysqli_error($Conn));
            mysql_select_db('studentsN');
            $sql = mysql_query("SELECT * FROM contact order by id DESC limit 28");

            echo "<center><div><table align='center' cellpadding='0' class='auto-style2'>";

            while($field = mysql_fetch_field($sql))
                echo "<td class='auto-style1'>&nbsp;".$field->name."&nbsp;</td>";//读出字段名
            while ( $row = mysql_fetch_array($sql))
                    echo "<tr><td class='auto-style1'>$row[0]</td><td class='auto-style1'>$row[1]</td><td class='auto-style1'>$row[2]</td><td class='auto-style1'>$row[3]</td><td class='auto-style1'>$row[4]</td></tr>";//读取数据
            echo "</table></center>";
            mysql_close($conn);
        ?>
```

login.php（登陆）<br>
说明：该页面为网站登陆页面。主要实现功能为注册用户登陆，功能实现操作网页为actionlogin.php，主要功能代码为：
```
if ($Email && $UserPassword){
	$sql = "SELECT Email FROM customs WHERE Email = '$Email' and UserPassword = '$UserPassword'";
	$res = mysql_query($sql);
	$row = mysql_fetch_assoc($res);
	if($row['Email']==$Email){
		session_start();
		$_SESSION['Email']=$Email;
		echo "<script>alert('恭喜您成功登陆!')</script>";
		echo "<script>window.location.href='index.php'</script>";
	}
	else{
		echo "<script>alert('对不起，登录失败，请重新登录！')</script>";
		echo "<script>window.location.href='login.php'</script>";
	}
	//session_destroy();
}
```

regist.php（注册页面）<br>
说明：该页面为网站用户注册页面，用户需要先注册才能成功登陆。注册功能执行页面为actionregist.php，主要功能实现代码为：
```
//验证邮箱是否被注册
			if($Email){
				$sql ="SELECT * FROM customs WHERE Email ='$Email'";
				$res = mysql_query($sql);
				$row = mysql_fetch_assoc($res);
				if($row['{Email}']==$Email){
					echo "<script>alert('对不起，您输入的邮箱已经被注册请重新输入!')</script>";
					echo "<script>window.location.href='regist.php'</script>";
				}
				else{
					$sql = "insert into `customs` values(null,'$UserName','$UserN','$UserY','$UserZ','$UserB','$Email','$UserPassword','$addtime')";
					$res=mysql_query($sql,$link);
					//session_start();
					$_SESSION['Email']=$Email;

					echo "<script>alert('恭喜您注册成功!')</script>";
					echo "<script>window.location.href='index.php'</script>";
				}
			}
```

others.php（其他通知）<br>
说明：该页面负责其他未分类信息的通知。

jiuye.php（就业咨询）<br>
说明：该页面提供就业咨询招生等方面的问题。若无法在留言版块得到想要的答复可根据此页面信息电话咨询。

dbconfig.php（连接页面）<br>
说明：本页面代码主要说明数据库的名称、数据库名、数据名、密码等信息。属于公共调用文件。文件主要代码为：
```
define("HOST","localhost");//数据库使用者
define("USER","root");//数据库用户名root
define("PASS","");//数据库连接密码为空
define("DBNAME","studentsN");//数据库名称
```

daohang.php（导航页面）<br>
说明：本页面为网站的导航菜单页面，负责各个页面的相互连接。为了简化代码的亢余，所有展示页面均适用php代码include直接连接。适用方法为在需要展示也满面的最顶部输入如下代码：
```
<?php include(daohang.php); ?>
```

footer.php（导航页面）<br>
说明：本页面为网站的底部说明页面，负责各个页面的底部说明。为了简化代码的亢余，所有展示页面均适用php代码include直接连接。适用方法为在需要展示也满面的最底部输入如下代码：
```
<?php include(footer.php); ?>
```

NewsSearch.php（信息展示）<br>
说明：本页面为学生信息展示页面，为保密，目前只展示最新的18条信息。执行代码为：
```
<?php
	            error_reporting(0);
	            include("dbconfig.php");
	            $conn = mysql_connect("localhost","root","");
	            mysql_select_db("studentsN",$conn);
	            // mysql_query("set names gbk_chinese_ci");
	            $Conn = mysqli_connect(HOST,USER,PASS,DBNAME) or die("Error " . mysqli_error($Conn));
	            mysql_select_db('studentsN');
	            $sql = mysql_query("SELECT * FROM customs order by id limit 18 ");

	            echo "<center><div><table align='center' cellpadding='0' class='auto-style2'>";

	            while($field = mysql_fetch_field($sql))
	                // echo "<td class='auto-style1'>&nbsp;".$field->name."&nbsp;</td>";//读出字段名
	            while ( $row = mysql_fetch_array($sql))
	                    echo "<tr><td class='auto-style1'>$row[0]</td><td class='auto-style1'>$row[1]</td><td class='auto-style1'>$row[2]</td><td class='auto-style1'>$row[3]</td><td class='auto-style1'>$row[4]</td></tr>";//读取数据
	            echo "</table></center>";
	            mysql_close($conn);
	        ?>
```

NewsPutin.php（信息录入）<br>
说明：本页面为学生信息的录入，录入后的信息可以在NewsSearch.php页面中看到。执行页面为actionNews.php，主要执行代码为：
```
if($UserN){
				$sql ="SELECT * FROM customs WHERE UserN ='$UserN'";
				$res = mysql_query($sql);
				$row = mysql_fetch_assoc($res);
					$sql = "insert into `News` values(null,'$UserN','$year','$mouth','$day','$CJ','$addtime')";
					$res=mysql_query($sql,$link);
					//session_start();

					echo "<script>alert('恭喜您录入成功!')</script>";
					echo "<script>window.location.href='NewsSearch.php'</script>";
				// }
			}
```

session.php（session判断页面）<br>
说明：本页面代码为session判断。若登陆后显示“登陆用户邮箱//注销”，若未登录则显示“登陆//注册”。主要代码为：
```
if(!array_key_exists("Email",$_SESSION))
{
 echo"<a href='login.php'>登陆</a>";
 echo "//";
 echo"<a href='regist.php'>注册</a>";
}else{
  $rest1 = substr($_SESSION['Email'],0,1);
  $rest2 = substr($_SESSION['Email'],-2);
  echo "<a href='NewsSearch.php'>$rest1...$rest2</a>";
  echo "//";
  echo "<a href='session_destroy.php'>注销</a>";
  //session_destroy("<div class='header-actions'><a class='button Logout'>Logout</a></div>");
}
```

session_destory.php（登陆注销）<br>
说明：登陆成功后会有一个按钮“注销”，点击注销能注销用户登陆。本页面为销毁session功能。主要代码为：

session_destory();

数据库设计及文件说明<br>
======
注意：本网站数据库已经设计好，可以直接在phpmyadmin中导入即可
数据库文件：studentsN.sql
数据库样式：<br>
```
CREATE DATABASE IF NOT EXISTS `studentsN` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;//创建数据库，数据库名称：studentsN
USE `studentsN`;//使用数据库studentsN
```

-- --------------------------------------------------------

```
/*学生个人留言板*/
DROP TABLE IF EXISTS `contact`;
CREATE TABLE IF NOT EXISTS `contact` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,//自动添加，不用输入
  `UserName` varchar(32) NOT NULL,//留言需要输入学生学号
  `Email` varchar(24) NOT NULL,//留言需要输入的邮箱（并未要求输入）
  `Subject` varchar(32) NOT NULL,//留言内容标题
  `Body` mediumtext NOT NULL,//留言的内容
  PRIMARY KEY (`id`)
) 
```

-----------------------------------------------------------

```
/*学生个人基本信息注册*/
DROP TABLE IF EXISTS `customs`;
CREATE TABLE IF NOT EXISTS `customs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,     /*学生编号*/
  `UserName` varchar(32) NOT NULL,     /*学生姓名*/
  `UserN` varchar(32) NOT NULL,     /*学生学号*/
  `UserY` varchar(32) NOT NULL,     /*学生院系*/
  `UserZ` varchar(32) NOT NULL,     /*学生专业*/
  `UserB` varchar(32) NOT NULL,     /*学生班级*/
  `Email` varchar(24) NOT NULL,     /*登陆邮箱*/
  `UserPassword` varchar(32) NOT NULL,     /*登录名密码*/
  `addtime` int(40) unsigned NOT NULL,     /*注册时间*/
  PRIMARY KEY (`id`)
)
```

-----------------------------------------------------------

```
/*学生个人成绩信息录入*/
DROP TABLE IF EXISTS `News`;
CREATE TABLE IF NOT EXISTS `News` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `UserN` varchar(64) NOT NULL,/*学生学号*/
  `year` varchar(64) NOT NULL,/*年份*/
  `mouth` varchar(32) NOT NULL,/*月份*/
  `day` varchar(64)  NOT NULL,/*学期*/
  `CJ` varchar(32) NOT NULL,/*学生成绩*/
  `addtime` int(10) unsigned NOT NULL,/*添加时间*/
  PRIMARY KEY (`id`)
)
```
