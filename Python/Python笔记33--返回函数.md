# Python笔记34--返回函数

### 函数作为返回值

+ 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

+ 以可变参数求和函数为例

  ```python
  def lazy_sum(*args):
      def sum():
          ax = 0
          for n in args:
              ax = ax + n
          return ax
      return sum
  print(lazy_sum)
  f1 = lazy_sum(1,3,5,7)
  print(f1)
  print(f1())
  f2 = lazy_sum(1,3,5,7)
  print(f1 == f2)
  ```

  ```python
  <function lazy_sum at 0x000001A6B7374EE8>
  <function lazy_sum.<locals>.sum at 0x000001A6B73873A8>
  16
  False
  ```

  + 调用lazy_sum时，返回的不是求和的结果，而是求和函数

  + 调用f时，才是真正计算求和的结果

  + 当调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

    即，f1()和f2()的调用结果互不影响

  + lazy_sum()函数形成了一个闭包结构

### 实例：利用闭包返回一个计数器函数，每次调用它返回递增整数

```python
def createCounter():
    last = 0
    def counter():
        last += 1
        return last+1
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```

```python
def createCounter():
    i=[0]
    def counter():
        i[0]+=1
        return i[0]
    return counter
```

+ 参考python10--函数与模块1-函数定义与使用 : 几种在函数内部修改实参值的情况

```python
def createCounter():
    def state():
        i=0
        while True:
            i=i+1
            yield i
    g=state()
    def counter():
        return next(g)
    return counter
```

+ 使用生成器记录状态

  







