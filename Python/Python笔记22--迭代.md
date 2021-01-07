# Python笔记22--迭代

### 描述

+ 如果给定一个list或tuple，我们可以通过`for`循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
+ 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
+ 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

---

### 对list实现类似Java那样的下标循环

+ 使用内置的enumerate函数可以把一个list变成索引-元素对

```python
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
```

```python
0 A
1 B
2 C
```

---

### 使用迭代查找一个list中最小和最大值，并返回一个tuple

```python
def findMinAndMax(L):
    if not L:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if min>i:
                min = i
            if max<i:
                max = i
        return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
```



