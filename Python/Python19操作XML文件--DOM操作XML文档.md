---
title: Python操作XML文件--DOM操作XML文档
date: 2019-04-10 16:56:44
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89186646](https://blog.csdn.net/zhaandzha/article/details/89186646)   
    
   一.使用DOM访问XML文件

 使用xml.dom.minidom来读取和访问XML文件；xml.dom.minidom是DOM的简化实现版本，比完整版的DOM简单的多，且这个模块也小的多

 在使用时需要导入minidom：import xml.dom.minidom

 (1).得到DOM对象

 dom=xml.dom.minidom.parse(xml文件路径/文件名)

 (2).得到文档元素对象(根元素)

 root=dom.documentElement

 (3).结点属性

 结点有三种属性：nodeName,nodeValue,nodeType

 root.nodeName:返回结点名字

 root.nodeValue:返回结点的值，只对文本结点有效

 root.nodeType:返回结点的类型

 =>属性结点：ATTRIBUTE_NODE =>注释结点：COMMENT_NODE =>元素结点：ELEMENT_NODE

 =>实体结点：ENTITY_NODE =>文本结点：TEXT_NODE

 (4).子元素(子节点)的访问

 root.getElementsByTagName('element')：得到元素名为element的结点；返回一个列表

 root.childNodes：得到某元素下所有子结点；元素标记间的内容都被视为文本结点。每行后面的回车，也都被看成文本结点。 

 node.data:得到文本结点的文本内容

 (5).XML形式输出:root.toxml()

 例：

 employee.xml:

 
```
 <?xml version="1.0" encoding="utf-8" ?>
<employees>
    <employee id="1001">
        <name>cxy</name>
        <age>21</age>
    </employee>
    <employee id="1002">
        <name>CXY</name>
        <age>31</age>
    </employee>
</employees>
```
 test.py:

 
```
 import xml.dom.minidom
def TestMinDom():
    doc=xml.dom.minidom.parse("employees.xml")    #dom对象

    root=doc.documentElement
    print(root.childNodes)       #输出根结点下所有子节点
    employees=root.getElementsByTagName("employee")
    #获得所有<employee>子元素
    for employee in employees:
        print(employee.nodeName,"---1")
        #遍历输出子元素
        for item in employee.childNodes:
            if item.nodeType==doc.ELEMENT_NODE:
                print(item.nodeName,"---2",end=":")
                for node in item.childNodes:
                    if node.nodeType==doc.TEXT_NODE:
                        print(node.data)

TestMinDom()


```
 结果：

 
```
 [<DOM Text node "'\n    '">, <DOM Element: employee at 0x1d67bf4c178>, <DOM Text node "'\n    '">, <DOM Element: employee at 0x1d67bf4c340>, <DOM Text node "'\n'">]
employee ---1
name ---2:cxy
age ---2:21
employee ---1
name ---2:CXY
age ---2:31
```
 注：root.childNode:会返回元素root两个标记间的所有内容，包括回车空格部分（视为文本结点）

 所以需要需要if判断截取需要的类型的子节点

 二.使用DOM添加新结点

 生成文本结点:text=dom.createTextNode(文本内容)

 文本内容若出现‘<’,'&'需要转换为相应的实体符号

 生成元素结点:item=dom.createElement(元素名)

 将子结点添加到元素结点中:item.appendChild(子结点)

 在item的子结点refchild前插入一个新的结点newchild:item.insertBefore(newNode,refchild)

 向元素item中添加属性:item.setAttribute(属性名，属性值)

 例：向book.xml中增加一本书

 book.xml

 
```
 <?xml version="1.0" encoding="UTF-8"?><!--book.xml--><图书信息表>
    <图书 书号="ISBN-7505407171">
        <书名>西游记</书名>
        <作者>吴承恩</作者>
    </图书>
    <图书 书号="ISBN-97873021495873">
        <书名>XML技术应用</书名>
        <作者>XXX</作者>
        <价格>35</价格>
    </图书>
</图书信息表>
```
 test.py:

 
```
 import xml.dom.minidom
def TestAddElement():
    doc = xml.dom.minidom.parse("book.xml")
    root = doc.documentElement
    item = doc.createElement("图书")
    item1 = doc.createElement("书名")
    text = doc.createTextNode("Python入门帮助")
    item1.appendChild(text)
    item2 = doc.createElement("作者")
    text = doc.createTextNode("陈锐")
    item2.appendChild(text)
    item3 = doc.createElement("价格")
    text = doc.createTextNode("42.5")
    item3.appendChild(text)
    text=doc.createTextNode("\n        ")
    item.appendChild(text)
    item.appendChild(item1)
    text = doc.createTextNode("\n        ")
    item.appendChild(text)
    item.appendChild(item2)
    text = doc.createTextNode("\n        ")
    item.appendChild(text)
    item.appendChild(item3)
    text = doc.createTextNode("\n    ")
    item.appendChild(text)

    text=doc.createTextNode("    ")
    root.appendChild(text)
    root.appendChild(item)
    text = doc.createTextNode("\n")
    root.appendChild(text)
    print(root.toxml())
    return doc

dom=TestAddElement()

try:
    with open('book.xml','w',encoding='UTF-8') as fh:
        #dom.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        dom.writexml(fh, indent='',addindent='',newl='',encoding='UTF-8')
        print('写入xml OK!')
except Exception as err:
    print('错误信息：{0}'.format(err))
```
 三.使用DOM修改删除结点

 从元素element中删除子元素childNode：element.removeChild(childNode)

 将元素element中子结点oldNode替换为新的结点newNode:element.replaceChild(newNode,oldNode)

 修改某元素element的属性:element.s

 etAttribute(属性名，属性值)

 例：将第二个图书元素作者改为“朱猪猪”

 删除第一个图书元素

 
```
 import xml.dom.minidom
def TestDelElement():
    doc=xml.dom.minidom.parse("book.xml")
    root=doc.documentElement
    item=doc.getElementsByTagName("图书")
    book=item[1]
    oldauthor=book.getElementsByTagName("作者")[0]
    newauthor=doc.createElement("作者")
    text=doc.createTextNode("朱猪猪")
    newauthor.appendChild(text)
    book.replaceChild(newauthor,oldauthor)
    root.removeChild(item[0])
    print(root.toxml())
    return doc

dom=TestDelElement()
try:
    with open('book.xml','w',encoding='UTF-8') as fh:
        #dom.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        dom.writexml(fh, indent='',addindent='',newl='',encoding='UTF-8')
        print('写入xml OK!')
except Exception as err:
    print('错误信息：{0}'.format(err))

```
 四.生成DOM对象树并写入到XML文件中

 DOM对象树生成后，可以调用DOM的writexml()方法将内容写入文件中。

 dom.writexml(writer,indent,addindent,newl,encoding)

 =>writer:文件对象

 =>indent:是每个tag前填充的字符，如“ ”表示每个tag前有四个空格

 =>addindent:是每个子结点的缩进字符

 =>newl:是每个tag后填充的字符，如“\n”表示每个tag后面有一个回车

 =>encoding:是生成的XML信息头中的encoding属性值，在输出时minidom并不真正进行编码的处理。

 若保存的文本内容有汉字，则需要进行编码转换

 writexml()方法除了writer参数必须要有外，其余可以省略

 
```
 dom=TestAddElement()
f=open("text.xml","w")
dom.writexml(f,encoding="utf-8")
f.close()
```
 

 

   
 