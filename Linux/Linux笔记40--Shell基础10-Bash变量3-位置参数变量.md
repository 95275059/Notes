# Linux笔记40--Shell基础10-Bash变量3-位置参数变量

1. 位置参数变量

   | 位置参数变量 | 作用                                                         |
   | :----------: | ------------------------------------------------------------ |
   |      $n      | n为数字，$0代表命令本身，$1-$9代表第一到第九个参数，十以上的参数需要用大括号包含，如${10} |
   |      $*      | 代表命令行中所有的参数，$*把所有的参数看成一个整体           |
   |      $@      | 代表命令行中所有的参数，不过$@把每个参数区分对待             |
   |      $#      | 代表命令行中所有参数的个数                                   |

   ---

   + 例一：加法程序sum.sh

     ```
     #!/bin/bash
     num1=$1
     num2=$2
     sum=$((num1+num2))
     echo $sum
     ```

     执行时：bash sum.sh 1 2

   ---

   + 例二

     ```
     #!/bin/bash
     echo "A total of $# parameters"     #输出参数个数
     echo "The parameters is:$*"         #输出所有参数
     echo "The parameters is:$@"         #输入所有参数
     ```

   ---

   + 例三：$*和$@的区别

     ```
     #!/bin/bash
     for i in "$*"   #&*中所有参数看成一个整体，该for循环只会循环一次
     	do
     		echo "The parameters is:$i"
     	done
     
     for y in "$@"  #$@中每个参数都是独立的，所以“$@”中有几个参数就会循环几次
     	do
     		echo "The parameters is:$y"
     	done
     ```

     bash canshu.sh 1 2 3 4

     第一个输出：

     The parameters is:1 2 3 4

     第二个输出：

     The parameters is:1

     The parameters is:2

     The parameters is:3

     The parameters is:4