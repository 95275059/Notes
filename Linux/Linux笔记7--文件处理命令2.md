---
title: Linux笔记--文件处理命令2
date: 2019-04-17 20:47:03
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89362998](https://blog.csdn.net/zhaandzha/article/details/89362998)   
    
   **1.文件处理命令 touch** 

 命令所在路径：/bin/touch

 执行权限：所有用户

 语法：touch [文件名]

 功能描述：创建空文件

 例：在当前所在目录下创建文件：touch test.list

 在其他目录下创建文件必须指明绝对路径：touch /tmp/China/test.list

 注：在Windows中，文件名可以含空格，但是用命令touch test one试图创建名为test one的文件是错误的，实际上是创建了两个文件，一个为test，一个为one

 若希望创建一个文件名带空格的文件：touch "test one"  (不建议这样起名字，因为一直需要带引号)

 **2.文件处理命令 cat**

 命令所在路径：/bin/cat

 执行权限：所有用户

 语法：cat [文件名]

 cat -n 显示行号(n即number)

cat -A 文件名    **查询所有文件内容，包括隐藏字符**

 功能：显示文件内容

 例：cat -n /etc/issue(系统中一个用于显示欢迎信息的文件)

 注：cat命令不适合用于查看数据量比较大的文件，因为最后只能显示最后几页数据，不方便。

**3.文件处理命令 tac**

 命令所在路径：/usr/bin/tac

 执行权限：所有用户

 语法：tac [文件名]

 功能：显示文件内容(反向列示)

 ![](https://img-blog.csdnimg.cn/20190417200620651.PNG)

 注：tac命令中没有-n选项

 **4.文件处理命令 more**

 命令所在路径：/bin/more

 执行权限：所有用户

 语法：more [文件名]

 (空格)或f 翻页

 (Enter) 换行

 q或Q 退出

 功能：分页显示文件内容

 **5.文件处理命令 less**

 命令所在路径：/usr/bin/less

 执行权限：所有用户

 语法：less [文件名]

 pageup : 一页一页向上翻

 ↑ : 一行一行向上翻

 功能：分页显示文件内容(可向上翻页)

 还可以进行搜索：在less浏览状态中，输入/关键词 回车可显示搜索结果；

 若在该搜索结果页中未找到想搜索的数据，按n(next)进行继续搜索

 **6.文件处理命令 head**

 命令所在路径：/usr/bin/head

 执行权限：所有用户

 语法：head [文件名]

 功能：显示文件前面几行

 -n 指定行数(没有-n指定行数 默认显示前十行)

 例：head -n 20 /etc/services

**7.文件处理命令 tail**

 命令所在路径：/usr/bin/tail

 执行权限：所有用户

 语法：tail [文件名]

 功能：显示文件后面几行

 -n 指定行数(没有-n指定行数 默认显示最后十行)

 -f 动态显示文件末尾内容

 例：tail -n 18 /etc/services

 tail -f /var/messages (messages文件是一个日志文件) 该操作会显示最后十行数据但不会回到命令行，若文件内容发生变化，在此命令操作状态下也会更新变化

   
