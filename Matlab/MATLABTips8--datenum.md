# MATLABTips8--datenum

1. datenum

   + 将日期和时间转换为日期序列值

     datenum函数创建一个数值数组，将每个时间点表示为从0000年1月0日起的天数

     数值还能表示以天为单位的过去的时间

     日期序列值表示从某个固定的预设日期（0000年1月0日）以来的整个天数及其最小值

   + 语法

     + DateNumber = datenum(t)

       将输入数组t中的日期时间或持续时间值转换为日期序列值

     + DateNumber = datenum(DateString)

       将表示日期和时间的文本转换为日期序列值

     + DateNumber = datenum(DateString,formatIn)

       用formatIn指定文本的格式

       不含formatIn的语法的执行速度远远慢于包含此项的语法的执行速度

     + DateNumber = datenum(DateString,formatIn,PivotYear)

       使用formatIn解析DateString表示的日期和时间

       使用PivotYear解析以两个字符指定年份的文本

       可以按照任意顺序指定formatIn和PivotYear

     + DateNumber = datenum(DateVector)

       将日期向量解释为日期序列值，并返回由m个日期数字构成的列向量

       m是DateVector中日期向量的总数

     + DateNumber = datenum(Y,M,D)

       返回Y,M,D(年月日)数组的对应元素的日期序列值

       这些数组的大小必须相同

     + DateNumber = datenum(Y,M,D,H,MN,S)

       另外返回 `H`、`MN` 和 `S`（小时、分、秒）数组的对应元素的日期序列值

       这些数组的大小必须相同

       ==若出现一天中的小时，则在当天0时的基础上加上n/24==

2. 实例

   + datenum(now)

     7.3778e+05

   + datenum(2019,12,25)

     737784

   + datenum(2019,12,25,20,32,00)

     7.3778e+05

   + datenum('25-Dec-2019','dd-mmm-yyyy')

     737784

   + datenum('25-12-2019','dd-mm-yyyy')

     737784

   + datenum('25 Dec 2019 20:35:39')

     7.3778e+05





