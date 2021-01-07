# Python笔记23--内置函数enumerate

### 描述

+ numerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

+ Python 2.3. 以上版本可用，2.6 添加 start 参数。

---

### 语法

```python
enumerate(sequence, [start=0])
```

+ sequence : 一个序列，迭代器或其他支持迭代对象
+ start : 下标起始位置
+ 返回值 : 返回enumerate(枚举)对象

---

### 实例

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(enumerate(seasons))
print(list(enumerate(seasons)))

for i, value in enumerate(seasons):
    print(i, value)
```

```python
<enumerate object at 0x0000024B8E075188>
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
0 Spring
1 Summer
2 Fall
3 Winter
```





