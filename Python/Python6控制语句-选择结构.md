---
title: Python控制语句-选择结构
date: 2019-04-02 19:34:22
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/88978921](https://blog.csdn.net/zhaandzha/article/details/88978921)   
    
   一.选择结构

 1.if语句

 if 表达式1：

 语句1

 elif 表达式2：

 语句2

 ...

 else:

 语句n

 

 注：条件表达式除了可以为关系表达式和逻辑表达式，可以是任何数值类型表达式，甚至可以是字符串，

 可以是‘a’,也可以是‘abc’

 2.pass语句

 类似于空语句，可以用在类和函数的定义中或者选择结构中。

 当暂时没有确定如何实现功能，或者为以后的软件升级预留空间，或者为其他类型功能时，可以用该关键字来占位。

 
```
 if a<b:
    pass
class A:
    pass
def demo():
    pass
```
 

 

 

   
 