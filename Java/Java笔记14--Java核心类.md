# Java笔记14--Java核心类

## 字符串

### String

* `String`是一个引用类型，它本身也是一个`class`。

* 但是，Java编译器对`String`有特殊处理，即可以直接用`"..."`来表示一个字符串：

  ```java
  String s1 = "Hello!";
  ```

* **实际上字符串在`String`内部是通过一个`char[]`数组表示的**，因此，按下面的写法也是可以的：

  ```java
  String s2 = new String(new char[] {'H', 'e', 'l', 'l', 'o', '!'});
  ```

* Java字符串的一个重要特点就是**字符串*不可变***。

  这种不可变性是通过内部的`private final char[]`字段，以及没有任何修改`char[]`的方法实现的。

* 示例

  ```java
  public class Main {
      public static void main(String[] args) {
          String s = "Hello";
          System.out.println(s);
          s = s.toUpperCase();
          System.out.println(s);
      }
  }
  ```

  * String是引用类型，s.toUpperCase()开辟了新的内存空间存放“HELLO”，s的指向转向了新的“HELLO”，但原来内存空间的“Hello”仍未变

### 字符串比较

* 当我们想要比较两个字符串是否相同时，要特别注意，我们实际上是想比较字符串的内容是否相同。

* **必须使用`equals()`方法而不能用`==`**。

* 示例

  ```java
  public class Main {
      public static void main(String[] args) {
          String s1 = "hello";
          String s2 = "hello";
          System.out.println(s1 == s2);
          System.out.println(s1.equals(s2));
      }
  }
  ```

  ```java
  true
  true
  ```

  从表面上看，两个字符串用`==`和`equals()`比较都为`true`

  但实际上那只是**Java编译器在编译期，会自动把所有相同的字符串当作一个对象放入常量池**，自然`s1`和`s2`的引用就是相同的。

  所以，这种`==`比较返回`true`纯属巧合。

  换一种写法，`==`比较就会失败：

  ```java
  public class Main {
      public static void main(String[] args) {
          String s1 = "hello";
          String s2 = "HELLO".toLowerCase();
          System.out.println(s1 == s2);
          System.out.println(s1.equals(s2));
      }
  }
  ```

  ```java
  false
  true
  ```

* **要忽略大小写比较，使用`equalsIgnoreCase()`方法。**

### 搜索子串

* str.contains() : 判断是否包含子串

  ```java
  "Hello".contains("ll"); // true
  ```

  注意到`contains()`方法的参数是`CharSequence`而不是`String`，因为**`CharSequence`是`String`的父类**。

* str.indexOf() : 查找子串第一次出现的位置

  ```java
  "Hello".indexOf("lo"); // 3
  ```

  ```java
  "abcdebcdfcd".indexOf("cd", 2) // 2
  ```

  ```java
  "abcdebcdfcd".indexOf("cd", 3) // 6
  ```

* str.lastIndexOf() : 查找子串最后最后一次出现的位置

  ```java
  "Hello".lastIndexOf("l"); // 3
  ```

  ```java
  System.out.println("abcdebcdfcd".lastIndexOf("cd")); // 9
  System.out.println("abcdebcdfcd".lastIndexOf("cd", 9)); // 9
  System.out.println("abcdebcdfcd".lastIndexOf("cd", 8)); // 6
  ```

* str.startsWith() : 判断是否以子串开头

  ```java
  "Hello".startsWith("He"); // true
  ```

* str.endsWith() : 判断是否以子串结尾

  ```java
  "Hello".endsWith("lo"); // true
  ```

### 提取子串

* str.substring() : 提取子串

  区间：左必右开，和python一致

  ```java
  "Hello".substring(2); // "llo"
  "Hello".substring(2, 4); // "ll"
  ```

### 去除收尾空白字符

* 空白字符包括空格，`\t`，`\r`，`\n`

* 使用`trim()`方法可以移除字符串首尾空白字符：

  ```java
  "  \tHello\r\n ".trim(); // "Hello"
  ```

  **`trim()`并没有改变字符串的内容，而是返回了一个新字符串**

* 另一个`strip()`方法也可以移除字符串首尾空白字符。

  它和`trim()`不同的是，类似中文的空格字符`\u3000`也会被移除：

  ```java
  "\u3000Hello\u3000".strip(); // "Hello"
  " Hello ".stripLeading(); // "Hello "
  " Hello ".stripTrailing(); // " Hello"
  ```

  * 只删除开头空白字符

    ```java
    " Hello ".stripLeading(); // "Hello "
    ```

  * 只删除结尾空白字符

    ```java
    " Hello ".stripTrailing(); // " Hello"
    ```

### 判断是否为空和空字符串

* `String`提供了`isEmpty()`来判断字符串是否为空：

  ```java
  "".isEmpty(); // true，因为字符串长度为0
  "  ".isEmpty(); // false，因为字符串长度不为0
  ```

