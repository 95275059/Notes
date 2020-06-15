# Linux笔记54--Shell编程9-流程控制2-case语句

1. 多分支case条件语句

   case只能判断一种条件关系，而if语句能够判断多种条件关系

   ```
   case $变量名 in
   	"值1")
   		如果变量的值等于值1，则执行程序1
   		;;
   	"值2")
   		如果变量的值等于值2，则执行程序2
   		;;
   	...省略其他分支...
   	*）
   		如果变量的值都不是以上的值，则执行此程序
   		;;
   esac
   ```

   例：

   ```
   #!/bin/bash
   
   read -t 30 -p "Please choose yes/no:" cho
   
   case $cho in
   	"yes")
   		echo "Your choose is yes!"
   		;;
   	"no")
   		echo "Your choose is no!"
   		;;
   	*)
   		echo "Your choose is error!"
   		;;
   esac
   ```

   