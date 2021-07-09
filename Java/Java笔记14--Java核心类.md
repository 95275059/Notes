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
  
  这个方法在内部使用了`StringJoiner`来拼接字符串，在不需要指定“开头”和“结尾”的时候，用`String.join()`更方便

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

* Java编译器对`String`做了特殊处理，使得我们可以直接用`+`拼接字符串

* 但**对String对象的任何改变都不影响到原对象，相关的任何change操作都会生成新的对象**

  ```java
  String s = "";
  for (int i = 0; i < 1000; i++) {
      s = s + "," + i;
  }
  ```

  * 虽然可以直接拼接字符串，但是，在循环中，每次循环都会创建新的字符串对象，然后扔掉旧的字符串。

    string+="s"的操作事实上会自动被JVM优化成：

    　　StringBuilder str = new StringBuilder(string);

    　　str.append("s");

    　　str.toString();

  * 这样，绝大部分字符串都是临时对象，不但浪费内存，还会影响GC效率。

* Java标准库提供了`StringBuilder`，它是一个可变对象，可以预分配缓冲区

  这样，往`StringBuilder`中新增字符时，不会创建新的临时对象：

  ```java
  StringBuilder sb = new StringBuilder(1024);
  for (int i = 0; i < 1000; i++) {
      sb.append(',');
      sb.append(i);
  }
  String s = sb.toString();
  ```

* `StringBuilder`还可以进行链式操作：

  ```java
  public class Main {
      public static void main(String[] args) {
          var sb = new StringBuilder(1024);
          sb.append("Mr ")
            .append("Bob")
            .append("!")
            .insert(0, "Hello, ");
          System.out.println(sb.toString());
      }
  }
  ```

  ```java
  Hello, Mr Bob!
  ```

  如果我们查看`StringBuilder`的源码，可以发现，**进行链式操作的关键是，定义的`append()`方法会返回`this`，这样，就可以不断调用自身的其他方法。**

* 仿照`StringBuilder`，我们也可以设计支持链式操作的类。

  例如：一个可以不断增加的计数器

  ```java
  public class Main {
      public static void main(String[] args) {
          Adder adder = new Adder();
          adder.add(3)
               .add(5)
               .inc()
               .add(10);
          System.out.println(adder.value()); // 19
      }
  }
  
  class Adder {
      private int sum = 0;
  
      public Adder add(int n) {
          sum += n;
          return this;
      }
  
      public Adder inc() {
          sum ++;
          return this;
      }
  
      public int value() {
          return sum;
      }
  }
  ```

* 注意

  对于普通的字符串`+`操作，并不需要我们将其改写为`StringBuilder`，因为Java编译器在编译时就自动把多个连续的`+`操作编码为`StringConcatFactory`的操作。

  在运行期，`StringConcatFactory`会自动把字符串连接操作优化为数组复制或者`StringBuilder`操作。

## StringBuffer

* StringBuilder和StringBuffer类拥有的成员属性以及成员方法基本相同

* 区别是StringBuffer类的成员方法前面多了一个关键字：**synchronized**

  这个关键字是在多线程访问时起到**安全保护作用**的

* 即，**StringBuffer是线程安全的**

* String、StringBuilder、StringBuffer三者的执行效率

  * 当字符串相加操作或者改动较少的情况下，建议使用 String str="hello"这种形式；

  * 当字符串相加操作较多的情况下，建议使用StringBuilder
  * 如果采用了多线程，则使用StringBuffer

## String str="hello world"和String str=new String("hello world")的区别

* 示例

  ```java
  public class Main {
           
      public static void main(String[] args) {
          String str1 = "hello world";
          String str2 = new String("hello world");
          String str3 = "hello world";
          String str4 = new String("hello world");
           
          System.out.println(str1==str2);  // false
          System.out.println(str1==str3);  // true
          System.out.println(str2==str4);  // false
      }
  }
  ```

* 在class文件中有一部分 来存储**编译期间**生成的 **字面常量以及符号引用**，这部分叫做**class文件常量池**；在运行期间对应着方法区的**运行时常量池**。

* String str1 = "hello world";和String str3 = "hello world"; 都在编译期间生成了 字面常量和符号引用，运行期间字面常量"hello world"被存储在运行时常量池（当然只保存了一份）。

* 通过这种方式来将String对象跟引用绑定的话，JVM执行引擎会先在运行时常量池查找是否存在相同的字面常量，如果存在，则直接将引用指向已经存在的字面常量；否则在运行时常量池开辟一个空间来存储该字面常量，并将引用指向该字面常量。

* 而**通过new关键字来生成对象是在堆区进行的，而在堆区进行对象生成的过程是不会去检测该对象是否已经存在的**。因此**通过new来创建对象，创建出的一定是不同的对象，即使字符串的内容是相同的**。

## StringJoiner

* 由于用分隔符拼接数组的需求很常见，所以Java标准库还提供了一个`StringJoiner`来干这个事

  ```java
  public class Main {
      public static void main(String[] args) {
          String[] names = {"Bob", "Alice", "Grace"};
          var sj = new StringJoiner(", ");
          for (String name : names) {
              sj.add(name);
          }
          System.out.println(sj.toString());  // Bob, Alice, Grace
      }
  }
  ```

