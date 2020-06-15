# Linux笔记56--Shell编程11-流程控制4-while循环与until循环

1. while循环：知道条件判断式不成立时结束循环

   while循环是不定循环

   ```
   while [ 条件判断式 ]
   	do
   		程序
   	done
   ```

   例：从1加到100

   ```
   #!/bin/bash
   i=1
   sum=0
   while [ $i -le 100 ]
   	do
   		sum=$(($sum+$i))
   		i=$(($i+1))
   	done
   echo "1+2+...+100=$sum"
   ```

2. until：知道条件判断式成立时结束循环

   ```
   until [  条件判断式 ]
   	do
   		程序
   	done
   ```

   例：从1加到100

   ```
   #!/bin/bash
   i=1
   sum=0
   until [ $i -gt 100 ]
   	do
   		sum=$(($sum+$i))
   		i=$(($i+1))
   	done
   echo "1+2+...+100=$sum"
   ```

   