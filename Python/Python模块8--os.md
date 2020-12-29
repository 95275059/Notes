# Python模块8--os

### 介绍

os 模块提供了非常丰富的方法用来**处理文件和目录**。

### os.listdir(path)

返回path指定的文件夹包含的文件或文件夹的名字的**列表**

### os.system(cmd)

+ python调用shell的一种方法
+ 返回值是脚本的退出状态码
  + 只有0(成功),1,2

### os.popen(cmd)

+ python调用shell的一种方法
+ 这种调用方式通过管道方式实现，函数返回一个file-like的对象，里面的内容是脚本输出的内容。
+ 需要获取内容时可使用read()或readlines()方法。

### os.getcwd()

+ 返当前最外层调用的脚本路径

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

  获取当前执行脚本的绝对路径

  ```
  os.path.dirname(os.path.realname(__file__))
  ```

  获取的\__file__所在脚本的路径，也就是fileName.py的路径

+ **永久添加路径到sys.path中，方式有三，如下：**
  1）将写好的py文件放到 已经添加到系统环境变量的 目录下 ；
  2) 在 /usr/lib/python2.6/site-packages 下面新建一个.pth 文件(以pth作为后缀名) 
  将模块的路径写进去，一行一个路径，如： vim pythonmodule.pth
  /home/liu/shell/config
  /home/liu/shell/base 
  3) 使用PYTHONPATH环境变量
  export PYTHONPATH=$PYTHONPATH:/home/liu/shell/config





