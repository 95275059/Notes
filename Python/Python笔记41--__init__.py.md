# Python笔记41--\__init__.py

## 标识该目录是一个python的模块包（module package）

如果你是使用python的相关IDE来进行开发，那么如果目录中存在该文件，该目录就会被识别为 module package 。

## 简化模块导入操作

假设我们的模块包的目录结构如下：

```python
.
└── mypackage
    ├── subpackage_1
    │   ├── test11.py
    │   └── test12.py
    ├── subpackage_2
    │   ├── test21.py
    │   └── test22.py
    └── subpackage_3
        ├── test31.py
        └── test32.py
```

这样的话，看起来就会很麻烦，查找的时候也会麻烦，此时`__init__.py`就起到了简化的作用。

### init.py的工作原理

实际上，**如果目录中包含了  `__init__.py`  时，当用 import 导入该目录时，会执行 `__init__.py` 里面的代码。**

我们在mypackage目录下增加一个 `__ init __.py` 文件来做一个实验：

```
.
└── mypackage
    ├── __init__.py
    ├── subpackage_1
    │   ├── test11.py
    │   └── test12.py
    ├── subpackage_2
    │   ├── test21.py
    │   └── test22.py
    └── subpackage_3
        ├── test31.py
        └── test32.py
```

`mypackage/__init__.py` 里面加一个print，如果执行了该文件就会输出

```python
print("You have imported mypackage")
```

下面直接用交互模式进行 import

```python
>>> import mypackage
You have imported mypackage
```

很显然，`__init__.py` 在包被导入时会被执行。

### 控制模块导入

我们再做一个实验，在 mypackage/\__init__.py 添加以下语句：

```python
from subpackage_1 import test11
```

我们导入 mypackage 试试:

```python
>>> import mypackage
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/taopeng/Workspace/Test/mypackage/__init__.py", line 2, in <module>
    from subpackage_1 import test11
ImportError: No module named 'subpackage_1'
```

原来，**在我们执行import时，当前目录是不会变的（就算是执行子目录的文件），还是需要完整的包名。**

```python
from mypackage.subpackage_1 import test11
```

**综上，我们可以在\__init__.py 指定默认需要导入的模块**

### 偷懒的导入方法

有时候我们在做导入时会偷懒，将包中的所有内容导入

```python
from mypackage import *
```

这是怎么实现的呢？ `__all__`变量就是干这个工作的

`__all__` 关联了一个模块列表，当执行 `from xx import *` 时，就会导入列表中的模块。

我们将 `__init__.py` 修改为 :

```python
__all__ = ['subpackage_1', 'subpackage_2']
```

这里没有包含 `subpackage_3`，是为了证明 `__all__` 起作用了，而不是导入了所有子目录。

```python
>>> from mypackage import *
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'subpackage_1', 'subpackage_2']
>>> 
>>> dir(subpackage_1)
['__doc__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
```

**子目录的中的模块没有导入！！！**

该例子中的导入等价于:

```python
from mypackage import subpackage_1, subpackage_2
```

因此，**导入操作会继续查找 subpackage_1 和 subpackage_2 中的 `__init__.py` 并执行。**（但是此时不会执行 import *）

我们在 subpackage_1 下添加 `__init__.py` 文件:

```python
__all__ = ['test11', 'test12']
# 默认只导入test11
from mypackage.subpackage_1 import test11
```

再导入试试：

```python
>>> from mypackage import *
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'subpackage_1', 'subpackage_2']
>>> 
>>> dir(subpackage_1)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'test11']
```

如果想要导入子包的所有模块，则需要更精确指定。

```python
>>> from mypackage.subpackage_1 import *
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'test11', 'test12']
```

### 配置模块的初始化操作

在了解了 __init__.py 的工作原理后，应该能理解该文件就是一个正常的python代码文件。

因此可以将初始化代码放入该文件中。

