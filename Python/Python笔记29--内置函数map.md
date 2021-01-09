# Python笔记29--内置函数map

### 描述

+ map()会根据提供的函数对指定序列做映射。
+ 是一种高阶函数

### 语法

```python
map(function, iterable, ...)
```

+  function : 函数对象function本身

  以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表或迭代器

+ iterable : 一个或多个序列

+ 返回值

  python 2.x 返回列表

  python 3.x 返回迭代器

### 实例

```python
def square(x):
    return x ** 2
res = map(square, [1,2,3,4,5])
print(type(res))
print(next(res))
print(next(res))
print("#"*10)
for i in res:
    print(i)
print("#"*20)
res1 = map(lambda x,y:x+y,[1,2,3],[4,5,6])
for i in res1:
    print(i)
```

```python
<class 'map'>
1
4
##########
9
16
25
####################
5
7
9
```

+ map()作为高阶函数，把运算规则抽象了
+ 当然可以通过一个for循环实现平方的计算，但是不如map函数简洁明了

### 实例：将list所有数字转为字符串

```python
print(list(map(str, [1,2,3,4,5])))
```

```python
['1', '2', '3', '4', '5']
```

