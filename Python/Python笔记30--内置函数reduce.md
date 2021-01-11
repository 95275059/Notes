# Python笔记31--内置函数reduce

### 描述

+ reduce()函数会对参数序列中元素进行累积。

+ 是一种高阶函数

+ reduce函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（必须有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

+ ```
  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
  ```

+ 注意

  Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：

  ```python
  from functools import reduce
  ```

### 语法

```python
reduce(function, iterable[, initializer])
```

+ function : 函数，有两个参数
+ iterable : 可迭代对象
+ initializer : 可选，初始参数
+ 返回值 : 返回函数计算结果

### 实例：累积求和

```python
from functools import reduce
def add(x,y):
    return x+y
sum1 = reduce(add, [1,2,3,4,5])
sum2 = reduce(lambda x,y:x+y, [1,2,3,4,5])
print(sum1)
print(sum2)
```

```python
15
15
```

### 实例：把序列[1,3,5,7,9]变成整数13579

```python
from functools import reduce
def fun(x, y):
    return x*10 + y
num = reduce(fun, [1,3,5,7,9])
print(num)
```

```python
13579
```

### 实例：把str转换为int

```python
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(strr):
    def mf(st):
        return DIGITS[st]
    return reduce(lambda x,y:x*10+y, map(mf, strr))

print(str2int('13579'))
```

```
13579
```

### 实例：利用`map()`函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

+ 示例：
  + 输入：`['adam', 'LISA', 'barT']`
  + 输出：`['Adam', 'Lisa', 'Bart']`

+ 代码

  ```python
  def normalize(name):
      return name.capitalize()
  L1 = ['adam', 'LISA', 'barT']
  L2 = list(map(normalize, L1))
  print(L2)
  ```
  
  ```python
  ['Adam', 'Lisa', 'Bart']
  ```

### 实例：Python提供的`sum()`函数可以接受一个list并求和，请编写一个`prod()`函数，可以接受一个list并利用`reduce()`求积

```python
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
```

### 实例：利用`map`和`reduce`编写一个`str2float`函数，把字符串`'123.456'`转换成浮点数`123.456`：

```python
from functools import reduce
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(int, s))
def str2float(s):
    i = s.index('.')
    result = str2int(s[0:i])*10**i + str2int(s[i+1:])
    return result/10**i
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
```

```python
str2float('123.456') = 123.456
测试成功!
```

