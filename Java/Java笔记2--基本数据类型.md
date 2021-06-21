# Java笔记2--基本数据类型
* 变量就是申请内存来存储值
当创建变量的时候，需要在内存中申请空间
* 内存管理系统根据变量的类型为变量分配存储空间
分配的空间只能用来存储该类型的数据
## 内置数据类型
### 整型

对于整型类型，Java只定义了带符号的整型，因此，**最高位的bit表示符号位**（0表示正数，1表示负数）。

#### byte

* byte数据类型是8位，有符号的，以二进制补码表示的整数（一个字节）
* 最小值是 -128（-2^7）
* 最大值是127（2^7-1）
* 默认值是0
* byte类型用在大型数组中节约空间，主要代替整数，因为byte变量占用的空间只有int类型的四分之一
* 例子：byte a = 100，byte b = -50
#### short
* short数据类型是16位，有符号的，以二进制补码表示的整数（两个字节）
* 最小值是-32768（-2^15）
* 最大值是32767（2^15-1）
* 默认值是0
* short数据类型也可以像byte那样节省空间，一个short变量是int型变量所占空间的二分之一
* 例子：short a = 1000，short b = -20000
#### int
* int数据类型是32位，有符号的，以二进制补码表示的整数（四个字节）
* 最小值是-2147483648（-2^31）
* 最大值是2147483647（2^31-1）
* 一般地整型变量默认为int类型
* 默认值是0
* 例子：int a = 100000，int b = -200000
#### long
* long数据类型是64位，有符号的，以二进制补码表示的整数（八个字节）
* long型的结尾需要加L
* 最小值是 -9223372036854775808（-2^63）
* 最大值是9223372036854775807（2^63-1）
* 这种类型主要使用在需要比较大整数的系统上
* 默认值是0L
* 例子：long a = 100000L， long b = -200000L
#### 示例

```java
public class Main {
    public static void main(String[] args) {
        int i = 2147483647;
        int i2 = -2147483648;
        int i3 = 2_000_000_000; // 加下划线更容易识别
        int i4 = 0xff0000; // 十六进制表示的16711680
        int i5 = 0b1000000000; // 二进制表示的512
        long l = 9000000000000000000L; // long型的结尾需要加L
    }
}
```

特别注意：同一个数的不同进制的表示是完全相同的，例如`15`=`0xf`＝`0b1111`。

### 浮点型

#### float
* float数据类型是单精度，32位，符合IEEE 754标准的浮点数（四个字节）
* 对于`float`类型，需要加上`f`后缀。
* 浮点数可表示的范围非常大，`float`类型可最大表示3.4x10^38
* float在存储大型浮点数组的时候可节省内存空间
* 默认值是0.0f
* 浮点数不能用来表示精确的值，如货币
* 例子：float f1 = 234.5f
#### double
* double数据类型是双精度，64位，符合IEEE 754标准的浮点数（八个字节）
* 浮点数的默认类型为double类型
* `double`类型可最大表示1.79x10^308。
* double类型同样不能表示精确的值，如货币
* 默认值是0.0d
* 例子：double d1 = 123.4
#### 示例

```java
float f1 = 3.14f;
float f2 = 3.14e38f; // 科学计数法表示的3.14x10^38
double d = 1.79e308;
double d2 = -1.79e308;
double d3 = 4.9e-324; // 科学计数法表示的4.9x10^-324
```

### 布尔类型

#### boolean
* boolean数据类型表示**一位**的信息
* 只有两个取值：true和false
* 这种类型只作为一种标志来记录true/false情况
* 默认值是false
* 例子：boolean one = true

#### 示例

```java
boolean b1 = true;
boolean b2 = false;
boolean isGreater = 5 > 3; // 计算结果为true
int age = 12;
boolean isAdult = age >= 18; // 计算结果为false
```

Java语言对布尔类型的存储并没有做规定，因为理论上存储布尔类型只需要1 bit，但是通常JVM内部会把`boolean`表示为4字节整数。

### 字符类型

#### char

* char数据类型是一个单一的16位Unicode字符（两个字节）
* 最小值是‘\u0000’（即为0）
* 最大值是‘\uffff’（即为65535）
* char数据类型可以存储任何字符
* Java的`char`类型除了可表示标准的ASCII外，还可以表示一个Unicode字符
* 例子：char letter = ‘A’
#### 示例

```java
public class Main {
    public static void main(String[] args) {
        char a = 'A';
        char zh = '中';
        System.out.println(a);
        System.out.println(zh);
    }
}
```

注意`char`类型使用单引号`'`，且仅有一个字符，要和双引号`"`的字符串类型区分开。

