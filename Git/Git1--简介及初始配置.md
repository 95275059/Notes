# Git1--简介及初始配置

1. 分布式版本控制系统

2. Git安装

   + 按默认选项安装即可

   + 检测

     在开始菜单找到Git - Git Bash

     出现命令行bash窗口就说明安装成功

   + 设置

     ```bash
     $ git config --global user.name "Your Name"
     $ git config --global user.email "email@example.com"
     ```

3. 创建版本库

   + 进入创建版本库的目标空目录

   + 在该空目录下打开Git Bash

     ```bash
     $ git init
     Initialized empty Git repository in E:/Git/.git/
     ```
     
     + git init命令可以把目录变成Git可以管理的仓库

   注：空目录下多出来的.git目录是Git用来跟踪管理版本库的，**没事不要手动修改该目录里面的文件**，不然改乱了，就把Git仓库给破坏了

4. 把文件添加到版本库

   + 所有的版本控制系统，只能跟踪文本文件的改动

     比如：TXT文件，网页，所有的程序代码

   + 图片，视频这种二进制文件虽然也能由版本控制系统管理，但是无法跟踪文件的变化，只能把二进制文件每次改动串起来，但是到底改了什么，版本控制系统不知道
   
   + word文档是二进制格式
   
   + 操作步骤
   
     + 在仓库目录下新建readme.txt文件
   
       ```
       Git is a version control system.
       Git is free software
       ```
     
   + 将文件添加到仓库
     
       ```bash
       $ git add readme.txt
     ```
     
     + 将文件提交到仓库
     
       ```bash
       $ git commit -m "wrote a readme file"
       ```
     
       + -m 后面输入本次提交的说明
       + commit可以一次提交很多添加到仓库的文件

