# Java笔记0--基础

## JVM

+ JVM是Java Virtual Machine（Java虚拟机）的缩写，JVM是一种用于计算设备的规范，它是一个虚构出来的计算机，是通过在实际的计算机上仿真模拟各种计算机功能来实现的。

+ 引入Java语言虚拟机后，Java语言在不同平台上运行时不需要重新编译。Java语言使用Java虚拟机屏蔽了与具体平台相关的信息，使得Java语言编译程序只需生成在Java虚拟机上运行的目标代码（字节码），就可以在多种平台上不加修改地运行。

+ Java虚拟机有自己完善的硬件架构，如处理器、堆栈等，还具有相应的指令系统。

+ Java虚拟机**本质上就是一个程序**，当它在命令行上启动的时候，就开始执行保存在某字节码文件中的指令。

+ Java语言的可移植性正是建立在Java虚拟机的基础上。

  任何平台只要装有针对于该平台的Java虚拟机，字节码文件（.class）就可以在该平台上运行。这就是**“一次编译，多次运行”**。

+ Java虚拟机不仅是一种跨平台的软件，而且是一种新的网络计算平台。

  该平台包括许多相关的技术，如符合开放接口标准的各种API、优化技术等。

+ Java技术使同一种应用可以运行在不同的平台上。

  Java平台可分为两部分，即Java虚拟机（Java virtual machine，JVM）和Java API类库。

## 如何运行Java程序

### 示例代码

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

### 运行原理

+ Java源码本质上是一个文本文件

+ 我们需要先用`javac`把`Hello.java`编译成字节码文件`Hello.class`，然后，用`java`命令执行这个字节码文件：

  ```java
  ┌──────────────────┐
  │    Hello.java    │<─── source code
  └──────────────────┘
            │ compile
            ▼
  ┌──────────────────┐
  │   Hello.class    │<─── byte code
  └──────────────────┘
            │ execute
            ▼
  ┌──────────────────┐
  │    Run on JVM    │
  └──────────────────┘
  ```

  因此，可执行文件`javac`是编译器，而可执行文件`java`就是虚拟机。

+ 第一步，在保存`Hello.java`的目录下执行命令`javac Hello.java`：

  ```shell
  $ javac Hello.java
  ```

  如果源代码无误，上述命令不会有任何输出，而当前目录下会产生一个`Hello.class`文件：

  ```shell
  $ ls
  Hello.class	Hello.java
  ```

+ 第二步，执行`Hello.class`，使用命令`java Hello`：

  ```shell
  $ java Hello
  Hello, world!
  ```

  注意：给虚拟机传递的参数`Hello`是我们定义的类名，虚拟机自动查找对应的class文件并执行。

+ 有一些童鞋可能知道，直接运行`java Hello.java`也是可以的：

  ```shell
  $ java Hello.java 
  Hello, world!
  ```

  这是Java 11新增的一个功能，它可以直接运行一个单文件源码！

  需要注意的是，在实际项目中，单个不依赖第三方库的Java源码是非常罕见的。所以，绝大多数情况下，我们无法直接运行一个Java源码文件，原因是它需要依赖其他的库。