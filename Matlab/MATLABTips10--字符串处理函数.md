# MATLABTips10--字符串处理函数

1. strsplit

   + 功能：在指定分隔符处拆分字符串或字符向量

   + 语法

     + ```matlab
       C = strsplit(str)
       ```

       + 在空白处将str拆分为C

       + 空白字符等效于集合{' ','\f','\n','\r','\t','\v'}中的任何转义序列

       + 如果str具有连续的空白字符，则strsplit将它们视为一个空格

     + ```matlab
       C = strsplit(str,delimiter)
       ```

       + 在delimiter指定的分隔符处拆分str
       + 如果str具有连续的分隔符，并且它们之间没有其他字符，则strsplit将它们视为一个分隔符
         + 例如，strsplit('Hello,world',',')和strsplit('Hello,,,world',',')返回相同的输出

     + ```matlab
       C = strsplit(str,delimiter,Name,Value)
       ```

       + 使用一个或多个名称-值对组参数指定其他分隔符选项
         + 例如，要将连续分隔符视为单独的分隔符，可以指定 'CollapseDelimiters','false'

     + ```matlab
       [C,matches] = strsplit(__)
       ```

       + 同时返还数组matches

         matches输出参数包含strsplit拆分str时遇到的所有分隔符

       + 可以将此语法与前面语法中的任何输入参数结合使用

   + 实例

     ```matlab
     str = 'The rain in Spain.';
     C = strsplit(str)
     ```

     输出：

     ```matlab
     C = 
     
         'The'    'rain'    'in'    'Spain.'
     ```

     ---

     ```matlab
     data = '1,2,3,4,,,5';
     C = strsplit(data,',')
     ```

     输出：

     ```matlab
     C = 
     
         '1'    '2'    '3'    '4'    '5'
     ```

   ---

2. strcmp

   + 功能

     比较字符串

   + 语法

     + ```matlab
       tf = strcmp(s1, s2)
       ```

       如果两者相同，则返回1（true），否则返回0（false）

       返回结果tf的数据类型为logical

       输入参数可以是字符串数组、字符向量和字符向量元胞数组的任何组合

   + 实例

     ---
     
     s1和s2都是字符串
     
     ```matlab
   s1 = 'Yes';
     s2 = 'Yes';
   tf = strcmp(s1,s2)
     ```
     
     输出：
     
     ```matlab
     tf =
     
          1
     ```
     
     ---
     
     s1是字符串，s2是cell型的数组
     
     ```matlab
     s='hello';
     c={'hello','matlab';'HELLO','matlab'};
     TF=strcmp(s,c);
     disp(TF);
     ```
     
     输出
     
     ```
          1     0
          0     0
     ```
     
     ---
     
     



