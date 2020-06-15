# Python模块7--argparse

1. 简介

   argparse是python用于解析命令行参数和选项的标准模块，用于代替已经过时的optparse模块

   程序定义它需要的参数，然后argparse 将弄清如何从sys.argv解析除那些参数

   argparse还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息

2. 使用方法

   + 导入

     ```python
     import argparse
     ```

   + 创建解析对象

     ```python
     parser = argparse.ArgumentParser(description = "your script description")
     ```

     description : 用于插入描述脚本用途的信息，可以为空

   + 添加命令行参数和选项

     ```python
     parser.add_argument("argument_name", help="description of the argument")
     ```

     其他可加参数：

     + type = "type of argument"

       **argparse会把传递给他的选项视为字符串，除非指定type类型**

     + action （针对可选参数）

       + action = "store_true"

         **对于可选参数，默认需要输入一个值。**

         如果指定action="store_true"，则该选项存在时，args.argument_name赋值为True；该选项不存在时，args.argument_name赋值为True。

         **可选参数没有被使用时，相关变量被赋值为None，即args.argument_name=None；并且它不能和整数值相比较，否则会产生TypeError异常**

         当为可选参数指定值时，则会报错

       + action = "count"

         计算可选参数出现的次数，args.argument_name返回次数

     + default = default_value

       设置可选参数默认指定的值

     + choices = [value1, value2, ...]

       限制可选参数可以接受的值

   + 指定彼此相互冲突的选项

     ```python
     group = parser.add_mutually_exclusive_group()
     ```

     ```python
     group.add_argument("argument_name", help="description of the argument")
     ```

     此时，直接用add_argument方法把彼此冲突的可选参数add到group而不是parser。

3. 实例

   参考：https://docs.python.org/zh-cn/3/howto/argparse.html#id1

   进阶：https://docs.python.org/zh-cn/3/library/argparse.html?highlight=argparse

