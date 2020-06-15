# Linux笔记28--软件包管理9-源码包管理1-源码包与RPM包的区别

1. RPM包安装位置

   RPM包安装在默认位置中

   | 位置            | 含义                         |
   | --------------- | ---------------------------- |
   | /etc/           | 配置文件安装目录             |
   | /usr/bin/       | 可执行的命令安装目录         |
   | /usr/lib/       | 程序所使用的的函数库保存位置 |
   | /usr/share/doc/ | 基本的软件使用手册保存位置   |
   | /usr/share/man/ | 帮助文件保存位置             |

   注：不推荐手工改安装位置

2. 源码包安装位置

   源码包手工指定安装位置

   一般是 /usr/local/软件名/        **usr是Linux的系统资源目录；local是系统为安装外来软件准备的安装位置**

3. 安装位置不同带来的影响

   + RPM包安装的服务可以使用系统服务管理命令（service）来管理

     如：RPM包安装的apache的启动方法有两种：

     ​		systemctl start httpd.service

     ​		service httpd start

   + 源码包安装的服务不能被服务管理命令管理，因为没有安装到默认路径中。所以只能用绝对路径进行服务的管理

     如：/usr/local/apache2/bin/apachect1 start

   