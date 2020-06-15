---
title: Python网络编程和多线程--UDP编程
date: 2019-04-10 10:43:39
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89176329](https://blog.csdn.net/zhaandzha/article/details/89176329)   
    
   编写一个简单的UDP演示下棋程序。服务器端把UDP客户端发来的下棋x,y坐标显示出来，并把x,y坐标加1后再发给UDP客户端

 Server.py:

 
```
 import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('172.18.146.213',8888))
print('Bind UDP on 8888...')
while True:
    data,addr=s.recvfrom(1024)
    print("Received from %s:%s."%addr)
    print("received:",data)
    p=data.decode('utf-8').split(",")
    x=int(p[0])
    y=int(p[1])
    print(p[0],p[1])
    pos=str(x+1)+","+str(y+1)
    s.sendto(pos.encode('utf-8'),addr)
```
 Client.py:

 
```
 import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x=input("请输入x坐标:")
y=input("请输入y坐标:")
data=str(x)+","+str(y)
s.sendto(data.encode('utf-8'),('172.18.146.213',8888))

data2,addr=s.recvfrom(1024)
print('接收服务器加1后的数据:',data2.decode('utf-8'))
s.close()

```
 

   
 