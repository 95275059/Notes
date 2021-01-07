# Python笔记1--异常处理

Python中包含错误和异常两种情况

+ 错误

  主要是常见的语法错误SyntaxError

  语法错误是直接显示在相关终端窗口

+ 异常

  指的是在语法和表达式上并没有错误，运行时会发生错误的情况。

  异常可以进行错误提示，也可以进行捕捉处理。

  捕捉异常可以使用try/except语句 

---

1. try/except

   try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。 

   如果不想在异常发生时结束程序，只需在try里捕获它。 

   + 语法

     ```python 
     try:
         <语句>
     except <name1>:
         <语句>         #如果在try部分发生了‘name1’异常
     except <name2>,<data>:
         <语句>         #如果在try部分发生了‘name1’异常，获得附加的数据为data
     else:
         <语句>         #如果没有异常发生
     ```

     + except不带任何异常类型

       若发生异常就执行except下的代码。但这不是一个很好的方式，因为由于会捕捉所有异常而不能识别出具体的异常信息。

     + except带多种异常类型

       ```python
       try:
           <语句>
       except(<name1>[,<name2>[,....]]):
           <语句>         #发生以上多个异常中的一个，执行这块代码
       else:
           <语句>         #如果没有异常发生
       ```

   + 工作原理

     当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。 

     + try后的语句执行时发生异常并匹配到异常的except语句

       python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕后，控制流就通过整个try语句。

     + try后的语句执行时发生异常但没有匹配到异常的except语句

       异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。

     + 如果在try子句执行时没有发生异常 

       python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。 

2. try/finally

   try-finally语句无论是否发生异常都将执行最后的代码。 

   ```python
   try:
       <语句>
   finally:
       <语句>     #退出try时总会执行
       
   ```

3. raise

   raise会引发一个异常 

   主动抛出异常的好处，一是可以抛出在语法上不被认为是异常但在功能上我们认为是异常的情况（如用户名密码错误等），二是可以自定义自己的异常报错语句更方便异常的定位和排查。

   + 语法
   
     ```python
    raise [Exception [, args [, traceback]]]
     ```

     Exception 是异常的类型参数标准异常中任一种 

   + 例：

     ```python
     def mye(level):
         if level < 1:
             raise Exception("Invalid level!")
             # 触发异常后，后面的代码就不会再执行
     try:
         mye(0)            # 触发异常
     except Exception as err:
         print(1,err)
     else:
         print(2)
     ```
   
     运行结果：1 Invalid level!

4. 用户自定义异常

   + 通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。

   + 例

     ```python
     class Networkerror(RuntimeError):
         def __init__(self, arg):
           self.args = arg
     ```
     
     在你定义以上类后，你可以触发该异常，如下所示：
     
     ```python
     try:
         raise Networkerror("Bad hostname")
     except Networkerror,e:
         print e.args
     ```

5. python标准异常

   | 异常名称          | 描述                          |
   | ----------------- | ----------------------------- |
   | BaseException     | 所有异常的基类                |
   | Exception         | 常见错误的基类                |
   | SystemExit        | 解释器请求退出                |
   | OverflowError     | 数值运算超出最大限制          |
   | ZeroDivisionError | 除（取模）零（所有数据类型）  |
   | **IOError**       | 输入\输出操作失败             |
   | **OSError**       | 操作系统错误                  |
   | ImportError       | 导入模块\对象失败             |
   | **SyntaxError**   | Python语法错误                |
   | NameError         | 未声明\初始化对象（没有属性） |
   | Warning           | 警告的基类                    |
   | SyntaxWarning     | 可以的语法的警告              |
   | RuntimeError      | 一般的运行时错误              |
| **ValueError**    | 输入无效的参数                |
   | **TypeError**     | 对类型无效的操作              |
   
   + typeerror：函数或方法接受了不适当的【类型】的参数
   
     比如sum('nick')，sum函数不接受字符串类型；
   
   + valueerror：函数或方法虽然接受了正确的【类型】的参数，但是该参数的【值】不适当
   
     比如int('nick')，int函数可以接受字符串类型，但是'nick'字符串不具备表示一个整数的含义。