* `String`提供了`isBlank()`来判断字符串是否为空字符串：

  ```java
  "  \n".isBlank(); // true，因为只包含空白字符
  " Hello ".isBlank(); // false，因为包含非空白字符
  ```

### 替换子串

* 一种是根据字符或字符串替换：

  ```java
  String s = "hello";
  s.replace('l', 'w'); // "hewwo"，所有字符'l'被替换为'w'
  s.replace("ll", "~~"); // "he~~o"，所有子串"ll"被替换为"~~"
  ```

* 另一种是通过正则表达式替换：

  ```java
  String s = "A,,B;C ,D";
  s.replaceAll("[\\,\\;\\s]+", ","); // "A,B,C,D"
  ```

  上面的代码通过正则表达式，把匹配的子串统一替换为`","`

### 分割字符串

* 要分割字符串，使用`split()`方法，并且传入的也是正则表达式：

  ```java
  String s = "A,B,C,D";
  String[] ss = s.split("\\,"); // {"A", "B", "C", "D"}  字符串列表
  ```

### 拼接字符串

* 拼接字符串使用静态方法`join()`，它用指定的字符串连接字符串数组：

  ```java
  String[] arr = {"A", "B", "C"};
  String s = String.join("***", arr); // "A***B***C"
  ```

### 格式化字符串

* 字符串提供了`formatted()`方法和`format()`静态方法，可以传入其他参数，替换占位符，然后生成新的字符串：

  ```java
  public class Main {
      public static void main(String[] args) {
          String s = "Hi %s, your score is %d!";
          System.out.println(s.formatted("Alice", 80));
          System.out.println(String.format("Hi %s, your score is %.2f!", "Bob", 59.5));
      }
  }
  
  ```

  ```java
  Hi Alice, your score is 80!
  Hi Bob, your score is 59.50!
  ```

* 有几个占位符，后面就传入几个参数。
* 参数类型要和占位符一致。
* 常用的占位符有：
  - `%s`：显示字符串；
  - `%d`：显示整数；
  - `%x`：显示十六进制整数；
  - `%f`：显示浮点数。
* 占位符还可以带格式，例如`%.2f`表示显示两位小数。
* 如果你不确定用啥占位符，那就始终用`%s`，因为**`%s`可以显示任何数据类型**。

### 类型转换

* 把任意基本类型或引用类型转换为字符串

  * 可以使用静态方法`valueOf()`，这是一个重载方法，编译器会根据参数自动选择合适的方法：

    ```java
    String.valueOf(123); // "123"
    String.valueOf(45.67); // "45.67"
    String.valueOf(true); // "true"
    String.valueOf(new Object()); // 类似java.lang.Object@636be97c
    ```

* 把字符串转换为其他类型

  * 把字符串转换为`int`类型

    ```java
    int n1 = Integer.parseInt("123"); // 123
    int n2 = Integer.parseInt("ff", 16); // 按十六进制转换，255
    ```

    要特别注意，`Integer`有个`getInteger(String)`方法，它不是将字符串转换为`int`，而是把该字符串对应的系统变量转换为`Integer`：

    ```java
    Integer.getInteger("java.version"); // 版本号，11
    ```

  * 把字符串转换为`boolean`类型

    ```java
    boolean b1 = Boolean.parseBoolean("true"); // true
    boolean b2 = Boolean.parseBoolean("FALSE"); // false
    ```

### 转换为char[]

* `String`转换为`char[]`

  ```java
  char[] cs = "Hello".toCharArray(); // String -> char[]
  ```

* `char[]`转换为`String`

  ```java
  String s = new String(cs); // char[] -> String
  ```

* 如果修改了`char[]`数组，`String`并不会改变

  ```java
  public class Main {
      public static void main(String[] args) {
          char[] cs = "Hello".toCharArray();
          String s = new String(cs);
          System.out.println(s);
          cs[0] = 'X';
          System.out.println(s);
      }
  }
  ```

  这是因为通过`new String(char[])`创建新的`String`实例时，它并不会直接引用传入的`char[]`数组，而是会复制一份，所以，修改外部的`char[]`数组不会影响`String`实例内部的`char[]`数组，因为这是两个不同的数组。

* **从`String`的不变性设计可以看出，如果传入的对象有可能改变，我们需要复制而不是直接引用**

  ```java
  import java.util.Arrays;
  public class Main {
      public static void main(String[] args) {
          int[] scores = new int[] { 88, 77, 51, 66 };
          Score s = new Score(scores);
          s.printScores();
          scores[2] = 99;
          s.printScores();
      }
  }
  
  class Score {
      private int[] scores;
      public Score(int[] scores) {
          this.scores = scores;
      }
  
      public void printScores() {
          System.out.println(Arrays.toString(scores));
      }
  }
  ```

  ```java
  [88, 77, 51, 66]
  [88, 77, 99, 66]
  ```

  观察两次输出，由于`Score`内部直接引用了外部传入的`int[]`数组，这会造成外部代码对`int[]`数组的修改，影响到`Score`类的字段。如果外部代码不可信，这就会造成安全隐患。

  请修复`Score`的构造方法，使得外部代码对数组的修改不影响`Score`实例的`int[]`字段。

  ```java
  class Score {
      private int[] scores;
      public Score(int[] scores) {
          this.scores = Arrays.copyOf(scores, scores.length);
      }
  
      public void printScores() {
          System.out.println(Arrays.toString(scores));
      }
  }
  ```

