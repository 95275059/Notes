# Python笔记5--reload

1. 功能

   + reload()函数用于重新载入之前载入的模块

   + 在调试过程中，如果修改了某模块，则**必须**使用reload() 函数重新载入该模块。(<https://blog.csdn.net/weixin_42714175/article/details/87782855>)

2. 语法

   ```python
   reload(module)
   ```

   + module : 模块对象
   + 返回值 : 返回模块对象

3. 注意

   + python2中可以直接使用reload(module)重载模块

   + python3需要import

     + 方式一

       ```python
       import imp
       imp.reload(module)
       ```

     + 方式二

       ```python
       from imp import reload
       reload(module)
       ```

   + python3.4

     ```python
     import importlib
     importlib.reload(module)
     ```



