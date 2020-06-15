# PythonTips2--MySQLdb import报错

+ Python 编译器下 运行 import MySQLdb 报错

  ```shell
  [root@compute6 lib64]# python
  Python 2.7.5 (default, Apr  2 2020, 13:16:51) 
  [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import MySQLdb
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/usr/lib64/python2.7/site-packages/MySQLdb/__init__.py", line 19, in <module>
      import _mysql
  ImportError: libmysqlclient.so.18: cannot open shared object file: No such file or directory
  ```

  **ImportError: libmysqlclient.so.18: cannot open shared object file: No such file or directory**

+ 方法一：

  ```shell
  yum uninstall MySQLdb
  ```

  ```shell
  yum install MySQLdb
  ```

+ 方法二（网传，没成功）

  + 原因

    在服务器上自己安装了MySQL而卸载了原有的MySQL，服务器就将原来/usr/lib64/mysql下的libmysqlclient.so.18删除掉了

  + 解决方案

    将原生系统文件(没有安装mysql的系统)中的/usr/lib64/mysql/libmysqlclient.so.18这个文件SCP到报错的系统中的/usr/lib64/mysql库文件目录中

    设置/etc/ld.so.conf文件，编辑该文件，在文件汇总加入libmysqlclient.so.18所在目录，保存退出

    运行ldconfig命令来确认刷新