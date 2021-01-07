# Python模块2--re

### 描述

+ Python自1.5版本起增加了re模块，它提供 Perl 风格的正则表达式模式。

+ re 模块使 Python 语言拥有全部的正则表达式功能。

+ compile 函数根据一个**模式字符串**和可选的标志参数生成一个**正则表达式对象**。该对象拥有一系列方法用于正则表达式匹配和替换。

+ re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

---

### re.match

+ re.match尝试从字符串的**起始位置**匹配**一个**模式

  匹配成功，则返回一个匹配的对象，否则返回None

  如果不是起始位置匹配成功的话，函数就返回None

+ re.match(pattern,string,flags=0)

  | 参数   | 描述                                                         |
  | ------ | ------------------------------------------------------------ |
  | patern | 匹配的正则表达式                                             |
  | string | 要匹配的字符串                                               |
  | flags  | 标志位，用于控制正则表达式的匹配方式。如：是否区分大小写，多行匹配等。 |

  ---

  flags标志位修饰符

  | 标志               | 含义                                                         |
  | ------------------ | ------------------------------------------------------------ |
  | re.S(DOTALL)       | 匹配包括换行在内的所有字符                                   |
  | re.M(MULTILINE)    | 多行匹配，影响^和$                                           |
  | re.I（IGNORECASE） | 匹配对大小写不敏感                                           |
  | re.L（LOCALE）     | 做本地化识别（locale-aware)匹配，法语等                      |
  | re.U               | 根据Unicode字符集解析字符。这个标志影响\w,\W,\b,\B           |
  | re.x               | 该标志通过给予更灵活的格式以便将正则表达式写得更加易于理解。 |

  ---

  | 方法名称 | 作用                                     |
  | -------- | ---------------------------------------- |
  | group    | 以str形式返回对象中匹配的元素            |
  | start    | 返回开始位置（第一个字符的索引）         |
  | end      | 返回结束位置（最后一个字符的索引**+1**） |
  | span     | 以tuple形式返回匹配的范围（start,end）   |

  ---

  **分组匹配：给分组起名字，方便group之后调用**

  格式：（?P\<name>）

  + 例1

    ```python
    import re
    s = '1102231990xxxxxxxx'
    res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
    print(res.groupdict())
    print(res.group('city'))
    ```

    输出：

    {'province': '110', 'city': '223', 'born_year': '1990'}
    223

    ---

  + 例2

    ```python
    import re
    
    s='ABC356'
    print(re.search('(?P<D>\D+)(?P<d>\d+)',s).group())
    print(re.search('(?P<D>\D+)(?P<d>\d+)',s).group('D'))
    print(re.search('(?P<D>\D+)(?P<d>\d+)',s).group('d'))
    print(re.search('(?P<D>\D+)(?P<d>\d+)',s).groups())
    ```

    输出：

    ABC356
    ABC
    356
    ('ABC', '356')

  ---

+ 可以使用group(num)或groups()匹配对象函数来获取匹配表达式

  | 匹配对象函数 | 描述                                                         |
  | ------------ | ------------------------------------------------------------ |
  | group(num=0) | 匹配的整个表达式的字符串，group()可以一次输入多个组号，在这种情况下它将返回一个包含那些组对应值的元组 |
  | groups()     | 返回一个包含所有小组字符串的元组，从1到包含的小组号          |

  ---
  
  例
  
  ```python
  import re
  
  line = "Cats are smarter than dogs"
  
  matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
  
  if matchObj:
      print("matchObj.group() : ", matchObj.group())
      print("matchObj.group(1) : ", matchObj.group(1))
      print("matchObj.group(2) : ", matchObj.group(2))
      print("matchObj.group(1，2) : ", matchObj.group(1,2))
      print("matchObj.groups() : ", matchObj.groups())
  else:
      print("No match!!")
  ```
  
  输出：
  
  matchObj.group() :  Cats are smarter than dogs
  matchObj.group(1) :  Cats
  matchObj.group(2) :  smarter
  matchObj.group(1,2) :  ('Cats', 'smarter')
  matchObj.groups() :  ('Cats', 'smarter')

---

### re.search

+ 扫描整个字符串并**返回==第一个成功==的匹配**

  匹配成功re.search方法返回一个匹配的对象，否则返回None