* 指定StringJoiner类型字符串指定开头和结尾

  ```java
  public class Main {
      public static void main(String[] args) {
          String[] names = {"Bob", "Alice", "Grace"};
          var sj = new StringJoiner(", ", "Hello ", "!");
          for (String name : names) {
              sj.add(name);
          }
          System.out.println(sj.toString());  // Hello Bob, Alice, Grace!
      }
  }
  ```

## 包装类型

### 包装类

* Java的数据类型分两种：

  - 基本类型：`byte`，`short`，`int`，`long`，`boolean`，`float`，`double`，`char`

    不能赋值为null，有各自默认值

  - 引用类型：所有`class`和`interface`类型

    可以赋值为null

* 包装类（Wrapper Class）

  基本类型转换为对应的引用类型称为对应的包装类

  * 示例：int -> Integer

    ```java
    public class Integer {
        private int value;
    
        public Integer(int value) {
            this.value = value;
        }
    
        public int intValue() {
            return this.value;
        }
    }
    ```

    int 和 Integer相互转换：

    ```java
    Integer n = null;
    Integer n2 = new Integer(99);
    int n3 = n2.intValue();
    ```

* Java核心库为每种基本类型都提供了对应的包装类型

  | 基本类型 | 对应的引用类型      |
  | :------- | :------------------ |
  | boolean  | java.lang.Boolean   |
  | byte     | java.lang.Byte      |
  | short    | java.lang.Short     |
  | int      | java.lang.Integer   |
  | long     | java.lang.Long      |
  | float    | java.lang.Float     |
  | double   | java.lang.Double    |
  | char     | java.lang.Character |

* 示例

  ```java
  public class Main {
      public static void main(String[] args) {
          int i = 100;
          // 通过new操作符创建Integer实例(不推荐使用,会有编译警告):
          Integer n1 = new Integer(i);
          // 通过静态方法valueOf(int)创建Integer实例:
          Integer n2 = Integer.valueOf(i);
          // 通过静态方法valueOf(String)创建Integer实例:
          Integer n3 = Integer.valueOf("100");
          System.out.println(n3.intValue());
      }
  }
  ```

* **所有的整数和浮点数的包装类型都继承自`Number`**，因此，可以非常方便地**直接通过包装类型获取各种基本类型**：

  ```java
  // 向上转型为Number:
  Number num = new Integer(999);
  // 获取byte, int, long, float, double:
  byte b = num.byteValue();
  int n = num.intValue();
  long ln = num.longValue();
  float f = num.floatValue();
  double d = num.doubleValue();
  ```

  

### Auto Boxing

* Java编译器可以帮助我们自动在`int`和`Integer`之间转型：

  ```java
  Integer n = 100; // 编译器自动使用Integer.valueOf(int)
  int x = n; // 编译器自动使用Integer.intValue()
  ```

* 这种直接把`int`变为`Integer`的赋值写法，称为**自动装箱（Auto Boxing）**，反过来，把`Integer`变为`int`的赋值写法，称为**自动拆箱（Auto Unboxing）**。

* **自动装箱和自动拆箱只发生在编译阶段，目的是为了少写代码**

* 装箱和拆箱会影响代码的执行效率，因为编译后的`class`代码是严格区分基本类型和引用类型的。

* 并且，自动拆箱执行时可能会报`NullPointerException`：

  ```java
  public class Main {
      public static void main(String[] args) {
          Integer n = null;
          int i = n;
      }
  }
  ```

### 不变类

* 所有的包装类型都是不变类。

  ```java
  // Integer的源码
  public final class Integer {
      private final int value;
  }
  ```

  因此，一旦创建了`Integer`对象，该对象就是不变的

* 对两个`Integer`实例进行比较要特别注意：**绝对不能用`==`比较，因为`Integer`是引用类型，必须使用`equals()`比较**：

  ```java
  public class Main {
      public static void main(String[] args) {
          Integer x = 127;
          Integer y = 127;
          Integer m = 99999;
          Integer n = 99999;
          System.out.println("x == y: " + (x==y)); // true
          System.out.println("m == n: " + (m==n)); // false
          System.out.println("x.equals(y): " + x.equals(y)); // true
          System.out.println("m.equals(n): " + m.equals(n)); // true
      }
  }
  ```

  因为`Integer`是不变类，编译器把`Integer x = 127;`自动变为`Integer x = Integer.valueOf(127);`，为了节省内存，`Integer.valueOf()`对于较小的数，始终返回相同的实例，因此，`==`比较“恰好”为`true`

  但我们*绝不能*因为Java标准库的`Integer`内部有缓存优化就用`==`比较，必须用`equals()`方法比较两个`Integer`。

* 因为`Integer.valueOf()`可能始终返回同一个`Integer`实例，因此，在我们自己创建`Integer`的时候，以下两种方法：

  * 方法1：`Integer n = new Integer(100);`
  * 方法2：`Integer n = Integer.valueOf(100);`

  方法2更好，因为方法1总是创建新的`Integer`实例，方法2把内部优化留给`Integer`的实现者去做，即使在当前版本没有优化，也有可能在下一个版本进行优化。

* 我们把能创建“新”对象的静态方法称为静态工厂方法。

  `Integer.valueOf()`就是静态工厂方法，它尽可能地返回缓存的实例以节省内存。

  **创建新对象时，优先选用静态工厂方法而不是new操作符**。

  如果我们考察`Byte.valueOf()`方法的源码，可以看到，**标准库返回的`Byte`实例全部是缓存实例**，但调用者并不关心静态工厂方法以何种方式创建新实例还是直接返回缓存的实例。

### 进制转化

