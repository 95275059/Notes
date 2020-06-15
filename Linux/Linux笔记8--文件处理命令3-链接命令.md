---
title: Linux笔记--文件处理命令3-链接命令
date: 2019-04-17 22:01:32
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89364806](https://blog.csdn.net/zhaandzha/article/details/89364806)   
    
   1、文件处理命令 ln(link)

 命令所在路径：/bin/ln

 执行权限：所有用户

 语法： ln -s [原文件] [目标文件] (原文件：需建立链接的文件，目标文件：新生成的链接文件名)

 -s 创建软链接

 功能：生成链接文件

 例： 创建文件/etc/issue的软链接/tmp/issue.soft : ln -s /etc/issue /tmp/issue.soft

 创建文件/etc/issue的硬链接/tmp/issue.hard : ln /etc/issue /tmp/issue.hard

 2.补充：软链接

 软链接特征：类似Windows快捷方式

 (1).lrwxrwxrwx l即软链接

 所有者，所属组和其他的权限都是rwx。但并不是所有用户都能运行源文件，即用户对软链接操作时具有的权限是由软链接对应的源文件的权限最终决定的

 (2).文件大小很小--只是符号链接 

 (3)./tmp/issue.soft -> /etc/issue 箭头指向源文件

 3.补充：硬链接

 硬链接特征：

 (1).(拷贝cp -p )+同步更新

 echo "testcxy" >> /etc/issue

 ![](https://img-blog.csdnimg.cn/20190417213636464.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70)

 注：在原文件新增一行后，issue.hard文件也同步进行了更新。

 而issue.soft只是一个符号链接，指向原文件，所以用cat命令显示issue.soft时内容也是更新后的

 同时，源文件丢失，不会影响硬链接文件。

 ![](https://img-blog.csdnimg.cn/20190417214834794.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70)

 注：本操作过程先将issue备份，然后删除该文件，软链接文件/tmp/issue.soft由于找不到源文件(通过windows快捷方式理解)在用cat命令显示文件内容时报错(no such file or directory)。而硬链接文件能正常打开访问，不受影响

 (2).通过i节点识别

 在Linux中每个文件都有一个唯一标识inode。一个文件只有一个i节点，但一个i节点不一定只对应一个文件。

 这就解释了将源(硬链接)文件删除，硬链接(源)文件，因为一个i节点映射到了多个文件。

 也解释了硬链接的同步更新功能。当对一个文件进行写操作时，在内核层面操作是针对的i节点进行操作。而该i节点映 射到了两个文件，也就能够进行同步更新

 ![](https://img-blog.csdnimg.cn/20190417220019792.PNG)

 (3).不能跨分区(软链接可以)

 (4).不能针对目录使用(软链接可以)

 

   
 