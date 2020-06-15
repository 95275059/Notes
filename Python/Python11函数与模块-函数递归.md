---
title: Python函数与模块-函数递归
date: 2019-04-04 10:40:49
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89013260](https://blog.csdn.net/zhaandzha/article/details/89013260)   
    
   1.闭包

 闭包：函数的嵌套。

 
```
 def func_lib():
    def add(x,y):
        return x+y
    return add
fadd=func_lib()
print(fadd(1,2))
```
 函数func_lib将函数add作为返回值

 2.函数的递归调用

 直接调用本函数:在fun1()中调用fun1()

 间接调用本函数:在fun1()中调用fun2(),在调用fun2()中又调用fun1()

 

   
 