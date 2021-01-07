# Python11--函数与模块2-函数递归

### 嵌套函数

+ python允许创建嵌套函数。

  也就是说我们可以在函数里面定义函数，而且现有的作用域和变量生存周期依旧不变。

+ 实例1

  ```python
  def outer():
      name="python"
      def inner():#outer函数内部定义的函数
          print(name)
      return inner()#返回该内部函数
  
  outer()
  ```

  ```python
  python
  ```

  + inner函数

    python解析器需要找一个叫name的本地变量

    查找失败后会继续在上层的作用域里面寻找，这个上层作用域定义在outer函数里，python函数可以访问封闭作用域。

  + outer函数

    + **return内层函数时加括号，返回内层函数调用的结果**

    + 需要知道非常重要一点就是，inner也仅仅是一个遵循python变量解析规则的变量名

      python解释器会优先在outer的作用域里面对变量名inner查找匹配的变量。

      把恰好是函数标识符的变量inner作为返回值返回回来

      每次函数outer被调用的时候，函数inner都会被重新定义

      如果它不被当做变量返回的话，每次执行过后它将不复存在。

    + 在python里，函数就是对象，它也只是一些普通的值而已。

      也就是说你可以把函数像参数一样传递给其他的函数或者说从函数里面返回函数

+ 实例2

  ```python
  def outer():
      name="python"
      def inner():#outer函数内部定义的函数
          print(name)
      return inner#返回该内部函数
  
  res = outer()
  print(res)
  res()
  ```

  ```python
  <function outer.<locals>.inner at 0x000001EBE2C173A8>
  python
  ```

  **return内层函数时不加括号,返回的是内层函数的函数引用（函数名称及函数地址）**

  想要执行内层函数，需要在outer()后边再加个括号，即outer()()，才会让内层函数执行

---

### 函数作为变量

```python
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def apply(func,x,y):
    return func(x,y)

print("apply(add,2,1):",apply(add,2,1))
print("apply(sub,2,1):",apply(sub,2,1))
```

```python
apply(add,2,1): 3
apply(sub,2,1): 1
```

+ apply函数准备接收一个函数的变量，它也只是一个普通的变量而已，和其他变量一样。
+ 然后我们调用传进来的函数：“()代表着调用的操作，并且调用变量包含的值”。
+ 在函数外，我们也能看到传递函数并没有什么特殊的语法，函数的名称只是和其他变量一样的标识符而已。

### 闭包

+ 实例1

  ```python
  def func_lib():
      def add(x,y):
          return x+y
      return add
  fadd=func_lib()
  print(fadd(1,2))
  ```

  ```python
  3
  ```

+ 实例2

  ```python
  def outer():
      name="python"
      def inner():#outer函数内部定义的函数
          print(name)
      return inner#返回该内部函数
  
  res = outer()
  print(res)
  res()
  ```

  ```python
  <function outer.<locals>.inner at 0x000001EBE2C173A8>
  python
  ```

+ 分析

  根据python的运行模式，我们是没法在函数outer执行退出之后还能继续调用inner函数的，并且在inner函数被调用时，变量name早已不存在了，但是为什么我们调用成功了呢？

  这是因为，python支持一个叫函数闭包的特性。

+ 闭包

  如果一个函数定义在另一个函数的作用域内，并且引用了外层函数的变量，则该函数称为闭包。

  简单的说，就是某个**内部函数**被当做对象返回时，**夹带了这个内部函数之外的变量**，这就形成了一个闭包。

  **闭包必须嵌套在一个函数里，必须返回一个调用外部变量的函数对象，才是闭包**

+ 闭包是Python所支持的一种特性

  它让在非global scope定义的函数可以引用其外围空间中的变量

  这些外围空间中被引用的变量叫做这个函数的环境变量。

  环境变量和这个非全局函数一起构成了闭包。

+ 实例改进

  ```python
  def outer(name,version):
      def inner():
          print(name)
          print(version)
      return inner
  
  res1=outer("python", 1)#返回闭包
  res2=outer("java", 2)#返回闭包
  res1()#执行函数
  res2()
  print(res1.__closure__)
  ```

  ```python
  python
  1
  java
  2
  (<cell at 0x00000172EA799B58: str object at 0x00000172EA76DFB0>, <cell at 0x00000172EA799B88: int object at 0x00007FFDFC3C7100>)
  ```

  res1.\__closure__打印闭包里包含哪些外部变量，可以看到结果里有两个，即python和1

+ 闭包特点

  一个函数返回的函数对象，这个函数对象执行的话依赖非函数内部的变量值，这个时候，函数返回的实际内容如下：

  + 函数对象
  + 函数对象需要使用的外部变量和变量值

###  函数的递归调用

 直接调用本函数:在fun1()中调用fun1()

 间接调用本函数:在fun1()中调用fun2(),在调用fun2()中又调用fun1()

 

   
