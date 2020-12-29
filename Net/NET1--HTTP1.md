# NET1--HTTP1

1. HTTP简介

   HTTP协议是Hyper Text Transfer Protocol(超文本传输协议)的缩写。用于从万维网服务器传输超文本到本地浏览器的传送协议

   HTTP是一个基于TCP/IP通信协议来传递数据(HTML文件，图片文件，查询结果等)的传送协议

2. HTTP工作原理

   + HTTP是无连接的：限制每次连接只处理一个请求。服务器处理完客户的请求，并受到客户的应答后，即断开连接。这种方式可以节省传输时间
   + HTTP是媒体独立的：只要客户端和服务器知道如何处理数据内容，任何类型的数据都可以通过HTTP发送。客户端以及服务器指定使用适合的MIME-type内容类型。

   + HTTP是无状态的：无状态是指协议对于事物处理没有记忆能力。

     意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大

     另一方面，在服务器不需要先前信息时它的应答就比较快。

3. HTTP消息结构

   ![1-1](E:\notes\Net\1-1.png)

   + 请求行

     例：GET /index.html HTTP/1.1

     + 请求方法：

       + HTTP1.0定义了三种请求方法：GET,POST,HEAD
       + HTTP1.1新增了五种请求方法：OPTIONS,PUT,DELETE,TRACE,CONNECT

       | 请求方法   | 描述                                                         |
       | ---------- | ------------------------------------------------------------ |
       | **GET**    | 请求指定的页面信息，并返回实体主题                           |
       | HEAD       | 类似于GET请求，只不过返回的相应中没有具体的内容，用于获取报头 |
       | **POST**   | 向指定资源提交数据进行处理请求（如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立或已有资源的修改 |
       | **PUT**    | 从客户端向服务器传送的数据取代指定的文档的内容               |
       | **DELETE** | 请求服务器删除指定的页面                                     |
       | CONNECT    | HTTP/1.1协议中预留该能够将连接改为管道方式的代理服务器       |
       | OPTIONS    | 允许客户端查看服务器的性能                                   |
       | TRACE      | 回显服务器收到的请求，主要用于测试或诊断                     |

     + GET

       + 最常见的一种请求方式

       + GET方法要求服务器将URL定位的资源放在响应报文的数据部分，回送给客户端。

       + 请求参数和对应的值附加在URL后面，利用一个问号“?”代表URL的结尾与请求参数的开始，传递参数 长度受限制。各个数据之间用“&”符号隔开

       + 地址的字符限制根据不同浏览器有所不同，一般最多只能识别1024个字符。

       + GET方式的请求一般不包含请求内容（请求数据）部分，请求数据以地址的形式表现在请求行。

       + GET方式不适合传送私密数据和传送大量数据。

       + GET提交，请求的数据会附在URL之后（就是把数据放置在HTTP协议头＜request-line＞中），以?分割URL和传输数据，多个参数用&连接;例如：login.action?name=hyddd&password=idontknow&verify=%E4%BD%A0 %E5%A5%BD。如果数据是英文字母/数字，原样发送，如果是空格，转换为+，如果是中文/其他字符，则直接把字符串用BASE64加密，得出如： %E4%BD%A0%E5%A5%BD，其中％XX中的XX为该符号以16进制表示的ASCII。

     + POST

       POST方法将请求参数封装在HTTP请求数据中，因此可以传输大量数据

       POST方式对传送的数据大小没有限制，而且也不会显示在URL中。

       POST方式的请求行中不包含数据字符串，这些数据保存在请求数据部分，各个数据之间也是使用“&”符号隔开。

     + HEAD

       HEAD类似于GET，但是服务器接收到HEAD请求后，只返回响应头，不会发送响应内容。

       当我们只需要查看某个页面的状态时，使用HEAD比较好。

   + 请求头

     请求头部由关键字/值 对组成，每行一对，关键字和值用英文冒号“:”分隔。

     请求头部通知服务器有关客户端请求的信息。

     对于POST请求来说 Content-Length必须出现。

     典型的请求头有：

     + User-Agent：包含发出请求的用户信息。

       浏览器类型，如果Servlet返回的内容与浏览器类型有关则该值非常有用。

     + ACCEPT：浏览器可接受的MIME类型。

     + Host：请求的主机名，允许多个域名同处一个IP地址，即虚拟主机。

       客户机通过这个头告诉服务器，想访问的主机名。对应URL中Web名称和端口号，用于指定被请求资源的internet主机和端口号

       HTTP/1.1请求必须包含主机头域，否则[系统](https://www.2cto.com/os/)会以400状态码返回。

     + Accept-Charset：浏览器可接受的字符集。

     + Accept-Encoding：浏览器能够进行解码的数据编码方式，比如gzip。

       Servlet能够向支持gzip的浏览器返回经gzip编码的HTML页面。许多情形下这可以减少5到10倍的下载时间。

     + Accept-Language：浏览器所希望的语言种类，当服务器能够提供一种以上的语言版本时要用到。

     + Authorization：授权信息，通常出现在对服务器发送的WWW-Authenticate头的应答中。

     + Content-Length：表示请求消息正文的长度。

     + If-Modified-Since：客户机通过这个头告诉服务器，资源的缓存时间。只有当所请求的内容在指定的时间后又经过修改才返回它，否则返回304“Not Modified”应答。

     + Referer：客户机通过这个头告诉服务器，它是从哪个资源来访问服务器的(防盗链)。包含一个URL，用户从该URL代表的页面出发访问当前请求的页面。

     + Cookie：客户机通过这个头可以向服务器带数据，这是最重要的请求头信息之一。

     + Pragma：指定“no-cache”值表示服务器必须返回一个刷新后的文档，即使它是代理服务器而且已经有了页面的本地拷贝。

     + From：请求发送者的email地址，由一些特殊的Web客户程序使用，浏览器不会用到它。

     + Connection：处理完这次请求后是否断开连接还是继续保持连接。

       如果Servlet看到这里的值为“Keep- Alive”，或者看到请求使用的是HTTP 1.1(HTTP 1.1默认进行持久连接)，它就可以利用持久连接的优点，当页面包含多个元素时(例如Applet，图片)，显著地减少下载所需要的时间。要实现这一点，Servlet需要在应答中发送一个Content-Length头，最简单的实现方法是：先把内容写入 ByteArrayOutputStream，然后在正式写出内容之前计算它的大小。

     + Range：Range头域可以请求实体的一个或者多个子范围。

       表示头500个字节：bytes=0-499

       表示第二个500字节：bytes=500-999

       表示最后500个字节：bytes=-500

       表示500字节以后的范围：bytes=500-

       第一个和最后一个字节：bytes=0-0,-1

       同时指定几个范围：bytes=500-600,601-999

       但是服务器可以忽略此请求头，如果无条件GET包含Range请求头，响应会以状态码206(PartialContent)返回而不是以200 (OK)。

     + UA-Pixels，UA-Color，UA-OS，UA-CPU：由某些版本的IE浏览器所发送的非标准的请求头，表示屏幕大小、颜色深度、操作系统和CPU类型。

   + 空行

     最后一个请求头之后是一个空行，发送回车符和换行符，通知服务器以下不再有请求头

   + 请求数据

     请求数据不在GET方法中使用，而在POST方法中使用。

     POST方法适用于需要客户填写表单的场合。

     与请求数据相关的最常使用的请求头是Content-Type和Content-Length

4. GET请求实例

   ```
   //请求首行
   
   GET /search?hl=zh-CN&source=hp&q=domety&aq=f&oq= HTTP/1.1
   
   //请求头信息，因为GET请求没有正文
   
   Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint,   
   application/msword, application/x-silverlight, application/x-shockwave-flash, */*
   
   Referer: <a href="http://www.google.cn/">http://www.google.cn/</a> 
   
   Accept-Language: zh-cn 
   
   Accept-Encoding: gzip, deflate
   
   User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld) 
   
   Host: <a href="http://www.google.cn">www.google.cn</a>
   
   Connection: Keep-Alive 
   
   Cookie: PREF=ID=80a06da87be9ae3c:U=f7167333e2c3b714:NW=1:TM=1261551909:LM=1261551917:S=ybYcq2wpfefs4V9g;
   NID=31=ojj8d-IygaEtSxLgaJmqSjVhCspkviJrB6omjamNrSm8lZhKy_yMfO2M4QMRKcH1g0iQv9u-2hfBW7bUFwVh7pGaRUb0RnHcJU37y-  
   FxlRugatx63JLv7CWMD6UB_O_r
   
   //空行
   
   //因为GET没有正文，所以下面为空
   ```

5. POST请求实例

   ```
   // 请求首行
   
   POST /search HTTP/1.1 
   
   //请求头信息
   
   Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint,   
   application/msword, application/x-silverlight, application/x-shockwave-flash, */* 
   
   Referer: <a href="http://www.google.cn/">http://www.google.cn/</a>   
   
   Accept-Language: zh-cn   
   
   Accept-Encoding: gzip, deflate  
   
   User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)    
   
   Host: <a href="http://www.google.cn">www.google.cn</a> 
   
   Connection: Keep-Alive 
   
   Cookie: PREF=ID=80a06da87be9ae3c:U=f7167333e2c3b714:NW=1:TM=1261551909:LM=1261551917:S=ybYcq2wpfefs4V9g;   
   NID=31=ojj8d-IygaEtSxLgaJmqSjVhCspkviJrB6omjamNrSm8lZhKy_yMfO2M4QMRKcH1g0iQv9u-2hfBW7bUFwVh7pGaRUb0RnHcJU37y-  
   FxlRugatx63JLv7CWMD6UB_O_r 
   
   // 这里是空行
   
   //POST有请求正文
   
   hl=zh-CN&source=hp&q=domety  
   ```

6. HTTP响应消息

   HTTP响应由三部分组成：状态行、响应头、空行、响应正文

   ![1-2](E:\notes\Net\1-2.jpg)

   + 状态行（status line）

     + 格式

       HTTP-Version   Status-Code   Reason-Phrase   CRLF

     +  HTTP-Version：服务器HTTP协议的版本

     + Status-Code：服务器发回的响应状态代码

       状态码由三位数字组成，第一个数字定义了响应的类别，由五种可能取值

       | 状态码 | 说明                                       |
       | ------ | ------------------------------------------ |
       | 1xx    | 指示信息--表示请求已接收，继续处理。       |
       | 2xx    | 成功--表示请求已被成功接收、理解、接受。   |
       | 3xx    | 重定向--要完成请求必须进行更进一步的操作。 |
       | 4xx    | 客户端错误--请求有语法错误或请求无法实现。 |
       | 5xx    | 服务器端错误--服务器未能实现合法的请求。   |

       常见状态码

       | 状态码                    | 状态描述                                                     |
       | ------------------------- | ------------------------------------------------------------ |
       | 200 OK                    | 客户端请求成功。                                             |
       | 400 Bad Request           | 客户端请求有语法错误，不能被服务器所理解。                   |
       | 401 Unauthorized          | 请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用。 |
       | 403 Forbidden             | 服务器收到请求，但是拒绝提供服务。                           |
       | 404 Not Found             | 请求资源不存在，举个例子：输入了错误的URL。                  |
       | 500 Internal Server Error | 服务器发生不可预期的错误。                                   |
       | 503 Server Unavailable    | 服务器当前不能处理客户端的请求，一段时间后可能恢复正常，举个例子：HTTP/1.1 200 OK（CRLF）。 |

     + Reason-Phrase：状态代码的文本描述

   

   

   

   

   



