# MATLABTips4--数学函数

1. floor

   + 朝负无穷大四舍五入

   + 语法

     + Y = floor(x)

       将x的每个元素四舍五入到小于或等于该元素的最接近整数

     + Y = floor(t)

       将duration数组t的每个元素四舍五入到小于或等于此元素的最接近的秒数

     + Y = floor(t,unit)

       将t的每个元素四舍五入到小于或等于此元素的最接近数（使用指定的时间单位）

---

2. mod

   + 除后取余   ==取模运算==

   + 语法

     + b = mod(a,m)

       用m除a后的余数，a为被除数，m为除数

---

3. num2str

   + 将数字转换为字符数组

   + 语法

     + s = num2str(A)

       将数值数组转换为表示数字的字符数组

       输出格式取决于原始值得量级

     + s = num2str(A,precision)

       返回表示数字的字符数组，最大有效位数由precision指定

       + 例

         ```matlab
         A = 12.3456;
         S = num2str(A,3)
         ```

         输出：12.3

     + s = num2str(A,formatSpec)

       将formatSpec指定的格式应用到A所有元素

       + 例

         ```matlab
         i = 11;
         M = num2str(i,'%03d')
         ```

         输出：011