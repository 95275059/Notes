# Java笔记9--字符和字符串
* 在Java中，字符和字符串是两种不同的类型
## 字符类型
* 字符类型char是基本数据类型，它是character的缩写
* 一个插入保存一个unicode字符
```java
char c1 = ‘A’;
char c2 = ‘中’;
```
因为Java在内存中总是使用unicode表示字符，所以，一个英文字符和一个中文字符都用一个char类型表示，都占用两个字节
* 要显示一个字符的unicode编码，只需要将char类型直接赋值给int类型即可
```java
int n1 = ‘A’;  // 字母“A”的Unicodde编码是65
int n2 = '中'; // 汉字“中”的Unicode编码是20013
```
* 还可以直接使用转移字符\u+unicode编码来表示一个字符
```java
// 注意是十六进制:
char c3 = '\u0041'; // 'A'，因为十六进制0041 = 十进制65
char c4 = '\u4e2d'; // '中'，因为十六进制4e2d = 十进制20013
```
## 字符串类型
* 字符串类型String是引用类型
* 使用双引号表示字符串
* 一个字符串可以存储0到任意个字符
```java
String s = ""; // 空字符串，包含0个字符
String s1 = "A"; // 包含一个字符
String s2 = "ABC"; // 包含3个字符
String s3 = "中文 ABC"; // 包含6个字符，其中有一个空格
```
* 转义字符
	* \” : 表示字符“
	* \’ : 表示字符‘
	* \\ : 表示字符\
	* \n : 表示换行符
	* \r : 表示回车符
	* \t : 表示Tab
	* \u#### : 表示一个unicode编码的字符
```java
String s = "ABC\n\u4e2d\u6587"; // 包含6个字符: A, B, C, 换行符, 中, 文
```
### 字符串连接
* Java的编译器对字符串做了特殊照顾，可以使用+连接任意字符串和其他数据类型
* 示例1
```java
public class Main {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = "world";
        String s = s1 + " " + s2 + "!";
        System.out.println(s); // Hello World!
    }
}
```
* 示例2
```java
public class Main {
    public static void main(String[] args) {
        int age = 25;
        String s = "age is " + age;
        System.out.println(s); // age is 25
    }
}
```
如果用+连接字符串和其他数据类型，会将其他数据类型先自动转型为字符串，再连接
### 多行字符串
* 从Java13开始，字符串可以用“”“...”””表示多行字符串（Text Blocks）
* 示例
```java
public class Main {
    public static void main(String[] args) {
        String s = """
                   SELECT * FROM
                     users
                   WHERE id > 100
                   ORDER BY name DESC
                   """;
        System.out.println(s);
    }
}
```
上述多行字符串实际上是5行，在最后一个DESC后面还有一个\n，如果我们不想在字符串末尾加\n，就需要这样写
```java
String s = """ 
           SELECT * FROM
             users
           WHERE id > 100
           ORDER BY name DESC""";
```
* 多行字符串前面共同的空格会被去掉
```java
String s = """
...........SELECT * FROM
...........  users
...........WHERE id > 100
...........ORDER BY name DESC
...........""";
```
用. 标注的空格都会被去掉。
如果多行字符串的排版不规则，那么，去掉的空格就会变成这样：
```java
String s = """
.........  SELECT * FROM
.........    users
.........WHERE id > 100
.........  ORDER BY name DESC
.........  """;
```
即总是以最短的行首空格为基准。
### 不可变性
* Java字符串不可变
* 示例1
```java
public class Main {
    public static void main(String[] args) {
        String s = "hello";
        System.out.println(s); // 显示 hello
        s = "world";
        System.out.println(s); // 显示 world
    }
}
```
观察执行结果，难道字符串s变了吗？其实变的不是字符串，而是变量s的“指向”。
执行`String s = "hello";`时，JVM虚拟机先创建字符串`"hello"` ，然后，把字符串变量s指向它：
```java
      s
      │
      ▼
┌───┬───────────┬───┐
│   │  "hello"  │   │
└───┴───────────┴───┘
```
紧接着，执行`s = "world";`时，JVM虚拟机先创建字符串`"world"`，然后，把字符串变量s指向它：
```java
      s ──────────────┐
                      │
                      ▼
┌───┬───────────┬───┬───────────┬───┐
│   │  "hello"  │   │  "world"  │   │
└───┴───────────┴───┴───────────┴───┘
```
原来的字符串`"hello"`还在，只是我们无法通过变量s访问它而已。
因此，字符串的不可变是指字符串内容不可变。
* 示例2
```java
public class Main {
    public static void main(String[] args) {
        String s = "hello";
        String t = s;
        s = "world";
        System.out.println(t); // t是"hello"
    }
}
```
### 空值null
* 引用类型的变量可以指向一个空值null，它表示不存在，即该变量不指向任何对象
```java
String s1 = null; // s1是null
String s2; // 没有赋初值值，s2也是null
String s3 = s1; // s3也是null
String s4 = ""; // s4指向空字符串，不是null
```
* 注意区分空值null和空字符串””，空字符串是一个有效的字符串对象，不等于null
## 题目：请将一组int值视为字符的Unicode编码，然后将它们拼成一个字符串
```java
public class Main {
    public static void main(String[] args) {
        // 请将下面一组int值视为字符的Unicode码，把它们拼成一个字符串：
        int a = 72;
        int b = 105;
        int c = 65281;
        // FIXME:
        String s = “\u” + a + “\u” + b + “\u” + c;
        System.out.println(s);
    }
}
```
* `String s = “” + (char)a + (char)b + (char)c; //Hi!` 
从左到右执行，强制类型转换过程也是从左到右，先碰到String就会强制转化为String
`String s = (char)a + (char)b + (char)c + “”; // 65458`
这行代码是先做char类型的加法，然后再+空字符串，最后再强制转换为String类型