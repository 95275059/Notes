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

+ 返回模块的搜索路径，初始化时使用pythonpath环境变量的值

+ sys模块包含了与python解释器和它的环境有关的函数, 里面有个 sys.path属性。它是一个list.默认情况下python导入文件或者模块的话，他会先在sys.path里找模块的路径。如果没有的话,程序就会报错。

+ python中import某个A模块时，首先会从python的内置模块中查找是否含义该模块的定义若未查询到会从sys.path对应的模块路径查询是否含有对应模块的定义，如果搜索完成依然没有对应A模块时则抛出import的异常

+ python的两种加载py文件的方式

  + python xxx.py

    直接运行方式

    sys.path[0]是当前脚本的运行目录

  + python -m xxx.py

    把模块当做脚本来启动

    sys.path[0]是空值字符串，也就是当前执行python的目录

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

### sys.exit

