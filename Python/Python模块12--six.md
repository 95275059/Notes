# Python模块12--six

### 简介

大家知道现在python主要有两个大的版本，一个是python2另一个是python3，那么不同的人可能会习惯不同的版本，而python2和python3又有一些区别和不兼容的地方，给程序猿造成了很大的烦恼。

Six 就是来解决这个烦恼的，这是一个专门用来兼容 Python 2 和 Python 3 的模块，它解决了诸如 urllib 的部分方法不兼容， str 和 bytes 类型不兼容等“知名”问题。

### 使用

```python
import six

six.PY2 #返回一个表示当前运行环境是否为python2的boolean值
six.PY3 #返回一个表示当前运行环境是否为python3的boolean值

six.integer_types # 在python2中，存在 int 和 long 两种整数类型；在python3中，仅存在一种类型int
six.string_types # 在python2中，使用的为basestring；在python3中，使用的为str
six.text_type # 在python2中，使用的文本字符的类型为unicode；在python3中使用的文本字符的类型为str
six.binary_type # 在python2中，使用的字节序列的类型为str；在python3中使用的字节序列的类型为bytes
```

```python
False
True
(<class 'int'>,)
(<class 'str'>,)
<class 'str'>
<class 'bytes'>
```

