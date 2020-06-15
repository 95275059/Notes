# Python笔记2--正则表达式字符匹配规则

就其本质而言，正则表达式（或 RE）是一种小型的、高度专业化的编程语言，它内嵌在Python中，并通过 re 模块实现。

正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行。

1. 普通字符

   大多数字符和字母都会和自身匹配

2. 元字符

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
   | \|     |                                                              |
   | []     | 匹配字符的类别，**元字符在类别中不起作用**                   |
   | ()     | 把括号内字符作为一个整体去处理                               |

   | 元字符 | 说明                                                         |
   | ------ | ------------------------------------------------------------ |
   | \d     | 匹配任何十进制数，相当于类[0-9]                              |
   | \D     | 匹配任何非数字字符，相当于类\[^0-9]                          |
   | \s     | 匹配任何空白字符，相当于类[\t\n\r\f\v]                       |
   | \S     | 匹配任何非空白字符，相当于类\[^\t\n\r\f\v]                   |
   | \w     | 匹配任何字母数字下划线和汉字字符（匹配非特殊字符），相当于类[a-zA-Z0-9_] |
   | \W     | 匹配任何的特殊字符，相当于类\[^a-zA-Z0-9_]                   |
   | \b     | 匹配一个单词边界，也就是指单词和空格间的位置                 |

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
     strr=ttest cxy_9527"
     str1=r"(te)*"    
     print(re.findall(str1,strr))
     ```
   
     输出：['', 'te', '', '', '', '', '', '', '', '', '', '', '', '']
   
     #te作为整体进行匹配
   
     if(t和第一个字符匹配)
   
     ​	if(e和第二个字符匹配)
   
     ​		输出匹配项
   
     ​	else
   
     ​		输出‘’
   
     else
   
     ​	输出‘’
   
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
   
     
   
   

