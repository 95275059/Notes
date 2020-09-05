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

  

