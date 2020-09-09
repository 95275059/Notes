## Python笔记4--字符串方法总结

1. str.rjust

   + 功能
   
     rjust()返回一个原字符串右对齐，并使用个空格填充至长度到width的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
   
   + 语法
   
     str.rjust(width[,fillchar])
   
     + width:指定填充指定字符后字符串的总长度
     + fillchar:填充的字符，默认为空格
     
   + 例子
   
     ```python
     s='123'
     print(s.rjust(6,'0'))
     #000123
     ```
   
   ---
   
2. str.join()

   + 功能

     将**序列(list)**中的元素以指定的字符连接成一个新的字符串并返回

   + 语法

     str.join(sequence)

     + sequence : 要连接的元素序列

   + 例子

     ```python
     str = "-"
     seq = ("a", "b", "c") # 字符串序列
     print(str.join(seq))
     #a-b-c
     ```

   ---

3. str.maketrans()

   - 功能

     用于创建字符映射的转换表

   - 语法

     ```python
     str.maketrans(intab,outtab)
     ```

     - intab : 字符串中要替代的字符组成的字符串
     - outtab : 相应的映射字符的字符串
     - 返回值：返回字符串转换后生成的新字符串

   - 实例

     ```python
     intab = "aeiou"
     outtab = "12345"
     trantab = str.maketrans(intab, outtab)
     
     strr = "this is string example....wow!!!"
     print(strr.translate(trantab))
     #th3s 3s str3ng 2x1mpl2....w4w!!!
     ```

     注意：python3不需要import string

   ---

4. str.translate()

   + 功能

     根据参数table给出的表（包含256个字符）转换字符串的字符，要过滤掉的字符防盗deletechars参数中

   + 语法

     ```python
     str.translate(table)
     bytes.translate(table[,delete])
     bytearray.translate(table[,delete])
     ```

     + table : 翻译表，翻译表是通过maketrans()方法转换而来
     + delete : 字符串中要过滤的字符列表
     + 返回值 ：返回翻译后的字符串，若给出了delete参数，则将原来的bytes中的属于delete的字符删除，剩下的字符按照table中给出的映射来进行映射

   + 实例

     ```python
     bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
     print(b'runoob'.translate(bytes_tabtrans, b'o'))
     #b'RUNB'
     ```

   ---

5. str.encode

   + 功能

     以encoding指定的编码格式编码字符串。

   + 语法

     ```python
     str.encode(encoding='UTF-8',errors='strict')
     ```

     + encoding : 指定编码格式
     + errors : 设置不同错误的处理方案
       + 默认为'strict'，意为编码错误引起一个UnicodeError。
       + 其他可能的值有'ignore','replace','xmlcharrefreplace','backslashreplace'，以及通过codecs.register_error()注册的任何值
     + 返回值 : 返回编码后的字符串

   + 实例

     ```python
     str = "this is string example....wow!!!";
     print("Encoded String: ")
     print(str.encode('UTF-8','strict'))
     ```

     ```python
     Output:
     Encoded String: 
     b'this is string example....wow!!!'
     ```

   ---

6. str.decode

   + 功能

     以encoding指定的编码格式解码字符串

     默认编码为字符串编码

   + 语法

     ```python
     str.decode(encoding='UTF-8',error='strict')
     ```

     + encoding : 要使用的编码
     + errors : 设置不同错误的处理方案
       + 默认为'strict'，意为编码错误引起一个UnicodeError。
       + 其他可能的值有'ignore','replace','xmlcharrefreplace','backslashreplace'，以及通过codecs.register_error()注册的任何值
     + 返回值 : 返回解码后的字符串

   + 实例

     ```python
     str = "this is string example....wow!!!"
     str = str.encode('UTF-8', 'strict')
     print("Encoded String: ")
     print(str)
     print("Decoded String: \n" + str.decode('UTF-8', 'strict'))
     ```

     ```python
     output:
     Encoded String: 
     b'this is string example....wow!!!'
     Decoded String: 
     this is string example....wow!!!
     ```

   ---

7. str.count()

   + 功能

     用于统计字符串里某个字符出现的次数

     可选参数为在字符串搜索的开始与结束位置

   + 语法

     ```python
     str.count(sub,start=0,end=len(string))
     ```

     + sub : 搜索的子字符串
     + start : 字符串开始搜索的位置。默认为第一个字符，**第一个字符索引值为0**
     + end : 字符串中结束搜索的位置。默认为字符串的最后一个位置
     + 返回值 : 该方法返回子字符串在字符串中出现的次数

   + 实例

     ```python
     str = "this is string example....wow!!!";
     sub = "i";
     print("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
     sub = "wow";
     print("str.count(sub) : ", str.count(sub))
     ```

     + output

       ```
       str.count(sub, 4, 40) :  2
       str.count(sub) :  1
       ```

   ---

8. str.split

   + 功能

     通过制定分隔符对字符串进行切片

   + 语法

     ```python
     str.split(str=" ",num=string.count(str))
     ```

     + str : 分隔符。默认为所有的空字符，包括空格、换行（\n）、制表符（\t）等
     + num : 分割次数。默认为-1，即分割所有。如果num有指定值，则分割为num+1个子字符串
     + 返回值 : 返回分割后的字符串**列表**

   + 实例

     ```python
     str = "this is string example....wow!!!"
     print (str.split( ))       # 以空格为分隔符
     print (str.split('i',1))   # 以 i 为分隔符
     print (str.split('w'))     # 以 w 为分隔符
     print("'network1','network2','network'".split("'"))
     ```

     + output

       ```
       ['this', 'is', 'string', 'example....wow!!!']
       ['th', 's is string example....wow!!!']
       ['this is string example....', 'o', '!!!']
       ['', 'network1', ',', 'network2', ',', 'network', '']
       ```

   ---

9. str.find()

   + 功能

     + 检测字符串中是否包含子字符串str

     + 如果指定beg(开始)和end（结束）范围，则检查是否包含在指定范围内

   + 语法

     ```python
     string.find(str,beg=0,end=len(string))
     ```

     + str : 指定检索的字符串
     + beg : 开始索引；默认为0
     + end : 结束索引；默认为字符串的长度
     + 返回值 : 如果包含子字符串，返回开始的索引值；否则返回-1
     + 注：索引值从0开始

   + 实例

     ```python
     str1 = "this is string example....wow!!!";
     str2 = "exam";
     
     print(str1.find(str2))
     print(str1.find(str2, 10))
     print(str1.find(str2, 40))
     ```

     + output

       ```
       15
       15
       -1
       ```

   ---

10. str.strip()

    + 功能

      用于移除字符串头尾指定的字符（默认为**空格**或**换行符**）或字符序列

    + 语法

      ```python
      str.strip([chars])
      ```

      + chars：移除字符串头尾指定的字符序列
      + 返回值：返回移除字符串头尾指定的字符生成的新字符串

    + 实例

      ```python
      #!/usr/bin/python
      # -*- coding: UTF-8 -*-
      
      str = "00000003210Runoob01230000000"
      # 去除首尾字符 0
      print(str.strip('0'))
      
      # 去除首尾空格
      str2 = "   Runoob      "
      print(str2.strip())
      
      #去除首尾字符包含指定字符序列中的字符
      # 字符序列为 12
      str = "123abcrunoob321"
      print(str.strip('12'))
      ```

      + 输出

        ```python
        3210Runoob0123
        Runoob
        3abcrunoob3
        ```

      

      










