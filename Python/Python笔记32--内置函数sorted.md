# Python笔记32--内置函数sorted

### 描述

+ sorted() 函数对所有可迭代的对象进行排序操作。
+ 是高阶函数
+ 排序也是在程序中经常用到的算法。

+ 无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。

  如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？

  直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

> **sort 与 sorted 区别：**
>
> sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
>
> list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

### 语法

```python
sorted(iterable, cmp = None, key = None, reverse = False)
```

+ iterable : 可迭代对象。

+ cmp : 比较的函数(python2有，python3没有)

  这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。

+ key : 主要是用来进行比较的元素

  只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。

+ reverse : 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

+ 返回值

  返回重新排序的列表。

### 实例：对list进行排序

```python
li = [36, 5, -12, 9, -21]
linew = sorted(li)
print(li)
print(linew)
```

```python
[36, 5, -12, 9, -21]
[-21, -12, 5, 9, 36]
```

### 实例：通过接收一个`key`函数来实现自定义的排序，比如按绝对值大小排序

```python
li = [36, 5, -12, 9, -21]
linew = sorted(li, key = abs)
print(li)
print(linew)
```

```python
[36, 5, -12, 9, -21]
[5, 9, -12, -21, 36]
```

key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

### 实例：字符串排序

+ 默认情况下，对字符串排序，是按照ASCII的大小比较的

  由于`'Z' < 'a'`，结果，大写字母`Z`会排在小写字母`a`的前面。

+ 现在，我们提出排序应该忽略大小写，按照字母序排序。

+ 要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。

  忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

+ 实现

  ```python
  li = ['bob', 'about', 'Zoo', 'Credit']
  linew = sorted(li, key = str.lower)
  print(li)
  print(linew)
  ```

  ```python
  ['bob', 'about', 'Zoo', 'Credit']
  ['about', 'bob', 'Credit', 'Zoo']
  ```

### 实例：使用sort分别对学生名字和成绩排序

+ 假设我们用一组tuple表示学生名字和成绩：

  ```python
  L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
  ```

+ python 3

  ````python
  L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
  def by_name(t):
      return t[0]
  def by_score(t):
      return t[1]
  
  print(sorted(L, key = by_name))
  print(sorted(L, key = by_score))
  ````

  ```python
  [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
  [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
  ```

  ```python
  L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
  
  print(sorted(L, key = lambda x:x[0]))
  print(sorted(L, key = lambda x:x[1]))
  ```

  ```python
  [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
  [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
  ```

+ python 2 可以用cmp但没必要，因为用key就行

  ```python
  L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
  
  print(sorted(L, cmp = lambda x,y:cmp(x[0], y[0])))
  print(sorted(L, cmp = lambda x,y:cmp(x[1], y[1])))
  ```

  ```python
  [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
  [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
  ```

  