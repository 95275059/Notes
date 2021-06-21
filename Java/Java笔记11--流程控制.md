# Java笔记11--流程控制
## 输入和输出
* `System.out.println()`
`println`是print line的缩写，表示输出并换行
`print`则表示只输出不换行
### 格式化输出
* 计算机表示的数据不一定适合阅读
```java
public class Main {
    public static void main(String[] args) {
        double d = 12900000;
        System.out.println(d); // 1.29E7
    }
}
```
* 格式化输出可以将数据显示为我们期望的格式
* 使用`System.out.printf()`实现格式化输出
通过使用占位符`%?`,`printf()`可以把后面的参数格式化成指定格式
```java
public class Main {
    public static void main(String[] args) {
        double d = 3.1415926;
        System.out.printf("%.2f\n", d); // 显示两位小数3.14
        System.out.printf("%.4f\n", d); // 显示4位小数3.1416
    }
}
```
* 占位符
｜占位符｜                         说明                            ｜
｜    ——   ｜                       ——                                  ｜
｜%d        |格式化输出整数                                   ｜
｜%x        |格式化输出十六进制整数                    ｜
｜%f        |格式化输出浮点数                                 ｜
｜%e        |格式化输出科学计数法表示的浮点数｜
｜%s        |格式化输出字符串                                 ｜
注意：由于%表示占位符，因此连续两个%%标记一个%本身
* 用零补足位数
```java
public class Main {
    public static void main(String[] args) {
        int n = 12345000;
        System.out.printf("n=%d, hex=%08x", n, n); // 注意，两个%占位符必须传入两个数
    }
}
```
### 输入
* 从控制台读取一个字符串和一个整数
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // 创建Scanner对象
        System.out.print("Input your name: "); // 打印提示
        String name = scanner.nextLine(); // 读取一行输入并获取字符串
        System.out.print("Input your age: "); // 打印提示
        int age = scanner.nextInt(); // 读取一行输入并获取整数
        System.out.printf("Hi, %s, you are %d\n", name, age); // 格式化输出
    }
}
```
	* `System.out`代表标准输出流
	* `System.in`代表标准输入流
	* 直接使用System.in读取用户输入虽然是可以的，但需要更复杂的代码，而通过Scanner就可以简化后续的代码。
	* 创建Scanner对象后，要读取用户输入的字符串，使用`scanner.nextLine()`，要读取用户输入的整数，使用`scanner.nextInt()`。
	* Scanner会自动转换数据类型，因此不必手动转换。
## If...else...判断
### 基本语法
```java 
if (条件1) {
    // 条件1满足时执行
} else if (条件2) {
    // 不满足条件1但满足条件2时执行
}
else { //可有可无
    // 以上条件均不满足时执行
}
```
* 当if语句只有一行语句时，可以省略花括号
### 浮点数判断
* 浮点数在计算机中常常不能精确表示，并且计算可能出现误差，因此，判断浮点数相等用==判断并不靠谱
```java
public class Main {
    public static void main(String[] args) {
        double x = 1 - 9.0 / 10;
        if (x == 0.1) {
            System.out.println("x is 0.1");
        } else {
            System.out.println("x is NOT 0.1"); //输出
        }
    }
}
```
* 正确的方法是利用差值小于某个临界值来判断
```java
public class Main {
    public static void main(String[] args) {
        double x = 1 - 9.0 / 10;
        if (Math.abs(x - 0.1) < 0.00001) {
            System.out.println("x is 0.1");
        } else {
            System.out.println("x is NOT 0.1");
        }
    }
}
```
### 判断引用类型相等
* 在Java中，判断值类型的变量是否相等，可以使用==运算符。
* 但是，判断引用类型的变量是否相等，==表示“引用是否相等”，或者说，是否指向同一个对象。
例如，下面的两个String类型，它们的内容是相同的，但是，分别指向不同的对象，用==判断，结果为false：
```java
public class Main {
    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = "HELLO".toLowerCase();
        System.out.println(s1);
        System.out.println(s2);
        if (s1 == s2) {
            System.out.println("s1 == s2");
        } else {
            System.out.println("s1 != s2");
        }
    }
}
```
```java
hello 
hello 
s1 != s2
```
* 要判断引用类型的变量内容是否相等，必须使用equals()方法
```java
public class Main {
    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = "HELLO".toLowerCase();
        System.out.println(s1);
        System.out.println(s2);
        if (s1.equals(s2)) {
            System.out.println("s1 equals s2");
        } else {
            System.out.println("s1 not equals s2");
        }
    }
}
```
```java
hello 
hello 
s1 equals s2
```
* 注意：执行语句`s1.equals(s2)`时，如果变量s1为null，会报
NullPointerException：
```java
public class Main {
    public static void main(String[] args) {
        String s1 = null;
        if (s1.equals("hello")) {
            System.out.println("hello");
        }
    }
}
```
```java
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "String.equals(Object)" because "<local1>" is null 
at Main.main(Main.java:5) 
```
要避免`NullPointerException`错误，可以利用短路运算符
```java
public class Main {
    public static void main(String[] args) {
        String s1 = null;
        if (s1 != null && s1.equals("hello")) {
            System.out.println("hello");
        }
    }
}
```
无输出
还可以把一定不是null的对象"hello"放到前面：例如：
`if ("hello".equals(s)) { ... }`
## switch多重选择
* switch语句根据switch (表达式)计算的结果，跳转到匹配的case结果，然后继续执行后续语句，直到遇到break结束执行。
* 示例
```java
public class Main {
    public static void main(String[] args) {
        int option = 1;
        switch (option) {
        case 1:
            System.out.println("Selected 1");
            break;
        case 2:
            System.out.println("Selected 2");
            break;
        case 3:
            System.out.println("Selected 3");
            break;
		  default:
            System.out.println("Not selected");
            break;
        }
    }
}
```

	* 如果option的值没有匹配到任何case，例如option = 99，那么，switch语句不会执行任何语句。这时，可以给switch语句加一个default，当没有匹配到任何case时，执行default
* 使用switch时，注意case语句并没有花括号{}，而且，case语句具有“穿透性”，漏写break将导致意想不到的结果：
```java
public class Main {
    public static void main(String[] args) {
        int option = 2;
        switch (option) {
        case 1:
            System.out.println("Selected 1");
        case 2:
            System.out.println("Selected 2");
        case 3:
            System.out.println("Selected 3");
        default:
            System.out.println("Not selected");
        }
    }
}
```
当option = 2时，将依次输出"Selected 2"、"Selected 3"、"Not selected"，原因是从匹配到case 2开始，后续语句将全部执行，直到遇到break语句。因此，任何时候都不要忘记写break。
* 使用switch语句时，只要保证有break，case的顺序不影响程序逻辑
```java
switch (option) {
case 3:
    ...
    break;
case 2:
    ...
    break;
case 1:
    ...
    break;
}
```
但是仍然建议按照自然顺序排列，便于阅读。
* switch语句还可以匹配字符串。字符串匹配时，是比较“内容相等”。
```java
public class Main {
    public static void main(String[] args) {
        String fruit = "apple";
        switch (fruit) {
        case "apple":
            System.out.println("Selected apple");
            break;
        case "pear":
            System.out.println("Selected pear");
            break;
        case "mango":
            System.out.println("Selected mango");
            break;
        default:
            System.out.println("No fruit selected");
            break;
        }
    }
}

