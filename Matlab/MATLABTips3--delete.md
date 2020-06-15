# MATLABTips3--delete

1. delete

   + 删除文件或对象

   + 语法

     + delete filename

       从磁盘中删除filename,不需要验证

       + 删除文件预设项

         永久删除文件还是放入回收站

         主页-环境-预设项-matlab-常规

         默认是永久删除

     + delete filename1 ... filenameN

       从磁盘上删除指定文件

     + delete(obj)

       删除指定的对象

       如果obj是数组，则delete将删除数组中的所有对象

       obj会保留在工作区中，但是不再有效