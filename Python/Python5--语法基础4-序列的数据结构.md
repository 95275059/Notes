# Python5--语法基础4-序列的数据结构

 序列是Python中最基本的数据结构

1. 列表List

   **最常用的Python数据类型**

   一维列表

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

   ---

   多维列表
   
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
   
   ---
   
   列表操作符
   
   + len([1,2,3])   =>   3
   + [1,2,3]+[4,5,6]   =>   [1,2,3,4,5,6]
   + ['Hi!']*4 => ['Hi!','Hi!','Hi!','Hi!']
   + 3 in [1,2,3] => True
   
   ---
   
   列表内置函数
   
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

---

---

2. 元组（tuple）

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

     



























 