* 静态方法`parseInt()`可以把字符串解析成一个整数

  ```java
  int x1 = Integer.parseInt("100"); // 100
  int x2 = Integer.parseInt("100", 16); // 256,因为按16进制解析
  ```

* 转化为指定进制的字符串

  ```java
  public class Main {
      public static void main(String[] args) {
          System.out.println(Integer.toString(100)); // "100",表示为10进制
          System.out.println(Integer.toString(100, 36)); // "2s",表示为36进制
          System.out.println(Integer.toHexString(100)); // "64",表示为16进制
          System.out.println(Integer.toOctalString(100)); // "144",表示为8进制
          System.out.println(Integer.toBinaryString(100)); // "1100100",表示为2进制
      }
  }
  ```

  注意：上述方法的输出都是`String`，在计算机内存中，只用二进制表示，不存在十进制或十六进制的表示方法。

  `int n = 100`在内存中总是以4字节的二进制表示：

  ```ascii
  ┌────────┬────────┬────────┬────────┐
  │00000000│00000000│00000000│01100100│
  └────────┴────────┴────────┴────────┘
  ```

  我们经常使用的`System.out.println(n);`是依靠核心库自动把整数格式化为10进制输出并显示在屏幕上，使用`Integer.toHexString(n)`则通过核心库自动把整数格式化为16进制。

  这里我们注意到**程序设计的一个重要原则：数据的存储和显示要分离**。

* Java的包装类型还定义了一些有用的静态变量

  ```java
  // boolean只有两个值true/false，其包装类型只需要引用Boolean提供的静态字段:
  Boolean t = Boolean.TRUE;
  Boolean f = Boolean.FALSE;
  // int可表示的最大/最小值:
  int max = Integer.MAX_VALUE; // 2147483647
  int min = Integer.MIN_VALUE; // -2147483648
  // long类型占用的bit和byte数量:
  int sizeOfLong = Long.SIZE; // 64 (bits)
  int bytesOfLong = Long.BYTES; // 8 (bytes)
  ```

### 处理无符号整型

* 在Java中，并没有无符号整型（Unsigned）的基本数据类型。

  `byte`、`short`、`int`和`long`都是带符号整型，最高位是符号位。

  而C语言则提供了CPU支持的全部数据类型，包括无符号整型。

* **无符号整型和有符号整型的转换在Java中就需要借助包装类型的静态方法完成。**

* 示例：把一个负的`byte`按无符号整型转换为`int`：

  byte是有符号整型，范围是`-128`~`+127`，但如果把`byte`看作无符号整型，它的范围就是`0`~`255`。

  ```java
  public class Main {
      public static void main(String[] args) {
          byte x = -1;
          byte y = 127;
          System.out.println(Byte.toUnsignedInt(x)); // 255
          System.out.println(Byte.toUnsignedInt(y)); // 127
      }
  }
  ```

  因为`byte`的`-1`的二进制表示是`11111111`，以无符号整型转换后的`int`就是`255`。

## JavaBean

* 在Java中，有很多class的定义都符合这样的规范：
	* 若干private实例字段；
	* 通过public方法来读写实例字段。
```java
public class Person {
    private String name;
    private int age;

    public String getName() { return this.name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return this.age; }
    public void setAge(int age) { this.age = age; }
}
```
* 如果读写方法符合以下这种命名规范,那么这种class被称为JavaBean：

  ```java
  // 读方法:
  public Type getXyz()
  // 写方法:
  public void setXyz(Type value)
  ```

  上面的字段是xyz，那么读写方法名分别以get和set开头，并且后接大写字母开头的字段名Xyz，因此两个读写方法名分别是getXyz()和setXyz()。

* boolean字段比较特殊，它的读方法一般命名为isXyz():

  ```java
  // 读方法:
  public boolean isChild()
  // 写方法:
  public void setChild(boolean value)
  ```

* 我们通常把一组对应的**读方法（getter）**和**写方法（setter）**称为**属性（property）**
	* 例如，name属性
		* 对应的读方法是String getName();
		* 对应的写方法是setName(String)
	
* 只有getter的属性称为只读属性（read-only）
	* 例如，定义一个age只读属性
		* 对应的读方法是int getAge()
		* 无对应的写方法setAge(int)
	
* 类似的，只有setter的属性称为只写属性（write-only）

* 很明显，只读属性很常见，只写属性不常见。 

* 属性只需要定义getter和setter方法，不一定需要对应的字段。
  例如，child只读属性定义如下：

  ```java
  public class Person {
      private String name;
      private int age;
  
      public String getName() { return this.name; }
      public void setName(String name) { this.name = name; }
  
      public int getAge() { return this.age; }
      public void setAge(int age) { this.age = age; }
  
      public boolean isChild() {
          return age <= 6;
      }
  }
  ```

  可以看出，getter和setter也是一种数据封装的方法。

### JavaBean的作用
* JavaBean主要用来传递数据，即把一组数据组合成一个JavaBean便于传输。

* 此外，JavaBean可以方便地被IDE工具分析，生成读写属性的代码，主要用在图形界面的可视化设计中。

* IDE自动生成JavaBean方法代码
  例如，在Eclipse中，先输入以下代码：

  ```java
  public class Person {
      private String name;
      private int age;
  }
  ```

  然后，点击右键，在弹出的菜单中选择“Source”，“Generate Getters and Setters”
  在弹出的对话框中选中需要生成getter和setter方法的字段，点击确定即可由IDE自动完成所有方法代码。

