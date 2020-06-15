---
title: Python函数与模块-函数定义与使用
date: 2019-04-03 19:03:00
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/88991514](https://blog.csdn.net/zhaandzha/article/details/88991514)   
    
   一.函数定义与使用

 1.函数定义

 Python中函数的定义与声明是视为一体的。

 def 函数名(函数参数)：

 函数体

 return 表达式或值

 注：

 =>Python中变量是弱类型的，Python会自动根据值来维护其类型。所以不用指定返回值及函数参数的类型

 =>若没有return语句，则自动返回None；如果有return语句但return后没有接表达式或值，则也返回None

 =>Python中可以返回多个值，将多个值放在一个元组或者其他类型的集合中来返回。 如：return (x,y)

 =>参数的传递是值传递，一般情况下，修改形参不会影响实参

 2.lambda表达式

 lambda表达式可以用来声明匿名函数

 匿名函数：没有函数名字的临时使用的函数，只可以包含一个表达式，且表达式的结果为函数返回值；

 不允许包含其他复杂的语句，但在表达式中可调用其他函数

 lambda 函数参数：表达式

 （1）函数的列表：将lambda表达式作为列表的元素，从而实现跳转表的功能

 L=[(lambda 表达式1),(lambda 表达式2),...]

 调用方法：L[索引](lambda表达式的参数列表)

 （2）lambda作为函数返回值

 

 
```
 """
定义一个math():
k=1,返回计算加法的lambda表达式；
k=2,返回计算减法的lambda表达式；
k=3,返回计算乘法的lambda表达式；
k=4,返回计算除法的lambda表达式；
"""
def math(k):
    if k==1:
        return lambda x,y:x+y
    elif k==2:
        return lambda x,y:x-y
    elif k==3:
        return lambda x,y:x*y
    elif k==4:
        return lambda x,y:x/y

action=math(1)
print("10+2=",action(10,2))
action=math(2)
print("10-2=",action(10,2))
action=math(3)
print("10*2=",action(10,2))
action=math(4)
print("10/2=",action(10,2))
```
 3.几种在函数内部修改实参值的情况

 
```
 def modify(m,K):
    m=2
    K[0]=0
    return 
n=100
L=[1,2,3]
modify(n,L)
print(n)
print(L)

```
 n=100

 L=[0,2,3]

 
```
 def modify2(v,item):
    v.append(item)
a=[2]
modify2(a,3)
print(a)
```
 a=[2,3]

 
```
 def modify3(d):
    d['age']=18
a={'name':'cxy','age':22,'sex':'Female'}
print(a)
modify3(a)
print(a)

```
 a={'name': 'cxy', 'age': 18, 'sex': 'Female'}

 4.函数参数类型

 =>默认值参数

 
```
 def display(a='Hello',b='World'):    #默认值参数能够给函数参数提供默认值
    print(a+b)
display()
display(b='world')                   #指定b的值
display(a='hello')                   #指定a的值
display('world')                     #未指定'world'传给a还是b,则默认从左向右匹配,即传给a
#HelloWorld
#Helloworld
#helloWorld
#worldWorld
```
 =>关键字参数

 位置参数：参数通过位置进行匹配，从左到右依次匹配，对参数位置和个数都有严格要求

 关键字参数：通过参数名字来匹配，不需要严格按照参数定义时的位置来传递参数

 如：display(a='hello')

 =>任意个数参数

 一般情况下定义函数时，函数参数个数确定，然而某些情况下不能确定参数个数，只需在参数前面加上‘*’或者'**'

 =>'*'表示将没有匹配的值都放在同一个元组中

 
```
 def storename(name,*nickName):
    print('real name is %s'%name)
    for nickname in nickName:
        print("小名 ",nickname)
storename('张海')
storename('张海','小海')
storename('张海','小海','小豆豆')
#real name is 张海
#real name is 张海
#小名  小海
#real name is 张海
#小名  小海
#小名  小豆豆
```
 =>表示将没有匹配的值都放在一个字典中

 
```
 def demo(**p):
    for item in p.items():
        print(item)
demo(x=1,y=2,z=3)
#('x', 1)
#('y', 2)
#('z', 3)
```
 5.变量作用域

 =>局部变量

 局部变量在函数内部定义的变量，旨在该函数内部起作用。

 与函数外具有相同名的其他变量没有任何关系-变量名称对于函数来说是局部的

 =>全局变量

 全局变量在函数外部定义，并且可以直接在函数中使用。

 若要在函数内部改变全局变量值，必须使用global关键字进行声明

 
```
 x=2
def fun1():
    print(x,end=" ")
def fun2():
    global x
    x=x+1
    print(x,end=" ")
fun1()
fun2()
print(x,end=" ")
#2 3 3 
```
 注 =>若在函数内部直接将一个变量声明为全局变量，在函数外没有定义，则在调用该函数后，将变量增加为新的全局变量

 =>若一个局部变量和一个全局变量重名，则局部变量会“屏蔽”全局变量，局部变量起作用

 

 

   
 