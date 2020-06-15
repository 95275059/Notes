---
title: Python面向对象程序设计--类和对象
date: 2019-04-08 11:31:30
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89070097](https://blog.csdn.net/zhaandzha/article/details/89070097)   
    
   1.定义和使用类

 (1).定义类：

 class 类名：

 属性(成员变量)

 ...

 成员函数(成员方法)

 注：=>类名的首字母一般大写

 =>成员函数一般指与特定实例绑定的函数，通过对象调用成员方法时，对象本身将被作为第一个参数传递过去

 =>类的成员函数必须有一个参数self，而且位于参数列表的开头。

 self代表类的实例(对象)自身，可以使用self引用类中的属性和成员函数。

 在类的成员函数中访问实例属性时需要以self为前缀

 但在外部通过对象名调用对象成员函数时不需要传递这个参数

 如果在外部通过类名调用对象成员函数则需要显式为self参数传值

 (2).定义对象

 对象名=类名([参数])

 2.构造函数__init__(self[,参数])

 该函数为一个特殊的方法，会在类实例化时自动为新生成的类实例调用__init__()方法。

 构造函数一般用于完成对象数据成员设置初值或进行其他必要的初始化工作。

 如果用户未定义构造函数，Python将提供一个默认的构造函数

 3.析构函数__del__(self)

 该函数用来释放对象占用的资源，在Python收回对象空间之前自动执行。

 若用户未定义析构函数，Python将提供一个默认的析构函数进行必要的清理工作。

 =>在外部调用方法: del 对象名 #系统会自动调用析构函数

 4.实例属性和类属性

 实例属性：在构造函数中定义，定义时以self为前缀；

 类属性：在类中方法之外定义的属性。

 在主程序（类的外部）中，实例属性属于实例（对象）只能通过实例访问；类属性属于类可以通过类名访问，也可以通过对象名访问，为类的所有实例所共享。

 
```
 class Person:
    num=0          #类属性
    def __init__(self,str,n):
        self.name=str        #实例属性
        self.age=n
        Person.num==1        #修改类属性
    def SayHello(self):
        print("Hello!")
    def PrintName(self):
        print("姓名:",self.name,"  年龄:",self.age)
    def PrintNum(self):
        print(Person.num)

P1=Person("cxy",21)
P2=Person("ccc",45)
P1.PrintName()
P2.PrintName()
Person.num=2                #修改类属性
P1.PrintNum()
P2.PrintNum()
#姓名: cxy   年龄: 21
#姓名: ccc   年龄: 45
#2
#2
```
 =>Python可以动态地位类和对象增加成员。

 为类增加类属性：类名.类属性名=值 

 为实例绑定成员函数：实例名.成员函数名=types.MethodType(函数名,实例名)

 =>需要导入模块types 即 import types

 =>函数需要提前写好，函数名与成员函数名相同

 
```
 P1=Person("cxy",21)
P2=Person("ccc",45)
Person.work='JNU'      #增加类属性
P1.age=22
print("姓名:",P1.name,"  年龄:",P1.age,"  单位:",Person.work)
print("姓名:",P2.name,"  年龄:",P2.age,"  单位:",Person.work)
def setAge(self,s):
    self.age=s
P2.setAge=types.MethodType(setAge,P2)    #为P2实例绑定成员函数setAge
P2.setAge(35)
print("姓名:",P2.name,"  年龄:",P2.age,"  单位:",Person.work)


```
 =>Python可以使用一些函数来访问属性

 getattr(obj,name):访问对象obj的属性name，并返回属性值

 hasattr(obj,name):检查是否存在某属性，存在返回True

 setattr(obj,name,value):设置一个属性。若不存在，会创建一个新属性并赋值为value

 delattr(obj,name):删除属性

 =>Python内置了一些类属性

 __dict__:类的属性（返回一个字典，由类的数据属性组成）

 __doc__:类的文档字符串

 __name__:类名

 __module__:类定义所在模块（类全名为__main__.className；若类位于一个导入模块mymod中，则返回mymod）

 __bases__:类的所有父类组成的元组

 5.私有成员与公有成员

 私有属性：以两个下划线“__”开头 注：Python不存在严格意义上的私有成员

 私有属性在类的外部不能直接访问，需要通过调用对象的共有成员方法来访问，或通过Python支持的特殊方法来访问

 Python提供了访问私有属性的特殊方式，可用于程序的测试和调试，对于成员方法也具有同样的性质（不推荐）

 =>对象名._类名+私有成员

 在Python中，以下划线 开头的变量名和方法名由特殊含义，尤其是在类的定义中

 =>_xxx:这样的对象为保护成员，不能用 from module import *导入；只有类和子类内部成员方法能访问这些成员

 =>__xxx__:系统定义的特殊成员

 =>__xxx:类中的私有成员

 6.方法

 =>公有方法：

 通过对象名直接调用；

 若通过类名调用属于对象的公有方法，需要显示为该方法的self参数传递一个对象名，来指定访问哪个对象的数据成员

 =>私有方法：

 私有方法名以两个下画线"__"开始

 私有方法只能在属于对象的方法中通过self调用或在外部通过Python支持的特殊方式调用

 =>静态方法:

 通过类名和对象名调用，但不能直接访问属于对象的成员，只能访问属于类的成员

 在定义静态方法前加@staticmethod

 

 

 

   
 