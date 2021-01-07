# Python模块14--collections

### 参考官网

https://docs.python.org/zh-cn/3/library/collections.html

---

### 介绍

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

### OrderdDict对象

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

  