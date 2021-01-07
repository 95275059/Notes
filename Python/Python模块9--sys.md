# Python模块9--sys

### 简介

sys模块提供了一系列有关Python运行环境的变量和函数

### sys.argv

+ 获取当前正在执行的命令行参数的参数列表

+ 列表结构

  sys.argv[0] 当前程序名

  sys.argv[1] 第一个参数

  sys.argv[2] 第二个参数

  ...

+ 参数个数

  ```python
  len(sys.argv)-1
  ```

---

### sys.path

+ 返回模块的搜索路径，初始化时使用python path环境变量的值

+ sys模块包含了与python解释器和它的环境有关的函数, 里面有个 sys.path属性。它是一个list.默认情况下python导入文件或者模块的话，他会先在sys.path里找模块的路径。如果没有的话,程序就会报错。

+ python中import某个A模块时，首先会从python的内置模块中查找是否含义该模块的定义若未查询到会从sys.path对应的模块路径查询是否含有对应模块的定义，如果搜索完成依然没有对应A模块时则抛出import的异常

+ python的两种加载py文件的方式

  + python xxx.py

    直接运行方式

    sys.path[0]是当前脚本的运行目录

  + python -m xxx.py

    把模块当做脚本来启动

    sys.path[0]是空值字符串，也就是当前执行python的目录

+ **永久添加路径到sys.path中，方式有三，如下：**
  1）将写好的py文件放到 已经添加到系统环境变量的目录下 ；
  2) 在 /usr/lib/python2.6/site-packages 下面新建一个.pth 文件(以pth作为后缀名) 
  将模块的路径写进去，一行一个路径，如： vim pythonmodule.pth
  /home/liu/shell/config
  /home/liu/shell/base 
  3) 使用PYTHONPATH环境变量
  export PYTHONPATH=$PYTHONPATH:/home/liu/shell/config

+ ```python
  sys.path.append()
  ```

  添加搜索目录

  在模块里面修改sys.path值，这种方法修改的sys.path作用域只是当前进程，进程结束后就失效了。

+ sys.path添加路径方法

  + 方案一

    sys.path.append()

  + 方案二

    sys.path.extend()

    extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

  + 方案三

    sys.path += ['path1', 'path2']

---

### sys.exit()

+ 执行该语句会直接退出程序

+ 这也是经常使用的方法，也不需要考虑平台等因素的影响，一般是退出Python程序的首选方法。

+ 该方法中包含一个参数status，默认为0，表示正常退出，也可以为1，表示异常退出。

  ```python
  import sys
  sys.exit()  #0
  sys.exit(0) #0
  sys.exit(1) #1
  ```

+ 该方法引发的是一个**SystemExit异常**(这是唯一一个不会被认为是错误的异常)

  当没有设置捕获这个异常将会直接退出程序执行，当然也可以捕获这个异常进行一些其他操作

  ```python
  import sys
  try:
      sys.exit(0)
  except SystemExit:
      print('SystemExit')
  ```

  ```python
  SystemExit
  ```

  