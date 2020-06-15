---
title: Python网络编程和多线程--TCP编程
date: 2019-04-09 15:31:59
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89150366](https://blog.csdn.net/zhaandzha/article/details/89150366)   
    
   一个简单的服务器客户端代码段

 Server.py:

 
```
 import socket
import threading
import time
def tcplink(sock, addr):
    print("接收一个来自%s:%s连接请求"%addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('来自%s:%s连接关闭了.'%addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('172.18.146.213',8888))
s.listen(5)
print("等待客户端连接...")
while True:
    sock, addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))  #创建新线程来处理TCP连接
    t.start()


```
 =>decode('utf-8'):以utf-8编码将字节串换成字符串

 encode('utf-8'):以utf-8编码将字符串编码成字节串

 =>Python3中join()函数不仅能连接字符串，还能连接字节串

 数据包中数据只能是字节串

 =>threading.Thread(target=线程函数，args=(参数列表)[，name=线程名，group=线程组])

 线程名和线程组都可以省略

 创建线程后，通常需要调用线程对象的setDaemon()方法将线程设置为守护线程。

 主线程执行完后，如果还有其他非守护线程，则主线程不会退出，会被无限挂起；必须将线程声明为守护线程后，如果队 列中的线程运行完了，整个程序不用等待就可以退出

 Client.py:

 
```
 import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('172.18.146.213',8888))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```
 

   
 