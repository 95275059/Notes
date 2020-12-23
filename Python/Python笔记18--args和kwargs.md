# Python笔记18--args和kwargs

+ 并不是必须写成\*args 和\*\*kwargs。只有变量前的\*(星号)才是必须的. 你也可以写成\*var和\**vars. 

+ 写成*args和**kwargs只是个通俗的命名约定。

+ *args和**kwargs主要用于函数定义,可以将不定数量的参数传递给某个函数。

  这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字

---

### *args

+ *args用来发送一个非键值对的可变数量的参数元组给一个函数.

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

### **kwargs

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