### 枚举JavaBean属性
* 要枚举一个JavaBean的所有属性，可以直接使用Java核心库提供的Introspector：
```java
import java.beans.*;
public class Main {
    public static void main(String[] args) throws Exception {
        BeanInfo info = Introspector.getBeanInfo(Person.class);
        for (PropertyDescriptor pd : info.getPropertyDescriptors()) {
            System.out.println(pd.getName());
            System.out.println("  " + pd.getReadMethod());
            System.out.println("  " + pd.getWriteMethod());
        }
    }
}

class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```
```java
age 
  public int Person.getAge() 
  public void Person.setAge(int) 
class 
  public final native java.lang.Class java.lang.Object.getClass() 
  null 
name 
  public java.lang.String Person.getName() 
  public void Person.setName(java.lang.String) 
```
运行上述代码，可以列出所有的属性，以及对应的读写方法。
注意class属性是从Object继承的getClass()方法带来的。

## 枚举

* 在Java中，我们可以通过static final来定义常量。
  例如，我们希望定义周一到周日这7个常量，可以用7个不同的int表示：

  ```java
  public class Weekday {
      public static final int SUN = 0;
      public static final int MON = 1;
      public static final int TUE = 2;
      public static final int WED = 3;
      public static final int THU = 4;
      public static final int FRI = 5;
      public static final int SAT = 6;
  }
  ```

  使用常量的时候，可以这么引用：

  ```java
  if (day == Weekday.SAT || day == Weekday.SUN) {
      // TODO: work at home
  }
  ```

* 也可以把常量定义为字符串类型
  例如，定义3种颜色的常量：

  ```java
  public class Color {
      public static final String RED = "r";
      public static final String GREEN = "g";
      public static final String BLUE = "b";
  }
  ```

  使用常量的时候，可以这么引用：

  ```java
  String color = ...
  if (Color.RED.equals(color)) {
      // TODO:
  }
  ```

* 无论是int常量还是String常量，使用这些常量来表示一组枚举值的时候，有一个严重的问题就是，编译器无法检查每个值的合理性。

  ```java
  if (weekday == 6 || weekday == 7) {
      if (tasks == Weekday.MON) {
          // TODO:
      }
  }
  ```

  上述代码编译和运行均不会报错，但存在两个问题：

  * 注意到Weekday定义的常量范围是0~6，并不包含7，编译器无法检查不在枚举中的int值；
  * 定义的常量仍可与其他变量比较，但其用途并非是枚举星期值。

### enum
* 为了让编译器能自动检查某个值在枚举的集合内，并且，不同用途的枚举需要不同的类型来标记，不能混用，我们可以使用enum来定义枚举类：

  ```java
  public class Main {
      public static void main(String[] args) {
          Weekday day = Weekday.SUN;
          if (day == Weekday.SAT || day == Weekday.SUN) {
              System.out.println("Work at home!");
          } else {
              System.out.println("Work at office!");
          }
      }
  }
  
  enum Weekday {
      SUN, MON, TUE, WED, THU, FRI, SAT;
  }
  ```

  注意到定义枚举类是通过关键字enum实现的，我们只需依次列出枚举的常量名。

* 和int定义的常量相比，使用enum定义枚举有如下好处：
  * 首先，enum常量本身带有类型信息，即Weekday.SUN类型是Weekday，编译器会自动检查出类型错误。例如，下面的语句不可能编译通过：

    ```java
    int day = 1;
    if (day == Weekday.SUN) { // Compile error: bad operand types for binary operator '=='
    }
    ```

  * 其次，不可能引用到非枚举的值，因为无法通过编译。

  * 最后，不同类型的枚举不能互相比较或者赋值，因为类型不符。

    例如，不能给一个Weekday枚举类型的变量赋值为Color枚举类型的值：

    ```java
    Weekday x = Weekday.SUN; // ok!
    Weekday y = Color.RED; // Compile error: incompatible types
    ```

  这就使得编译器可以在编译期自动检查出所有可能的潜在错误。

### enum的比较
* **使用enum定义的枚举类是一种引用类型。**

* 前面我们讲到，引用类型比较，要使用equals()方法，如果使用==比较，它比较的是两个引用类型的变量是否指同一个对象。

* 因此，引用类型比较，要始终使用equals()方法，但enum类型可以例外。

* **这是因为enum类型的每个常量在JVM中只有一个唯一实例，所以可以直接用==比较**：

  ```java
  if (day == Weekday.FRI) { // ok!
  }
  if (day.equals(Weekday.SUN)) { // ok, but more code!
  }
  ```

### enum类型
* 通过enum定义的枚举类，和其他的class有什么区别？
	答案是没有任何区别。
	enum定义的类型就是class，只不过它有以下几个特点：
	* 	定义的enum类型总是继承自java.lang.Enum，且无法被继承；
	* 	只能定义出enum的实例，而无法通过new操作符创建enum的实例；
	* 	定义的每个实例都是引用类型的唯一实例；
	* 	可以将enum类型用于switch语句。
	
* 例如，我们定义的Color枚举类：

  ```java
  public enum Color {
      RED, GREEN, BLUE;
  }
  ```

  编译器编译出的class大概就像这样：

  ```java
  public final class Color extends Enum { // 继承自Enum，标记为final class
      // 每个实例均为全局唯一:
      public static final Color RED = new Color();
      public static final Color GREEN = new Color();
      public static final Color BLUE = new Color();
      // private构造方法，确保外部无法调用new操作符:
      private Color() {}
  }
  ```

  所以，编译后的enum类和普通class并没有任何区别。
  但是我们自己无法按定义普通class那样来定义enum，必须使用enum关键字，这是Java语法规定的。

