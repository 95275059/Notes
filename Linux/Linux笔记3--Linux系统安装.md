---
title: Linux笔记--Linux系统安装
date: 2019-04-15 17:13:37
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89307734](https://blog.csdn.net/zhaandzha/article/details/89307734)   
    
   所用软件：VMware;Linux版本：CentOS7

 1.打开虚拟机后进入BIOS设置

 计算机开机默认是通过硬盘启动。但虚拟机硬盘是空的，通过硬盘启动会报错：系统找不到操作系统。只有通过光盘启动才能进入操作界面。

 进入BIOS设置后，BOOT=>将光盘驱动移到最上面(+)(CD-ROM Drive)=>Exit=>Exit Saving Changes

 实际上，在第一次开机安装操作系统时，虚拟机会自动调整顺序，先通过光盘启动，之后开机仍然先通过硬盘启动，所以用虚拟机不需要这一步，而真实机不会自动调整，必须手动调整。真实机在第一次安装操作系统后，还需要将启动顺序改回来，改成硬盘先启动。

 2.install centOS7

 linux开始进入系统自检，检测内存大小，太小会进入linux的字符界面，而不是图形界面( 图形界面比字符界面更简单和可靠)。

 之后会自动检测磁盘，显卡等。

 3.语言设置=>时区设置=>主机名设置(建议就用默认主机名)=>分区=>创建ROOT密码

 (1)主机名

 Linux对主机名不敏感。Windows中，局域网内主机名不可重复。但Linux没有这个要求，所以可以所有主机都用同一主机名

 (2)分区

 在分区时，可直接用自动分区。

 若手动分区，其中/boot存放启动数据，自动分配在sda1。若强制改成别的，会造成系统不能正常启动；根分区最后分，大小为硬盘大小减去所有已分配分区大小；swap分区不需要挂载点，文件类型为swap，因为swap分区是由Linux操作系统/内核直接调用；在分第四个分区时，系统不能确定用户是否还会再分区，就将sda4设为扩展分区，之后分的区称为逻辑分区。

 (3)ROOT密码

 密码原则：

 复杂性：八位字符以上，大小写字母，数字，符号；含这三种字符则满足复杂性；不能是英文单词；内容不能和用户相 关

 易记忆性

 

 时效性

 (4)软件包选择

 Desktop;Minimal Desktop;Minimal(最小化);Basic Server(基本服务器);Database Server;Web Server(网页服务器);Virtual Host(虚拟主机);software development workstation(软件开发工作站)

 若用做服务器，推荐最小化安装。最小化：无图形界面，应用性低，安全性高，稳定性高

 

 4.安装日志

 /root/install.log:存储了安装在系统中的软件包及其版本信息

 /root/install.log.syslog:存储了安装过程中留下的事件记录

 /root/anaconda-ks.cfg:以Kickstart配置文件的格式记录安装过程中设置的选项信息

 

 注：管理员家目录：/root

 普通用户目录：/home/cxy(用户名为cxy)

 

   
 