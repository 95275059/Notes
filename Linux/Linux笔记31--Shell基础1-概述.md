# Linux笔记31--Shell基础1-概述

1. Shell

   + Shell是一个==命令行解释器==，为用户提供了一个向Linux内核发送请求以便运行程序的界面系统级程序，用户可以用Shell来启动、挂起、停止甚至是编写一些程序。（其实就是交互界面）

     硬件   -->   内核   -->   Shell命令解释器   -->外层应用程序

     ​               （0101）                                          （ls,cd,...）

     Shell就是一个交互界面，将输入的命令翻译为内核可以识别的机器语言。

     内核将命令传递给硬件执行，然后将执行结果翻译为用户可识别的执行结果送给外层交互界面

   + Shell是一个功能强大的==编程语言==，易编写、易调试，灵活性较强。Shell是==解释执行==的脚本语言，在Shell中可以直接调用Linux系统命令。

     解释执行：不需要先单独进行编译，命令在输入完执行过程中自动进行编译。

   ---

2. Shell分类

   + Bourne Shell：从1979起Unix开始使用Bourne Shell，Bourne Shell的主文件名为sh。
   + C Shell：C Shell主要在BSD版的Unix系统中使用，其语法和C语言相类似。

   注：Shell的两种主要语法类型有Bourne和C，这两种语法彼此不兼容。Bourne家族主要包括sh、ksh、==Bash==、psh、zsh；C家族主要包括：csh、tcsh。

   + Bash：Bash与sh兼容，现在使用的Linux就是使用Bash作为用户的基本Shell

   ---

3. Linux支持的Shell

   + /etc/shells 文件可以查询系统支持的shell

   + 注：/etc/passwd 为用户信息文件

     能登陆的用户使用的是Linux标准Shell

     其他伪用户（系统用户）使用的Shell是/sbin/nologin或者只能执行某一条系统命令。