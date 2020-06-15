# Python笔记6--字符串大小写

1. 字符串大小写转换

   + data.title()

     所有单词首字母大写，其余小写

   + data.capitalize()

     字符串首字母大写，其余小写

   + data.upper()

     所有字母大写

   + data.lower()

     所有字母小写

2. 大小写转换实例

   ```python
   s = 'hEllo pYthon'
   print s.upper()
   print s.lower()
   print s.capitalize()
   print s.title()
   ```

   输出：

   ```python
   HELLO PYTHON
   hello python
   Hello python
   Hello Python
   ```

3. 大小写判断
   + data.isupper()
   + data.islower()
   + data.istitle()
   + 没有data.iscapitalize()方法

4. 大小写判断实例

   ```python
   print('ABCD'.isupper()) #true
   print('Abcd'.isupper()) #false
   print('abcd'.islower()) #true
   print('abcD'.islower()) #false
   print('Abcd'.istitle()) #true
   print('abCd'.istitle()) #false
   print('AbCd'.istitle()) #false
   ```

5. 实现iscapitalize()

   ```python
   import string
   notrans = string.maketrans('', '')
   def containsAny(str, strset):
       return len(strset) != len(strset.translate(notrans, str))
   def iscapitalized(s):
       return s == s.capitalize( ) and containsAny(s, string.letters)
   	#return s == s.capitalize( ) and len(s) > 0 #如果s为数字组成的字符串，这个方法将行不通
   ```

   

