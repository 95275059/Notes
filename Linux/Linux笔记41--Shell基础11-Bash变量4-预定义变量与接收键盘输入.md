# Linux笔记41--Shell基础11-Bash变量4-预定义变量与接收键盘输入

1. 预定义变量

   | 预定义变量 | 作用                                                         |
   | ---------- | ------------------------------------------------------------ |
   | $?         | 最后一次执行的命令的返回状态。如果这个变量的值为0，证明上一个命令正确执行。如果这个变量的值为非0（具体是哪个数，由命令自己决定），则证明上一个命令执行不正确（echo $?） |
   | $$         | 当前进程的进程号（PID）                                      |
   | $!         | 后台运行的最后一个进程的进程号（PID）                        |

   + 例

     ```
     #!/bin/bash
     echo "The current process is "$$"   #输出当前进程的PID，该PID就是当前脚本执行时，生成的PID
     
     find /home/cxy/sh -name hello.sh &  #使用find命令在root目录下查找hello.sh文件
     							        #符号&的意思是把命令放入后台执行
     echo "The last one Daemon process is $!"
     ```

2. 接收键盘输入

   read [选项] [变量名]

   | 选项          | 含义                                                   |
   | ------------- | ------------------------------------------------------ |
   | -p “提示信息” | 在等待read输入时，输出提示信息                         |
   | -t 秒数       | read命令会一直等待用户输入，使用此选项可以指定等待时间 |
   | -n 字符数     | read命令只接收指定的字符数就会执行                     |
   | -s            | 隐藏输入的数据，适用于机密信息的输入                   |

   + 例

     ```
     #!/bin/bash
     
     read -t 30 -p "Please input your name:" name
     echo "Name is $name"
     
     read -s -t 30 -p "Please input your age:" age
     echo -e "\n"
     echo "Age is $age"
     
     read -n 1 -t 30 -p "Please select your gender[M/F]:" gender
     echo -e "\n"
     echo "Sex is $gender"
     
     ```

     