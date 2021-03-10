# Python模块21--pandas

## 简介

+ Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的
+ Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具

## 数据结构

+ Series: 一维数组

  与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近

  区别：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。

+ Time-Series: 以时间为索引的Series

+ DataFrame: 二维的表格型数据结构

  很多功能与R中的data.frame类似

  可以将DataFrame理解为Series的容器

+ Panel: 三维的数组

  可以理解为DataFrame的容器

Pandas 有两种自己独有的基本数据结构。读者应该注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以，Python 中有的数据类型在这里依然适用，也同样还可以使用类自己定义数据类型。只不过，Pandas 里面又定义了两种数据类型：Series 和 DataFrame，它们让数据操作更简单了。

## 安装

```shell
pip install pandas
```

## 两种数据结构的使用

### Series

+ Series就是竖起来的list

+ 导入

  ```python
  from pandas import Series
  ```

+ 基本使用

  ```python
  s1 = Series([4, 22, 'cxy', '9527'])
  print(s1)
  print(s1.index)
  print(s1.values)
  ```

  ```python
  0       4
  1      22
  2     cxy
  3    9527
  dtype: object
  RangeIndex(start=0, stop=4, step=1)
  [4 22 'cxy' '9527']
  ```

+ Series可自定义索引，还可以根据索引查看和修改值

  ```python
  s2 = Series(data=['cxy', 'woman', 24], index=['name', 'gender', 'age'])
  print(s2)
  print(s2.index)
  print(s2.values)
  print(s2['name'])
  ```

  ```python
  name        cxy
  gender    woman
  age          24
  dtype: object
  Index(['name', 'gender', 'age'], dtype='object')
  ['cxy' 'woman' 24]
  cxy
  ```

  ```python
  s3 = Series({'python': 3.6, 'module': 'pandas', 'name': 'test'})
  print(s3)
  ```

  ```python
  python       3.6
  module    pandas
  name        test
  dtype: object
  ```

+ 如果自定义了索引，自定的索引会自动寻找原来的索引，如果一样的，就取原来索引对应的值，这个可以简称为“自动对齐”，如果找不到一样的索引，就对齐赋给NaN

+ series对象和pandas有专门的方法来判断值是否为空

  ```python
  s4 = Series({'python': 3.6, 'module': 'pandas', 'name': 'test'}, index=['PYTHON', 'module', 'name'])
  print(s4)
  print(pd.isnull(s4))
  print(pd.isnull(s4['PYTHON']))
  print(s4.isnull())
  print(s4.isnull()['PYTHON'])
  ```

  ```python
  PYTHON       NaN
  module    pandas
  name        test
  dtype: object
  PYTHON     True
  module    False
  name      False
  dtype: bool
  True
  PYTHON     True
  module    False
  name      False
  dtype: bool
  True
  ```

+ 索引的名字可以重新定义

  ```python
  s5 = Series({'python': 3.6, 'module': 'pandas', 'name': 'test'})
  s5.index = ['PYTHON', 'MODULE', 'NAME']
  print(s5)
  ```

  ```python
  PYTHON       3.6
  MODULE    pandas
  NAME        test
  dtype: object
  ```

+ series数据可以做相关的运算

  ```python
  s6 = Series({'Chinese': 90, 'Math': 100, 'English': 95})
  print(s6)
  print(s6*2)
  ```

  ```python
  Chinese     90
  Math       100
  English     95
  dtype: int64
  Chinese    180
  Math       200
  English    190
  dtype: int64
  ```

### DataFrame

+ DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。

+ 它的竖行称之为 columns，横行跟前面的 Series 一样，称之为 index，也就是说可以通过 columns 和 index 来确定一个主句的位置。

+ 导入

  ```python
  from pandas import Series, DataFrame
  ```

+ 基本使用

  定义一个 DataFrame 对象的常用方法——使用 dict 定义

  字典的“键”（"name"，"marks"，"price"）就是 DataFrame 的 columns 的值（名称），字典中每个“键”的“值”是一个列表，它们就是那一竖列中的具体填充数据。上面的定义中没有确定索引，所以，按照惯例（Series 中已经形成的惯例）就是从 0 开始的整数。从上面的结果中很明显表示出来，这就是一个**二维的数据结构**（类似 excel 或者 mysql 中的查看效果）。

  ```python
  data1 = {"name": ['google', 'baidu', 'yahoo'], 'marks': [100, 200, 300], 'price': [1, 2, 3]}
  f1 = DataFrame(data1)
  print(f1)
  print(f1.columns)
  print(f1['name'])
  ```

  ```python
       name  marks  price
  0  google    100      1
  1   baidu    200      2
  2   yahoo    300      3
  ```

