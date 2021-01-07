# Python笔记21--切片(Slice)

### 说明

截取一个list或tuple或字符串的部分元素时可以使用切片(Slice)操作符简化操作

### 使用

+ 取一个序列的前三个元素

  ```python
  a = ['Hello', 'World', 15, 'Apple', None]
  b = a[0:3]
  print(b)
  c = ('Hello', 'World', 15, 'Apple', None)
  d = c[0:3]
  print(d)
  e = 'Hello World!'
  f = e[:3]
  print(f)
  ```

  ```python
  ['Hello', 'World', 15]
  ('Hello', 'World', 15)
  Hel
  ```

  + a[0:3]表示从索引0开始取，到索引3为止，但不包括索引3
  + 如果第一个索引是0，则可以省略写为a[:3]

+ 取一个序列的倒数三个元素

  ```python
  a = ['Hello', 'World', 15, 'Apple', None]
  b = a[-3:]
  print(b)a = ['Hello', 'World', 15, 'Apple', None]
  b = a[-3:]
  print(b)
  c = ('Hello', 'World', 15, 'Apple', None)
  d = c[-3:]
  print(d)
  e = 'Hello World!'
  f = e[-3:]
  print(f)
  ```

  ```python
  [15, 'Apple', None]
  (15, 'Apple', None)
  ld!
  ```

  + python 支持 a[-1]取倒数第一个元素

  ```python
  a = ['Hello', 'World', 15, 'Apple', None]
  b = a[-3:-1]
  print(b)
  ```

  ```python
  [15, 'Apple']
  ```

  + a[-3:-1]表示取倒数第三、第二个元素，不包括倒数第一个元素

+ 取一个序列的前十个数，每两个取一个

  ```python
  a = list(range(0, 100))
  b = a[:10:2]
  print(b)
  c = tuple(range(0,100))
  d = c[:10:2]
  print(d)
  e = ''
  for i in range(0,10):
      e += str(i)
  print(e)
  f = e[:10:2]
  print(f)
  ```

  ```python
  [0, 2, 4, 6, 8]
  (0, 2, 4, 6, 8)
  0123456789
  02468
  ```

+ 取一个序列的所有数，每五个取一个

  ```python
  a = list(range(0, 100))
  b = a[::5]
  print(b)
  c = tuple(range(0,100))
  d = c[::5]
  print(d)
  e = ''
  for i in range(0,10):
      e += str(i)
  print(e)
  f = e[::5]
  print(f)
  ```

  ```python
  [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
  (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95)
  0123456789
  05
  ```

+ 原样复制一个序列

  ```python
  a = list(range(0, 100))
  b = a[:]
  print(b)
  c = tuple(range(0, 100))
  d = a[:]
  print(d)
  e = ''
  for i in range(0,10):
      e += str(i)
  print(e)
  f = e[:]
  print(f)
  ```

  ```python
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
  0123456789
  0123456789
  ```

+ 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的`strip()`方法：

  ```python
  def trim(s):
      if s == '':
          return s
      else:
          if s[0] != ' ' and s[-1] != ' ':
              return s
          elif s[0] == ' ' and s[-1] != ' ':
              return trim(s[1:])
          elif s[0] != ' ' and s[-1] == ' ':
              return trim(s[:-1])
          else:
              return trim(s[1:-1])
  
  if trim('hello  ') != 'hello':
      print('测试失败!')
  elif trim('  hello') != 'hello':
      print('测试失败!')
  elif trim('  hello  ') != 'hello':
      print('测试失败!')
  elif trim('  hello  world  ') != 'hello  world':
      print('测试失败!')
  elif trim('') != '':
      print('测试失败!')
  elif trim('    ') != '':
      print('测试失败!')
  else:
      print('测试成功!')
  ```

  ```python
  测试成功!
  ```

  其他参考：

  ```python
  def trim(s):
      while len(s) > 0 and s[0] == ' ':
          s = s[1:]
      while len(s) > 0 and s[-1] == ' ':
          s = s[:-1]
      return s
  ```

  ```
  
  ```

  

