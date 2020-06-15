# Python模块6--select

1. 功能

   + 主要用于socket通信当中，**能监视我们需要的文件描述的变化**

   + 非阻塞式I/O编程
     + 阻塞程序：进程或是线程执行到某函数时必须等待某个时间的发生，如果时间没有发生，进程或县城就被阻塞，函数不能立即返回
       + connect , accept , recv 或 recvfrom 这样的都是阻塞程序
     + 非阻塞程序：进程或线程执行到某函数时，不必非要等待事件的发生
       + 一旦执行一定返回，以返回值的不同来反映函数的执行情况
       + 如果事件发生，则与阻塞方式相同
       + 如果时间没有发生，则返回一个代码来告知事件未发生，进程或线程继续执行，效率因此而提高
       + 它能够监视我们需要监视的文件描述符的变化情况--读写或是异常
       + 返回值：准备就绪的描述符数，若超时则返回0，若出错则返回

   ---

2. 语法

   + 进程指定内核监听哪些文件描述符（fd:file descriptor）（最多监听1024个fd）的哪些事件，当没有文件描述符事件发生时，进程被阻塞；当一个或者多个文件描述符事件发生时，进程被唤醒

   + 调用select()时

     + 上下文切换为内核态
     + 将fd从用户控件复制到内核控件
     + 内核便利所有fd，查看其对应事件是否发生
     + 如果没有发生，将进程阻塞，当设备驱动产生中断或者timeout时间后，将进程唤醒，再次进行遍历
     + 返回遍历后的fd
     + 将fd从内核空间复制到用户空间

   + select语法

     ```python
     fd_r_list, fd_w_list, fd_e_list = select.select(rlist, wlist, xlist, [timeout])
     ```

     + rlist : wait until ready for reading 

     + wlist : wait until ready for writing

     + xlist : wait for an "exceptional condition"

     + timeout : 超时时间

       + 当超时时间为空

         select会一直阻塞，直到监听的句柄发生变化

       + 当超时时间 = n(正整数)

         如果监听的句柄均无任何变化，则select会阻塞n秒，之后返回三个空列表，如果监听的句柄有变化，则直接执行

     + 返回值 ：三个列表

       + select方法用来监视文件描述符（当文件描述符条件不满足时，select会阻塞），当某个文件描述符状态改变后，会返回三个列表
       + fd_r_list : 当参数1序列中的fd满足“可读”条件时，则获取发生变化的fa并添加到fd_r_list中
       + fd_w_list : 当参数2序列中含有fd时，将该序列中的所有fd添加到fd_w_list中
       + fd_e_list : 当参数3序列中的fd发生错误时，将该发生错误的fd添加到fd_e_list中

   ---

3. 实例1

   + server

     ```python
     import socket
     import select
     
     sk1 = socket.socket()
     sk1.bind(('0.0.0.0', 8001))
     sk1.listen()
     
     sk2 = socket.socket()
     sk2.bind(('0.0.0.0', 8002))
     sk2.listen()
     
     sk3 = socket.socket()
     sk3.bind(('0.0.0.0', 8003))
     sk3.listen()
     
     inputs = [sk1, sk2, sk3, ]
     
     while True:
         r_list, w_list, e_list = select.select(inputs,[],inputs,1)
         print('test')
         for sk in r_list:
             # conn表示每一个连接对象
             conn, address = sk.accept()
             print(r_list)
             print(conn)
             print(address)
             conn.sendall(bytes('hello', encoding='utf-8'))
             conn.close()
     
         for sk in e_list:
             inputs.remove(sk)
     ```

     + select内部自动监听sk1,sk2,sk3三个对象，监听三个句柄是否发生变化，把发生变化的元素放入r_list中

       + 如果有人连接sk1,则r_list=[sk1]
       + 如果有人连接sk1,sk2,则r_list=[sk1,sk2]
       + 如果有人连接sk1,sk2,sk3,则r_list=[sk1,sk2,sk3]

     + select第一个参数：inputs中发生变化的句柄放入r_list

     + select第二个参数：[]中的值原封不动的传递给w_list

     + select第三个参数：inputs中发生错误的句柄放入e_list

     + select第四个参数：参数1表示1秒监听一次

     + output

       client1连接时server端的结果

       ```python
       test
       test
       test
       test
       test
       test
       test
       [<socket.socket fd=472, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8001)>]
       <socket.socket fd=524, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8001), raddr=('127.0.0.1', 49354)>
       ('127.0.0.1', 49354)
       test
       test
       test
       test
       test
       test
       ```

   + client1

     ```python
     import socket
     
     obj = socket.socket()
     obj.connect(('127.0.0.1', 8001))
     
     content = str(obj.recv(1024), encoding='utf-8')
     print(content)
     
     obj.close()
     ```

     + output

       ```python
       hello
       ```

   + client2

     ```python
     # 客户端c2.py
     import socket
     
     obj = socket.socket()
     obj.connect(('127.0.0.1', 8002))
     
     content = str(obj.recv(1024), encoding='utf-8')
     print(content)
     
     obj.close()
     ```

   + python3

     ```python
     # 客户端c3.py
     import socket
     
     obj = socket.socket()
     obj.connect(('127.0.0.1', 8003))
     
     content = str(obj.recv(1024), encoding='utf-8')
     print(content)
     
     obj.close()
     ```

   ---

3. 实例2

   + I\O多路复用--使用socket模拟多线程，并实现读写分离

   + server

     ```python
     #使用socket模拟多线程，使多用户可以同时连接
     import socket
     import select
     
     sk1 = socket.socket()
     sk1.bind(('0.0.0.0', 8001))
     sk1.listen()
     
     inputs = [sk1, ]
     outputs = []
     message_dict = {}
     
     while True:
         r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)
         print('正在监听的socket对象%d' % len(inputs))
         print(r_list)
         for sk1_or_conn in r_list:
             #每一个连接对象
             if sk1_or_conn == sk1:
                 # 表示有新用户来连接
                 conn, address = sk1_or_conn.accept()
                 inputs.append(conn)
                 message_dict[conn] = []
             else:
                 # 有老用户发消息了
                 try:
                     data_bytes = sk1_or_conn.recv(1024)
                 except Exception as ex:
                     # 如果用户终止连接
                     inputs.remove(sk1_or_conn)
                 else:
                     data_str = str(data_bytes, encoding='utf-8')
                     message_dict[sk1_or_conn].append(data_str)
                     outputs.append(sk1_or_conn)
     
         #w_list中仅仅保存了谁给我发过消息
         for conn in w_list:
             recv_str = message_dict[conn][0]
             del message_dict[conn][0]
             conn.sendall(bytes(recv_str+'好', encoding='utf-8'))
             outputs.remove(conn)
     
         for sk in e_list:
     
             inputs.remove(sk)
     ```

     + output

       ```python
       正在监听的socket对象1
       []
       正在监听的socket对象1
       []
       正在监听的socket对象1
       [<socket.socket fd=468, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8001)>]
       正在监听的socket对象2
       []
       正在监听的socket对象2
       []
       正在监听的socket对象2
       []
       ```

   + client

     ```python
     import socket
     
     obj = socket.socket()
     obj.connect(('127.0.0.1', 8001))
     
     while True:
         inp = input('>>>')
         obj.sendall(bytes(inp, encoding='utf-8'))
         ret = str(obj.recv(1024),encoding='utf-8')
         print(ret)
     
     obj.close()
     ```

     + output

       ```python
       >>>hi
       hi好
       >>>
       ```

       

