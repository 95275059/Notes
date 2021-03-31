# Linux笔记49--Shell编程4-字符截取命令3-awk命令

### student.txt:

```
ID      Name    PHP     LINUX   MySQL   Average
1       Liming  82      95      86      87.66
2       Sc      74      96      87      85.65
3       Gao     99      83      93      91.66
```

### awk '条件1{动作1} 条件2{动作2} ...' 文件名

+ awk命令是一行一行读取文件，根据条件动作输出要求进行输出后再读取下一行
+ 处理每一行数据时，先读入一行数据，在根据条件动作执行输出。
+ awk默认空格为分隔符

+ 条件(Pattern)

  一般使用关系表达式作为条件

  x>=10	判断变量x是否大于等于10

+ 动作(Action)

  格式化输出

  流程控制语句

### 实例

+ 例1：输出第二列第六列并用制表符Tab分开，回车键换行

  ```shell
  awk '{printf $2 "\t" $6 "\n"}' student.txt
  ```
  
  **$0代表整个行本身**

+ 例2：提取sda1磁盘的已用百分数(不加%输出)

  ```shell
  df -h | grep "sda1" | awk '{printf $5 "\n"}' | cut -d "%" -f 1   
  ```

---

2. BEGIN:在所有数据读取之前，执行BEGIN后面的动作，然后处理后面的内容

   awk 'BEGIN{printf "This is a transcript\n"} {printf $2 "\t" $6 "\n"}' student.txt

   输出：

   This is a transcript
   Name	Average
   Liming	87.66
   Sc	85.65
   Gao	91.66

   ---

3. FS内置变量：指定分隔符

   若想要指定“:”为分隔符，用FS=“:”来指定，或者-F

   awk '==BEGIN=={FS=":"} {printf $1 "\t" $3 "\n"}' /etc/passwd

   ping -c 3 www.baidu.com | grep loss | awk -F ':' {print $6}

   #注：这里必须加BEGIN，否则第一行是输出整行数据，因为awk是先读取了第一行，再执行后面的条件动作

   ---

4. END:在所有行都读取完毕执行结束后，执行END后面的动作

   awk 'END{printf “The End\n”} {printf $1 "\t" $3 "\n"}' /etc/passwd

   ---

5. 关系运算符

   cat student.txt | grep -v Name | awk '$6>=87 {printf $2 "\n"}'     

   输出：

   Liming
   Gao

