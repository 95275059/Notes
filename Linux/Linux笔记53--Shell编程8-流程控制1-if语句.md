# Linux笔记53--Shell编程8-流程控制1-if语句

1. 单分支if条件语句

   ```
   if [ 条件判断式 ];then
   	程序
   fi
   ```

   ```
   if [ 条件判断式 ]
   	then
   		程序
   fi
   ```

   + 注意：
     + if语句使用fi结尾
     + [ 条件判断式 ]就是使用test命令判断，中括号和条件判断式之间必须有空格

   + 例：判断分区使用率

     ```
     #!/bin/bash
     
     rate = $(df -h | grep "/dev/mapper/centos-root" | awk '{print $5}' | cut -d "%" -f 1)
     if [ $rate -ge 80 ]
     	then 
     		echo "Warning! /dev/mapper/centos-root is full!!!"
     fi
     ```

2. 双分支if条件语句

   ```
   if [ 条件判断式 ]
   	then
   		条件成立时，执行的程序
   	else
   		条件不成立时，执行的另一个程序
   fi
   ```

   + 例：备份etc目录

     ```
     #!/bin/bash
     
     ntpdate asia.pool.ntp.org &>/dev/null    #同步系统时间,必须联网才行
     date=$(date +%y%m%d)      #将当前系统时间按照“年月日”格式赋予变量date
     size=$(du -sh /etc)     #统计mysql数据库的大小，并把大小赋予size变量
     
     if [ -d /tmp/dbbak ]
     	then
     		echo "Date : $date!" > /tmp/dbbak/dbinfo.txt
     		echo "Data size : $size" >> /tmp/dbbak/dbinfo.txt
     		cd /tmp/dbbak
     		tar -zcf mysql-lib-$date.tar.gz /etc dbinfo.txt &>/dev/null
     		rm -rf /tmp/dbbak/dbinfo.txt
     	else
     		mkdir /tmp/dbbak
     		echo "Date : $date!" > /tmp/dbbak/dbinfo.txt
     		echo "Data size : $size" >> /tmp/dbbak/dbinfo.txt
     		cd /tmp/dbbak
     		tar -zcf mysql-lib-$date.tar.gz /etc dbinfo.txt &>/dev/null
     		rm -rf /tmp/dbbak/dbinfo.txt
     fi
     ```

     date +%y%m%d         这条命令能够将系统时间按照“年月日”的格式输出

   + 例：判断apache是否启动

     ```
     #!/bin/bash
     
     port=$(nmap -sT 192.168.1.161 | grep tcp | grep http | awk '{print $2}')
     #使用nmap命令扫描服务器，并截取apache服务的状态，赋予变量port
     
if [ "$port" == "open" ]          #双等号两边空格必须有
     	then
  		echo "$(date) httpd is ok!" >> /home/cxy/sh/autostart-acc.log
     	else
     		systemctl start httpd &> /dev/null
     		echo "$(date) restart httpd!" >> /home/cxy/sh/autostart-err.log
     fi
     ```

3. 多分支if条件语句

   ```
   if [ 条件判断式1 ]
   	then
   		当条件判断式1成立时，执行程序1
   elif [ 条件判断式2 ]
   	then
   		当条件判断式2成立时，执行程序2
   ...
   else
   	当所有条件都不成立时，最后执行此程序
   fi
   ```

   例：判断用户输入的是什么文件

   ```
   #!/bin/bash
   
   read -p "Please input a filename：" file
   #接收键盘输入并赋予变量file
   
   if [ -z $file ]
   #判断file是否为空
   	then
   		echo "Error,please input a filename!"
   		exit 1        #退出程序，返回值为1，可用$?查看
   		              #报错语句记得加Exit直接跳出
   elif [ ! -e $file ]
   #判断file是否存在
   	then
   		echo "Your input is not a file!"
   		exit 2
   elif [ -f $file ]
   #判断file是否为普通文件
   	then 
   		echo "$file is a regulare file!"
   elif [ -d $file ]
   #判断file是否为目录文件
   	then
       	echo "$file is a directory!"
   else
   	echo "$file is an other file!"
   fi
   ```

   

​	



