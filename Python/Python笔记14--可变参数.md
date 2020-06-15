# Python笔记14--可变参数

1. 位置参数与关键字参数

   + 位置参数 args(arguments)
   + 关键字参数 kwargs(keyword arguments)
   + 位置参数在关键字参数前面
   + \**args必须放在**kwargs前面

2. *args的用法

   + *args传递一个可变参数列表**（元组）**给函数实参，这个参数列表的数目未知，甚至长度可以为0

   + 实例

     ```python
     def test_args(first, *args):
         print('Required argument: ', first)
         print(type(args))
         for v in args:
             print ('Optional argument: ', v)
     
     test_args(1, 2, 3, 4)
     ```

     output:

     ```python
     Required argument:  1
     <class 'tuple'>
     Optional argument:  2
     Optional argument:  3
     Optional argument:  4
     ```

3. **kwargs

   + \**kwargs将一个可变的关键字参数的**字典**传递给函数实参，参数列表长度可以为0或为其他值

   + 实例

     ```python
     def test_kwargs(first, *args, **kwargs):
         print('Required argument: ', first)
         print(type(kwargs))
         for v in args:
             print ('Optional argument (args): ', v)
         print(kwargs)
         print(kwargs.items())
         for k, v in kwargs.items():
             print ('Optional argument %s (kwargs): %s' % (k, v))
         for k, v in kwargs.items():
             print ('Optional argument %s (kwargs): %s' % (k, v))
     
     test_kwargs(1, 2, 3, 4, k1=5, k2=6)
     ```

     output:

     ```python
     Required argument:  1
     <class 'dict'>
     Optional argument (args):  2
     Optional argument (args):  3
     Optional argument (args):  4
     {'k1': 5, 'k2': 6}
     dict_items([('k1', 5), ('k2', 6)])
     Optional argument k1 (kwargs): 5
     Optional argument k2 (kwargs): 6
     Optional argument k1 (kwargs): 5
     Optional argument k2 (kwargs): 6
     ```

4. 调用函数

   + args和kwargs不仅可以在函数定义中使用，还可以在函数调用中使用

   + 在调用时使用就相当于pack(打包)和unpack(解包)，类似于元组的打包和解包

   + 实例

     ```python
     def test_args_kwargs(arg1, arg2, arg3):
         print("arg1:", arg1)
         print("arg2:", arg2)
         print("arg3:", arg3)
     
     args = ("two", 3, 5)
     test_args_kwargs(*args)
     print()
     kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
     test_args_kwargs(**kwargs)
     ```

     output:

     ```python
     arg1: two
     arg2: 3
     arg3: 5
     
     arg1: 5
     arg2: two
     arg3: 3
     ```

     