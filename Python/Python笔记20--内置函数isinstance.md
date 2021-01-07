# Python笔记20--内置函数isinstance

### 说明

isinstance()函数用来判断一个对象是否是一个已知的类型，类似type()

+ isinstance与type的区别
  + type()不会认为子类是一种父类类型，不考虑继承关系。
  + isinstance() 会认为子类是一种父类类型，考虑继承关系。

---

### 语法

```python
isinstance(object, classinfo)
```

+ object : 实例对象

+ classinfo : 可以是直接或间接类名，基本类型或者由他们组成的元组

+ 返回值

  如果object的类型与classinfo相同，则返回True，否则返回False

---

### 实例

```python
a = '6'
b = 6
print(isinstance(a, str))
print(isinstance(b, str))
print(isinstance(b, (str, int, tuple, dict, list)))   # 是元组中的一个就返回True
```

```python
True
False
True
```

```python
class A:
    print('class A')

class B(A):
    print('class B')

a = A()
b = B()
print('type(A) : ', type(A))
print('type(a) : ', type(a))
print('type(B) : ', type(B))
print('type(b) : ', type(b))
print('isinstance(a, A) : ', isinstance(a, A))
print('isinstance(b, A) : ', isinstance(b, A))
print('type(b) == B : ', type(b) == B)
print('type(B) == B : ', type(B) == B)
print('type(b) == A : ', type(b) == A)
print('type(B) == A : ', type(B) == A)
print('type(A) == type : ', type(A) == type)
print('type(B) == type : ', type(B) == type)
```

```python
class A
class B
type(A) :  <class 'type'>
type(a) :  <class '__main__.A'>
type(B) :  <class 'type'>
type(b) :  <class '__main__.B'>
isinstance(a, A) :  True
isinstance(b, A) :  True
type(b) == B :  True
type(B) == B :  False
type(b) == A :  False
type(B) == A :  False
type(A) == type :  True
type(B) == type :  True
```

### 判断一个对象是否可迭代

```python
from collections import Iterable
print(isinstance('abc', Iterable))
```

```python
True
```



