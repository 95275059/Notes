# Python笔记2--正则表达式字符匹配规则

### 描述

+ 就其本质而言，正则表达式（或 RE）是一种小型的、高度专业化的编程语言，它内嵌在Python中，并通过 re 模块实现。

+ 正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行。

---

### 规则

+ 普通字符

  大多数字符和字母都会和自身匹配

+ 元字符

  | 元字符 | 说明                                                         |
  | ------ | ------------------------------------------------------------ |
  | .      | 匹配一个除了换行符的任意一个**字符**                         |
  | ^      | 之后后面跟的**字符串**在开头，才能匹配                       |
  | $      | 只有它前面的**字符串**在待检测的字符串的最后，才能匹配上     |
  | *      | 控制它前面的**字符**，前面的字符出现零个或多个都可以匹配上   |
  | +      | 匹配它前面的**字符**至少一次                                 |
  | ？     | 匹配它前面的**字符**零个到一个                               |
  | {}     | 控制它前面一个**字符**的匹配个数，可以有区间（闭区间）。有区间的情况下按照多的匹配 |
  | \      | 后面跟元字符去除特殊功能；后面跟普通字符实现特殊功能；引用序号对应的字组所匹配的字符串（一个括号为一个组）；**在开头加r表示不转义** |
  | \|     | 或                                                           |
  | []     | 匹配字符的类别，**元字符在类别中不起作用**                   |
  | ()     | 把括号内字符作为一个整体去处理                               |

  + [] 

    + [0-9a-zA-Z\\_]可以匹配一个数字、字母或者下划线
    + [0-9a-zA-Z\\_]+ 可以匹配至少由一个数字、字母或者下划线组成的字符串
    + \[a-zA-Z\\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
    + \[a-zA-Z\\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）

  + |

    A|B可以匹配A或B

    + (P|p)ython可以匹配‘Python’或者‘python’

  | 元字符 | 说明                                                         |
  | ------ | ------------------------------------------------------------ |
  | \d     | 匹配任何十进制数，相当于类[0-9]                              |
  | \D     | 匹配任何非数字字符，相当于类\[^0-9]                          |
  | \s     | 匹配任何空白字符，相当于类[\t\n\r\f\v]                       |
  | \S     | 匹配任何非空白字符，相当于类\[^\t\n\r\f\v]                   |
  | \w     | 匹配任何字母数字下划线和汉字字符（匹配非特殊字符），相当于类[a-zA-Z0-9_] |
  | \W     | 匹配任何的特殊字符，相当于类\[^a-zA-Z0-9_]                   |
  | \b     | 匹配一个单词边界，也就是指单词和空格间的位置                 |

---

### 实例


+ *例

  ```python
  strr="cxy9527_cxyy_test_0422cx"
  str1="cxy*"
  print(re.findall(str1,strr))
  ```

  输出：['cxy', 'cxyy', 'cx']
  
  ---

+ +例

  ```python
  strr="cxy9527_cxyy_test_0422cx"
  str1="cxy+"
  print(re.findall(str1,strr))
  ```

  输出：['cxy', 'cxyy']

  ---

+ ?例

  ```python
  strr="cxy9527_cxyy_test_0422cx"
  str1="cxy?"
  print(re.findall(str1,strr))
  ```

  输出：['cxy', 'cxy', 'cx']
  
  ---

+ {}例

  ```python
  strr="cxyyy9527_cxyyyyyy_test_0422cxy"
  str1="cxy{3}"
  print(re.findall(str1,strr))
  ```

  输出：['cxyyy', 'cxyyy']

  ---

  ```python
  strr="cxyyy9527_cxyyyyyy_test_0422cxy"
  str1="cxy{3,5}"
  print(re.findall(str1,strr))
  ```

  输出：['cxyyy', 'cxyyyyy']

  ---

+ \例

  ```python
  strr="cxy9527_cxyyyyyy_test_0422cxy"
  str1=r"(cxy)(9527)_\1"      #\1相当于第一组
  print(re.search(str1,strr).group())
  ```

  输出：cxy9527_cxy

  ---

  ```
  strr="cxy9527_cxyyyyyy_test_0422cxy"
  str1=r"cxy\d"
  print(re.findall(str1,strr))
  ```

  输出：['cxy9']

  ---

  ```python
  strr="test cxy9527_cxyyyyyy_test_0422cxy"
  str1=r"test\scxy"
  print(re.findall(str1,strr))
  ```

  输出：['test cxy']

  ---

  ```python
  strr="test..9527_!@#$%^&*(){}[]\|?><:;"
  str1=r"\w"
  print(re.findall(str1,strr))
  ```

  输出：['t', 'e', 's', 't', '9', '5', '2', '7', '_']

  ---

  ```python
  strr="test..9527_!@#$%^&*(){}[]\|?><:;"
  str1=r"\W"
  print(re.findall(str1,strr))
  ```

  输出：['.', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '\\', '|', '?', '>', '<', ':', ';']

  ---

  ```python
  strr="test cxy  9527"
  str1=r"\bcxy\b"
  print(re.findall(str1,strr))
  ```

  输出：['cxy']

  和str1="cxy"效果一样

  ---

+ ()例

  ```python
  strr="test cxy_9527"
  str1=r"test cxy_(\d+)"
  print(re.search(str1,strr).group())
  ```

  输出：test cxy_9527

  ---

  ```python
  strr="test cxy_9527"
  str1=r"(te)*"    
  print(re.findall(str1,strr))
  ```

  输出：['', 'te', '', '', '', '', '', '', '', '', '', '', '', '']

  ```
#te作为整体进行匹配
  
  ```

if(t和第一个字符匹配)
  	if(e和第二个字符匹配)
		输出匹配项
  	else
		输出‘’
  else
	输出‘’
  ```

  ---

  ```python
strr="test cxy_9527"
  str1=r"test cxy_(\d+?)"     #+最小次数为1
print(re.search(str1,strr).group())
  ```

  输出：test cxy_9

---

  ```python
strr="test cxy_9527"
  str1=r"test cxy_(\d*?)"     #*最小次数为0
print(re.search(str1,strr).group())
  ```

  输出：test cxy_

  ==加了‘？’变成非贪婪匹配模式。但是如果后面还有匹配字符，就无法实现非贪婪匹配==

  ==非贪婪模式即只匹配符合条件的最少字符==

---

  ```
strr="test cxy_9527_test"
  str1=r"test cxy_(\d*?)_test"
print(re.search(str1,strr).group())
  ```

  输出：test cxy_9527_test

+ []例

  ```python
  strr="test cxy_9527_$test"
  str1=r"[c$xy]"
  print(re.findall(str1,strr))
  ```

  输出：['c', 'x', 'y', '$']

  ==元字符$在类[]中不起作用==

  ---

---

### 匹配区号号码

+ 匹配任意一个空格隔开的带区号的电话号码

  ```python
  str1 = "\d{3}\s\d{3,8}"
  ```

+ 匹配任意一个以‘-’隔开的带区号的电话号码

  ```python
  str1 = "\d{3}\-\d{3,8}"
  ```

  由于‘-’是特殊字符，需要用‘\’转义

+ 匹配‘010 - 123456’这样的号码

  ```python
  str1 = "\d{3}[\s\-]+\d{3,8}"
  ```

---

### 转义的问题

+ python 提供re的模块包含所有正则表达式的功能

+ 由于Python的字符串本身也用\转义，所以需要注意

  ```python
  s = 'ABC\-001'
  s1 = 'ABC\\-001'
  print(s)
  print(s1)
  ```

  ```python
  ABC\-001
  ABC\-001
  ```

+ 因此建议使用python 的 r 前缀，就不用考虑转义的问题

  ```python
  s = r'ABC\-001'
  s1 = r'ABC\\-001'
  print(s)
  print(s1)
  ```

  ```
  ABC\-001
  ABC\\-001
  ```

---

### 切分字符串

+ 正则表达式切分字符串比用固定的字符更灵活

  ```python
  import re
  s = 'a b   c'.split(" ")
  print(s)
  s1 = re.split(r'\s+', 'a b   c')
  print(s1)
  ```

  ```python
  ['a', 'b', '', '', 'c']
  ['a', 'b', 'c']
  ```

+ ```python
  import re
  s2 = re.split(r'[\s\,\;]+', 'a b,c   d;   ; e')
  print(s2)
  ```

  ```python
  ['a', 'b', 'c', 'd', 'e']
  ```

---

### 分组

+ 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用`()`表示的就是要提取的分组（Group）

  比如：‘^(\d{3})-(\d{3,8})$’分别定义了两个组，可以直接从匹配的字符串猴子那个提取出区号和本地号码

  ```python
  import re
  m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
  print(m)
  print(m.groups())
  print(m.group(0))
  print(m.group(1))
  print(m.group(2))
  ```

  ```python
  <re.Match object; span=(0, 10), match='010-123456'>
  ('010', '123456')
  010-123456
  010
  123456
  ```

  注：group(0)永远是原始字符串，group(1),group(2),...表示第1,2,...个字符串

+ 识别合法时间

  ```python
  import re
  t = '19:05:30'
  m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
  print(m.groups())
  ```

  ```
  ('19', '05', '30')
  ```

+ 但是有些时候，用正则表达式也无法做到完全验证，比如识别日期：

  ```python
  '^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
  ```

  对于`'2-30'`，`'4-31'`这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

+ 关闭捕获

  ```python
  (?:)
  ```

  括号在正则表达式中创建一个“捕获”组，但如果对分组内容并不感兴趣，可以使用?:关闭分组的捕获

---

### 贪婪匹配

+ 最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

+ 举例如下，匹配出数字后面的`0`：

  ```python
  >>> re.match(r'^(\d+)(0*)$', '102300').groups()
  ('102300', '')
  ```

  由于`\d+`采用贪婪匹配，直接把后面的`0`全部匹配了，结果`0*`只能匹配空字符串了。

  必须让`\d+`采用非贪婪匹配（也就是尽可能少匹配），才能把后面的`0`匹配出来，加个`?`就可以让`\d+`采用非贪婪匹配：

  ```python
  >>> re.match(r'^(\d+?)(0*)$', '102300').groups()
  ('1023', '00')
  ```

+ ==加了‘？’变成非贪婪匹配模式。但是如果后面还有匹配字符，就无法实现非贪婪匹配==

  ==非贪婪模式即只匹配符合条件的最少字符==

---

### 编译

+ 当我们在Python中使用正则表达式时，re模块内部会干两件事情：

  + 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
  + 用编译后的正则表达式去匹配字符串。

+ 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

  ```python
  import re
  re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
  m = re_telephone.match('010-123456')
  print(m.groups())
  ```

  ```python
  ('010', '123456')
  ```

---

### 一个验证Email地址的正则表达式

+ 版本1应该可以验证出类似的Email:

  + someone@gmail.com
  + bill.gates@microsoft.com

  ```python
  import re
  def is_valid_email(addr):
      m = re.match(r'^([\w\.]+)@([\w\.]+)$', addr)
      return m
  assert is_valid_email('someone@gmail.com')
  assert is_valid_email('bill.gates@microsoft.com')
  assert not is_valid_email('bob#example.com')
  assert not is_valid_email('mr-bob@example.com')
  print('ok')
  ```

  ```python
  def is_valid_email(addr):
      re_email = re.compile(r'([a-z\.]+@[a-z]+).(com)$')
      return re_email.match(addr)
  ```

+ 版本二可以提取出带名字的Email地址：

  - <Tom Paris> tom@voyager.org => Tom Paris
  - bob@example.com => bob

  ```python
  import re
  def name_of_email(addr):
      m = re.match(r'(<[\w\s]+>)?\s*([\w\.]+)@[\w\.]+$', addr)
      if m.group(1):
          return str(re.split(r'[<>]', m.group(1))[1])
      elif m.group(2):
          return m.group(2)
      else:
          return None
  assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
  assert name_of_email('tom@voyager.org') == 'tom'
  print('ok')
  ```

  ```python
  import re
  def name_of_email(addr):
      re_email= re.compile(r'\<*([a-zA-Z\s+]+)\>*[a-zA-Z\s]*@([a-z]+).(com|org)')
      return re_email.match(addr).group(1)
  assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
  assert name_of_email('tom@voyager.org') == 'tom'
  print('ok')
  ```

  