* 因为enum是一个class，每个枚举的值都是class实例

  因此，这些实例有一些方法：

  ```java
  // 返回常量名
  String s = Weekday.SUN.name(); // "SUN"
  // 返回定义的常量的顺序，从0开始计数
  int n = Weekday.MON.ordinal(); // 1
  ```

* **新增的常量必须放在最后。**
  改变枚举常量定义的顺序就会导致ordinal()返回值发生变化。
  如果在代码中编写了类似if(x.ordinal()==1)这样的语句，就要保证enum的枚举顺序不能变。

* **Weekday的枚举常量如果要和int转换，不推荐使用ordinal**

* 但是，如果不小心修改了枚举的顺序，编译器是无法检查出这种逻辑错误的。

* 要编写健壮的代码，就不要依靠`ordinal()`的返回值。

* 因为`enum`本身是`class`，所以我们可以定义`private`的构造方法，并且，给每个枚举常量添加字段：

  ```java
  public class Main {
      public static void main(String[] args) {
          Weekday day = Weekday.SUN;
          if (day.dayValue == 6 || day.dayValue == 0) {
              System.out.println("Work at home!");
          } else {
              System.out.println("Work at office!");
          }
      }
  }
  
  enum Weekday {
      MON(1), TUE(2), WED(3), THU(4), FRI(5), SAT(6), SUN(0);
  
      public final int dayValue;
  
      private Weekday(int dayValue) {
          this.dayValue = dayValue;
      }
  }
  ```

  这样就无需担心顺序的变化，新增枚举常量时，也需要指定一个`int`值。

  **注意：枚举类的字段也可以是非final类型，即可以在运行期修改，但是不推荐这样做！**

* 默认情况下，对枚举常量调用`toString()`会返回和`name()`一样的字符串。

  但是，`toString()`可以被覆写，而`name()`则不行。

  我们可以给`Weekday`添加`toString()`方法：

  ```java
  public class Main {
      public static void main(String[] args) {
          Weekday day = Weekday.SUN;
          if (day.dayValue == 6 || day.dayValue == 0) {
              System.out.println("Today is " + day + ". Work at home!");
          } else {
              System.out.println("Today is " + day + ". Work at office!");
          }
      }
  }
  
  enum Weekday {
      MON(1, "星期一"), TUE(2, "星期二"), WED(3, "星期三"), THU(4, "星期四"), FRI(5, "星期五"), SAT(6, "星期六"), SUN(0, "星期日");
  
      public final int dayValue;
      private final String chinese;
  
      private Weekday(int dayValue, String chinese) {
          this.dayValue = dayValue;
          this.chinese = chinese;
      }
  
      @Override
      public String toString() {
          return this.chinese;
      }
  }
  ```

  ```java
  Today is 星期日. Work at home!
  ```

  覆写`toString()`的目的是在输出时更有可读性。

  注意：判断枚举常量的名字，要始终使用name()方法，绝不能调用toString()！

### switch

* 枚举类可以应用在`switch`语句中。

* 因为枚举类天生具有类型信息和有限个枚举常量，所以比`int`、`String`类型更适合用在`switch`语句中：

  ```java
  public class Main {
      public static void main(String[] args) {
          Weekday day = Weekday.SUN;
          switch(day) {
          case MON:
          case TUE:
          case WED:
          case THU:
          case FRI:
              System.out.println("Today is " + day + ". Work at office!");
              break;
          case SAT:
          case SUN:
              System.out.println("Today is " + day + ". Work at home!");
              break;
          default:
              throw new RuntimeException("cannot process " + day);
          }
      }
  }
  
  enum Weekday {
      MON, TUE, WED, THU, FRI, SAT, SUN;
  }
  
  ```

  加上`default`语句，可以在漏写某个枚举常量时自动报错，从而及时发现错误。

## 记录类

### 不变类

* 一个不变类具有以下特点：

  * 定义class时使用`final`，无法派生子类；
  * 每个字段使用`final`，保证创建实例后无法修改任何字段。

* 假设我们希望定义一个`Point`类，有`x`、`y`两个变量，同时它是一个不变类，可以这么写：

  ```java
  public final class Point {
      private final int x;
      private final int y;
  
      public Point(int x, int y) {
          this.x = x;
          this.y = y;
      }
  
      public int x() {
          return this.x;
      }
  
      public int y() {
          return this.y;
      }
  }
  ```

* 为了保证不变类的比较，还需要正确覆写`equals()`和`hashCode()`方法，这样才能在集合类中正常使用。

* 后续我们会详细讲解正确覆写`equals()`和`hashCode()`，这里演示`Point`不变类的写法目的是，这些代码写起来都非常简单，但是很繁琐。

### record

* 从Java 14开始，引入了新的`Record`类。

* 我们定义`Record`类时，使用关键字`record`。