+ 在 DataFrame 中，columns 跟字典键相比，有一个明显不同，就是其顺序可以被规定

  ```python
  data1 = {"name": ['google', 'baidu', 'yahoo'], 'marks': [100, 200, 300], 'price': [1, 2, 3]}
  f2 = DataFrame(data=data1, columns=['name', 'price', 'marks'])
  print(f2)
  ```

  ```python
       name  price  marks
  0  google      1    100
  1   baidu      2    200
  2   yahoo      3    300
  ```

+ DataFrame 数据的索引也能够自定义

  ```python
  data1 = {"name": ['google', 'baidu', 'yahoo'], 'marks': [100, 200, 300], 'price': [1, 2, 3]}
  f3 = DataFrame(data=data1, columns=['name', 'price', 'marks'], index = ['a', 'b', 'c'])
  print(f3)
  ```

  ```python
       name  price  marks
  a  google      1    100
  b   baidu      2    200
  c   yahoo      3    300
  ```

  还可以使用**“字典套字典”**的方式。

  ```python
  data2 = {'name':{'first':'python','second':'java'}, 'price':{'first':5000,'second':2000}}
  f4 = DataFrame(data2)
  print(f4)
  ```

  ```python
            name  price
  first   python   5000
  second    java   2000
  ```

  在字典中就规定好数列名称（第一层键）和每横行索引（第二层字典键）以及对应的数据（第二层字典值），也就是在字典中规定好了每个数据格子中的数据，没有规定的都是空。

+ 赋值

  ```python
  data2 = {'name':{'first':'python','second':'java'}, 'price':{'first':5000,'second':2000}}
  f5 = DataFrame(data=data2, columns=['name', 'price', 'marks'])
  print(f5)
  f5['marks'] = 1
  print(f5)
  marks = Series([1, 2], index=['first', 'second'])
  f5['marks'] = marks
  print(f5)
  f5['marks']['second'] = 3
  print(f5)
  ```

  ```python
            name  price marks
  first   python   5000   NaN
  second    java   2000   NaN
            name  price  marks
  first   python   5000      1
  second    java   2000      1
            name  price  marks
  first   python   5000      1
  second    java   2000      2
            name  price  marks
  first   python   5000      1
  second    java   2000      3
  E:\CMD-SGIN-ET\CMD-SGIN-EP36\CMD_SGIN_EP\test\test.py:38: SettingWithCopyWarning: 
  A value is trying to be set on a copy of a slice from a DataFrame
  
  See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    f5['marks']['second'] = 3
  ```

## 读取文件

### 文件类别

+ csv文件 : read_csv

  ```python
  import pandas as pd
  data = pd.read_csv('E:/CMD-SGIN-ET/CMD-SGIN-EP36/CMD_SGIN_EP/link_emulation/workspace/link_delay_WX_Station_LEO_A1.csv')
  ```

  从文件、URL、文件型队形中加载待分隔符的数据。默认分隔符为逗号

### DataFrame.head()

```python
data.head()
```

```python
               Time (UTCG)  Path Delay (sec)
0  1 Feb 2021 00:38:37.353             0.016
1  1 Feb 2021 00:39:37.000             0.015
2  1 Feb 2021 00:40:37.000             0.014
3  1 Feb 2021 00:41:37.000             0.013
4  1 Feb 2021 00:42:37.000             0.013
```

+ 从文件头开始读取，默认读取前五行数据

+ 读取指定行数数据

  ```python
  data.head(1)
  ```

  ```python
                 Time (UTCG)  Path Delay (sec)
  0  1 Feb 2021 00:38:37.353             0.016
  ```

### DataFrame.shape

```python
data.shape
```

```python
(127, 2)
```

+ 获取文件行列数
+ 行数：data.shape[0]
+ 列数：data.shape[1]

### DataFrame.columns.tolist()

```
data.columns
```





