---
title: Linux笔记--权限管理命令2
date: 2019-04-19 14:38:30
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89375330](https://blog.csdn.net/zhaandzha/article/details/89375330)   
    
   1.权限管理命令 chown(change file ownership)--对文件或目录都可以

 命令所在路径：/bin/chown

 执行权限：root

 语法：chown [用户] [文件或目录] (用户:新的所有者)

 功能：改变文件或目录的所有者

 2.权限管理命令 chgrp(change file group ownership)

 命令所在路径：/bin/chgrp

 执行权限：root

 语法：chgrp [用户组] [文件或目录]

 功能：改变文件或目录的所属组

 ![](https://img-blog.csdnimg.cn/20190419134004786.PNG)

 注：groupadd命令为添加组，只能由root创建

 3.权限管理命令 umask(the user file-creation mask)

 命令所在路径：Shell内置命令

 执行权限：所有用户

 语法：umask [-S]

 -S 以rwx形式显示新建文件缺省权限

 功能：显示，设置文件的缺省权限 

 例1：

 ![](https://img-blog.csdnimg.cn/20190419140240555.PNG)

 在创建文件或目录时，所有者是创建该文件/目录的用户，所属组是缺省权限

 注意到，目录China(rwxrx-r-x)和文件test(rw-r--r--)的权限不一样，这是因为在Linux中权限管理有一个基本定义：缺省创建 的文件不能具有可执行权限(x)，这是基于安全性考虑(对于一些病毒木马文件，使其没有执行权限)

 例2：

 ![](https://img-blog.csdnimg.cn/20190419140947883.PNG)

 0：一种特殊权限 ；

 022：代表三种用户(UGO)的权限

 如果是目录：将777(rwx rwx rwx)与022(--- -w- -w-)做异或运算求得755(rwx r-x r-x)

 如果是文件：默认缺省权限为 : rw- r-- r--

 注：如果希望目录的缺省权限为700(rwx --- ---)(此时文件的缺省权限为600 : rw- --- ---) 则需要修改umask 

 将运算过程逆过来，得到umask应该改为077(--- rwx rwx) **[不推荐更改umask]**

 ![](https://img-blog.csdnimg.cn/20190419143529294.PNG)

 

   
 