* 把上述`Point`类改写为`Record`类，代码如下：

  ```java
  public class Main {
      public static void main(String[] args) {
          Point p = new Point(123, 456);
          System.out.println(p.x());
          System.out.println(p.y());
          System.out.println(p);
      }
  }
  
  public record Point(int x, int y) {}
  ```

  仔细观察`Point`的定义：

  ```java
  public record Point(int x, int y) {}
  ```

  把上述定义改写为class，相当于以下代码：

  ```java
  public final class Point extends Record {
      private final int x;
      private final int y;
  
      public Point(int x, int y) {
          this.x = x;
          this.y = y;
      }
  
      public int x() {
          return this.x;
      }
  
      public int y() {
          return this.y;
      }
  
      public String toString() {
          return String.format("Point[x=%s, y=%s]", x, y);
      }
  
      public boolean equals(Object o) {
          ...
      }
      public int hashCode() {
          ...
      }
  }
  ```

* 除了用`final`修饰class以及每个字段外，编译器还自动为我们创建了构造方法，和字段名同名的方法，以及覆写`toString()`、`equals()`和`hashCode()`方法。

* 换句话说，使用`record`关键字，可以一行写出一个不变类。

* 和`enum`类似，**我们自己不能直接从`Record`派生，只能通过`record`关键字由编译器实现继承。**

### 构造方法

* 编译器默认按照`record`声明的变量顺序自动创建一个构造方法，并在方法内给字段赋值。

* 那么问题来了，如果我们要检查参数，应该怎么办？

  假设`Point`类的`x`、`y`不允许负数，我们就得给`Point`的构造方法加上检查逻辑：

  ```java
  public record Point(int x, int y) {
      public Point {
          if (x < 0 || y < 0) {
              throw new IllegalArgumentException();
          }
      }
  }
  ```

  注意到方法`public Point {...}`被称为Compact Constructor，它的目的是让我们编写检查逻辑

  编译器最终生成的构造方法如下：

  ```java
  public final class Point extends Record {
      public Point(int x, int y) {
          // 这是我们编写的Compact Constructor:
          if (x < 0 || y < 0) {
              throw new IllegalArgumentException();
          }
          // 这是编译器继续生成的赋值代码:
          this.x = x;
          this.y = y;
      }
      ...
  }
  ```

* 作为`record`的`Point`仍然可以添加静态方法。

* **一种常用的静态方法是`of()`方法**，用来创建`Point`：

  ```java
  public record Point(int x, int y) {
      public static Point of() {
          return new Point(0, 0);
      }
      public static Point of(int x, int y) {
          return new Point(x, y);
      }
  }
  ```

  这样我们可以写出更简洁的代码：

  ```java
  var z = Point.of();
  var p = Point.of(123, 456);
  ```

### 测试

```java
public class Main {
	public static void main(String[] args) {
		Point a = Point.of();
		Point b = Point.of(1,2);
		Point c = Point.of();
		Point d = Point.of(1,2);
		System.out.println(a.x());
		System.out.println(b.y());
		System.out.println(a.equals(b));
		System.out.println(a.equals(c));
		System.out.println(b.equals(d));
	}
}
```

```java
0
2
false
true
true
```

## BigInteger

* 在Java中，由CPU原生提供的整型最大范围是64位`long`型整数。

* 使用`long`型整数可以直接通过CPU指令进行计算，速度非常快。

* 如果我们使用的整数范围超过了`long`型怎么办？

  这个时候，就只能用软件来模拟一个大整数。

* `java.math.BigInteger`就是用来表示任意大小的整数。

* `BigInteger`内部用一个`int[]`数组来模拟一个非常大的整数：

  ```java
  BigInteger bi = new BigInteger("1234567890");
  System.out.println(bi.pow(5)); // 2867971860299718107233761438093672048294900000
  ```

* 对`BigInteger`做运算的时候，只能使用实例方法

  例如，加法运算：

  ```java
  BigInteger i1 = new BigInteger("1234567890");
  BigInteger i2 = new BigInteger("12345678901234567890");
  BigInteger sum = i1.add(i2); // 12345678902469135780
  ```

* 和`long`型整数运算比，`BigInteger`不会有范围限制，但缺点是速度比较慢。

* 也可以把`BigInteger`转换成`long`型：

  ```java
  BigInteger i = new BigInteger("123456789000");
  System.out.println(i.longValue()); // 123456789000
  System.out.println(i.multiply(i).longValueExact()); // java.lang.ArithmeticException: BigInteger out of long range
  ```

  使用`longValueExact()`方法时，如果超出了`long`型的范围，会抛出`ArithmeticException`。

* `BigInteger`和`Integer`、`Long`一样，也**是不可变类**，并且也继承自`Number`类。因为`Number`定义了转换为基本类型的几个方法：

  - 转换为`byte`：`byteValue()`
  - 转换为`short`：`shortValue()`
  - 转换为`int`：`intValue()`
  - 转换为`long`：`longValue()`
  - 转换为`float`：`floatValue()`
  - 转换为`double`：`doubleValue()`

  因此，通过上述方法，可以把`BigInteger`转换成基本类型。

  如果`BigInteger`表示的范围超过了基本类型的范围，转换时将**丢失高位信息**，即**结果不一定是准确的**。

  如果需要准确地转换成基本类型，可以使用`intValueExact()`、`longValueExact()`等方法，在转换时如果超出范围，将直接抛出`ArithmeticException`异常。

* 如果`BigInteger`的值甚至超过了`float`的最大范围（3.4x1038），那么返回的float是什么呢？

  ```java
  public class Main {
      public static void main(String[] args) {
          BigInteger n = new BigInteger("999999").pow(99);
          float f = n.floatValue();
          System.out.println(f);
      }
  }
  ```

  ```java
  Infinity
  ```

