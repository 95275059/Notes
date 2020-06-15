# Python笔记12--内置函数set

1. set()

   + 功能

     + 创建一个**无序不重复**元素集
     + 可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

   + 语法

     ```python
     class set([iterable])
     ```

     + iterable : 可迭代对象
     + 返回值 : 返回新的集合对象

   + 实例

     ```python
     x = set('runoob')
     y = set('google')
     print('x=',x)
     print('y=',y)
     print('x & y = ',x&y)   # 交集
     print('x | y = ',x|y)   # 并集
     print('x - y = ',x-y)   # 差集
     ```

     + output

       ```
       x= {'u', 'n', 'o', 'b', 'r'}
       y= {'o', 'l', 'g', 'e'}
       x & y =  {'o'}
       x | y =  {'u', 'n', 'o', 'l', 'g', 'e', 'b', 'r'}
       x - y =  {'b', 'r', 'u', 'n'}
       ```

   ---

2. set intersection()

   + 功能

     用于返回两个或更多集合中都包含的元素，即**交集**

   + 语法

     ```python
     set.intersection(set1,set2 ... etc)
     ```

     + set1 : 必须，要查找相同元素的集合
     + set2 : 可选，其他要查找相同元素的集合
     + 返回值 : 返回一个新的集合

   + 实例

     ```python
     x = {"apple", "banana", "cherry"}
     y = {"google", "runoob", "apple"}
      
     z = x.intersection(y) 
      
     print(z)
     ```

     + output

       ```
       {'apple'}
       ```

       

   

