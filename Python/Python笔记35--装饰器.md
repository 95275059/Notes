# Python笔记25--装饰器

### 装饰器（Decorators）

+ 装饰器(Decorators)是Python的一个重要部分。

+ 简单地说：他们是修改函数的功能的函数。

  他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。

+ 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

+ 本质上，装饰器是一个返回函数的高阶函数

### 实例

+ 对于一个函数now()

  ```python
  def now():
      print('2020.1.11')
  ```

+ 如果要给now()增加功能，比如在函数调用前后自动打印日志，但又不希望修改now()函数的定义。

  + 定义一个可以打印日志的decorator

    ```python
    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    ```

    log是一个装饰器，接受一个函数作为参数，并返回一个函数

  + 借助python的@语法，把装饰器置于函数的定义处

    ```python
    @log
    def now():
        print('2015-3-25')
    ```

  + 调用now

    ```python
    call now():
    2020.1.11
    ```

+ 即：把@log放到now()函数的定义处，相当于执行了

  ```python
  now = log(now)
  ```

  + 由于`log()`是一个decorator，返回一个函数，所以，原来的`now()`函数仍然存在，只是现在同名的`now`变量指向了新的函数，于是调用`now()`将执行新函数，即在`log()`函数中返回的`wrapper()`函数。
  + `wrapper()`函数的参数定义是`(*args, **kw)`，因此，`wrapper()`函数可以接受任意参数的调用。在`wrapper()`函数内，首先打印日志，再紧接着调用原始函数。

+ 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

  ```python
  def log(text):
      def decorator(func):
          def wrapper(*args, **kw):
              print('%s %s():' % (text, func.__name__))
              return func(*args, **kw)
          return wrapper
      return decorator
  ```

  + 这个3层嵌套的decorator用法如下：

    ```python
    @log('execute')
    def now():
        print('2015-3-25')
    ```

  + 调用now

    ```python
    execute now():
    2015-3-25
    ```

  + 和两层嵌套的decorator想比，3层嵌套的效果是：

    ```python
    now = log('excute')(now)
    ```

    + 首先执行`log('execute')`，返回的是`decorator`函数
    + 再调用返回的函数，参数是`now`函数，返回值最终是`wrapper`函数。

+ 经过decorator装饰过的函数，\__name__会变化

  ```python
  def log(text):
      def decorator(func):
          def wrapper(*args, **kw):
              print('%s %s():' % (text, func.__name__))
              return func(*args, **kw)
          return wrapper
      return decorator
  
  @log('execute')
  def now():
      print('2015-3-25')
  now()
  print(now.__name__)
  ```

  ```python
  execute now():
  2015-3-25
  wrapper
  ```

  + **需要把原始函数的\__name__等属性复制到wrapper()函数中，否则对于有些依赖函数签名的代码会报错**

    使用python内置的functools.wraps完成

    ```python
    import functools
    
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    
    @log('execute')
    def now():
        print('2015-3-25')
    now()
    print(now.__name__)
    ```

    ```python
    execute now():
    2015-3-25
    now
    ```

### 实例：设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

```python
import functools
import time
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        r = fn(*args, **kwargs)
        end_time = time.time()
        t = end_time - start_time
        print('%s executed in %s ms' %(fn.__name__, str(t)))
        return r
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
```

```python
fast executed in 0.002991199493408203 ms
slow executed in 0.12466788291931152 ms
```

### 思考一下能否写出一个`@log`的decorator，使它既支持带参数的装饰器又支持不带参数的装饰器

```python
def log(temp):

    if not isinstance(temp,str):
        #使用decorator后,func指向log(func)
        #将更名后的'__name__'更改回原函数名称防止签名错误
        @functools.wraps(temp)
        def wrapper(*args,**kw):
            ##operations
            return temp(*args,**kw)
        return wrapper
    else: #此时temp为一串str参数
        #new decorator
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print(temp) #打印字符串temp
                #operations
                return func(*args,**kw)
            return wrapper
        return decorator
```