+ re.search(pattern,string,flags=0)

  | 参数    | 描述                                                         |
  | ------- | ------------------------------------------------------------ |
  | pattern | 匹配的正则表达式                                             |
  | string  | 要匹配的字符串                                               |
  | flags   | 标志位，用于控制正则表达式的匹配方式。如，是否区分大小写，多行匹配等。 |

+ 同样可以使用group(num)或groups()匹配对象函数来获取匹配表达式

+ 例

  ```python
  import re
  print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
  print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
  ```

  输出：

  (0, 3)
  (11, 14)

---

### re.sub

+ 用于替换字符串中的匹配项
+ re.sub(pattern,repl,string,count=0,flags=0)
  + pattern：正则中的模式字符串
  + repl：替换的字符串，也可为一个函数
  + string：要被查找替换的原始字符串
  + count：模式匹配候替换的最大次数，默认0表示替换所有的匹配
  + flags：标志位，用于控制正则表达式的匹配方式。如：是否区分大小写，多行匹配等。

+ 例1

  ```python
  import re
  phone= "2004-959-559    #电话号码"
  
  num = re.sub(r'#.*$',"",phone)   #删除注释
  print(num)
  num = re.sub(r'\D',"",phone)     #删除-
  print(num)
  ```

  输出：

  2004-959-559    
  2004959559

+ 例2

  ```python
  import re
  
  def double(matched):
      value = int(matched.group('value'))
      return str(value * 2)
  
  s='A23G4HFD567'
  print(re.sub('(?P<value>\d+)',double,s))
  ```

  输出：A46G8HFD1134

4. **re.compile**

   + 用于编译正则表达式，生成一个正则表达式（pattern）对象，供match()和search()调用
   
   + re.compile(pattern[,flags])
     + pattern：一个字符串形式的正则表达式
  + flags：可选，表示匹配模式。如忽略大小写，多行匹配等
   
+ 例
   
     ```python
     import re
     
     pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
     m = pattern.match('Hello World Wide Web')
     print(m.group())
     print(m.group(1))
     print(m.group(2))
     print(m.groups())
  ```
   
  输出：
   
     Hello World
     Hello
     World
  ('Hello', 'World')

---

### re.findall

+ 在字符串中找到正则表达式所匹配的**所有子串**，并返回一个**列表**。如果没有找到匹配的，则返回空列表

+ re.findall(string[,pos[,endpos]])

  + string：待匹配的字符串
  + pos：可选参数，指定字符串的起始位置，默认为0
  + endpos：可选参数，指定字符串的结束为止，默认为字符串的长度

  **==注：match和search也可以指定字符串的起始和结束位置，用法相同==**

+ 例

  ```python
  import re
  
  pattern = re.compile(r'\d+')  # 查找数字
  result1 = pattern.findall('runoob 123 google 456')
  result2 = pattern.findall('run88oob123google456', 0, 10)
  
  print(result1)
  print(result2)
  ```

  输出：

  ['123', '456']
  ['88', '12']

---

### re.finditer

+ 在字符串中找到正则表达式所匹配的**所有子串**，并把他们作为一个**迭代器**返回

+ re.finditer(pattern,string,flags=0)
  + pattern：匹配的正则表达式
  + string：要匹配的字符串
  + flags：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。

+ 例

  ```python
  import re
   
  it = re.finditer(r"\d+","12a32bc43jf3") 
  for match in it: 
      print (match.group())
  ```

  输出：

  12
  32
  43
  3

---

### re.split

+ 按照能够匹配的子串将字符串分割后返回列表
+ re.split(pattern,string[,maxsplit=0,flags=0])
  + pattern：匹配的正则表达式
  + string：要匹配的字符串
  + maxsplit：分割次数；默认为零，即不限制分割次数。例：maxsplit=1分割一次
  + flags：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等

+ 例

  ```python
  import re
  
  print(re.split('\W+', 'runoob runoob, runoob.'))
  print(re.split('(\W+)', 'runoob runoob, runoob.'))
  print(re.split('\W+', 'runoob runoob, runoob.',1))
  
  print(re.split('a*', 'hello world'))    #给定的模式正则表达式没有可匹配的
  ```

  输出：

  ['runoob', 'runoob', 'runoob', '']
  ['runoob', ' ', 'runoob', ', ', 'runoob', '.', '']
  ['runoob', 'runoob, runoob.']
  ['', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '']