## BigDecimal

* 和`BigInteger`类似，`BigDecimal`可以表示一个任意大小且精度完全准确的浮点数。

  ```java
  BigDecimal bd = new BigDecimal("123.4567");
  System.out.println(bd.multiply(bd)); // 15241.55677489
  ```

* `BigDecimal`用`scale()`表示小数位数，例如：

  ```java
  BigDecimal d1 = new BigDecimal("123.45");
  BigDecimal d2 = new BigDecimal("123.4500");
  BigDecimal d3 = new BigDecimal("1234500");
  System.out.println(d1.scale()); // 2,两位小数
  System.out.println(d2.scale()); // 4
  System.out.println(d3.scale()); // 0
  ```

* 通过`BigDecimal`的`stripTrailingZeros()`方法，可以将一个`BigDecimal`格式化为一个相等的，但去掉了末尾0的`BigDecimal`：

  ```java
  BigDecimal d1 = new BigDecimal("123.4500");
  BigDecimal d2 = d1.stripTrailingZeros();
  System.out.println(d1.scale()); // 4
  System.out.println(d2.scale()); // 2,因为去掉了00
  
  BigDecimal d3 = new BigDecimal("1234500");
  BigDecimal d4 = d3.stripTrailingZeros();
  System.out.println(d3.scale()); // 0
  System.out.println(d4.scale()); // -2
  ```

  如果一个`BigDecimal`的`scale()`返回负数，例如，`-2`，表示这个数是个整数，并且末尾有2个0。

* 可以对一个`BigDecimal`设置它的`scale`，如果精度比原始值低，那么按照指定的方法进行四舍五入或者直接截断：

  ```java
  import java.math.BigDecimal;
  import java.math.RoundingMode;
  public class Main {
      public static void main(String[] args) {
          BigDecimal d1 = new BigDecimal("123.456789");
          BigDecimal d2 = d1.setScale(4, RoundingMode.HALF_UP); // 四舍五入，123.4568
          BigDecimal d3 = d1.setScale(4, RoundingMode.DOWN); // 直接截断，123.4567
          System.out.println(d2);
          System.out.println(d3);
      }
  }
  ```

* 对`BigDecimal`做加、减、乘时，精度不会丢失，但是做除法时，存在无法除尽的情况，这时，就必须指定精度以及如何进行截断：

  ```java
  BigDecimal d1 = new BigDecimal("123.456");
  BigDecimal d2 = new BigDecimal("23.456789");
  BigDecimal d3 = d1.divide(d2, 10, RoundingMode.HALF_UP); // 保留10位小数并四舍五入
  BigDecimal d4 = d1.divide(d2); // 报错：ArithmeticException，因为除不尽
  ```

* 还可以对`BigDecimal`做除法的同时求余数：

  ```java
  import java.math.BigDecimal;
  public class Main {
      public static void main(String[] args) {
          BigDecimal n = new BigDecimal("12.345");
          BigDecimal m = new BigDecimal("0.12");
          BigDecimal[] dr = n.divideAndRemainder(m);
          System.out.println(dr[0]); // 102
          System.out.println(dr[1]); // 0.105
      }
  }
  ```

  调用`divideAndRemainder()`方法时，返回的数组包含两个`BigDecimal`，分别是商和余数，其中商总是整数，余数不会大于除数。我们可以利用这个方法判断两个`BigDecimal`是否是整数倍数：

  ```java
  BigDecimal n = new BigDecimal("12.75");
  BigDecimal m = new BigDecimal("0.15");
  BigDecimal[] dr = n.divideAndRemainder(m);
  if (dr[1].signum() == 0) {
      // n是m的整数倍
  }
  ```

### 比较BigDecimal

* 在比较两个`BigDecimal`的值是否相等时，要特别注意，**使用`equals()`方法不但要求两个`BigDecimal`的值相等，还要求它们的`scale()`相等：**

  ```java
  BigDecimal d1 = new BigDecimal("123.456");
  BigDecimal d2 = new BigDecimal("123.45600");
  System.out.println(d1.equals(d2)); // false,因为scale不同
  System.out.println(d1.equals(d2.stripTrailingZeros())); // true,因为d2去除尾部0后scale变为2
  System.out.println(d1.compareTo(d2)); // 0
  ```

  必须使用**`compareTo()`**方法来比较，它根据两个值的大小分别返回负数、正数和`0`，分别表示小于、大于和等于。

* **总是使用compareTo()比较两个BigDecimal的值，不要使用equals()！**

* 如果查看`BigDecimal`的源码，可以发现，实际上一个`BigDecimal`是通过一个`BigInteger`和一个`scale`来表示的，即`BigInteger`表示一个完整的整数，而`scale`表示小数位数：

  ```java
  public class BigDecimal extends Number implements Comparable<BigDecimal> {
      private final BigInteger intVal;
      private final int scale;
  }
  ```

* **`BigDecimal`也是从`Number`继承的，也是不可变对象。**

* `BigDecimal`用于表示精确的小数，常用于财务计算；

## 常用工具类

### Math

顾名思义，`Math`类就是用来进行数学计算的，它提供了大量的静态方法来便于我们实现数学计算：

* 求绝对值：

  ```java
  Math.abs(-100); // 100
  Math.abs(-7.8); // 7.8
  ```

* 取最大或最小值：

  ```java
  Math.max(100, 99); // 100
  Math.min(1.2, 2.3); // 1.2
  ```

