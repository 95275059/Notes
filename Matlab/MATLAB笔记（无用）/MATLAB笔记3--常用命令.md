# MATLAB笔记3--常用命令

1. 工作区变量

   工作区变量包含 在MATLAB中创建 或 从数据文件或其他程序导入的变量

   + 用whos查看工作区内容

   + 退出MATLAB后，工作区变量不会保留。

     + save命令可以保存数据供将来使用

       save myfile.mat

       系统会使用.mat扩展名将保存在当前工作文件夹中名为MAT文件的压缩文件中

   + clear命令能够清除工作区中所有变量

   + load将MAT文件中的数据还原到工作区

     load myfile.mat

2. 清空命令行窗口

   clc

3. 查看帮助文档

   doc mean        #查看mean函数的帮助文档

   help mean       #查看mean函数的简明文档