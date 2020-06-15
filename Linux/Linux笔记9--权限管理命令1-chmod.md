---
title: Linux笔记--权限管理命令1-chmod
date: 2019-04-18 11:35:10
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89372659](https://blog.csdn.net/zhaandzha/article/details/89372659)   
    
   1.权限管理命令chmod(change the permissions mode of a file)

 命令所在路径：/bin/chmod

 执行权限：文件所有者或者root

 语法：chmod [{ugoa}{+-=}{rwx}] [文件或目录] (a=all:所有人)

 [mode=421] [文件或目录]

 -R 递归修改

 功能：改变文件或目录权限

 例1：可以同时改变多种用户的权限，用逗号隔开

 ![](https://img-blog.csdnimg.cn/20190418102135262.PNG)

 例2：实际上，用的最多的是用数字方式

 权限的数字表示：r----4 ; w----2 ; x----1

 例：rwxrw-r-- =>7640.

 ![](https://img-blog.csdnimg.cn/20190418105131861.PNG)

 例3：递归修改权限

 递归修改就是在改变某目录权限的同时，递归修改其下所有子目录和文件的权限

 ![](https://img-blog.csdnimg.cn/20190418105716531.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70) 

 2.**文件目录权限总结**

 
     代表字符 | 权限       | 对文件的含义       | 对目录的含义 | r | w | x
     ---- | -------- | ------------ | ------ | - | - | - 
     读权限  | 可以查看文件内容 | 可以列出目录中的内容   |        |   |   |  
     写权限  | 可以修改文件内容 | 可以在目录中创建删除文件 |        |   |   |  
     执行权限 | 可以执行文件   | 可以进入目录       |        |   |   |  



 

 

 

 

 对file: r=>cat/more/less/head/tail

 w=>vim 对文件有写权限只是说能修改文件内容

 x=>该文件可能是一个 script || command

 对directory: r=>ls 

 w=>touch/mkdir/rmdir/rm 对目录有写权限，可以创建删除目录下的文件

 x=>cd (一般r x同时出现) 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

   
 