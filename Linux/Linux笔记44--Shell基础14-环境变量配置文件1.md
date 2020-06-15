# Linux笔记44--Shell基础14-环境变量配置文件1

1. source命令

   source 配置文件    或    .配置文件

   配置文件修改后，必须重新登录配置文件才会重新生效，source命令能够强制让配置文件直接重新生效。

2. 环境变量配置文件

   环境变量配置文件主要是定义对系统的操作环境生效的系统默认环境变量，比如PATH、HISTSIZE、PS1、HOSTNAME等默认环境变量

   **注：/etc下的所有配置文件对登录的所有用户都生效**

   + /etc/profile
   + /etc/profile.d/*.sh
   + ~/.bash_profile     #只对root用户生效    #修改哪个用户家目录下的.bash_profile对哪个用户生效
   + ~/.bashrc               #只对root用户生效    #修改哪个用户家目录下的.bashrc对哪个用户生效
   + /etc/bashrc

3. 环境变量配置文件调用顺序

   ![笔记45-1](E:\notes\Linux\笔记45-1.PNG)

   注：/etc/profile.d/lang.sh主要用于定义系统语言；/etc/sysconfig/i18n用于保存系统默认语言环境

   注：在centos7之后，是在/etc/locale.conf中保存系统默认语言环境，不是/etc/sysconfig/i18n

4. /etc/profile作用
   + USER变量
   + LOGNMAE变量
   + MAIL变量
   + PATH变量
   + HOSTNAME变量
   + HISTSIZE变量
   + umask
   + 调用/etc/profile.d/*.sh文件

5. ~/.bash_profile作用
   + 调用了~/.bashrc文件
   + 在PATH变量后面加入了“:$HOME/bin”这个目录并声明PATH为环境变量

6. ~/.bashrc作用
   + 定义别名
   + 调用/etc/bashrc

7. /etc/bashrc作用
   + 定义了默认登录提示符PS1
   + umask变量（没有登录Shell的情况）
   + PATH变量（没有登录Shell的情况）
   + 调用/etc/profile.d/*.sh文件（没有登录Shell的情况）