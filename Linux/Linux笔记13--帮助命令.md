---
title: Linux笔记--文件搜索命令3-帮助命令
date: 2019-04-22 10:53:06
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89406840](https://blog.csdn.net/zhaandzha/article/details/89406840)   
    
   1.帮助命令 man(manual)

 命令所在路径：/usr/bin/man

 执行权限：所有用户

 语法：man [命令或配置文件]

 功能：获得帮助信息

 可以精确查找：/搜索关键词，并可以按n进行继续查找。 例如希望查看所有关于-l选项的说明可以输入/-l回车查看。

 注：查看配置文件的帮助信息时，不需要写其绝对路径，否则会将该配置文件的内容显示出来。只需要写配置文件名 

 有些命令和配置文件同名(如passwd),再用man查看passwd的帮助文档时，系统默认先查看命令的帮助文档。

 帮助类型有很多，man1一般存放命令的帮助，man5一般存放配置文件的帮助

 若希望查看passwd配置文件的帮助：man 5 passwd

 

 2.帮助命令whatis

 命令所在路径：/usr/bin/whatis

 执行权限：所有用户

 语法：whatis [命令名称]

 功能：查看命令帮助文档的NAME部分，即该命令的功能

 3.帮助命令apropos 

 命令所在路径：/usr/bin/apropos

 执行权限：所有用户

 语法：apropos [配置文件名称]

 语法：查看配置文件帮助文档的NAME部分，即该配置文件的功能

 4.帮助命令--help

 语法：[命令] --help

 功能：显示命令的常用选项及功能

 

 5.帮助命令 help

 命令所在路径：Shell内置命令

 执行权限：所有用户

 语法：help 命令

 功能：获得Shell内置命令的帮助信息

 注：找不到命令所在路径的的命令都是Shell内置命令 ；centos7 中能查看到cd umask的路径

 ![](https://img-blog.csdnimg.cn/20190422104009595.PNG)

 用man 命令查看命令NAME部分如上显示的，都是Shell内置命令。这不是命令的帮助文档。NAME下的都是Shell命令。

 这时要用help命令查看对应命令的帮助信息

 

   
 