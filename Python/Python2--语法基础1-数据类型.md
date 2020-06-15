# Python2--语法基础1-数据类型

1. Python数据类型

   + 数值类型

     int:只有一种整数类型int

     float:复数(complex): a+bj 或者 a+bJ 或者 complex(a,b)

   + 字符串

     Python不支持字符类型，单字符被当作一个字符串使用。

     var1="Hello World!"print("var1[0]:",var1[0]) #访问子字符串 H

     print("var1[0:5]:",var1[0:5]) #访问子字符串Hello :返回的切片内容从开始位置开始，在结束为止之前结束

     注：若不指定第一个数，就从字符串首开始；若不指定第二个数，就读到字符串尾。

2. 转义字符

   用反斜杠(\)转义字符

   \r:回车；\f:换页；\000：空。

3. 字符串运算符

   a="Hello" b="Python"

   + 字符串连接：a+b="HelloPython"

   + 重复输出字符串：a*2="HelloHello"

   + 成员运算符：
     + ‘H’ in a ==>True
     + ‘M’ not in a ==>True

   原始字符串：所有字符串直接按照字面意思使用，没有转义字符或不能打印的字符print(r'\n prints \n') 或 print(R'\n prints \n')

4. 字符串格式化

   print("我的名字是%s,年龄是%d" % ('cxy', 22))

5. 布尔类型

   与运算and: A and B

   或运算or: A or B

   非运算not: not A

   False: 0; 空字符串 '' , "";空值 None;空集合 包括空元组(),空序列[],空字典{}; 

6. 类型转换

   int(x);

   float(x);

   str(x);

   chr(x):将整数ASCII码转换为一个字符；

   ord(x):将一个字符转换为ASCII码；

   bin(x):二进制；

   oct(x):八进制；

   hex(x):十六进制；

 

 

 

 

 

   
