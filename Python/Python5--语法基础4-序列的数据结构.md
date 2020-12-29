# Python5--语法基础4-序列的数据结构

 序列是Python中最基本的数据结构

### 列表List

**最常用的Python数据类型**

+ 一维列表
  + **数据项不需要具有相同的类型。**

    list1=['美国','中国',1997,2000];

  + 创建一个元素为0-9的列表

    L=[i for i in range(10)]

  + 删除列表元素

    del list1[2]                   #删除列表第三个元素

    list1.remove(1997)    #删除列表中的1997元素

    list1.pop(2)                 #删除列表中第三个元素，无参数时删除最后一个元素

  + 添加列表元素

    list1.append(2003)   #在列表末尾添加元素。

+ 多维列表
  + 二维列表

    list2=[["CPU","内存"],["硬盘","声卡"]]

    ```python
    rows = 3  
    cols = 6  
    matrix = [[0 for col in range(cols)] for row in range(rows)] #3行6列的全零矩阵 
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = i * 3 + j
            print(matrix[i][j],end = ",")
        print()
    ```

+ 列表操作符
  + len([1,2,3])   =>   3
  + [1,2,3]+[4,5,6]   =>   [1,2,3,4,5,6]
  + ['Hi!']*4 => ['Hi!','Hi!','Hi!','Hi!']
  + 3 in [1,2,3] => True

+ 列表内置函数
  + list.append(obj):在列表末尾添加新对象obj

  + list.count(obj):统计obj在列表中出现的次数

  + list.extend(seq):在列表末尾一次性追加另一个序列中的多个值

  + list.index(obj):从列表中找到值obj第一个匹配项的索引位置

  + list.insert(index,obj):将obj插入到index索引位置上，index位置上的数以及之后的数后移 

  + list.pop(index):移除列表中index位置的元素，默认为最后一个元素，返回该元素的值

  + list.remove(obj):移除列表中某个值的第一个匹配项

  + list.reverse():反转列表中元素顺序

  + list.sort([func]):对原列表进行排序

    list.sort():从小到大

    list.sort(reverse=True):从大到小

  + len(list):返回列表元素个数

  + max(list):返回列表元素最大值

  + min(list):返回列表元素最小值

  + list(seq):将元组转换为列表

