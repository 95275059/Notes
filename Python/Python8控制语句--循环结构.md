---
title: Python控制语句--循环结构
date: 2019-04-02 21:54:01
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/88979245](https://blog.csdn.net/zhaandzha/article/details/88979245)   
    
   二.循环结构

 1.while语句

 while 判断条件：

 执行语句

 2.for语句

 for 循环索引值 in 序列：

 循环体

 注：对于列表可通过索引（列表下标）遍历

 
```
 fruits=['banana','apple','mango']
for i in range(len(fruits)):
    print("当前水果:",fruits[i])
```
 3.continue与break语句

 4.循环嵌套 

 5.列表生成式

 =>生成一个list[1,2,3,4,5,6,7,8,9]

 L=list(range(1,10))

 =>生成一个list[1*1,2*2,3*3,...,9*9]

 
```
 L=[]
for x in range(1,10):
    L.append(x*x)
print(L)
```
 用列表生成式：L=[x*x for x in range(1,10)]

 列表生成式的书写格式：将要生成的元素(x*x)放到最前面，后面跟for循环。for循环后可以加上if判断进行筛选。

 =>筛选偶数的平方 即L=[4,16,36,64]

 L=[x*x for x in range(1,10) if x%2==0]

 =>将列表中所有字符串变成小写形式

 L=["Hello","World"]  
 L=[s.lower() for s in L] 

 =>列表生成式可以使用两层循环

 生成“ABC” 和“XYZ”的全部组合 

 L=[m+n for m in 'ABC' for n in 'XYZ']

 =>列表生成式也可以使用两个变量来生成list列表

 for循环可以同时使用两个甚至多个变量

 字典的items()可以同时迭代key和value  

 
```
 d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'键=',v,end=";")
```
 
```
 d={'x':'A','y':'B','z':'C'}
L=[k+"="+v for k,v in d.items()]
print(L)
```
 

 

 

 

 

 

 

   
 