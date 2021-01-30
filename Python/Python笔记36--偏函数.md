# Python笔记36--偏函数

### 偏函数是functools模块提供的一种功能

> functools.partial

+ functools.partial可以把一个函数的某些参数给固定住（即，设置默认值），返回一个新的函数

### 实例

```python
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1000000',base=10))
```

```python
64
1000000
```

+ **创建偏函数时，实际上可以接收函数对象、`*args`和`**kw`这3种参数**

  实际上，`int2 = functools.partial(int, base=2)`相当于：

  ```
  kw = {'base':2}
  int('1000000', **kw)
  ```

  类似的，`max2=functools.partial(max,10)`，实际上会把10作为*args的一部分自动加到左边，也就是

  ```
  max2(5,6,7)
  ```

  相当于

  ```
  args = (10,5,6,7)
  max(*args)
  ```

  



