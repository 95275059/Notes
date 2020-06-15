# Python笔记7--python编码格式

1. Python编码格式

   + 文本文件存储的内容是基于字符编码的文件，常见的编码有ASCII编码和UNICODE编码等。

   + python3

     默认是UTF-8，或者说是Unicode编码

     + UTF-8

       UTF-8是Unicode的一种编码方式，主要作用于对Unicode码的数据进行转换，转换后方便存储和网络传输

     + python3内存中使用的字符串全部是Unicode码
     + **网络传输的数据或者从磁盘读取的数据是把Unicode码转换过的数据，通常情况下是UTF-8数据**
     + **如果从网络中读取或者从磁盘中读取，其实就是把UTF-8格式的数据解码成Unicode码数据**
     + 如果想把内存中的Unicode码数据存储到磁盘或者网络中需要对Unicode码进行编码，通常可以采用UTF-8的形式进行编码

   + python2

     + python2默认使用ASCII编码格式

2. ASCII

   + 计算机中只有256个ASCII字符

   + 一个ASCII在内存中占用**一个字节**的空间

     + 8个0/1的排列组合方式共256中

   + ASCII表

     ![笔记7-1](E:\Notes\Python\笔记7-1.png)

3. UTF-8

   + 计算机中使用**1-6个字节**来表示一个UTF-8字符，涵盖了地球上几乎所有地区的文字
   + 大多数汉字使用3个字节表示
   + UTF-8是Unicode编码的一种编码格式

4. python2中使用中文

   + 在python2文件的第一行增加以下代码

     + 方式一

       ```python
       # *-* coding:utf8 *-*
       ```

     + 方式二

       ```python
       # coding=utf8
       ```

   + u“***”

     + 在python2中即使指定了文件使用UTF-8的编码格式，但是在便利字符串时，仍然会**以字节为单位遍历字符串**

     + 要能够正确的遍历字符串，在定义字符串时，需要在字符串的引号前，增加小写字母u，告诉解释器这是一个Unicode字符串（使用UTF-8编码格式的字符串）

     + 实例

       ```python
       # *-* coding:utf8 *-*
        
       # 在字符串前，增加一个 `u` 表示这个字符串是一个 utf8 字符串
       hello_str = u"你好世界"
        
       print(hello_str)
        
       for c in hello_str:
           print(c)
       ```

       

     

   

   