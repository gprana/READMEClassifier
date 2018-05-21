GreenPHP Framework
===
###框架特色：
专为多平台应用开发订制，经历三年线上运行保持稳定！

在移动互联网时代 **APP + Web + 后台管理** 已经成为标配，本框架集成：

1、*RestAPI快速开发并且自动生成API文档和测试，方便APP开发。*  
2、*Web开发无需学习模板语言，只需记住两个标签 {} 和 <\!--{}--> 即可使用原生PHP语法，即方便开发又降低学习门槛。*  
3、*后台管理已经集成后台用户管理和用户权限减少重复劳动。*  

[在线Demo][1]

----------

###目录说明：
    -apps 项目文件
        -api    RestApi接口
        -admin  后台管理项目
        -web    前端项目
    -core 公共文件与配置
        -extends 项目扩展类
        -library 框架类库
    -source 框架资源(Linux中需配置递归读写权限)
        -config 项目配置文件
        -static 前端静态脚本文件
        -temp   模板编译目录
    -startup 框架文档工具
    
###如何访问：
    前端页面：http://host/dir/view/module/phpfilename
    后台页面：http://host/dir/admin/module/phpfilename
    host 主机域名
    dir 定向到框架根目录（即 index.php 所在目录）
    view 或 admin 固定（区分前台与后台可在.htaccess文件修改）
    module 即apps项目下的目录名
    phpfilename 即 apps 项目目录下的php文件名(不包含php后缀)
    如要访问 htdocs/apps/admin/mgr/login.php 文件
    URL为 http://localhost/admin/mgr/login
        
###使用配置：
    Config::addPath(dirname(__FILE__).'/config/'); //设置配置目录
    $conf = Config::get('filename.conf/arraykey'); //多维数组可像访问目录一样增加"/"来获取
###使用DB：
    $db = Database::connect(Config::get('db.conf/default'),true);
    $insertid = $db->insertInto(’tablename‘, array('field'=>'value'))->execute();
    $bool = $db->delete('tablename')->where('field','value')->execute();
    $bool = $db->update('tablename')->set(array('field'=>'value'))->where('field',$value)->execute();
    $result = $db->from('tablename')->where('field',$value)->fetchAll();
    还可以直接使用PDO
    $pdo = $db->getPdo();
    $pdo->query($sql)->fetchAll();
    
    DB集成FluentPDO，更多功能请查阅
    http://fluentpdo.com/documentation.html#todo
###使用模板
    php中加载模板：
    $assign = array ('name'=>'GreenPHP');
    $tpl = new Tpl(Config::get ('tpl.conf/web'));
    $tpl->display ('index.html', $assign);
    模板标签：
    输出变量使用 {$name}
    PHP代码使用 <!--{phpcode}-->
    循环列表如：
    <!--{foreach($list as $key=>$item):}-->
        {$item} //输出列表变量
    <!--{endforeach;}-->


  [1]: http://mnew14.yyport.com/view/docs/api
