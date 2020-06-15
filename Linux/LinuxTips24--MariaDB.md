# LinuxTips24--MariaDB

MariaDB是MySQL的一个分支，取代Mysql称为Centos 7的默认数据库。

1. 安装并启动服务

   + yum install -y mariadb-server mariadb

   + 设置开机自启动

     systemctl enable mariadb

   + 开启服务

     systemctl start mariadb

   + 启动安全配置程序

     + mysql_secure_installation

       ```
       NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
             SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!
       
       In order to log into MariaDB to secure it, we'll need the current
       password for the root user.  If you've just installed MariaDB, and
       you haven't set the root password yet, the password will be blank,
       so you should just press enter here.
       
       Enter current password for root (enter for none): #密码是空，回车即可。
       OK, successfully used password, moving on...
       
       Setting the root password ensures that nobody can log into the MariaDB
       root user without the proper authorisation.
       
       Set root password? [Y/n] y #是否设置root密码，这里进行设置
       New password: 
       Re-enter new password: 
       Password updated successfully!
       Reloading privilege tables..
        ... Success!
       
       
       By default, a MariaDB installation has an anonymous user, allowing anyone
       to log into MariaDB without having to have a user account created for
       them.  This is intended only for testing, and to make the installation
       go a bit smoother.  You should remove them before moving into a
       production environment.
       
       Remove anonymous users? [Y/n] y  #是否删除匿名用户
        ... Success!
       
       Normally, root should only be allowed to connect from 'localhost'.  This
       ensures that someone cannot guess at the root password from the network.
       
       Disallow root login remotely? [Y/n] n #是否允许root远程登陆数据库
        ... skipping.
       
       By default, MariaDB comes with a database named 'test' that anyone can
       access.  This is also intended only for testing, and should be removed
       before moving into a production environment.
       
       Remove test database and access to it? [Y/n] n #是否删除test数据库
        ... skipping.
       
       Reloading the privilege tables will ensure that all changes made so far
       will take effect immediately.
       
       Reload privilege tables now? [Y/n] y #重载授权表
        ... Success!
       
       Cleaning up...
       
       All done!  If you've completed all of the above steps, your MariaDB
       installation should now be secure.
       
       Thanks for using MariaDB!
       ```

2. 目录结构

   | 目录                   | 说明                              |
   | ---------------------- | --------------------------------- |
   | /var/lib/mysql         | mysql数据文件存放路径，可以自定义 |
   | /etc/my.cnf            | mysql配置文件地址                 |
   | /usr/lib64/mysql       | mysql库文件路径                   |
   | /etc/rc.d/init.d/mysql | mysql服务器管理脚本地址           |
   | /usr/bin/mysql*        | mysql二进制可执行文件路径         |
   | /var/log/mysqld.log    | mysql日志文件地址                 |

3. 登录数据库

   + mysql -u root -p

4. 基本命令

   + 查看数据库

     show databases;

   + 进入数据库mysql

     use mysql

   + 查看查看当前数据库的表

     show tables;

   + 查看表结构

     desc user;

   + ==刷新数据库==

     FLUSH privileges

     当设置新用户、修改密码、设置权限后使用，也可以直接重启服务

   + 查看版本

     select version();

   + 创建新用户dbuser

     CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'password';

   + 创建新数据库cxy

     create database cxy;

     + 在终端创建数据库cxy

       mysqladmin -u user -p create cxy;

   + 删除数据库cxy

     drop database cxy;

     + 在终端删除数据库cxy

       mysqldadmin -u root -p drop cxy;

   + 权限授予

     + 授权用户dbuser对数据库cxy的所有权限

       GRANT ALL PRIVILEGES ON cxy.* TO 'dbuser'@'localhost';

     + 授予用户dbuser对所有数据库的权限

       GRANT ALL PRIVILEGES ON *.\* TO 'dbuser'@'localhost' 

     + 授予用户dbuser对数据库cxy的SELECT权限  ==分配INSERT,DELETE,UPDATE权限类似==

       GRANT SELECT ON cxy.* TO 'dbuser'@'localhost';

       **若用户dbuser，会直接创建用户**

     + 授予用户dbuser对数据库cxy的INSERT和UPDATE权限

       GRANT INSERT,UPDATE ON cxy.* TO 'dbuser'@'localhost';

     + 授予用户dbuser对数据库cxy的操作权限和授予权限

       GRANT ALL PRIVILEGES ON cxy.* TO 'dbuser'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

     + 授予用户dbuser外网登录数据库cxy的权限

       GRANT ALL PRIVILEGES ON cxy.* TO 'dbuser'@'%' IDENTIFIED BY  'password';

   + 更改MariaDB用户密码

     + 登录MariaDB

       mysql -u root -p

     + 进入mysql数据库

       USE mysql;

     + 更新密码

       UPDATE user SET password=PASSWORD('new password') WHERE User='root' AND Host='localhost';

     + 更新数据库

       FLUSH PRIVILEGES

     + 退出

       EXIT