## 字符编码

* ASCII编码

  在早期的计算机系统中，为了给字符编码，美国国家标准学会（American National Standard Institute：ANSI）制定了一套英文字母、数字和常用符号的编码，它占用一个字节，编码范围从`0`到`127`，最高位始终为`0`，称为**`ASCII`编码**。例如，字符`'A'`的编码是`0x41`，字符`'1'`的编码是`0x31`。

* GB2312编码

  如果要把汉字也纳入计算机编码，很显然一个字节是不够的。`GB2312`标准使用两个字节表示一个汉字，其中第一个字节的最高位始终为`1`，以便和`ASCII`编码区分开。例如，汉字`'中'`的**`GB2312`编码**是`0xd6d0`。

* 类似的，日文有`Shift_JIS`编码，韩文有`EUC-KR`编码，这些编码因为标准不统一，同时使用，就会产生冲突。

* Unicode编码

  为了统一全球所有语言的编码，全球统一码联盟发布了**`Unicode`编码**，它把世界上主要语言都纳入同一个编码，这样，中文、日文、韩文和其他语言就不会冲突。

* `Unicode`编码需要两个或者更多字节表示，我们可以比较中英文字符在`ASCII`、`GB2312`和`Unicode`的编码：

  * 英文字符`'A'`的`ASCII`编码和`Unicode`编码：

    ```ascii
             ┌────┐
    ASCII:   │ 41 │
             └────┘
             ┌────┬────┐
    Unicode: │ 00 │ 41 │
             └────┴────┘
    ```

    英文字符的`Unicode`编码就是简单地在前面添加一个`00`字节。

  * 中文字符`'中'`的`GB2312`编码和`Unicode`编码：

    ```ascii
             ┌────┬────┐
    GB2312:  │ d6 │ d0 │
             └────┴────┘
             ┌────┬────┐
    Unicode: │ 4e │ 2d │
             └────┴────┘
    ```

* UTF-8编码

  + 节省空间

    因为英文字符的`Unicode`编码高字节总是`00`，包含大量英文的文本会浪费空间，所以，出现了`UTF-8`编码，它是一种变长编码，用来把固定长度的`Unicode`编码变成1～4字节的变长编码。

    通过`UTF-8`编码，英文字符`'A'`的`UTF-8`编码变为`0x41`，正好和`ASCII`码一致，而中文`'中'`的`UTF-8`编码为3字节`0xe4b8ad`。

  * 容错能力强

    如果传输过程中某些字符出错，不会影响后续字符，因为`UTF-8`编码依靠高字节位来确定一个字符究竟是几个字节，它经常用来作为传输编码。

* 字符串编码转换

  * 在Java中，`char`类型实际上就是两个字节的`Unicode`编码。

  * 如果我们要手动把字符串转换成其他编码，可以这样做：

    ```java
    byte[] b1 = "Hello".getBytes(); // 按系统默认编码转换，不推荐
    byte[] b2 = "Hello".getBytes("UTF-8"); // 按UTF-8编码转换
    byte[] b2 = "Hello".getBytes("GBK"); // 按GBK编码转换
    byte[] b3 = "Hello".getBytes(StandardCharsets.UTF_8); // 按UTF-8编码转换
    ```
    
    注意：**转换编码后，就不再是`char`类型，而是`byte`类型表示的数组。**

* 把已知编码的`byte[]`转换为`String`

  ```java
  byte[] b = ...
  String s1 = new String(b, "GBK"); // 按GBK转换
  String s2 = new String(b, StandardCharsets.UTF_8); // 按UTF-8转换
  ```

* **始终牢记：Java的`String`和`char`在内存中总是以Unicode编码表示。**

### String优化方式

* 对于不同版本的JDK，`String`类在内存中有不同的优化方式。

* 早期JDK版本的`String`总是以`char[]`存储，它的定义如下：

  ```java
  public final class String {
      private final char[] value;
      private final int offset;
      private final int count;
  }
  ```

* 而较新的JDK版本的`String`则以`byte[]`存储

  如果`String`仅包含ASCII字符，则每个`byte`存储一个字符，否则，每两个`byte`存储一个字符，这样做的目的是为了节省内存，因为大量的长度较短的`String`通常仅包含ASCII字符

  ```java
  public final class String {
      private final byte[] value;
      private final byte coder; // 0 = LATIN1, 1 = UTF16
  ```

  对于使用者来说，`String`内部的优化不影响任何已有代码，因为它的`public`方法签名是不变的。

## StringBuilder



## StringJoiner



## 包装类型



## JavaBean



## 枚举



## 常用工具类



