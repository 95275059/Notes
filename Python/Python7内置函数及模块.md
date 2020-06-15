---
title: Python内置函数及模块
date: 2019-04-02 20:24:08
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/88980007](https://blog.csdn.net/zhaandzha/article/details/88980007)   
    
   一.内置函数

 常用内置函数有数学运算函数，类型转换函数和反射函数。

 查询所有内置函数名：

 在python命令行方式输入：dir(__builtins__)

 1.数学运算函数

 =>abs(x):求绝对值。x可以是整型或者复数。若为复数，返回复数的模

 =>complex([real[,imag]]):创建一个复数

 =>divmod(a,b):求商和余数；例如：divmod(20,6)结果为(3,2)

 =>float(x):将一个数或字符串转换为浮点型，若无参数则返回0.0

 =>int([x[,base]]):将一个字符转换为int型，base代表x的进制；例如：int('100',2)结果为4

 =>pow(x,y):求x的y次幂

 =>range(a,b):生成从a开始小于b的整数序列（不包括b）

 range(b):生成从0开始小于b的整数序列

 =>round(x[,n]):对参数x的第n+1位小数进行四舍五入，返回一个小数位数为n的浮点数

 =>sum(iterable[,start]):对集合求和。start：指初始相加的参数，默认值为0

 =>bool(x):将x转换为bool类型。x!=0为True,x=0为False

 =>eval(str):将字符串str当成有效的表达式来求值并返回结果

 例如：eval('1+2*3')结果为7

 2.字符串函数

 =>string.capitalize():将字符串的第一个字符大写

 =>string.count(str,beg=0,end=len(string)):返回str在string中出现的次数；beg和end可指定搜索范围，下同

 =>string.endwith(obj,beg=0,end=len(string)):检查字符串是否以obj结束

 =>string.startwith(obj,beg=0,end=len(string)):检查字符串是否以obj开头

 =>string.find(str,beg=0,end=len(string)):检测str是否包含在string中，如果是返回开始的索引值，否则返回-1

 =>string.rfind(str,beg=0,end=len(string)):类似find方法，但是从右边开始查找

 =>string.index(str,beg=0,end=len(string)):同find方法，但如果str不在string中，则会报一个异常

 =>string.rindex(str,beg=0,end=len(string)):类似index方法，但是从右边开始

 =>string.join(seq):以string作为分隔符，将集合seq中所有元素合并为一个新的字符串

 =>max(str):返回str中最大的字母

 =>min(str):返回str中最小的字母

 =>string.replace(str1,str2,num):把string中str1替换成str2，如果num指定则替换不超过num次

 =>string.split(str="",num=string.count(str)):以str为分割符切片string,如果num有指定，则仅分割num个子字符串

 
```
 str='cxycxycxy'
l=str.split("x")
print(l)
ll=str.split('x',2)
print(ll)
#['c', 'yc', 'yc', 'y']
#['c', 'yc', 'ycxy']
```
 
```
 str1="Hello World Python"
list1=str1.split(" ")
print(list1)
str1="Hello World\nPython"
list1=str1.splitlines()     #按换行符分割字符串
print(list1)
list1=["Hello","World","Python"]
str="#"
print(str.join(list1))
#['Hello', 'World', 'Python']
#['Hello World', 'Python']
#Hello#World#Python
```
 =>string.lower():转换string中所有大写字母为小写字母 

 =>string.upper():转换string中所有小写字母为大写字母

 3.反射函数 

 反射函数主要用于获取类型，对象标识，基类等操作

 =>id(object):返回对象object的id标识（在内存中的地址）

 =>type(object):返回对象object的类型

 

 二.模块

 模块就是一个保存了Python代码的文件。模块中能定义函数，类和变量。

 1.import导入模块

 =>import 模块名

 调用模块中的函数：模块名.函数名

 由于可能在多个模块中含有相同名称的函数，所以必须加上模块名，否则解释器不知道调用哪个模块中的函数。

 =>导入模块中的某些函数：from 模块名 import 函数名1，函数名2，...

 通过这种方式导入，调用函数时只给函数名，但当两模块中含有相同名称函数时，后面依次导入会覆盖前一次导入。

 =>一次性导入模块说有项目：from 模块名 import * #不建议过多使用这种方式

 =>模块位置搜索顺序

 当前目录=>Python PATH环境下的每个目录=>查看由安装过程决定的默认目录

 模块搜索路径存储在system模块的sys.path变量中，包含以上三种目录。

 =>列举模块内容

 dir(模块名)返回排好序的关于模块中定义的变量和函数的字符串列表

 import math

 content=dir(math)

 print(content)

 2.自定义模块

 Python中，每个Python文件都可以作为一个模块，模块名字就是文件的名字

 3.random模块

 random.randrange([start,]stop[,step]):从[start,stop)中按照指定step(默认为1)递增的集合中随机挑一个整数

 random.random():随机生成一个[0,1)内的实数

 random.shuffle(list):将序列list的所有元素随机排序

 random.uniform(x,y):随机生成一个[x,y]内的实数

 random.randint(x,y):随机生成一个[x,y]内的整数

 random.choice(list):从list列表中随机选取元素

 

 

   
 