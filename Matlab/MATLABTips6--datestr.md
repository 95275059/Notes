# MATLABTips6--datestr

1. datestr

   + 将日期和时间转换为字符串格式

   + 语法

     + DateString = datestr(t)

       + 将数组t中的日期和时间值转换为表示日期和时间的文本

       + datestr函数返回包含m行的字符数组

         m是t中日期时间值得总数

       + 默认情况下，datestr以day-month-year hour:minute:second格式返回文本

         如果hour:minute:second是00:00:00，则返回的文本格式为day-month-year

     + DateString = datestr(DateVector)

       + 将日期向量转换为表示日期和时间的文本

       + datestr函数返回包含m行的字符数组

         m是DateVector中的日期向量的总数

     + DateString = datestr(DateNumber)

       + 将日期序列值转换为表示日期和时间的文本

       + `datestr` 函数返回包含 `m` 行的字符数组

          `m` 是 `DateNumber` 中的日期值的总数

     + DateString = datestr(__,formatOut)

       + 使用formatOut指定输出文本的格式
       + 可以将 `formatOut` 与上述语法中的任何输入参数结合使用

     + DateString = datestr(DateStringIn)

       + 将 `DateStringIn` 转换为 day-month-year hour:minute:second 格式的文本
       + 以 `DateStringIn` 表示的所有日期和时间必须具有相同的格式

     + DateString = datestr(DateStringIn,formatOut,PivotYear)

       +以 `formatOut` 指定的格式将 `DateStringIn` 转换为 `DateString`

       使用可选的 `PivotYear` 解释以双字符形式指定年份的文本

     + DateString = datestr(__,'local')

       + 返回以当前区域设置的语言表示的日期，此语言是您通过计算机的操作系统选择的语言
       + 如果参数列表中不包括 `'local'`，则 `datestr` 以默认语言（美国英语）返回文本
       + `'local'` 可与上述的任何语法结合使用。`'local'` 参数必须排在参数序列的最后

2. 实例

   + datestr(now,21)

     Dec.25,2019 19:55:41

   + datestr(now,31)

     2019-12-25 19:59:54

   + datestr(now, 'dd mmm yyyy HH:MM:SS')

     25 Dec 2019 20:01:21

   + datestr(now,'yyyy HH:MM:SS mmm dd')

     2019 20:01:51 Dec 25

   

   

   