```
* switch语句还可以使用枚举类型
* 编译检查
	* 使用IDE时，可以自动检查是否漏写了break语句和default语句，方法是打开IDE的编译检查。
	* 在Eclipse中，选择Preferences - Java - Compiler - Errors/Warnings - Potential programming problems，将以下检查标记为Warning：
		* 	'switch' is missing 'default' case
		* 	'switch' case fall-through
	* 在Idea中，选择Preferences - Editor - Inspections - Java - Control flow issues，将以下检查标记为Warning：
		* 	Fallthrough in 'switch' statement
		* 	'switch' statement without 'default' branch
* switch表达式
使用switch时，如果遗漏了break，就会造成严重的逻辑错误，而且不易在源代码中发现错误。
从Java 12开始，switch语句升级为更简洁的表达式语法，使用类似模式匹配（Pattern Matching）的方法，保证只有一种路径会被执行，并且不需要break语句
```java
public class Main {
    public static void main(String[] args) {
        String fruit = "apple";
        switch (fruit) {
        case "apple" -> System.out.println("Selected apple");
        case "pear" -> System.out.println("Selected pear");
        case "mango" -> {
            System.out.println("Selected mango");
            System.out.println("Good choice!");
        }
        default -> System.out.println("No fruit selected");
        }
    }
}
```
	* 注意新语法使用->，如果有多条语句，需要用{}括起来。
	* 不要写break语句，因为新语法只会执行匹配的语句，没有穿透效应。
很多时候，我们还可能用switch语句给某个变量赋值。例如：
```java
int opt;
switch (fruit) {
case "apple":
    opt = 1;
    break;
case "pear":
case "mango":
    opt = 2;
    break;
default:
    opt = 0;
    break;
}
```
使用新的switch语法，不但不需要break，还可以直接返回值。把上面的代码改写如下：
```java
public class Main {
    public static void main(String[] args) {
        String fruit = "apple";
        int opt = switch (fruit) {
            case "apple" -> 1;
            case "pear", "mango" -> 2;
            default -> 0;
        }; // 注意赋值语句要以;结束
        System.out.println("opt = " + opt);
    }
}
```
* yield
大多数时候，在switch表达式内部，我们会返回简单的值。
但是，如果需要复杂的语句，我们也可以写很多语句，放到{...}里，然后，用yield返回一个值作为switch语句的返回值：
```java
public class Main {
    public static void main(String[] args) {
        String fruit = "orange";
        int opt = switch (fruit) {
            case "apple" -> 1;
            case "pear", "mango" -> 2;
            default -> {
                int code = fruit.hashCode();
                yield code; // switch语句返回值
            }
        };
        System.out.println("opt = " + opt);
    }
}
```
## while循环
```java
while (条件表达式) {
    循环语句
}
// 继续执行后续代码
```
* while循环在每次循环开始前，首先判断条件是否成立。如果计算结果为true，就把循环体内的语句执行一遍，如果计算结果为false，那就直接跳到while循环的末尾，继续往下执行。
* 注意到while循环是先判断循环条件，再循环，因此，有可能一次循环都不做。
* 对于循环条件判断，以及自增变量的处理，要特别注意边界条件
* 如果循环条件永远满足，那这个循环就变成了死循环。死循环将导100%的CPU占用，用户会感觉电脑运行缓慢，所以要避免编写死循环代码。
* 如果循环条件的逻辑写得有问题，也会造成意料之外的结果
```java
public class Main {
    public static void main(String[] args) {
        int sum = 0;
        int n = 1;
        while (n > 0) {
            sum = sum + n;
            n ++;
        }
        System.out.println(n); // -2147483648
        System.out.println(sum);
    }
}
```
表面上看，上面的while循环是一个死循环，但是，Java的int类型有最大值，达到最大值后，再加1会变成负数，结果，意外退出了while循环。
## do while循环
* 在Java中，while循环是先判断循环条件，再执行循环。
* 而另一种do while循环则是先执行循环，再判断条件，条件满足时继续循环，条件不满足时退出。
```java
do {
    执行循环语句
} while (条件表达式);
```
* 可见，do while循环会至少循环一次。
## for循环
* for循环的功能非常强大，它使用计数器实现循环。for循环会先初始化计数器，然后，在每次循环前检测循环条件，在每次循环后更新计数器。计数器变量通常命名为i。
* 和while循环相比，for循环把更新计数器的代码统一放到了一起。在for循环的循环体内部，不需要去更新变量i。
```java
for (初始条件; 循环检测条件; 循环后更新计数器) {
    // 执行语句
}
```
* 注意for循环的初始化计数器总是会被执行，并且for循环也可能循环0次。
* 使用for循环时，千万不要在循环体内修改计数器！在循环体中修改计数器常常导致莫名其妙的逻辑错误。对于下面的代码：
```java
public class Main {
    public static void main(String[] args) {
        int[] ns = { 1, 4, 9, 16, 25 };
        for (int i=0; i<ns.length; i++) {
            System.out.println(ns[i]);
            i = i + 1;
        }
    }
}
```
虽然不会报错，但是，数组元素只打印了一半，原因是循环内部的i = i + 1导致了计数器变量每次循环实际上加了2（因为for循环还会自动执行i++）。
因此，在for循环中，不要修改计数器的值。
计数器的初始化、判断条件、每次循环后的更新条件统一放到for()语句中可以一目了然。
如果希望只访问索引为奇数的数组元素，应该把for循环改写为：
```java
int[] ns = { 1, 4, 9, 16, 25 };
for (int i=0; i<ns.length; i=i+2) {
    System.out.println(ns[i]);
}
```
通过更新计数器的语句i=i+2就达到了这个效果，从而避免了在循环体内去修改变量i。
* 使用for循环时，计数器变量i要尽量定义在for循环中
```java
int[] ns = { 1, 4, 9, 16, 25 };
for (int i=0; i<ns.length; i++) {
    System.out.println(ns[i]);
}
// 无法访问i
int n = i; // compile error!
```
如果变量i定义在for循环外：
```java
int[] ns = { 1, 4, 9, 16, 25 };
int i;
for (i=0; i<ns.length; i++) {
    System.out.println(ns[i]);
}
// 仍然可以使用i
int n = i;
```
那么，退出for循环后，变量i仍然可以被访问，这就破坏了变量应该把访问范围缩到最小的原则。
* for循环还可以缺少初始化语句、循环条件和每次循环更新语句
```java
// 不设置结束条件:
for (int i=0; ; i++) {
    ...
}
```
```java
// 不设置结束条件和更新语句:
for (int i=0; ;) {
    ...
}
```
```java
// 什么都不设置:
for (;;) {
    ...
}
```
通常不推荐这样写，但是，某些情况下，是可以省略for循环的某些语句的。

### **for each循环**

for循环经常用来遍历数组，因为通过计数器可以根据索引来访问数组的每个元素

```java
int[] ns = { 1, 4, 9, 16, 25 };
for (int i=0; i<ns.length; i++) {
    System.out.println(ns[i]);
}
```
但是，很多时候，我们实际上真正想要访问的是数组每个元素的值。Java还提供了另一种for each循环，它可以更简单地遍历数组：
```java
public class Main {
    public static void main(String[] args) {
        int[] ns = { 1, 4, 9, 16, 25 };
        for (int n : ns) {
            System.out.println(n);
        }
    }
}
```
和for循环相比，for each循环的变量n不再是计数器，而是直接对应到数组的每个元素。
for each循环的写法也更简洁。但是，for each循环无法指定遍历顺序，也无法获取数组的索引。
除了数组外，for each循环能够遍历所有“可迭代”的数据类型，包括后面会介绍的List、Map等。
## break
* 在循环过程中，可以使用break语句跳出当前循环
* break语句通常都是配合if语句使用。
* 要特别注意，break语句总是跳出自己所在的那一层循环。
```java
public class Main {
    public static void main(String[] args) {
        for (int i=1; i<=10; i++) {
            System.out.println("i = " + i);
            for (int j=1; j<=10; j++) {
                System.out.println("j = " + j);
                if (j >= i) {
                    break;
                }
            }
            // break跳到这里
            System.out.println("breaked");
        }
    }
}
```
上面的代码是两个for循环嵌套。因为break语句位于内层的for循环，因此，它会跳出内层for循环，但不会跳出外层for循环。
## continue
* break会跳出当前循环，也就是整个循环都不会执行了。
* 而continue则是提前结束本次循环，直接继续执行下次循环。
* 在多层嵌套的循环中，continue语句同样是结束本次自己所在的循环。
