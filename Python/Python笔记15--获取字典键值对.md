# Python笔记15--获取字典键值对

1. items(),keys(),values()的输出

   ```python
   d = {'name':'haohao','age':'23','country':'China'}
   print(d.keys())
   print(list(d.keys()))
   print(d.values())
   print(list(d.values()))
   print(d.items())
   print(list(d.items()))
   ```

   输出：

   ```python
   dict_keys(['name', 'age', 'country'])
   ['name', 'age', 'country']
   dict_values(['cc', '23', 'China'])
   ['cc', '23', 'China']
   dict_items([('name', 'cc'), ('age', '23'), ('country', 'China')])
   [('name', 'cc'), ('age', '23'), ('country', 'China')]
   ```

   ---

2. 方法一

   ```python
   d = {'name':'cc','age':'23','country':'China'}
   for k in d:
       print(k,d[k])
   ```

   输出

   ```python
   name cc
   age 23
   country China
   ```

   ---

3. 方法二

   ```python
   d = {'name':'cc','age':'23','country':'China'}
   for k, v in d.items():
       print(k, v)
   ```

   输出

   ```python
   name cc
   age 23
   country China
   ```

   + iteriems()返回的是一个迭代器，在需要迭代结果的时候使用最适合，而且它的工作效率非常高。
   + 在Python2.x中，iteritems() 用于返回本身字典列表操作后的迭代器【Returns an iterator on all items(key/value pairs) 】，不占用额外的内存。
   + 在Python 3.x 里面，iteritems()方法已经废除了。在3.x里用 items()替换iteritems() ，可以用于 for 来循环遍历

3. 获取**单元素字典**的key和value

   + 方法一

     ```python
     d = {'name':'cc'}
     (key, value), = d.items()
     print('key=',key)
     print('value=',value)
     ```

     输出

     ```python
     key= name
     value= cc
     ```

   + 方法二

     ```python
     d = {'name':'cc'}
     key = list(d)[0]
     value = list(d.values())[0]
     print('key=',key)
     print('value=',value)
     ```

     输出

     ```python
     key= name
     value= cc
     ```

   + 方法三

     ```python
     d = {'name':'cc'}
     key, = d
     value, = d.values()
     print('key=',key)
     print('value=',value)
     ```

     输出

     ```python
     key= name
     value= cc
     ```

   + 方法四

     ```python
     d = {'name':'cc'}
     keys = list(d.keys())[0]
     values = list(d.values())[0]
     print('key=',key)
     print('value=',value)
     ```

     输出

     ```
     key= name
     value= cc
     ```

     

