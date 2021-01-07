# Python2--语法基础1-数据类型

### Python数据类型

+ 数值类型

  + 整数（int）

    + 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

    + 整数的除法

      ```python
      print(10/3)
      print(10/2)
      print(10//3)
      print(10%3)
      ```

      ```python
      3.3333333333333335
      5.0
      3
      1
      ```

      + `/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
      + 还有一种除法是`//`，称为地板除，两个整数的除法仍然是整数，`//`除法只取结果的整数部分
      + 

  + 浮点数（float）

  + 复数(complex)

    a+bj 或者 a+bJ 或者 complex(a,b)

  + 特殊值
    + 正无穷

      ```python
      float('+inf')
      float('inf')
      float('Inf')
      float('INF')
      ```

      这些写法都可以

    + 负无穷

      ```python
      float('-inf')
      float('-Inf')
      float('-INF')
      ```

    + nan

      ```python
      float('nan')
      ```

      + 代表Not A Number（不是一个数），它并不等于0

      + 因为nan不是一个数，所以相关计算都无法得到数字。

      + 所有涉及nan的运算操作，返回的都是nan。

      + 所有涉及nan的比较操作，返回的都是false。

        因此`float('nan') == float('nan')`返回False，即两个float('nan')并不相等

    + 运算

      ```python
      print(0*float('inf'))
      print(float('inf') / float('inf'))
      print(float('-inf') / float('-inf'))
      print(float('inf') - float('inf'))
      print(float('-inf') - float('-inf'))
      ```

      ```python
      nan
      nan
      nan
      nan
      nan
      ```

    + 检测

      python中可以用math.isinf()与math.isnan()来判断数据是否为inf或nan。

      ```python
      import math
      n = float('inf')
      print(math.isinf(n))
      m = float('nan')
      print(math.isnan(m))
      ```

      ```python
      True
      True
      ```

      

+ 字符串

  + Python不支持字符类型，单字符被当作一个字符串使用。

  + 字符串是以单引号`'`或双引号`"`括起来的任意文本，比如`'abc'`，`"xyz"`等等。

  + 请注意，`''`或`""`本身只是一种表示方式，不是字符串的一部分，因此，字符串`'abc'`只有`a`，`b`，`c`这3个字符。

  + 如果`'`本身也是一个字符，那就可以用`""`括起来
  
    ```python
    print('a"v"b')
    print("I'm cxy")
    ```
  
    ```python
    a"v"b
    I'm cxy
    ```
  
  + 如果字符串内部既包含`'`又包含`"`怎么办？可以用转义字符`\`来标识
  
    ```python
    print('I\'m \"OK\"')
    ```
  
    ```python
    I'm "OK"
    ```

---

### 转义字符

+ 用反斜杠(\\)转义字符

+ 一些转义字符

  | 转义字符 | 说明   |
  | -------- | ------ |
  | \n       | 回车   |
  | \t       | 制表符 |
  | \f       | 换页   |
  | \000     | 空     |
  | \\\      | \      |

+ Python允许用`r''`或`R''`表示‘’内部的字符串默认不转义

  ```python
  print('\\\t\\')
  print(r'\\\t\\')
  ```

  ```python
  \	\
  \\\t\\
  ```

+ Python允许用`'''...'''`的格式表示多行内容

  ```python
  print('''line1
  line2
  line3
  ''')
  ```

  ```python
  line1
  line2
  line3
  ```

---

### 字符串运算符

```python
a="Hello" b="Python"
```

+ 字符串连接：a+b="HelloPython"

+ 重复输出字符串：a*2="HelloHello"

+ 成员运算符：
  + ‘H’ in a ==>True
  + ‘M’ not in a ==>True

---

### 字符串格式化

```python
print("我的名字是%s,年龄是%d" % ('cxy', 22))
```

---

### 布尔类型

+ 布尔值

  + False

    + 0

    + 空字符串 '' , ""

    + 空值 None 

    + 空集合

      包括空元组(),空序列[],空字典{};

  +  True

+ 布尔运算

  + 与运算and

    A and B

  + 或运算or

    A or B

  + 非运算not

    not A

---

### 类型转换

+ int(x);

+ float(x);

+ str(x);

+ chr(x):将整数ASCII码转换为一个字符；

+ ord(x):将一个字符转换为ASCII码；

+ bin(x):二进制；

+ oct(x):八进制；

+ hex(x):十六进制；

 

 

 

 

 

   
