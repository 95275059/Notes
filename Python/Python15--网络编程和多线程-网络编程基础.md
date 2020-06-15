# Python15--网络编程和多线程--网络编程基础

1. IP地址:互联网上每个计算机的唯一标识

   + 若一台计算机同时接入到两个或更多网络，它就会有两个或多个IP地址
   + IP地址对应的实际上是计算机的网络接口，通常是网卡
   + IP协议:负责将数据从一台计算机通过网络发送到另一台计算机。
   + 数据被分割成小块，然后通过IP包发送出去。
   + 互联网链路复杂，两台计算机之间通常有多条线路，路由器负责决定如何把一个IP包转发出去
   + IPv4:32位（8*4）；IPv6:128位（16*8）

   ---

2. TCP和UDP协议

   + TCP协议：建立在IP协议之上，负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。

     通过握手建立连接，然后对每个IP包编号，确保对方按顺序收到。如果包丢了，就自动重发。

   + UDP协议：建立在IP协议之上，但UDP协议是面向无连接的通信协议，不保证数据包的顺利到达，是不可靠传输，但效率比 TCP高。

   ---

3. 端口

   每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。

   ---

4. Socket(套接字)

   + Socket是网络编程的一个抽象概念，用于网络通信编程。

   + Socket是TCP/IP网络最为通用的API，任何网络通信都是通过Socket来完成的

   + 一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

   + Socket构造函数

     + socket(family,type[,protocal])
       + family:套接字家族
         + socket.AF_UNIX:只能够用于单一的Unix系统进程间通信
         + socket.AF_INET:服务器之间网络通信
         + socket.AF_INET6:IPv6
       + type:套接字类型
         + socket.SOCK_STREAMO:流式socket,针对TCP
         + socket.SOCK_DGRAM:数据报式socket,针对UDP
       + protocol:一般不填，默认为0

   + Socket对象函数

     + 服务器端套接字

       + s.bind(host,port)

         绑定地址(host,port)到套接字

         在AF_INET下以元组(host,port)的形式表示地址

       + s.listen(backlog)

         开始TCP监听

         backlog指定在拒绝连接之前，最大的连接数量；至少为1，一般设为5即可

       + s.accept()

         被动接受TCP客户端连接，（阻塞式）等待连接的到来

     + 客户端套接字

       + s.connect(address)

         主动与TCP服务器连接

         一般address格式为元组(hostname,port)，如果连接出错，返回socket.error 错误 

       + s.connect_ex(address)

         connect()的拓展版本，出错时返回出错码，而不是抛出异常

     + 公共用途的套接字函数

       + s.recv(bufsize[,flag])

         **接收TCP数据**，数据以字节串形式返回

         bufsize指定要接收的最大数据量。

         flag提供有关消息的其他 信息，通常可以忽略

       + s.send(data)

         **发送TCP数据**，将data中的数据发送到连接的套接字。

         返回值是要发送的字节数量，该数量可能小于data的 字节大小

       + s.sendall(data)

         完整发送TCP数据

         将data中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。

         若成功返回None，失败则抛出异常

       + s.recvform(bufsize[,flag])

         **接收UDP数据**，与recv()类似，但返回值是(data,address)

       + s.sendto(data,address)

         **发送UDP数据**，将数据发送到套接字

         address指定远程地址，返回值是发送的字节数

       + s.close()

         关闭套接字

       + s.getpeername()

         返回连接套接字的远程地址

         返回值通常是元组(ipaddr,port)

       + s.getsockname()

         返回套接字自己的地址

         返回值通常是一个元组(ipaddr,port)

       + s.setsockopt(level,optname,value)

         设置给定套接字选项的值

       + s.getsockopt(level,optname)

         返回套接字选项的值

       + s.settimeout(timeout)

         设置套接字操作的超时时间

         timeout是一个浮点数，单位是秒;None表示没有超时时间

         一般超时时间应在刚创建套接字时设置，因为它们可能用于连接的操作

       + s.gettimeout()

         返回当前超时时间的值，单位是秒，如果没有设置超时时间，则返回None

       + s.fileno()

         返回套接字的文件描述符

       + s.setblocking(flag)

         如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）

         非阻塞模式下，若调用recv()没有发现任何数据，或send()调用无法立即发送数据，将引起socket.error异常

       + s.makefile()

         创建一个与该套接字相关联的文件 





 

 

 

   
