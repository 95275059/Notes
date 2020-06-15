---
title: Python操作XML文件--XML概述
date: 2019-04-10 15:20:29
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89183399](https://blog.csdn.net/zhaandzha/article/details/89183399)   
    
   XML：可扩展标置语言，为HTML（超文本标置语言）的补充。HTML用于显示数据，而XML用于传输和存储数据

 一.XML语法

 XML文件通常分为两部分：文件声明和文件主体

 =>文件声明：位于第一行

 <?xml version="1.0" encoding="utf-8"?>

 =>version标明此文件所用的标准的版本号，必须要有

 =>encoding标明此文件中所使用的字符类型，可以省略；省略时后面的字符码必须是Unincode字符码（建议不省略）

 =>文件主体

 =>必须有根元素

 =>标签对大小写敏感

 =>属性

 应尽量避免使用属性，因为属性难以阅读和维护，尽量使用元素来描述数据，仅使用属性来提供与数据无关的信息。

 =>元数据(有关数据的数据,如id)应当存储为属性，而数据本身应存储为元素

 属性值必须加“”或者‘’。当属性值含有“”时，用‘’；当属性值含有‘’时，用“”；当属性值既含有‘’又含有“”时，用实体字符

 =>&lt 小于(<) =>&gt 大于(>) =>&amp 和号(&) =>&apos 单引号(') =>&quot 引号(")

 =>注释

 <!--注释内容-->

 =>空格

 HTML中会把多个连续空格字符合并为一个；但XML不会

 =>换行

 windows应用程序中，换行通常以一对字符来存储：回车符(CR)和换行符(LF)

 XML以LF存储换行

 二.DOM(Document Object Model，文档对象模型)

 DOM以树状的层次结构存储XML文档中的数据，每个结点都是一个相应对象。

 DOM解析器在任何处理任务开始之前，必须把基于XML文件生成的树状数据放在内存，所以DOM解析器的内存使用量完全根据XML文件的大小来决定。=>占用内存大，解析和加载整个文档可能很慢且很耗资源

 三.SAX(simple API for XML)

 SAX是事件驱动（基于回溯机制的程序运行方法）的，牺牲了便捷性来换取速度和内存占用。不需要一次性读入整个文档，而文档的读入过程就是SAX的解析过程，即逐行扫描文档，边扫描边解析。

 四.ElementTree

 ET的性能与SAX模块大致相仿，但它的API更加高层次，用户使用起来更加便捷。

 

 

 

 

 

 

 

 

   
 