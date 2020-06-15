# LinuxTips5--关于启动httpd服务的简单操作

1. Apache

   + 软件包：httpd,httpd-devel,httpd-mannal

   + 服务类型：由systemd启动的守护进程

   + 配置单元：/usr/lib/systemd/system/httpd.service

   + 守护进程：/usr/sbin/httpd

   + 端口：80(http),443(htps)

   + 配置：/etc/httpd/

   + 主配置文件：/etc/httpd/conf/httpd.conf

   + Web文档：/var/www/html/

   + 日志目录：/var/log/httpd/

     ​					access_log：记录客户端访问Apache的信息

     ​					error_log：记录访问页面错误信息

   + 服务启动的记录日志：/var/log/messages

   ---

2. httpd.conf文件内容

   ```
   31 ServerRoot "/etc/httpd"                  #存放配置文件的目录
   42 Listen 80                                #Apache服务监听端口
   66 User apache                              #子进程的用户
   67 Group apache                             #子进程的组
   86 ServerAdmin root@localhost               #设置管理员邮件地址
   119 DocumentRoot "/var/www/html"            #网站家目录
   #设置DocumentRoot指定目录的属性
   131 <Directory "/var/www/html">             #网站容器开始标识
   144     Options Indexes FollowSymLinks      #找不到主页时，以目录方式呈现，并允许链接到网                                             #站根目录以外
   151     AllowOverride None                  #none不使用.htaccess控制，all允许
   156     Require all granted                 #granted表示运行所有访问，denied表示拒绝所                                             #有访问
   157 </Directory>                            #容器属性
   164     DirectoryIndex index.html           #定义主页文件，当访问到网站目录时如果有定义的                                             #主页文件，网站会自动访问
   316 AddDefaultCharset UTF-8                 #字符编码，如果中文的话，有可能需要改为                                                 #gb2312或者gbk，因网站文件的默认编码而异
   ```

   ------

3. 启动httpd

   - yum命令安装Apache

     ​	yum install -y httpd

     ​	rpm -q httpd

   - 关闭防火墙

     ​	systemctl stop firewalld      #临时关闭

     ​	systemctl disable firewalled     #永久关闭

   - 关闭selinux**(关闭防火墙后客户端还是无法访问时再执行这一步)**

     - 临时关闭

       setenforce 0   

     - 永久关闭

       - vim /etc/selinux/config

         ​	SELINUX=disabled       #将enforcing改为disabled

       - reboot           #重启系统永久生效

   + 启动Apache网站
     + systemctl start httpd.service
     + lsof -i:80              #查看http服务是否启动

   + 测试

     + 方法一：用浏览器直接输入虚拟机IP，查看是否跳出红帽测试页面
     + 方法二：使用文本浏览器，方便测试
       + yum install -y elinks          #安装elinks文本浏览器
       + elinks IP                              #使用文本浏览器查看页面，Ctrl+c退出

     + 方法三：curl IP

4. 建立网站主页

   **注：网站主页默认：index.html**

   例：

   ```
   [root@localhost html]# vim index.html
   
   <html>
   <head>
   <title>TEST</title>
   </head>
   <body>
   <center><h1>Welcome!</h1></center>
   </body>
   </html>
   ```

   



​	