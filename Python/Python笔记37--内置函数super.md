# Python笔记37--内置函数super

### 描述

+ **super()** 函数是用于调用父类(超类)的一个方法。

+ **super()** 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

  MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

### 语法

```
super(type[, object-or-type])
```

+ type : 类
+ object-or-type : 类，一般是self
+ Python2和Python3的区别
  + Python3可以直接使用super().xxx替代super(class, self).xxx

### 实例（Python3）

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class A(object):   # Python2.x 记得继承 object
    def add(self, x):
         y = x+1
         print(y)
class B(A):
    def add(self, x):
        super(B, self).add(x)
b = B()
b.add(2)  # 3
```

### 实例（Python3）

```python
class A:
     def add(self, x):
         y = x+1
         print(y)
class B(A):
    def add(self, x):
        super().add(x)
b = B()
b.add(2)  # 3
```

### 实例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
```

```python
Parent
Child
HelloWorld from Parent
Child bar fuction
I'm the parent.
```

### super解决多重继承问题的

+ 对于定义的类，在Python中会创建一个MRO(Method Resolution Order)列表，它代表了类继承的顺序。

+ 在单继承时，`super().__init__()`和`Base.__init__()`是一样的

  `super`获取的类刚好是父类

+ 在多继承时

  `super`获取的是继承顺序中的下一个类

  + 以下面的继承方式为例：

    > Base
    >   /  \
    >  /    \
    > A      B
    >  \    /
    >   \  /
    >    C

  + 使用super

    ```python
    class Base(object):
        def __init__(self):
            print("enter Base")
            print("leave Base")
    
    class A(Base):
        def __init__(self):
            print("enter A")
            super(A, self).__init__()
            print("leave A")
    
    class B(Base):
        def __init__(self):
            print("enter B")
            super(B, self).__init__()
            print("leave B")
    
    class C(A, B):
        def __init__(self):
            print("enter C")
            super(C, self).__init__()
            print("leave C")
    
    C()
    print(C.mro())
    ```

    ```python
    enter C
    enter A
    enter B
    enter Base
    leave Base
    leave B
    leave A
    leave C
    [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
    ```

  + 不使用super

    ```python
    class Base(object):
        def __init__(self):
            print("enter Base")
            print("leave Base")
    
    class A(Base):
        def __init__(self):
            print("enter A")
            Base().__init__()
            print("leave A")
    
    class B(Base):
        def __init__(self):
            print("enter B")
            Base().__init__()
            print("leave B")
    
    class C(A, B):
        def __init__(self):
            print("enter C")
            A().__init__()
            B().__init__()
            print("leave C")
    
    C()
    print(C.mro())
    ```

    ```python
    enter C
    enter A
    enter Base
    leave Base
    enter Base
    leave Base
    leave A
    enter A
    enter Base
    leave Base
    enter Base
    leave Base
    leave A
    enter B
    enter Base
    leave Base
    enter Base
    leave Base
    leave B
    enter B
    enter Base
    leave Base
    enter Base
    leave Base
    leave B
    leave C
    [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
    ```

  + 从上面可以看到如果不使用`super`，会导致基类被多次调用，开销非常大。

  + 从测试结果来看，两种方式的MRO列表是一样的。MRO的查找顺序是按广度优先来的(基类继承object，Python 2.3之后)。

  