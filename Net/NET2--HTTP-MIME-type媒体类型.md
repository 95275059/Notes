# NET2--HTTP2-MIME-type媒体类型

1. MIME-type功能

   MIME--多功能网际邮件扩充协议

   帮助浏览器区分HTML，XML，GIF，FLASH等多种类型的数据内容，并决定用相对应的形式显示

2. 实现

   + 在把输出结果传送到浏览器上的时候，浏览器必须启动适当的应用程序来处理这个输出文档。

   + MIME-type通常通过HTTP协议，由Web服务器告知浏览器，更准确地说，是通过Content-Type header来表示的。

   + 由于MIME类型与文档的后缀相关，因此服务器使用文档的后缀来区分不同文件的MIME类型。服务器中必须定义文档后缀和MIME类型之间的对应关系。而客户程序从服务器上接收数据的时候，只是从服务器接收数据流，并不了解文档的名字。因此服务器必须使用附加信息来告诉客户程序数据的MIME类型。服务器在发送真正的数据之前，就要先发送标志数据的MIME类型的信息，这个信息使用Content-type关键字进行定义。

     + 例如，对于HTML文档，服务器首先发送以下两行MIME标识信息，这个标识并不是真正的数据文件的一部分：

       Content-type:text/html

       注：第二行为一个空行，使用这个空行的目的是将MIME信息与真正的数据内容分隔开

3. 命名格式

   + 通常只有一些在互联网上获得广泛应用的格式才会获得一个MIME Type，如果是某个客户端自己定义的格式，一般只能以application/x-开头

   + 处理本地的文件，在没有人告诉浏览器某个文件的MIME-type的情况下，浏览器也会做一些默认处理，这可能和主机操作系统中给文件配置的MIME type有关。

     例如在Windows下，打开注册表的"HKEY_LOCAL_MACHINE/SOFTWARE/Classes/MIME/Database/Content Type"，可以看到所有MIME type的配置信息

4. 常见的MIME类型

   超文本标记语言文本：.html   text/html

   普通文本：.txt   text/plain

   RTF文本：.rtf   application/rtf

   GIF图形：.gif   image/gif

   JPEG图形：.jpeg/.jpg   image/jpeg

   au声音文件：.au   audo/basic

   MIDI音乐文件：.mid/.midi    audio/midi   audio/x-midi

   RealAudio音乐文件：.ra/.ram   audio/x-pn-realaudio

   MPEG文件：.mpg/.mpeg   video/mpeg

   AVI文件：.avi   video/x-msvideo

   GZIP文件：.gz   application/x-gzip

   TAR文件：.tar   application/x-tar





