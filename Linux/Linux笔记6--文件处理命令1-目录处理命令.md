---
title: Linux笔记--文件处理命令1-目录处理命令
date: 2019-04-17 18:49:42
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89355577](https://blog.csdn.net/zhaandzha/article/details/89355577)   
    

**1.命令格式**


> 命令 [-选项] [参数] 
> 
>  
 注：个别命令使用不遵循此格式；

 当有多个选项时，可以写在一起，一般不强调顺序；

 简化选项与完整选项 ( -a等于--all )

 **2.目录处理命令 ls(list)**

 命令所在路径：/bin/ls

 执行权限：所有用户

 功能描述：显示目录文件

 (1).ls -a : a即all查看目录下所有文件(隐藏文件以.开头)

 (2).ls -l : l即long长格式显示，会显示目录下文件的相关属性

 文件和用户的关系：U(USER所有者) G(GROUP所属组) O(OTHER 其他)

 第一部分：例如：-rw-r--r-- 文件类型+权限

 文件类型 ：-(二进制文件)；d(d即directory 目录)；l(l即link 软链接文件)

 权限：r(read) ; w(write) ; x(execute)(最高权限) rw-(U) r--(G) r--(O)

 第二部分：引用计数

 第三部分：所有者 (一般情况所有者是创建文件的人，只有一个，理论上所有者可以变化，但一般不变) 

 第四部分：所属组

 第五部分：文件大小，默认大小是字节

 第六部分：最后修改时间

 第七部分：文件名

 (3).ls -h : h即human即人性化显示，可人性化显示文件、分区大小。

 (4).ls -d : 查看目录属性 经常和-l连用，显示目录详细信息

 (5).ls -i : i即inode 查看文件/目录的inode

 inode:每个文件或目录都有的唯一标识的id号

 **3.目录处理命令mkdir(make directories)**

 命令所在路径：/bin/mkdir

 执行权限：所有用户

 语法：mkdir -p [目录名]

 功能描述：创建新目录 ;-p 递归创建

 递归创建：在/tmp下创建China后，希望在/tmp/China目录下再创建Hebei子目录时

 若：mkdir /tmp/China/Hebei 会报错：No such file or directory

 此时用-p选项即可：mkdir -p /tmp/China/Hebei

 另外可以同时创建多个目录：mkdir /tmp/China/Hebei /tmp/China/Henan

 **4.目录处理命令cd(change directory)**

 命令所在路径：shell内置命令 (兄弟连教程)|| which命令显示在：/usr/bin/cd

 执行权限：所有用户

 语法：cd [目录]

 功能：切换目录

 切换到制定目录 : cd /tmp/China/Hebei

 切换到上级目录 : cd .. ('.'代表当前目录，'..'代表当前目录的上一级目录)

 **5.目录处理命令pwd(print working directory)**

 命令所在路径：/bin/pwd

 执行权限：所有用户

 语法：pwd

 功能：显示当前目录

 **6.目录处理命令rmdir(remove empty directory)**

 命令所在路径：/bin/rmdir

 执行权限：所有用户

 语法：rmdir [目录名]

 功能：删除空目录

 rmdir /tmp/China/Hebei

 **7.目录处理命令cp(copy)--对文件和目录都可以**

 命令所在路径：/bin/cp

 执行权限：所有用户

 语法： cp -rp [原文件或目录] [目标目录]

 cp -r 复制目录

 cp -p 保留文件或目录属性

 功能描述：复制文件或目录

 例：cp /etc/grub.conf /tmp : 将etc目录下的grub.conf文件复制到tmp目录下(若复制文件则没有选项)

 cp /root/install.log /root/install.log.syslog /tmp :同时将多个文件复制，只要最后写上目标目录即可

 cp -r /tmp/China/Hebei /root : 复制目录Hebei到root目录下

 注：将一个文件拷贝到另一个位置/r，/r下的文件的最后修改时间为拷贝时间，相当于在这个目录下创建了一 个文件。原文件的最后修改时间不变

 若不希望改变文件的最后修改时间等属性，需要加-p选项

 复制同时更名：cp -r /tmp/text /tmp/China/textrenamed

 复制同时更名同时保留属性：cp -rp /tmp/text tmp/China textrenamed

 **8. 目录处理命令mv(move)--对文件或目录都可以**

 命令所在路径：/bin/mv

 执行权限：所有用户

 语法：mv [原文件或目录] [目标目录]

 功能描述：剪切文件或目录，改名

 剪切： mv /tmp/text /tmp/China(若当前位置已在/tmp 则可以直接：mv text /tmp/China)

 剪切同时改名：mv /tmp/text /tmp/China/textrenamed

 在某文件当前目录下改其文件名：mv text textrenamed

 **9. 目录处理命令rm(remove)--对文件或目录都可以**  

 命令所在路径：/bin/rm

 执行权限：所有用户

 语法：rm -rf [文件或目录]

 rm -r 删除目录

 rm -f 强制执行(不进行询问)

 功能描述：删除文件或目录

 注：在删除非空目录时，会从最底层子目录(文件)一个一个开始删除，在目录数据较多时，会很不方便

 例如：删除tmp目录下的China目录，已知China目录下还有text目录

 ![](https://img-blog.csdnimg.cn/20190417172011411.PNG)

 所以一般用 rm -rf /tmp/China:即使China目录下文件再多，也可以直接删除

 ![](https://img-blog.csdnimg.cn/20190417172928893.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70)

 例如：rm -rf *    =>删除当前目录下所有文件