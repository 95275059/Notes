# Python笔记24--内置函数classmethod

### 描述

+ classmethod 修饰符对应的函数不需要实例化，不需要self参数，但第一个参数需要是表示自身类的cls参数，cls参数可以来调用类的属性，类的方法，实例化对象等

### 语法

```python
@classmethod
def function(cls, arg1[,...]):
    ...
```

### 实例

```python
class A(object):
    # 属性默认为类属性（可以给直接被类本身调用）
    num = 1
    # 实例化方法（必须实例化类之后才能被调用）
    def func1(self):  # self : 表示实例化类后的地址id
        print ('foo') 
    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):   # cls : 表示没有被实例化的类本身
        print ('func2')
        print (cls.num)
        cls().func1()   # 调用 func1 方法
    # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
    def func3():
        print("func3")
        print(A.num) # 属性是可以直接用类本身调用的
# A.func1() 这样调用会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
A.func2()               # 不需要实例化
A.func3()
```

```python
func2
1
foo
func3
1
```

