# Python模块14--collections

## 参考官网

https://docs.python.org/zh-cn/3/library/collections.html

---

## 介绍

+ 这个模块实现了特定目标的容器，以提供Python标准内建容器 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) , [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) , [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) , 和 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 的替代选择。

| 函数          | 说明                                                      |
| ------------- | --------------------------------------------------------- |
| namedtuple()  | 创建命名元组子类的工厂函数                                |
| deque()       | 类似列表的容器，实现了在两端能快速添加(append)和弹出(pop) |
| ChainMap()    | 类似字典的容器，将多个映射集合到一个视图里                |
| Counter()     | 字典的子类，提供了可哈希对象的计数功能                    |
| OrderedDict() | 字典的子类，保存了他们被添加的顺序                        |
| defaultdict() | 字典的子类，提供了一个工厂函数，为字典查询提供一个默认值  |
| UserDict()    | 封装了字典对象，简化了字典子类化                          |
| UserList()    | 封装了列表对象，简化了列表子类化                          |
| UserString()  | 封装了字符串对象，简化了字符串子类化                      |

*Deprecated since version 3.3, will be removed in version 3.10:* 已将 [容器抽象基类](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections-abstract-base-classes) 移至 [`collections.abc`](https://docs.python.org/zh-cn/3/library/collections.abc.html#module-collections.abc) 模块。 为了保持向下兼容性，它们在 Python 3.9 版的这个模块中仍然存在。

---

## OrderdDict

+ 有序词典就像常规词典一样，但有一些与排序操作相关的额外功能。

+ 由于内置的 `dict`类获得了记住插入顺序的能力（在 Python 3.7 中保证了这种新行为），它们变得不那么重要了。

+ 一些与dict的不同仍然存在

  + 常规的 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 被设计为非常擅长映射操作。 跟踪插入顺序是次要的。
  + [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 旨在擅长重新排序操作。 空间效率、迭代速度和更新操作的性能是次要的。
  + 算法上， [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 可以比 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 更好地处理频繁的重新排序操作。 这使其适用于跟踪最近的访问（例如在 [LRU cache](https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237) 中）。
  + 对于 [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) ，相等操作检查匹配顺序。
  + [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 类的 `popitem()` 方法有不同的签名。它接受一个可选参数来指定弹出哪个元素。
  + [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 类有一个 `move_to_end()` 方法，可以有效地将元素移动到任一端。
  + Python 3.8之前， [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 缺少 [`__reversed__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__reversed__) 方法。

+ 语法

  ```python
  class collections.OrderedDict([items])
  ```

  返回一个 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 子类的实例，它具有专门用于重新排列字典顺序的方法

+ 3.1新版功能

  + ```python
    popitem(last=True)
    ```

    有序字典的 [`popitem()`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict.popitem) 方法移除并返回一个 (key, value) 键值对。 如果 *last* 值为真，则按 LIFO 后进先出的顺序返回键值对，否则就按 FIFO 先进先出的顺序返回键值对。

  + ```python
    move_to_end(key, last=True)
    ```

    将现有 *key* 移动到有序字典的任一端。 如果 *last* 为真值（默认）则将元素移至末尾；如果 *last* 为假值则将元素移至开头。如果 *key* 不存在则会触发`KeyError`

+ 3.2新版功能

  + 相对于通常的映射方法，有序字典还另外提供了逆序迭代的支持，通过 [`reversed()`](https://docs.python.org/zh-cn/3/library/functions.html#reversed) 。

  + `OrderedDict`之间的相等测试是顺序敏感的，实现为 `list(od1.items())==list(od2.items())` 。 
  + `OrderedDict` 对象和其他的 [`Mapping`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Mapping) 的相等测试，是顺序敏感的字典测试。
  + 这允许 [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 替换为任何字典可以使用的场所。

+ 3.5版本更改

  [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 的项(item)，键(key)和值(value) [视图](https://docs.python.org/zh-cn/3/glossary.html#term-dictionary-view) 现在支持逆序迭代，通过 [`reversed()`](https://docs.python.org/zh-cn/3/library/functions.html#reversed) 。

+ 3.6版本更改

   [**PEP 468**](https://www.python.org/dev/peps/pep-0468) 赞成将关键词参数的顺序保留， 通过传递给 [`OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 构造器和它的 `update()` 方法。

+ 3.9 版本更改

  增加了合并 (`|`) 与更新 (`|=`) 运算符，相关说明见 [**PEP 584**](https://www.python.org/dev/peps/pep-0584)。

+ 实例1：

  ```python
  import collections
  odic = collections.OrderedDict()
  odic['key1'] = 'value1'
  odic['key2'] = 'value2'
  odic['key3'] = 'value3'
  print(odic)
  odic['key1'] = 'newvalue1'
  print(odic)
  ```

  ```python
  OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
  OrderedDict([('key1', 'newvalue1'), ('key2', 'value2'), ('key3', 'value3')])
  ```

## Counter

### 功能

* Counter类的目的是用来跟踪值出现的次数。

* 它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。

  计数值可以是任意的Interger（包括0和负数）。

* Counter类和其他语言的bags或multisets很相似。

### 实例

```python
c = Counter("abedbcdcba")
print(c)
```

```python
Counter({'b': 3, 'a': 2, 'd': 2, 'c': 2, 'e': 1})
```

* counter会从小到大排序，同一数量的情况下会按照原出现顺序排序

### 创建

```python
c = Counter()  # 创建一个空的Counter类
c = Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
c = Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
c = Counter(a=4, b=2)  # 从一组键值对创建
```

### 访问

* 当所访问的键不存在时，返回0，而不是KeyError；否则返回它的计数。

```python
>>> c = Counter("abcdefgab")
>>> c["a"]
2
>>> c["c"]
1
>>> c["h"]
0
```

### 更新

* 可以使用一个iterable对象或者另一个Counter对象来更新键值。

* 计数器的更新包括增加和减少两种

  + 增加：update()

    ```python
    >>> c = Counter('which')
    >>> c.update('witch')  # 使用另一个iterable对象更新
    >>> c['h']
    3
    >>> d = Counter('watch')
    >>> c.update(d)  # 使用另一个Counter对象更新
    >>> c['h']
    4
    ```

  + 减少：subtract()

    ```python
    >>> c = Counter('which')
    >>> c.subtract('witch')  # 使用另一个iterable对象更新
    >>> c['h']
    1
    >>> d = Counter('watch')
    >>> c.subtract(d)  # 使用另一个Counter对象更新
    >>> c['a']
    -1
    ```

### 删除

* 当计数值为0时，并不意味着元素被删除，删除元素应当使用`del`。

```python
>>> c = Counter("abcdcba")
>>> c
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
>>> c["b"] = 0
>>> c
Counter({'a': 2, 'c': 2, 'd': 1, 'b': 0})
>>> del c["a"]
>>> c
Counter({'c': 2, 'b': 0, 'd': 1})
```

### elements()

* 返回一个迭代器。
* 元素被重复了多少次，在该迭代器中就包含多少个该元素。
* 元素排列无确定顺序，个数小于1的元素不被包含。

```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
```

### most_common([n])

* 返回一个TopN列表。
* 如果n没有被指定，则返回所有元素。
* 当多个元素计数值相同时，排列是无确定顺序的。

```python
>>> c = Counter('abracadabra')
>>> c.most_common()
[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
>>> c.most_common(3)
[('a', 5), ('r', 2), ('b', 2)]
```

### fromkeys

* 未实现的类方法。

### 浅拷贝copy

```python
>>> c = Counter("abcdcba")
>>> c
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
>>> d = c.copy()
>>> d
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
```

### 算术和集合操作

* +、-、&、|操作也可以用于Counter。
* 其中&和|操作分别返回两个Counter对象各元素的最小值和最大值。
* 需要注意的是，得到的Counter对象将删除小于1的元素。

```python
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d  # c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d  # subtract（只保留正数计数的元素）
Counter({'a': 2})
>>> c & d  # 交集:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
>>> c | d  # 并集:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
```

### 常用操作

```python
sum(c.values())  # 所有计数的总数
c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
c.items()  # 转为(elem, cnt)格式的列表
Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
c.most_common()[:-n:-1]  # 取出计数最少的n-1个元素
c += Counter()  # 移除0和负值
```

## deque

* 队列是一种只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
* 在Python文档中搜索队列（queue）会发现，Python标准库中包含了四种队列，分别是:
  * queue.Queue
  * asyncio.Queue
  * multiprocessing.Queue
  * collections.deque
* deque是双端队列（double-ended queue）的缩写，由于两端都能编辑，deque既可以用来实现栈（stack）也可以用来实现队列（queue）。

### 创建

```python
d = deque([])
```

### 添加元素

* 单向队列具有先进后出的特点，而双向队列则更加灵活。
* 添加元素有两个方向：
  * append( value ) 函数，向队列的最右端添加一个元素
  * appendleft( value ) 函数，向队列的最左端添加一个元素
  * extend([value_1, value_2,…, value_n]) 函数，向队列的最右端添加多个元素
  * extendleft([value_1, value_2,…, value_n]) 函数，向队列的最左端添加多个元素

### 删除元素

- pop( ) 函数，将最右边的元素取出一个元素
- popleft( ) 函数，将最左边的元素取出一个元素
- remove( value ) 函数，将 value 对应值在队列中删除，其他元素顺序不变

### 移动队列中的元素

- rotate( num ) 函数， 向右旋转 num 个位置，num>0时，向右旋转；num<0时，向左旋转
- reverse() 函数，将队列倒序排列

### 查询指定元素的个数

- count( value ) 函数，返回队列中 value 值相等的元素个数
