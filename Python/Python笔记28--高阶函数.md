# Python笔记29--高阶函数

### 变量可以指向函数

```python
print(abs(-10))
print(abs)
x = abs(-10)
print(x)
y = abs
print(y)
print(y(-10))
```

```python
10
<built-in function abs>
10
<built-in function abs>
10
```

+ 变量可以指向函数，即函数本身可以赋值给变量
+ 变量指向函数后，可以直接通过该变量调用函数

### 函数名也是变量

+ 函数名其实就是指向函数的变量

  对于`abs()`这个函数，完全可以把函数名`abs`看成变量，它指向一个可以计算绝对值的函数！

+ 如果把`abs`指向其他对象，会有什么情况发生？

  ```python
  print(abs(-10))
  abs = 10
  print(abs(-10))
  ```

  ```python
  10
  Traceback (most recent call last):
    File "E:/Python/Study/venv/test.py", line 3, in <module>
      print(abs(-10))
  TypeError: 'int' object is not callable
  ```

  把`abs`指向`10`后，就无法通过`abs(-10)`调用该函数了！因为`abs`这个变量已经不指向求绝对值函数而是指向一个整数`10`！

  由于`abs`函数实际上是定义在`import builtins`模块中的，所以要让修改`abs`变量的指向在其它模块也生效，要用`import builtins; builtins.abs = 10`。

### 传入函数

+ 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数

  这种函数就称之为**高阶函数（Higher-order function）**

+ 实例

  ```python
  def add(x, y, f):
      return f(x) + f(y)
  print(add(-5, 6, abs))
  ```

  ```python
  11
  ```

### 高阶函数

+ 把函数作为参数传入，这样的函数称为高阶函数
+ 函数式编程就是指这种高度抽象的编程范式。