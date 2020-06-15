# Linux笔记65--启动管理1-启动流程1-运行级别

1. 运行级别

   centos6

   | 运行级别 | 含义                                                         |
   | -------- | ------------------------------------------------------------ |
   | 0        | 关机                                                         |
   | 1        | 单用户模式，可以想想为windows的安全模式，主要用于系统修复（至启东最基本的程序，服务） |
   | 2        | 不完全的命令行模式，不含NFS（Network File System）服务       |
   | 3        | 完全的命令行模式，就是标准字符界面                           |
   | 4        | 系统保留                                                     |
   | 5        | 图形模式                                                     |
   | 6        | 重启动                                                       |

   centos7

   | 运行级别 | 含义              |
   | -------- | ----------------- |
   | 0        | shutdown.target   |
   | 1        | emergency.target  |
   | 2        | rescure.target    |
   | 3        | multi-user.target |
   | 4        | 无                |
   | 5        | graphical.target  |
   | 6        | 无                |

   

2. 运行级别命令（centos6）

   + 查看运行级别

     runlevel

     输出：N 3

     含义：N：在进入3级别之前所处的级别，N代表null，即开机后直接进入3级别

   + 改变运行级别命令

     init 运行级别

3. 系统默认运行级别（centos6）
   + 设置系统开机后直接进入的运行级别
     + vim /etc/inittab
     + id:3:initdefault:

4. 设置运行级别（centos7）

   systemctl [command] [unit.target]

   + command

     get-default:取得当前的target

     set-default:设置指定的target为默认的运行级别

     isolate:切换到指定的运行级别

     



