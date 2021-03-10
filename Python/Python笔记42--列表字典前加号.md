# Python笔记42--列表字典前加*号

## 列表前加*号

列表前面加星号作用是将列表中所有元素解开成独立的参数，传入函数，参数数量等于`len(data)`

```python
def add(a,b):
    return a+b

data = [4, 3]
print(add(*data))
```

```python
7
```

## 字典前加两个*号

字典前面加两个星号，是将字典解开成独立的元素作为形参

```python
def add(a,b):
    return a+b

data = {'b': 4, 'a': 3}
print(add(**data))
```

```python
7
```

+ 注：字典中的键必须和函数形参一致