+ 列表生成式（List Comprehensions）

  是Python内置的非常简单却强大的可以用来创建list的生成式。

  + 生成[1,2,3,4,5,6,7,8,9,10]

    ```python
    li = list(range(1, 11))
    ```

  + 生成[1x1, 2x2, 3x3, ..., 10x10]

    ```python
    li = []
    for x in range(1, 11):
        li.append(x*x)
    ```

    通过列表生成是可以用一行语句代替循环生成上面的list

    ```python
    >>> [x * x for x in range(1, 11)]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

    写列表生成式时，把要生成的元素`x * x`放到前面，后面跟`for`循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

  + for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

    ```python
    >>> [x * x for x in range(1, 11) if x % 2 == 0]
    [4, 16, 36, 64, 100]
    ```

  + 可以使用两层循环，生成全排列

    ```python
    >>> [m + n for m in 'ABC' for n in 'XYZ']
    ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    ```

    三层和三层以上的循环就很少用到了

  + 列出当前目录下的所有文件和目录名，可以通过一行代码实现：

    ```python
    import os
    li = [d for d in os.listdir('.')]
    print(li)
    ```

    ```python
    ['.idea', '.vs', 'args_Study.py', 'args_Study2.py', 'client.py', 'count_study.py', 'dictionary_test.py', 'encode_decode_study.py', 'find_study.py', 'intersection_study.py', 'IOselect_client.py', 'IOselect_server.py', 'iscapitalize.py', 'isupper.py', 'join_test.py', 'kwargs_study.py', 'list_test.py', 'locals_test.py', 'main.py', 'maketrans.py', 'pool_study.py', 'print_format.py', 'process_study.py', 'reload_study.py', 'remove_test.py', 'res_test.py', 're_Study.py', 'select_client1.py', 'select_client2.py', 'select_client3.py', 'select_server.py', 'server.py', 'set_study.py', 'split_study.py', 'string_study.py', 'strip_test.py', 'str_to_list.py', 'test.py', 'time_test.py', 'translate_study.py', 'upper.py', 'venv', 'zip_test.py', '__pycache__']
    ```

  + `for`循环其实可以同时使用两个甚至多个变量，比如`dict`的`items()`可以同时迭代key和value：

    ```python
    >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
    >>> for k, v in d.items():
    ...     print(k, '=', v)
    ...
    y = B
    x = A
    z = C
    ```

    因此，列表生成式也可以使用两个变量来生成list：

    ```python
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    li = [k + '=' + v for k, v in d.items()]
    print(li)
    ```

    ```python
    ['x=A', 'y=B', 'z=C']
    ```

  + 把一个list中的所有字母变成小写

    ```python
    d = ['Hello', 'World', 'IBM', 'Apple']
    li = [x.lower() for x in d]
    print(li)
    ```

    ```python
    ['hello', 'world', 'ibm', 'apple']
    ```

  + if ... else

    不能在最后的if加上else

    ```python
    >>> [x for x in range(1, 11) if x % 2 == 0 else 0]
      File "<stdin>", line 1
        [x for x in range(1, 11) if x % 2 == 0 else 0]
                                                  ^
    SyntaxError: invalid syntax
    ```

    

  

---

### 元组（tuple）

**元组元素不能修改**

+ 创建元组

  空元组：tup=() 

  只有一个元素：tup1=(1,)           #,可加可不加

  tup2=('美国','中国',1997,2000)

+ 元组的连接

  tup3 = tup1 + tup2

+ 元组的删除

  **不能删除元组中的元素值，但可以删除整个元组**

  del tup

+ 内置函数：

  len(tuple)

  max(tuple)

  min(tuple)

  tuple(seq):将列表转换为元组

+ 使用元组一次性对多个变量赋值

  (x,y,z)=(1,2,3)

+ 交换x,y

  x,y=y,x

+ 列表\元组与字符串的相互转化

  + 列表转化为字符串

    ```python
    nums=[1,2,3,4,5]
    str1=str(nums)                # str1=[1,2,3,4,5]
    
    str2="%"
    num2=['c','x','y']
    str2=str2.join(num2)          # str2=c%x%y
    
    str2=""
    str2=str2.join(num2)          # str2=cxy
    ```

---

---

3. 字典（dict）（关联数组，哈希表）

   + 创建字典

     d={key1 : value1 , key2 : value2}

     + 键唯一，值不必：键不可变，值可取任何数据类型；
     + 不允许出现相同的键，若同一键被赋值两次，后一个值会覆盖前面的值。
     + 列表不能充当键

   + 访问字典

     dict[键']

   + 修改字典

     dict={'Name':'cxy' , 'Age' : 18 , 'Class' : '计算机一班'}

     dict['Age'] = 22                  #更新键/值对

     dict['School'] = 'jnu'         #新增键/值对

   + 删除字典元素

     del dict['Name']              #del 删除字典中的元素

     dict.clear()                       #clear 清空字典所有元素

   + in运算

     ‘Age’ in dict                     #判断键Age是否在字典里 等价于dict.has_key('Age')

   + 获取字典所有(value)值

     dict.values() 

     ```python
     dict={'Name' : 'cxy' , 'Age' : 22 , 'Class' : '计算机1505'}
     x=dict.values()
     print(x)
     ```

     输出：dict_values(['cxy', 22, '计算机1505'])

   + items()方法

     把字典中每对key和value组成一个元组，并把这些元组放在列表中返回

     注：字典打印出来的顺序与创建之初的顺序不同，因为字典中各个元素并没有顺序值分，在存储元素时进行了优化，使字典的存储和查询效率最高。 列表是有顺序之分的。

   + 实例

     ```python
     d = {'name':'haohao','age':'23'}
     print(d.keys())
     print(list(d.keys()))
     print(d.values())
     print(list(d.values()))
     print(d.items())
     print(list(d.items()))
     ```
   
     输出：
   
     ```python
     dict_keys(['name', 'age'])
     ['name', 'age']
     dict_values(['haohao', '23'])
     ['haohao', '23']
     dict_items([('name', 'haohao'), ('age', '23')])
     [('name', 'haohao'), ('age', '23')]
     ```
   
   + 内置函数
   
     | 函数                              | 说明                                                         |
     | --------------------------------- | ------------------------------------------------------------ |
     | dict.clear()                      | 清空字典中所有元素                                           |
     | dict.copy()                       | 返回一个字典副本                                             |
     | dict.fromkeys(seq[, val])         | 创建一个新字典，以序列seq中元素做字典的键，val为字典**所有键**对应的初始值(默认为none) |
     | dict.get(key,default=None)        | 返回指定键的值，如果值不在字典中则返回default值              |
     | dict.has_key(key)                 | 键在字典返回True,否则返回False                               |
     | dict.items()                      | 以列表返回可遍历的(键，值)元组数组                           |
     | dict.keys()                       | 以列表返回一个字典所有的键                                   |
     | dict.setdefault(key,default=None) | 类似get(),但若键不存在字典中，将会添加键并将值设为default    |
     | dict.update(dict2)                | 把字典dict2的键/值对更新到dict中                             |
     | dict.values()                     | 以列表返回字典中所有值                                       |
     | cmp(dict1,dict2)                  | 比较两个字典元素                                             |
     | len(dict)                         | 返回字典元素个数（键的总数）                                 |
     | str(dict)                         | 输出值可以打印的字符表示                                     |
     | type(variable)                    | 返回输入的变量类型，如果变量时字典就返回字典类型             |

---

---

4. 集合

   集合是一个**无序不重复**元素序列，用于进行成员关系测试及删除重复元素

   + 创建集合

     student={'Tom','Jack','Mary'}            #输出时会自动删除重复值

     student=set('Tom','Jack','Mary') 

     **创建空集合必须使用set()，student={}创建的是字典**

   + 集合运算

     ```python
     a=set('abcd')
     b=set('cdef')
     
     print(a)
     print("差集a-b:",a-b)
     print("并集a|b:",a|b)
     print("交集a&b:",a&b)
     print("a,b不同时存在的元素a^b:",a^b)
     
     
     #结果
     {'d', 'c', 'b', 'a'}
     差集a-b: {'b', 'a'}
     并集a|b: {'f', 'd', 'b', 'a', 'c', 'e'}
     交集a&b: {'c', 'd'}
     a,b不同时存在的元素a^b: {'f', 'b', 'a', 'e'}
     ```

     



























 