### 例子
```java
public class PrimitiveTypeTest {
    public static void main(String[] args) {
        // byte
        System.out.println("基本类型：byte 二进制位数：" + Byte.SIZE);
        System.out.println("包装类：java.lang.Byte");
        System.out.println("最小值：Byte.MIN_VALUE=" + Byte.MIN_VALUE);
        System.out.println("最大值：Byte.MAX_VALUE=" + Byte.MAX_VALUE);
        System.out.println();
    // short
    System.out.println("基本类型：short 二进制位数：" + Short.SIZE);
    System.out.println("包装类：java.lang.Short");
    System.out.println("最小值：Short.MIN_VALUE=" + Short.MIN_VALUE);
    System.out.println("最大值：Short.MAX_VALUE=" + Short.MAX_VALUE);
    System.out.println();

    // int
    System.out.println("基本类型：int 二进制位数：" + Integer.SIZE);
    System.out.println("包装类：java.lang.Integer");
    System.out.println("最小值：Integer.MIN_VALUE=" + Integer.MIN_VALUE);
    System.out.println("最大值：Integer.MAX_VALUE=" + Integer.MAX_VALUE);
    System.out.println();

    // long
    System.out.println("基本类型：long 二进制位数：" + Long.SIZE);
    System.out.println("包装类：java.lang.Long");
    System.out.println("最小值：Long.MIN_VALUE=" + Long.MIN_VALUE);
    System.out.println("最大值：Long.MAX_VALUE=" + Long.MAX_VALUE);
    System.out.println();

    // float
    System.out.println("基本类型：float 二进制位数：" + Float.SIZE);
    System.out.println("包装类：java.lang.Float");
    System.out.println("最小值：Float.MIN_VALUE=" + Float.MIN_VALUE);
    System.out.println("最大值：Float.MAX_VALUE=" + Float.MAX_VALUE);
    System.out.println();

    // double
    System.out.println("基本类型：double 二进制位数：" + Double.SIZE);
    System.out.println("包装类：java.lang.Double");
    System.out.println("最小值：Double.MIN_VALUE=" + Double.MIN_VALUE);
    System.out.println("最大值：Double.MAX_VALUE=" + Double.MAX_VALUE);
    System.out.println();

    // char
    System.out.println("基本类型：char 二进制位数：" + Character.SIZE);
    System.out.println("包装类：java.lang.Character");
    // 以数值形式而不是字符形式将Character.MIN_VALUE输出到控制台
    System.out.println("最小值：Character.MIN_VALUE="
            + (int) Character.MIN_VALUE);
    // 以数值形式而不是字符形式将Character.MAX_VALUE输出到控制台
    System.out.println("最大值：Character.MAX_VALUE="
            + (int) Character.MAX_VALUE);
}
} 
```
```java
基本类型：byte 二进制位数：8
包装类：java.lang.Byte
最小值：Byte.MIN_VALUE=-128
最大值：Byte.MAX_VALUE=127
基本类型：short 二进制位数：16
包装类：java.lang.Short
最小值：Short.MIN_VALUE=-32768
最大值：Short.MAX_VALUE=32767


基本类型：int 二进制位数：32
包装类：java.lang.Integer
最小值：Integer.MIN_VALUE=-2147483648
最大值：Integer.MAX_VALUE=2147483647


基本类型：long 二进制位数：64
包装类：java.lang.Long
最小值：Long.MIN_VALUE=-9223372036854775808
最大值：Long.MAX_VALUE=9223372036854775807


基本类型：float 二进制位数：32
包装类：java.lang.Float
最小值：Float.MIN_VALUE=1.4E-45
最大值：Float.MAX_VALUE=3.4028235E38


基本类型：double 二进制位数：64
包装类：java.lang.Double
最小值：Double.MIN_VALUE=4.9E-324
最大值：Double.MAX_VALUE=1.7976931348623157E308


基本类型：char 二进制位数：16
包装类：java.lang.Character
最小值：Character.MIN_VALUE=0
最大值：Character.MAX_VALUE=65535
```
* Float和Double的最小值和最大值都是以科学记数法的形式输出的
结尾的“E+”数字表示E之前的数字要乘以10的数字次幂
* 实际上，Java中还存在另外一种基本类型void，它也有对应的包装类java.lang.Void，不过我们无法直接对它们进行操作
——
## 引用数据类型
* 引用类型变量由类的构造函数创建
  可以使用它们访问所引用的对象，这些变量在声明时被指定为一个特定的类型，变量一旦声明后，类型就不能被改变了

* 对象，数组都是引用数据类型

* 所有引用类型的默认值都是null

* 一个引用变量可以用来引用与之兼容的类型

* 例子：Animal animal = new Animal(“giraffe”)

* 引用类型最常用的就是String字符串

  ```java
  String s = "hello";
  ```

* 引用类型的变量类似于C语言的指针，它内部存储一个“地址”，指向某个对象在内存的位置，后续我们介绍类的概念时会详细讨论。
## Java常量
* 常量就是一个固定值，是不能改变的量
它们不需要计算，直接代表相应的值
* 在Java中用final标志，声明方式和变量类似
```java
final double PI = 3.14; // PI是一个常量
double r = 5.0;
double area = PI * r * r;
PI = 300; // compile error!
```
常量在定义时进行初始化后就不可再次赋值，再次赋值会导致编译错误。

* 虽然变量名也可以用小写，但为了便于识别，通常使用大写字母表示常量
* 当使用常量的时候，前缀0表明是8进制，而0x代表16进制
```java
final int A = 100;
final int B = 0144;
final int C = 0x64;
```
* 和其他语言一样，Java的字符串常量也是包含在两个引号之间的字符序列
## var关键字

有些时候，类型的名字太长，写起来比较麻烦。例如：

```java
StringBuilder sb = new StringBuilder();
```

这个时候，如果想省略变量类型，可以使用`var`关键字：

```java
var sb = new StringBuilder();
```

编译器会根据赋值语句自动推断出变量`sb`的类型是`StringBuilder`。对编译器来说，语句：

```java
var sb = new StringBuilder();
```

实际上会自动变成：

```java
StringBuilder sb = new StringBuilder();
```

因此，使用`var`定义变量，仅仅是少写了变量类型而已。

## 特殊转义字符序列
| 符号 | 字符含义             |
| :------- | :--------------- |
| \n       | 换行(0x0a)           |
| \r        | 回车(0x0d)        |
| \f        |  换页符(0xoc)          |
| \b       | 退格(0x08)            |
| \0       | 空字符(0x0)          |
| \s        | 字符串   |
| \t       | 制表符    |
| \”       | 双引号           |
| \’        | 单引号      |
| \\       | 反斜杠          |
| \ddd       | 八进制字符(ddd)          |
| \uxxxx     | 16进制Unicode字符(xxxx)        |
