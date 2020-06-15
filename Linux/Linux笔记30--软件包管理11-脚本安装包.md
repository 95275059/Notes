# Linux笔记30--软件包管理11-脚本安装包

​       **==注：必须桥接模式==**

1. 脚本安装包

   脚本安装包并不是堵路的软件包类型，常见脚本安装包安装的是源码包

   脚本安装包是人为把安装过程写成了自动安装的脚本，只要执行脚本，定义简单的参数，就可以完成安装

   类似于Windows下软件的安装方式

2. Webmin

   Webmin是一个基于Web的Linux系统管理界面。可以通过图形化（Web）的方式设置用户账号、Apache、DNS、文件共享等服务

   + 下载软件

     http://sourceforge.net/projects/webadmin/files/webmin/

   + 解压缩，并进入解压缩目录

   + 执行安装脚本setup.sh

     ./setup.sh

     默认用户名：admin

     密码：123456

     http://localhost.localdomain:10000/  **呸，直接IP:10000就可以**

   * 注意：开放10000端口

     systemctl-cmd --zone=public --add-port=10000/tcp --permanent

   + 如果浏览器打不开尝试重新打开webmin

     /etc/webmin/restart      #重启

     /etc/webmin/start          #启动

     /etc/webmin/stop          #停止