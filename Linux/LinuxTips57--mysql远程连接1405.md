# LinuxTips57--mysql远程连接1405

+ 原因

  Linux服务器安装mysql数据库后，MySQL默认安装完后只有本地访问的权限，没有远程访问的权限，需要给指定用户设置访问权限才能远程访问该数据库

+ 解决方案

  ```mysql
  grant all privileges on *.* to 'root'@'%' identified by 'password';  
  ```

  root代表root用户，%代表所有IP地址都可远程访问，password代表给予root用户远程登录访问数据库的密码，替换为数据库的密码