# MATLAB笔记4--文本和字符

1. 文本赋值给变量

   + 含文本的变量同样是数组，数据类型为char

   + myText='Hello World'

   + 文本中包含单引号：用两个单引号

     otherText='You''re right'

   + 使用方括号串联字符数组

     longText=[myText,' - ',otherText]       #longText='Hello World - you're right'

2. 数值转换为字符

   使用num2str或int2str函数

   + num2str：将==数值型变量==转换为字符串类型

     支持：single,double.int8,int16,int32,int64,uint8,uint16,uint32,uint64,logical

     str=num2str(A)

     str=num2str(A,precision)    #precision指定最大数字总位数

   + int2str：将==整数值==转换为字符串

     若该值不是整数，就将该值四舍五入后转换为字符串

     如果是向量和矩阵，列数字之间会加两个空格

