## Linux笔记55--Shell编程10-流程控制3-for循环

1. 语法一

   ```
   for 变量 in 值1 值2 值3 ...
   	do
   		程序
   	done
   ```

   例：打印时间

   ```
   #!/bin/bash
   
   for time in morning noon afternoon evening 
   	do
   		echo "This time is $time!"
   	done
   ```

   例：批量解压缩脚本

   ```
   #!/bin/bash
   
   cd /lamp
   ls *.tar.gz > ls.log
   for i in $(cat ls.log)
   	do 
   		tar -zxf $i &> /dev/null
   	done
   rm -rf /lamp/ls.log
   ```

2. 语法二

   ```
   for((初始值;循环控制条件;变量变化))
   	do
   		程序
       done
   ```

   例：从1加到100

   ```
   #!/bin/bash
   
   sum=0
   for ((i=1;i<=100;i=i+1))
   	do
   		sum=$(($sum+$i))
   	done
   echo "1+2+3+...+100=$sum"
   ```

3. 例：批量添加指定数量的用户

   ```
   #!/bin/bash
   
   read -t 30 -p "Please input user name:" name
   read -t 30 -p "Please input the number of users:" num
   read -t 30 -p "Please input the password of users:" pass
   
   if [ ! -z $name -a ! -z $num -a ! -z $pass ]
   	then
   		y=$(echo $num | sed 's/[0-9]//g')
   		if [ -z $y ]
   			then
   				for ((i=1;i<=$num;i=i+1))
   					do
   						useradd $name$i &> /dev/null
   						echo $pass | passwd --stdin $name$i &> /dev/null
   					done
   		fi
   fi
   ```

   **注：passwd --stdin 中的--stdin选项用于从标准输入管道读入新的密码**

   