* 计算x^y次方：

  ```java
  Math.pow(2, 10); // 2的10次方=1024
  ```

* 计算√x：

  ```java
  Math.sqrt(2); // 1.414...
  ```

* 计算e^x次方：

  ```java
  Math.exp(2); // 7.389...
  ```

* 计算以e为底的对数：

  ```java
  Math.log(4); // 1.386...
  ```

* 计算以10为底的对数：

  ```java
  Math.log10(100); // 2
  ```

* 三角函数：

  ```java
  Math.sin(3.14); // 0.00159...
  Math.cos(3.14); // -0.9999...
  Math.tan(3.14); // -0.0015...
  Math.asin(1.0); // 1.57079...
  Math.acos(1.0); // 0.0
  ```

* Math还提供了几个数学常量：

  ```java
  double pi = Math.PI; // 3.14159...
  double e = Math.E; // 2.7182818...
  Math.sin(Math.PI / 6); // sin(π/6) = 0.5
  ```

* 生成一个随机数x，x的范围是`0 <= x < 1`：

  ```java
  Math.random(); // 0.53907... 每次都不一样
  ```

* 如果我们要生成一个区间在`[MIN, MAX)`的随机数，可以借助`Math.random()`实现，计算如下：

  ```java
  // 区间在[MIN, MAX)的随机数
  public class Main {
      public static void main(String[] args) {
          double x = Math.random(); // x的范围是[0,1)
          double min = 10;
          double max = 50;
          double y = x * (max - min) + min; // y的范围是[10,50)
          long n = (long) y; // n的范围是[10,50)的整数
          System.out.println(y);
          System.out.println(n);
      }
  }
  ```

* Java标准库还提供了一个`StrictMath`，它提供了和`Math`几乎一模一样的方法。

  这两个类的区别在于，由于浮点数计算存在误差，不同的平台（例如x86和ARM）计算的结果可能不一致（指误差不同）

  因此，`StrictMath`保证所有平台计算结果都是完全相同的，而`Math`会尽量针对平台优化计算速度

  所以，绝大多数情况下，使用`Math`就足够了。

### Random

* `Random`用来创建伪随机数。

* 所谓伪随机数，是指只要给定一个初始的种子，产生的随机数序列是完全一样的。

* 要生成一个随机数，可以使用`nextInt()`、`nextLong()`、`nextFloat()`、`nextDouble()`：

  ```java
  Random r = new Random();
  r.nextInt(); // 2071575453,每次都不一样
  r.nextInt(10); // 5,生成一个[0,10)之间的int
  r.nextLong(); // 8811649292570369305,每次都不一样
  r.nextFloat(); // 0.54335...生成一个[0,1)之间的float
  r.nextDouble(); // 0.3716...生成一个[0,1)之间的double
  ```

* 每次运行程序，生成的随机数都是不同的，没看出*伪随机数*的特性来。

  这是因为我们创建`Random`实例时，如果不给定种子，就使用系统当前时间戳作为种子，因此每次运行时，种子不同，得到的伪随机数序列就不同。

  如果我们在创建`Random`实例时指定一个种子，就会得到完全确定的随机数序列：

  ```java
  import java.util.Random;
  public class Main {
      public static void main(String[] args) {
          Random r = new Random(12345);
          for (int i = 0; i < 10; i++) {
              System.out.println(r.nextInt(100));
          }
          // 51, 80, 41, 28, 55...
      }
  }
  ```

* 前面我们使用的`Math.random()`实际上内部调用了`Random`类，所以它也是伪随机数，只是我们无法指定种子。

### SecureRandom

* 有伪随机数，就有真随机数。

* 实际上真正的真随机数只能通过量子力学原理来获取，而我们想要的是一个不可预测的安全的随机数，`SecureRandom`就是用来创建安全的随机数的：

  ```java
  SecureRandom sr = new SecureRandom();
  System.out.println(sr.nextInt(100));
  ```

* `SecureRandom`无法指定种子，它使用RNG（random number generator）算法。

* JDK的`SecureRandom`实际上有多种不同的底层实现，有的使用安全随机种子加上伪随机数算法来产生安全的随机数，有的使用真正的随机数生成器。

* 实际使用的时候，可以优先获取高强度的安全随机数生成器，如果没有提供，再使用普通等级的安全随机数生成器：

  ```java
  import java.util.Arrays;
  import java.security.SecureRandom;
  import java.security.NoSuchAlgorithmException;
  public class Main {
      public static void main(String[] args) {
          SecureRandom sr = null;
          try {
              sr = SecureRandom.getInstanceStrong(); // 获取高强度安全随机数生成器
          } catch (NoSuchAlgorithmException e) {
              sr = new SecureRandom(); // 获取普通的安全随机数生成器
          }
          byte[] buffer = new byte[16];
          sr.nextBytes(buffer); // 用安全随机数填充buffer
          System.out.println(Arrays.toString(buffer));
      }
  }
  ```

* `SecureRandom`的安全性是通过操作系统提供的安全的随机种子来生成随机数。这个种子是通过CPU的热噪声、读写磁盘的字节、网络流量等各种随机事件产生的“熵”。
* 在密码学中，安全的随机数非常重要。如果使用不安全的伪随机数，所有加密体系都将被攻破。因此，时刻牢记必须使用`SecureRandom`来产生安全的随机数。
* **需要使用安全随机数的时候，必须使用SecureRandom，绝不能使用Random！**

