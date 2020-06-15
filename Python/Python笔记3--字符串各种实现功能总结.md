## Python笔记3--字符串各种实现功能总结

1. 字符串比较

   + 利用operator模块方法比较（python3.X取消了cmp函数） 
     + lt(a, b)   小于 
     + le(a, b)   小于等于 
     + eq(a, b)   等于 
     + ne(a, b)   不等于 
     + ge(a, b)   大于等于 
     + gt(a, b)   大于  

   ```python
   import operator  
   operator.eq('abc','edf') #根据ASCII码比较  
   #Flase  
   operator.gt('abc','ab')  
   #True 
   ```

   ---

   + 关系运算符比较（>,<,>=,<=,==,!=） 

     ```python
     s1 = 'abc'  
     s2 = 'ab'  
     s1 > s2  
     #True
     ```

   ---

   + 用is, is not比较是否一样

     + is:用于比较两变量是否取自同一对象

     详解链接：[https://www.jb51.net/article/131559.htm](https://www.jb51.net/article/131559.htm)

     **总之尽量少使用is**

--------
2. 字符串修改/截取/替换方法

   + 将字符串转换为列表(list)后更改之后再转换回字符串(join)

     ```python
     s='abcdef'
     s1=list(s)
     s1[4]='E'
     s=''.join(s1)
     print(s)
     #abcdEf
     ```

     ---

   + 通过切片截取部分字符串并连接

     ```python
     s='Hello World'
     s=s[:5]+s[6:]
     print(s)
     #HelloWorld
     ```

     ==注：s[:5]代表s[0]-s[4]==

     ---

   + 使用replace函数

     + str.replace(old,new[,max])

       old:旧子字符串

       new:替换的新子字符串

       max:可选字符串，替换不超过max次；若省略，默认替换所有旧子字符串

     ```python
     s='abcdef'
     s=s.replace('a','A')
     print(s)
     #Abcdef
     s=s.replace('def','DEF')
     print(s)
     #AbcDEF
     ```

--------
3. 修改字符串大小写
   + str.upper():将字符串变成大写形式
   + str.lower():将字符串变成小写形式

---

