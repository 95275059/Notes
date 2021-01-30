# Python笔记18--args和kwargs

+ 并不是必须写成\*args 和\*\*kwargs。只有变量前的\*(星号)才是必须的. 你也可以写成\*var和\**vars. 

+ 写成*args和**kwargs只是个通俗的命名约定。

+ *args和**kwargs主要用于函数定义,可以将不定数量的参数传递给某个函数。

  这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字

---

## *args

+ *args用来发送一个非键值对的可变数量的参数**元组**给一个函数.

```python
def test_args(f_arg, *args):
    print('first normal arg:', f_arg)
    print('*args:', *args)
    print('args:', args)
    print('type of *args:', type(args))
    for arg in args:
        print('another arg through *args:', arg)
        
test_args('aaa', 'bbb', 'ccc', 'ddd')
```

```python
first normal arg: aaa
*args: bbb ccc ddd
args: ('bbb', 'ccc', 'ddd')
type of *args: <class 'tuple'>
another arg through *args: bbb
another arg through *args: ccc
another arg through *args: ddd
```

---

```python
def q2(*args):
    print('例2')
    print(args)
    print(type(args))
    print(args[0])
t1 = 123,234,345
q2(*t1)
t2 = (234,345,456)
q2(*t2)
t3=[345,456,567]
q2(*t3)
q2(t3)
print('-----------------')
```

```python
例2
(123, 234, 345)
<class 'tuple'>
123
例2
(234, 345, 456)
<class 'tuple'>
234
例2
(345, 456, 567)
<class 'tuple'>
345
例2
([345, 456, 567],)
<class 'tuple'>
[345, 456, 567]
-----------------
```

---

## **kwargs

+ \**kwargs将不定长度的键值对（字典）作为参数传递给一个函数。
+ 如果你想要在一个函数里处理带名字的参数，你应该使用**kwargs。

```python
def test_kwargs(**kwargs):
    print('*kwargs:', *kwargs)
    print('kwargs:', kwargs)
    print('type of **kwargs:', type(kwargs))
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

test_kwargs(name='cxy', gender='female', age=23)
```

```python
*kwargs: name gender age
kwargs: {'name': 'cxy', 'gender': 'female', 'age': 23}
type of **kwargs: <class 'dict'>
name == cxy
gender == female
age == 23
```

---

```python
def q3(**kwargs):
    print('例3')
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name1'])
di = {
    'name1': 'jack',
    'name2': 'rose',
}
q3(**di)
print('-----------------')
```

```python
例3
{'name1': 'jack', 'name2': 'rose'}
<class 'dict'>
jack
-----------------
```

## 同时使用*args和**kwargs

```python
def q4(*args, **kwargs):
    print('例4')
    print(args)
    print(kwargs)
tl = 123, 456
di = {
    'name1': 'jack',
    'name2': 'rose',
}
print('方案1')
q4(123, name1='jack', name2='rose')
print('-----------------')
print('方案2')
q4(tl, di)
print('-----------------')
print('方案3')
q4(*tl, **di)
print('-----------------')
```

```python
方案1
例4
(123,)
{'name1': 'jack', 'name2': 'rose'}
-----------------
方案2
例4
((123, 456), {'name1': 'jack', 'name2': 'rose'})
{}
-----------------
方案3
例4
(123, 456)
{'name1': 'jack', 'name2': 'rose'}
-----------------
```

+ 注意同时使用时使用第一种方案或者第三种方案

  第二种方案会把字典也当成\*args的参数，被加入*args元组中

  

  