# Python模块3--socket

1. socket定义

   Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是**一组接口**。

   Socket把复杂的TCP/IP协议族隐藏在Socket接口后面

   对用户来说，无需深入理解TCP/IP协议，只需要遵循Socket的规定去编程，写出的程序即符合TCP/IP标准

   + 也有人将Socket说成ip+port

     ip是主机网卡，port是应用程序开启的，ip+port可以精确定位一个应用程序

   ![模块3-1](E:\Notes\Python\模块3-1.png)

   ---

2. socket分类

   + 基于文件类型的套接字家族（AF_UNIX）

     UNIX一切皆文件，基于文件类型的套接字调用的就是底层的文件系统来取数据，两个套接字进程运行在同一机器，可以通过访问同一个文件系统间接完成通信

   + 基于网络类型的套接字家族（AF_INET）

     使用最广泛的地址家族

   + AF_INET6:ipv6

   + 其他

     还有一些其他的地址家族，有些只用于某个平台，有些早已经被废弃，或者很少使用，有些甚至根本没有实现

   ---

3. socket工作流程

   ![模块3-2](E:\Notes\Python\模块3-2.png)

   + 服务端先初始化socket，然后与端口绑定（bind），对端口进行监听（listen），调用accept阻塞，等待客户端连接
   + 如果客户端初始化一个socket，然后连接服务器（connect），如果连接成功，这时客户端与服务端的连接就建立了
   + 客户端发送数据请求，服务端接收请求并处理请求，然后把回应数据发送给客户端
   + 客户端读取数据，最后关闭连接，一次交互结束

   ---

4. socket函数使用

   + 导入模块

     ```python
     import socket
     ```

   + socket()函数

     socket.socket([family[,type[,proto]]])

     + family：套接字家族，AF_UNIX或AF_INET
     + type：套接字类型
       + socket.SOCK_STREAM：流式socket，针对TCP
       + socket.SOCK_DGRAM：数据报式socket，针对UDP
     + proto：协议，一般不填，默认为0

   + socket对象方法

     + 服务端socket

       | 函数              | 描述                                                         |
       | ----------------- | ------------------------------------------------------------ |
       | s.bind(host,port) | 绑定地址（host,port）到套接字；在AF_INET下，以元组（host,port）的形式表示地址 |
       | s.listen(backlog) | 开始TCP监听；backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量，该值至少为1，大部分应用程序设置为5即可 |
       | s.accept()        | 被动接受TCP客户端连接，（阻塞式）等待连接的到来              |

     + 客户端socket

       | 函数                  | 描述                                                         |
       | --------------------- | ------------------------------------------------------------ |
       | s.connect(address)    | 主动初始化TCP服务器连接。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误 |
       | s.connect_ex(address) | connect()函数的扩展版本，出错时返回出错码，而不是抛出异常    |

     + 公用socket

       | 函数                              | 描述                                                         |
   | --------------------------------- | ------------------------------------------------------------ |
       | s.recv(bufsize[,flag])            | **接收TCP数据**，数据以字符串形式返回；bufsize指定要接收的最大数据量；flag提供有关消息的其他信息，通常可以忽略 |
   | s.send(data)                      | **发送TCP数据**，将data中的数据发送到连接的套接字；返回值是要发送的字节数量，该数据可能小于data的字节大小 |
       | s.sendall(data)                   | **完整发送TCP数据**；将data中的数据发送到连接的套接字，但在返回前会尝试发送所用数据；若成功返回None，失败则抛出异常 |
   | s.recvform(bufsize[,flag])        | **接收UDP数据**，与recv()类似，但返回值是(data,address)      |
       | s.sendto(data,address)            | **发送UDP数据**，将数据发送到套接字；address指定远程地址，返回值是发送的字节数 |
   | s.close()                         | 关闭套接字                                                   |
       | s.getpeername()                   | 返回连接套接字的远程地址；返回值通常是元组(ipaddr,port)      |
   | s.getsockname()                   | 返回套接字自己的地址；返回值通常是元组(ipaddr,port)          |
       | s.setsockopt(level,optname,value) | 设置给定套接字选项的值                                       |
   | s.getsockopt(level,optname)       | 返回套接字选项的值                                           |
       | s.settimeout(timeout)             | 设置套接字操作的超时时间；timeout是一个浮点数，单位是秒；None表示没有超时时间；一般超时时间应该在刚创建套接字时设置，因为它可能用于连接的操作 |
   | s.gettimeout()                    | 返回当前超时时间的值，单位是秒；如果没有设置超时时间，则返回None |
       | s.fileno()                        | 返回套接字的文件描述符                                       |
       | s.setblocking(flag)               | 如果flag为0，则将套接字设置为非阻塞模式，否则将套接字设置为阻塞模式（默认值）；非阻塞模式下，若调用recv()没有发现任何数据，后send()调用后无法立即发送数据，将引起socket.error异常 |
       | s.makefile()                      | 创建一个与该套接字相关联的文件                               |
     
   
5. 实例

   + server

     ```python
     import socket
     # 建立一个服务端
     server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     server.bind(('localhost',9090)) #绑定要监听的端口
     server.listen(5) #开始监听 表示可以使用五个连接排队
     while True:# conn就是客户端连接过来而在服务端为其生成的一个连接实例
         conn,addr = server.accept() #等待链接,多个连接的时候就会出现问题,其实返回了两个值
         print(conn,addr)
         data = conn.recv(1024) #接收数据
         while data:
             print('recive:',data.decode()) #打印接收到的数据
             conn.send(data.upper()) #然后再发送数据
             data = conn.recv(1024)
         conn.close()
     ```
   
   + client
   
     ```python
     import socket# 客户端 发送一个数据，再接收一个数据
     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
     client.connect(('localhost',9090)) #建立一个链接，连接到本地的9090端口
     msg = 'test'  #strip默认取出字符串的头尾空格
     client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
     data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
     print('recv:',data.decode()) #输出接收的信息
     client.close() #关闭这个链接    
     ```
   
   + output
   
     + server
   
       ```python
       <socket.socket fd=568, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9090), raddr=('127.0.0.1', 62072)> ('127.0.0.1', 62072)
          recive: test
       ```
   
     + client
   
       ```python
       recv: TEST
       ```



  

   

   

   

   

   

   

   

   