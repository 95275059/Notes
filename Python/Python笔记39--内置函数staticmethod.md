# Python笔记39--内置函数staticmethod

### 介绍

+ python staticmethod 返回函数的静态方法。

  + 关于静态方法和非静态方法

    + 静态方法

      + 静态方法是在类中使用staitc修饰的方法，在类定义的时候已经被装载和分配。

      + 静态方法中只能调用静态成员或者方法，不能调用非静态方法或者非静态成员
      + 

    + 非静态方法

      + 非静态方法是不加static关键字的方法，在类定义时没有占用内存，只有在类被实例化成对象时，对象调用该方法才被分配内存。

      + 非静态方法既可以调用静态成员或者方法又可以调用其他的非静态成员或者方法。

  + 被staticmethod装饰的方法可以认为是类的方法

    即可以直接 **类.方法()**，也可以通过类的实例，也就是**对象.方法()**进行调用。

+ 该方法不强制要求传递参数，如下声明一个静态方法：

  ```python
  class C(object):
      @staticmethod
      def f(arg1, arg2, ...):
          ...
  ```

  以上实例声明了静态方法 f，从而可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。

### 语法

```python
staticmethod(function)
```

### 实例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class C(object):
    @staticmethod
    def f():
        print('runoob');
 
C.f();          # 静态方法无需实例化
cobj = C()
cobj.f()        # 也可以实例化后调用
```

```python
runoob
runoob
```

