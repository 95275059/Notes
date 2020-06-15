---
title: Linux笔记--文件搜索命令4-用户管理命令
date: 2019-04-22 11:28:00
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89447687](https://blog.csdn.net/zhaandzha/article/details/89447687)   
    
   1.用户管理命令 useradd

 命令所在路径：/usr/sbin/useradd

 执行权限：root

 语法：useradd 用户名

 功能：添加新用户。只是添加了用户的基本信息(家目录等)

 2.用户管理命令 passwd

 命令所在路径：/usr/bin/passwd

 执行权限：所有用户

 语法：passwd 用户名

 功能：设置用户密码

 注：root可以随意指定任何用户任何形式的密码，而普通用户只能改自己的密码且必须遵守密码规则

 3.用户管理命令 who

 命令所在路径：/usr/bin/who

 执行权限：所有用户

 语法：who

 功能：查看登录用户信息

 ![](https://img-blog.csdnimg.cn/20190422111146302.PNG)

 格式： 用户名 登录终端 登录日期(登录终端的主机地址，若为本地登录则没有此部分)

 tty为本地登录(即虚拟机)，若将VMware上的root退出登录(exit)，则第一行消失.

 pts为远程终端，用终端号区分不同终端。

 4.用户管理命令 w

 命令所在路径：/usr/bin/w

 执行权限：所有用户

 语法：w

 功能：查看登录用户详细信息

 ![](https://img-blog.csdnimg.cn/20190422111849908.PNG)

 up:为连续运行时间(可以用uptime命令查看)。 

 load average:为负载均衡指数，分别显示过去一分钟，五分钟，十五分钟的负载情况

 IDLE：用户登录后空闲时间

 JCPU：用户登录后累计占用CPU时间

 PCPU：用户当前占用CPU时间

 WHAT：用户当前执行的操作

 

   
 