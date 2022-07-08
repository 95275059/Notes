# Python模块8--os

### 介绍

os 模块提供了非常丰富的方法用来**处理文件和目录**。

---

### os.listdir(path)

返回path指定的文件夹包含的文件或文件夹的名字的**列表**

---

### os.system(cmd)

+ python调用shell的一种方法
+ 返回值是脚本的退出状态码
  + 只有0(成功),1,2

---

### os.popen(cmd)

+ python调用shell的一种方法
+ 这种调用方式通过管道方式实现，函数返回一个file-like的对象，里面的内容是脚本输出的内容。
+ 需要获取内容时可使用read()或readlines()方法。

---

### os.getcwd()

+ 返当前最外层调用的脚本路径

---

### os.path

+ ```python
  os.path
  ```

  返回python解析器搜索路径

  ```python
  >>> import sys
  >>> sys.path
  ['', '/usr/lib/python2.7/site-packages/xlrd-1.2.0-py2.7.egg', '/usr/lib/python2.7/site-packages/xlwt-1.3.0-py2.7.egg', '/usr/lib/python2.7/site-packages/xlutils-2.0.0-py2.7.egg', '/usr/lib64/python27.zip', '/usr/lib64/python2.7', '/usr/lib64/python2.7/plat-linux2', '/usr/lib64/python2.7/lib-tk', '/usr/lib64/python2.7/lib-old', '/usr/lib64/python2.7/lib-dynload', '/usr/lib64/python2.7/site-packages', '/usr/lib/python2.7/site-packages']
  ```

+ ```python
  os.path.dirname('path')
  ```

  去掉文件名，返回目录

  ```python
  os.path.dirname('__file__')
  ```

  + 当脚本是以绝对路径运行，将输出该脚本所在完整路径
  + 当脚本是以相对路径被运行，将输出空目录（空字符串）

  ```python
  test.py:
  import sys
  import os
  print(os.getcwd())
  print(os.path.dirname('__file__'))
  print(os.path.dirname(os.path.realpath('__file__')))
  print(os.path.dirname('/home/cxy/test/test.py'))
  print(os.path.dirname('/home/cxy/test'))
  print(os.path.dirname(sys.path[0]))
  print(__file__)
  ```

  ```shell
  [root@network test]# python test.py 
  /home/cxy/test
  
  /home/cxy/test
  /home/cxy/test
  /home/cxy
  /home/cxy
  test.py
  [root@network test]# python /home/cxy/test/test.py 
  /home/cxy/test
  
  /home/cxy/test
  /home/cxy/test
  /home/cxy
  /home/cxy
  /home/cxy/test/test.py
  [root@network ~]# python /home/cxy/test/test.py 
  /root
  
  /root
  /home/cxy/test
  /home/cxy
  /home/cxy
  /home/cxy/test/test.py
  ```

+ ```python
  os.path.realpath()
  ```

  获取当前执行脚本的绝对路径，如果文件软连接指向别的文件，会返回别的文件的路径

  ```
  os.path.dirname(os.path.realname(__file__))
  ```

  获取的\__file__所在脚本的路径，也就是fileName.py的路径

* ```python
  os.path.abspath()
  ```

  获取当前执行脚本的绝对路径


+ ```python
  os.path.exists(path)
  ```

  如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。

---

### os.stat(path)

+ os.stat() 方法用于在给定的路径上执行一个系统 stat 的调用。

+ 语法

  ```python
  os.stat(path)
  ```

  + path : 指定路径

  + 返回值：stat结构

    + st_mode : inode保护模式

    + st_ino : inode节点号

    + st_dev : inode驻留的设备

    + st_nlink : inode的链接数

    + st_uid : 所有者的用户ID

    + st_gid : 所有者的组ID

    + st_size : 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。

    + st_atime : 上次访问的时间

    + st_mtime : 最后一次修改的时间

    + st_ctime : 由操作系统报告的"ctime"。

      在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。

+ 实例

  ```python
  import os
  statinfo = os.stat('a.json')
  print(statinfo)
  ```

  ```python
  os.stat_result(st_mode=33206, st_ino=13510798882158949, st_dev=3094283438, st_nlink=1, st_uid=0, st_gid=0, st_size=35, st_atime=1609406128, st_mtime=1609406128, st_ctime=1609406128)
  ```

---

### os.kill

+ 一般用于直接Kill掉进程，但是只能在**UNIX平台**上有效。

+ 基本原理

  该函数是**模拟传统的UNIX函数发信号给进程**，其中包含两个参数：

  + 一个是进程名，即所要接收信号的进程；
  + 一个是所要进行的操作。
    + SIGINT 终止进程 中断进程
    + SIGTERM 终止进程 软件终止信号
    + SIGKILL 终止进程 杀死进程
    + SIGALRM 闹钟信号
  
+ 实例

  ```python
  import os
  import signal
  os.kill(pid, signal.SIGTERM)
  ```

---

### os.remove(path)

+ 功能

  os.remove() 方法用于删除指定路径的文件。

  如果指定的路径是一个目录，将抛出OSError。

  在Unix, Windows中有效。

+ 语法

  ```python
  os.remove(path)
  ```

  + path : 要移除的文件路径

---

### os.getcwd()

+ 功能

  返回当前工作目录

+ 语法

  ```python
  path = os.getcwd()
  ```

---

### os.getpid()

+ 功能

  返回当前进程ID

  可在记录日志或者Dump系统日志时使用

+ 语法

  ```python
  pidID = os.getpid()
  ```

  + 返回值：int类型的进程号

---

### os.getppid()

+ 功能

  返回父进程pid

  只在 unix或linux 系统中有效

+ 语法

  ```python
  ppid = os.getppid()
  ```

---

### os.fork

+ 功能

  创建子进程

  使用fork创建子进程后，子进程会复制父进程的数据信息，而后程序就分两个进程继续运行后面的程序，这也是fork（分叉）名字的含义了。

  在子进程内，这个方法会返回0；

  在父进程内，这个方法会返回子进程的编号PID。

  **既然子进程是父进程创建的，那么父进程退出之后，子进程会被PID为1的进程接管，就是init进程了。这样子进程就不会受终端退出影响了，使用这个特性就可以创建在后台执行的程序，俗称守护进程（daemon）。**

+ 语法

  ```python
  pid = os.fork()
  ```

+ 实例

  ```python
  import os
  
  print('Process (%s) start...' % os.getpid())
  # Only works on Unix/Linux/Mac:
  pid = os.fork()
  if pid == 0:
      print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
  else:
      print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
  ```

  ```python
  Process (876) start...
  I (876) just created a child process (877).
  I am child process (877) and my parent is 876.
  ```

  







