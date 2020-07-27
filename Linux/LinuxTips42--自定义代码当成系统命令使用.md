# LinuxTips42--自定义代码当成系统命令使用

### 方法一

将代码放在环境变量的任意路径中取用

### 方法二

+ shell脚本

  + 先查看缺省shell是哪一个。
     如果是/bin/sh 则在文件的第一行中写#!/bin/sh
     如果是/bin/bash 则在文件的第一行中写#!/bin/bash

  + 将shell脚本放到环境变量的路径中去

    如：/usr/bin目录

  + 设定可执行权限

+ python

  + 首行“#!/usr/bin/python” 或 "#!/usr/bin/env python" 

  + 将python代码放到环境变量的路径中去

    如：/usr/bin目录

  + 设定可执行权限