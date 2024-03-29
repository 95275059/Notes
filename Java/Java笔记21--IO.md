# Java笔记21--IO
## File对象
* 在计算机系统中，文件是非常重要的存储方式。
* Java的标准库java.io提供了File对象来操作文件和目录。
* 要构造一个File对象，需要传入文件路径：
```java
import java.io.*;
public class Main {
    public static void main(String[] args) {
        File f = new File("C:\\Windows\\notepad.exe");
        System.out.println(f);
    }
}
```
* 构造File对象时，既可以传入绝对路径，也可以传入相对路径。
绝对路径是以根目录开头的完整路径，例如：
```java
File f = new File("C:\\Windows\\notepad.exe");
```
```java
File f = new File("/usr/bin/javac");
```
	* Windows平台使用\作为路径分隔符，在Java字符串中需要用\\表示一个\。
	* Linux平台使用/作为路径分隔符
传入相对路径时，相对路径前面加上当前目录就是绝对路径：
```java
// 假设当前目录是C:\Docs
File f1 = new File("sub\\javac"); // 绝对路径是C:\Docs\sub\javac
File f3 = new File(".\\sub\\javac"); // 绝对路径是C:\Docs\sub\javac
File f3 = new File("..\\sub\\javac"); // 绝对路径是C:\sub\javac
```
可以用.表示当前目录，..表示上级目录。
* File对象有3种形式表示的路径，
	* 一种是getPath()，返回构造方法传入的路径
	* 一种是getAbsolutePath()，返回绝对路径
	* 一种是getCanonicalPath，它和绝对路径类似，但是返回的是规范路径。
```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        File f = new File("..");
        System.out.println(f.getPath()); 
        System.out.println(f.getAbsolutePath());
        System.out.println(f.getCanonicalPath());
    }
}
```
```java
.. 
/app/.. 
/ 
```
绝对路径可以表示成C:\Windows\System32\..\notepad.exe，而规范路径就是把.和..转换成标准的绝对路径后的路径：C:\Windows\notepad.exe。
* 因为Windows和Linux的路径分隔符不同，File对象有一个静态变量用于表示当前平台的系统分隔符：
```java
System.out.println(File.separator); // 根据当前平台打印"\"或"/"
```
### 文件和目录
* File对象既可以表示文件，也可以表示目录。
* 特别要注意的是，构造一个File对象，即使传入的文件或目录不存在，代码也不会出错，因为构造一个File对象，并不会导致任何磁盘操作。只有当我们调用File对象的某些方法的时候，才真正进行磁盘操作。
例如，调用isFile()，判断该File对象是否是一个已存在的文件，调用isDirectory()，判断该File对象是否是一个已存在的目录：
```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        File f1 = new File("C:\\Windows");
        System.out.println(f1.isFile());
        System.out.println(f1.isDirectory());
    }
}
```
* 用File对象获取到一个文件时，还可以进一步判断文件的权限和大小：
	* 	boolean canRead() ：是否可读；
	* 	boolean canWrite() ：是否可写；
	* 	boolean canExecute() ：是否可执行；
	对目录而言，是否可执行表示能否列出它包含的文件和子目录。
	* 	long length() ：文件字节大小。
### 创建和删除文件
* 当File对象表示一个文件时，可以通过createNewFile()创建一个新文件，用delete()删除该文件：
```java
File file = new File("/path/to/file");
if (file.createNewFile()) {
    // 文件创建成功:
    // TODO:
    if (file.delete()) {
        // 删除文件成功:
    }
}
```
* 有些时候，程序需要读写一些临时文件，File对象提供了createTempFile()来创建一个临时文件，以及deleteOnExit()在JVM退出时自动删除该文件。
```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        File f = File.createTempFile("tmp-", ".txt"); // 提供临时文件的前缀和后缀
        f.deleteOnExit(); // JVM退出时自动删除
        System.out.println(f.isFile());
        System.out.println(f.getAbsolutePath());
    }
}
```
```java
true 
/tmp/tmp-2200188531917171427.txt 
```
### 遍历文件和目录
* 当File对象表示一个目录时，可以使用list()和listFiles()列出目录下的文件和子目录名。listFiles()提供了一系列重载方法，可以过滤不想要的文件和目录：
```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        File f = new File("C:\\Windows");
        File[] fs1 = f.listFiles(); // 列出所有文件和子目录
        printFiles(fs1);
        File[] fs2 = f.listFiles(new FilenameFilter() { // 仅列出.exe文件
            public boolean accept(File dir, String name) {
                return name.endsWith(".exe"); // 返回true表示接受该文件
            }
        });
        printFiles(fs2);
    }

    static void printFiles(File[] files) {
        System.out.println("==========");
        if (files != null) {
            for (File f : files) {
                System.out.println(f);
            }
        }
        System.out.println("==========");
    }
}
```
* 和文件操作类似，File对象如果表示一个目录，可以通过以下方法创建和删除目录：
	* 	boolean mkdir()：创建当前File对象表示的目录；
	* 	boolean mkdirs()：创建当前File对象表示的目录，并在必要时将不存在的父目录也创建出来；
	* 	boolean delete()：删除当前File对象表示的目录，当前目录必须为空才能删除成功。
### Path
* Java标准库还提供了一个Path对象，它位于java.nio.file包。
* Path对象和File对象类似，但操作更加简单：
```java
import java.io.*;
import java.nio.file.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Path p1 = Paths.get(".", "project", "study"); // 构造一个Path对象
        System.out.println(p1);
        Path p2 = p1.toAbsolutePath(); // 转换为绝对路径
        System.out.println(p2);
        Path p3 = p2.normalize(); // 转换为规范路径
        System.out.println(p3);
        File f = p3.toFile(); // 转换为File对象
        System.out.println(f);
        for (Path p : Paths.get("..").toAbsolutePath()) { // 可以直接遍历Path
            System.out.println("  " + p);
        }
    }
}
```
```java
./project/study 
/app/./project/study 
/app/project/study 
/app/project/study 
  app 
  .. 
```
* 如果需要对目录进行复杂的拼接、遍历等操作，使用Path对象更方便。
### 练习
请利用File对象列出指定目录下的所有子目录和文件，并按层次打印
```java
import java.io.File;

public class Main {
	public static void main(String[] args) throws IOException {
		File currentDir = new File(".");
		listDir(currentDir.getCanonicalFile());
	}

	static void listDir(File dir) {
		printName(dir, 1);
	}
	
	static void printName(File dir, int level) {
        //获取文件级别，生成空格
		StringBuilder sp = new StringBuilder("");
		for(int i=1; i<level; i++) {
			sp.append("  ");
		}

        //打印空格及文件名，若为目录加入"\"
		System.out.print(sp.toString()+dir.getName());
		if (dir.isDirectory()) {
			System.out.println("\\");
		}else {
			System.out.println();
		}
		
        //获取子目录及子文件，有子目录则进行递归
		File[] fs = dir.listFiles();
		if (fs != null) {
			for(File f:fs) {
				printName(f, level+1);
			}
		}
	}
}
```
## InputStream
* InputStream就是Java标准库提供的最基本的输入流。
* 它位于java.io这个包里。java.io包提供了所有同步IO的功能。
* 要特别注意的一点是，InputStream并不是一个接口，而是一个抽象类，它是所有输入流的超类。
* 这个抽象类定义的一个最重要的方法就是int read()，签名如下：
```java
public abstract int read() throws IOException;
```
这个方法会读取输入流的下一个字节，并返回字节表示的int值（0~255）。
如果已读到末尾，返回-1表示不能继续读取了。
### FileInputStream
* FileInputStream是InputStream 的一个子类。
* 顾名思义，FileInputStream 就是从文件流中读取数据。
* 下面的代码演示了如何完整地读取一个FileInputStream 的所有字节：
```java
public void readFile() throws IOException {
    // 创建一个FileInputStream对象:
    InputStream input = new FileInputStream("src/readme.txt");
    for (;;) {
        int n = input.read(); // 反复调用read()方法，直到返回-1
        if (n == -1) {
            break;
        }
        System.out.println(n); // 打印byte的值
    }
    input.close(); // 关闭流
}
```
### 关闭流
* 在计算机中，类似文件、网络端口这些资源，都是由操作系统统一管理的。
* 应用程序在运行的过程中，如果打开了一个文件进行读写，完成后要及时地关闭，以便让操作系统把资源释放掉，否则，应用程序占用的资源会越来越多，不但白白占用内存，还会影响其他应用程序的运行。
* InputStream 和OutputStream 都是通过close() 方法来关闭流。关闭流就会释放对应的底层资源。
### 读写错误
* 我们还要注意到在读取或写入IO流的过程中，可能会发生错误
* 例如，文件不存在导致无法读取，没有写权限导致写入失败，等等，这些底层错误由Java虚拟机自动封装成IOException异常并抛出。
* 因此，所有与IO操作相关的代码都必须正确处理IOException。
* 仔细观察上面的代码，会发现一个潜在的问题：如果读取过程中发生了IO错误，InputStream就没法正确地关闭，资源也就没法及时释放。
* 因此，我们需要用try ... finally来保证InputStream在无论是否发生IO错误的时候都能够正确地关闭：
```java
public void readFile() throws IOException {
    InputStream input = null;
    try {
        input = new FileInputStream("src/readme.txt");
        int n;
        while ((n = input.read()) != -1) { // 利用while同时读取并判断
            System.out.println(n);
        }
    } finally {
        if (input != null) { input.close(); }
    }
}
```
用try ... finally来编写上述代码会感觉比较复杂，更好的写法是利用Java 7引入的新的try(resource)的语法，只需要编写try语句，让编译器自动为我们关闭资源。推荐的写法如下：
```java
public void readFile() throws IOException {
    try (InputStream input = new FileInputStream("src/readme.txt")) {
        int n;
        while ((n = input.read()) != -1) {
            System.out.println(n);
        }
    } // 编译器在此自动为我们写入finally并调用close()
}
```
实际上，编译器并不会特别地为InputStream 加上自动关闭。编译器只看try(resource = ...) 中的对象是否实现了java.lang.AutoCloseable 接口，如果实现了，就自动加上finally 语句并调用close() 方法。InputStream和OutputStream 都实现了这个接口，因此，都可以用在
try(resource)中。
### 缓冲
* 在读取流的时候，一次读取一个字节并不是最高效的方法。
* 很多流支持一次性读取多个字节到缓冲区，对于文件和网络流来说，利用缓冲区一次性读取多个字节效率往往要高很多。
* InputStream提供了两个重载方法来支持读取多个字节：
	* 	int read(byte[] b)：读取若干字节并填充到byte[]数组，返回读取的字节数
	* 	int read(byte[] b, int off, int len)：指定byte[]数组的偏移量和最大填充数
* 利用上述方法一次读取多个字节时，需要先定义一个byte[]数组作为缓冲区，read()方法会尽可能多地读取字节到缓冲区， 但不会超过缓冲区的大小。read()方法的返回值不再是字节的int值，而是返回实际读取了多少个字节。如果返回-1，表示没有更多的数据了。
* 利用缓冲区一次读取多个字节的代码如下：
```java
public void readFile() throws IOException {
    try (InputStream input = new FileInputStream("src/readme.txt")) {
        // 定义1000个字节大小的缓冲区:
        byte[] buffer = new byte[1000];
        int n;
        while ((n = input.read(buffer)) != -1) { // 读取到缓冲区
            System.out.println("read " + n + " bytes.");
        }
    }
}
```
### 阻塞
* 在调用InputStream的read()方法读取数据时，我们说read()方法是阻塞（Blocking）的。它的意思是，对于下面的代码：
```java
int n;
n = input.read(); // 必须等待read()方法返回才能执行下一行代码
int m = n;
```
执行到第二行代码时，必须等read()方法返回后才能继续。
* 因为读取IO流相比执行普通代码，速度会慢很多，因此，无法确定read()方法调用到底要花费多长时间。
### InputStream实现类
* 用FileInputStream 可以从文件获取输入流，这是InputStream 常用的一个实现类。
* 此外，ByteArrayInputStream 可以在内存中模拟一个InputStream ：
```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        byte[] data = { 72, 101, 108, 108, 111, 33 };
        try (InputStream input = new ByteArrayInputStream(data)) {
            int n;
            while ((n = input.read()) != -1) {
                System.out.println((char)n);
            }
        }
    }
}
```
* ByteArrayInputStream 实际上是把一个byte[] 数组在内存中变成一个
InputStream ，虽然实际应用不多，但测试的时候，可以用它来构造一个InputStream 。
* 举个栗子：我们想从文件中读取所有字节，并转换成char然后拼成一个字符串，可以这么写：
```java
public class Main {
    public static void main(String[] args) throws IOException {
        String s;
        try (InputStream input = new FileInputStream("C:\\test\\README.txt")) {
            int n;
            StringBuilder sb = new StringBuilder();
            while ((n = input.read()) != -1) {
                sb.append((char) n);
            }
            s = sb.toString();
        }
        System.out.println(s);
    }
}
```
要测试上面的程序，就真的需要在本地硬盘上放一个真实的文本文件。
如果我们把代码稍微改造一下，提取一个readAsString()的方法：
```java
public class Main {
    public static void main(String[] args) throws IOException {
        String s;
        try (InputStream input = new FileInputStream("C:\\test\\README.txt")) {
            s = readAsString(input);
        }
        System.out.println(s);
    }

    public static String readAsString(InputStream input) throws IOException {
        int n;
        StringBuilder sb = new StringBuilder();
        while ((n = input.read()) != -1) {
            sb.append((char) n);
        }
        return sb.toString();
    }
}
```
对这个String readAsString(InputStream input) 方法进行测试就相当简单，因为不一定要传入一个真的FileInputStream：
```java
public class Main {
    public static void main(String[] args) throws IOException {
        byte[] data = { 72, 101, 108, 108, 111, 33 };
        try (InputStream input = new ByteArrayInputStream(data)) {
            String s = readAsString(input);
            System.out.println(s);
        }
    }

    public static String readAsString(InputStream input) throws IOException {
        int n;
        StringBuilder sb = new StringBuilder();
        while ((n = input.read()) != -1) {
            sb.append((char) n);
        }
        return sb.toString();
    }
}
```
这就是面向抽象编程原则的应用：接受InputStream抽象类型，而不是具体的FileInputStream类型，从而使得代码可以处理InputStream的任意实现类。
## OutputStream
* 和InputStream相反，OutputStream是Java标准库提供的最基本的输出流。
* 和InputStream类似，OutputStream也是抽象类，它是所有输出流的超类。
* 这个抽象类定义的一个最重要的方法就是void write(int b)，签名如下：
```java
public abstract void write(int b) throws IOException;
```
这个方法会写入一个字节到输出流。
要注意的是，虽然传入的是int参数，但只会写入一个字节，即只写入int最低8位表示字节的部分（相当于b & 0xff）。
* 和InputStream类似，OutputStream也提供了close()方法关闭输出流，以便释放系统资源。
* 要特别注意：OutputStream还提供了一个flush()方法，它的目的是将缓冲区的内容真正输出到目的地。
为什么要有flush()？因为向磁盘、网络写入数据的时候，出于效率的考虑，操作系统并不是输出一个字节就立刻写入到文件或者发送到网络，而是把输出的字节先放到内存的一个缓冲区里（本质上就是一个byte[]数组），等到缓冲区写满了，再一次性写入文件或者网络。对于很多IO设备来说，一次写一个字节和一次写1000个字节，花费的时间几乎是完全一样的，所以OutputStream有个flush()方法，能强制把缓冲区内容输出。
* 通常情况下，我们不需要调用这个flush()方法，因为缓冲区写满了OutputStream会自动调用它，并且，在调用close()方法关闭OutputStream之前，也会自动调用flush()方法。
* 但是，在某些情况下，我们必须手动调用flush()方法。举个栗子：
小明正在开发一款在线聊天软件，当用户输入一句话后，就通过OutputStream的write()方法写入网络流。小明测试的时候发现，发送方输入后，接收方根本收不到任何信息，怎么肥四？
原因就在于写入网络流是先写入内存缓冲区，等缓冲区满了才会一次性发送到网络。如果缓冲区大小是4K，则发送方要敲几千个字符后，操作系统才会把缓冲区的内容发送出去，这个时候，接收方会一次性收到大量消息。
解决办法就是每输入一句话后，立刻调用flush()，不管当前缓冲区是否已满，强迫操作系统把缓冲区的内容立刻发送出去。
* 实际上，InputStream也有缓冲区。例如，从FileInputStream读取一个字节时，操作系统往往会一次性读取若干字节到缓冲区，并维护一个指针指向未读的缓冲区。然后，每次我们调用int read()读取下一个字节时，可以直接返回缓冲区的下一个字节，避免每次读一个字节都导致IO操作。当缓冲区全部读完后继续调用read()，则会触发操作系统的下一次读取并再次填满缓冲区。
### FileOutputStream
* 我们以FileOutputStream为例，演示如何将若干个字节写入文件流：
```java
public void writeFile() throws IOException {
    OutputStream output = new FileOutputStream("out/readme.txt");
    output.write(72); // H
    output.write(101); // e
    output.write(108); // l
    output.write(108); // l
    output.write(111); // o
    output.close();
}
```
* 每次写入一个字节非常麻烦，更常见的方法是一次性写入若干字节。这时，可以用OutputStream提供的重载方法void write(byte[])来实现：
```java
public void writeFile() throws IOException {
    OutputStream output = new FileOutputStream("out/readme.txt");
    output.write("Hello".getBytes("UTF-8")); // Hello
    output.close();
}
```
* 和InputStream一样，上述代码没有考虑到在发生异常的情况下如何正确地关闭资源。写入过程也会经常发生IO错误，例如，磁盘已满，无权限写入等等。我们需要用try(resource)来保证OutputStream在无论是否发生IO错误的时候都能够正确地关闭：
```java
public void writeFile() throws IOException {
    try (OutputStream output = new FileOutputStream("out/readme.txt")) {
        output.write("Hello".getBytes("UTF-8")); // Hello
    } // 编译器在此自动为我们写入finally并调用close()
}
```
### 阻塞
* 和InputStream一样，OutputStream的write()方法也是阻塞的。
### OutputStream实现类
* 用FileOutputStream可以从文件获取输出流，这是OutputStream常用的一个实现类。
* 此外，ByteArrayOutputStream可以在内存中模拟一个OutputStream：
```java
public class Main {
    public static void main(String[] args) throws IOException {
        byte[] data;
        try (ByteArrayOutputStream output = new ByteArrayOutputStream()) {
            output.write("Hello ".getBytes("UTF-8"));
            output.write("world!".getBytes("UTF-8"));
            data = output.toByteArray();
        }
        System.out.println(new String(data, "UTF-8"));
    }
}
```
* ByteArrayOutputStream 实际上是把一个byte[] 数组在内存中变成一个
OutputStream ，虽然实际应用不多，但测试的时候，可以用它来构造一个OutputStream 。
* 同时操作多个AutoCloseable资源时，在try(resource) { ... }语句中可以同时写出多个资源，用;隔开。例如，同时读写两个文件：
```java
// 读取input.txt，写入output.txt:
try (InputStream input = new FileInputStream("input.txt");
     OutputStream output = new FileOutputStream("output.txt"))
{
    input.transferTo(output); // transferTo的作用是?
}
```
对应还有transferFrom(), 与transferTo()相反
### 练习
请利用InputStream和OutputStream，编写一个复制文件的程序，它可以带参数运行：
```java
java CopyFile.java source.txt copy.txt
```
```java
public class CopyFile {

	public static void main(String[] args) throws IOException {
		args = new String[] {".\\input.txt",".\\output.txt"};
		if (args.length != 2) {
			System.err.println("Usage:\n  java CopyFile.java <source> <target>");
			System.exit(1);
		}
		copy(args[0], args[1]);
	}

	static void copy(String source, String target) throws IOException {
		// 友情提示：测试时请使用无关紧要的文件
		// 
		File inputFile = new File(source);
		File outputFile = new File(target);
		try(InputStream fileInputStream = new FileInputStream(inputFile);
			OutputStream fileOutputStream = new FileOutputStream(outputFile)){
			fileInputStream.transferTo(fileOutputStream);
		}
	}
}
```
## Filter模式
* Java的IO标准库提供的InputStream根据来源可以包括：
	* 	FileInputStream：从文件读取数据，是最终数据源；
	* 	ServletInputStream：从HTTP请求读取数据，是最终数据源；
	* 	Socket.getInputStream()：从TCP连接读取数据，是最终数据源；
	* 	...
* 如果我们要给FileInputStream添加缓冲功能，则可以从FileInputStream派生一个类：
```java
BufferedFileInputStream extends FileInputStream
```
* 如果要给FileInputStream添加计算签名的功能，类似的，也可以从
FileInputStream派生一个类：
```java
DigestFileInputStream extends FileInputStream
```
* 如果要给FileInputStream添加加密/解密功能，还是可以从FileInputStream派生一个类：
```java
CipherFileInputStream extends FileInputStream
```
* 如果要给FileInputStream添加缓冲和签名的功能，那么我们还需要派生
BufferedDigestFileInputStream。如果要给FileInputStream添加缓冲和加解密的功能，则需要派生BufferedCipherFileInputStream。
* 我们发现，给FileInputStream添加3种功能，至少需要3个子类。这3种功能的组合，又需要更多的子类：
```
                          ┌─────────────────┐
                          │ FileInputStream │
                          └─────────────────┘
                                   ▲
             ┌───────────┬─────────┼─────────┬───────────┐
             │           │         │         │           │
┌───────────────────────┐│┌─────────────────┐│┌─────────────────────┐
│BufferedFileInputStream│││DigestInputStream│││CipherFileInputStream│
└───────────────────────┘│└─────────────────┘│└─────────────────────┘
                         │                   │
    ┌─────────────────────────────┐ ┌─────────────────────────────┐
    │BufferedDigestFileInputStream│ │BufferedCipherFileInputStream│
    └─────────────────────────────┘ └─────────────────────────────┘
```
* 这还只是针对FileInputStream设计，如果针对另一种InputStream设计，很快会出现子类爆炸的情况。
* 因此，直接使用继承，为各种InputStream附加更多的功能，根本无法控制代码的复杂度，很快就会失控。
* 为了解决依赖继承会导致子类数量失控的问题，JDK首先将InputStream分为两大类：
	一类是直接提供数据的基础InputStream，例如：
	* 	FileInputStream
	* 	ByteArrayInputStream
	* 	ServletInputStream
	* 	...
	一类是提供额外附加功能的InputStream，例如：
	* 	BufferedInputStream
	* 	DigestInputStream
	* 	CipherInputStream
	* 	...
* 当我们需要给一个“基础”InputStream附加各种功能时，我们先确定这个能提供数据源的InputStream，因为我们需要的数据总得来自某个地方，例如，FileInputStream，数据来源自文件：
```java
InputStream file = new FileInputStream("test.gz");
```
* 紧接着，我们希望FileInputStream能提供缓冲的功能来提高读取的效率，因此我们用BufferedInputStream包装这个InputStream，得到的包装类型是BufferedInputStream ，但它仍然被视为一个InputStream：
```java
InputStream buffered = new BufferedInputStream(file);
```
* 最后，假设该文件已经用gzip压缩了，我们希望直接读取解压缩的内容，就可以再包装一个GZIPInputStream：
```java
InputStream gzip = new GZIPInputStream(buffered);
```
* 无论我们包装多少次，得到的对象始终是InputStream，我们直接用InputStream来引用它，就可以正常读取：
```asciidoc
┌─────────────────────────┐
│GZIPInputStream          │
│┌───────────────────────┐│
││BufferedFileInputStream││
││┌─────────────────────┐││
│││   FileInputStream   │││
││└─────────────────────┘││
│└───────────────────────┘│
└─────────────────────────┘
```
* 上述这种通过一个“基础”组件再叠加各种“附加”功能组件的模式，称之为Filter模式（或者装饰器模式：Decorator）。
* 它可以让我们通过少量的类来实现各种功能的组合：
```
                 ┌─────────────┐
                 │ InputStream │
                 └─────────────┘
                       ▲ ▲
┌────────────────────┐ │ │ ┌─────────────────┐
│  FileInputStream   │─┤ └─│FilterInputStream│
└────────────────────┘ │   └─────────────────┘
┌────────────────────┐ │     ▲ ┌───────────────────┐
│ByteArrayInputStream│─┤     ├─│BufferedInputStream│
└────────────────────┘ │     │ └───────────────────┘
┌────────────────────┐ │     │ ┌───────────────────┐
│ ServletInputStream │─┘     ├─│  DataInputStream  │
└────────────────────┘       │ └───────────────────┘
                             │ ┌───────────────────┐
                             └─│CheckedInputStream │
                               └───────────────────┘
```
类似的，OutputStream也是以这种模式来提供各种功能：
```
                  ┌─────────────┐
                  │OutputStream │
                  └─────────────┘
                        ▲ ▲
┌─────────────────────┐ │ │ ┌──────────────────┐
│  FileOutputStream   │─┤ └─│FilterOutputStream│
└─────────────────────┘ │   └──────────────────┘
┌─────────────────────┐ │     ▲ ┌────────────────────┐
│ByteArrayOutputStream│─┤     ├─│BufferedOutputStream│
└─────────────────────┘ │     │ └────────────────────┘
┌─────────────────────┐ │     │ ┌────────────────────┐
│ ServletOutputStream │─┘     ├─│  DataOutputStream  │
└─────────────────────┘       │ └────────────────────┘
                              │ ┌────────────────────┐
                              └─│CheckedOutputStream │
                                └────────────────────┘
```
### 编写FilterInputStream
* 我们也可以自己编写FilterInputStream，以便可以把自己的
FilterInputStream“叠加”到任何一个InputStream中。
* 下面的例子演示了如何编写一个CountInputStream，它的作用是对输入的字节进行计数：
```java
public class Main {
    public static void main(String[] args) throws IOException {
        byte[] data = "hello, world!".getBytes("UTF-8");
        try (CountInputStream input = new CountInputStream(new ByteArrayInputStream(data))) {
            int n;
            while ((n = input.read()) != -1) {
                System.out.println((char)n);
            }
            System.out.println("Total read " + input.getBytesRead() + " bytes");
        }
    }
}

class CountInputStream extends FilterInputStream {
    private int count = 0;

    CountInputStream(InputStream in) {
        super(in);
    }

    public int getBytesRead() {
        return this.count;
    }

    public int read() throws IOException {
        int n = in.read();
        if (n != -1) {
            this.count ++;
        }
        return n;
    }

    public int read(byte[] b, int off, int len) throws IOException {
        int n = in.read(b, off, len);
        if (n != -1) {
            this.count += n;
        }
        return n;
    }
}
```
```java
h 
e 
l 
l 
o 
, 
  
w 
o 
r 
l 
d 
! 
Total read 13 bytes 
```
* 注意到在叠加多个FilterInputStream，我们只需要持有最外层的InputStream
* 并且，当最外层的InputStream关闭时（在try(resource)块的结束处自动关闭），内层的InputStream的close()方法也会被自动调用，并最终调用到最核心的“基础”InputStream，因此不存在资源泄露。
## 操作Zip
* ZipInputStream 是一种FilterInputStream，它可以直接读取zip包的内容：
```
┌───────────────────┐
│    InputStream    │
└───────────────────┘
          ▲
          │
┌───────────────────┐
│ FilterInputStream │
└───────────────────┘
          ▲
          │
┌───────────────────┐
│InflaterInputStream│
└───────────────────┘
          ▲
          │
┌───────────────────┐
│  ZipInputStream   │
└───────────────────┘
          ▲
          │
┌───────────────────┐
│  JarInputStream   │
└───────────────────┘
```
另一个JarInputStream是从ZipInputStream派生，它增加的主要功能是直接读取jar文件里面的MANIFEST.MF文件。
因为本质上jar包就是zip包，只是额外附加了一些固定的描述文件。
### 读取zip包
* 我们要创建一个ZipInputStream，通常是传入一个FileInputStream作为数据源，然后，循环调用getNextEntry()，直到返回null，表示zip流结束。
* 一个ZipEntry表示一个压缩文件或目录，如果是压缩文件，我们就用read()方法不断读取，直到返回-1：
```java
try (ZipInputStream zip = new ZipInputStream(new FileInputStream(...))) {
    ZipEntry entry = null;
    while ((entry = zip.getNextEntry()) != null) {
        String name = entry.getName();
        if (!entry.isDirectory()) {
            int n;
            while ((n = zip.read()) != -1) {
                ...
            }
        }
    }
}
```
### 写入zip包
* ZipOutputStream是一种FilterOutputStream，它可以直接写入内容到zip包。
* 我们要先创建一个ZipOutputStream ，通常是包装一个FileOutputStream 
* 然后，每写入一个文件前，先调用putNextEntry()，然后用write()写入
byte[]数据
* 写入完毕后调用closeEntry()结束这个文件的打包。
```java
try (ZipOutputStream zip = new ZipOutputStream(new FileOutputStream(...))) {
    File[] files = ...
    for (File file : files) {
        zip.putNextEntry(new ZipEntry(file.getName()));
        zip.write(getFileDataAsBytes(file));
        zip.closeEntry();
    }
}
```
上面的代码没有考虑文件的目录结构。
如果要实现目录层次结构，new ZipEntry(name)传入的name要用相对路径。
## 读取classpath资源
* 很多Java程序启动的时候，都需要读取配置文件。例如，从一个.properties文件中读取配置：
```java
String conf = "C:\\conf\\default.properties";
try (InputStream input = new FileInputStream(conf)) {
    // TODO:
}
```
这段代码要正常执行，必须在C盘创建conf目录，然后在目录里创建default.properties文件。
但是，在Linux系统上，路径和Windows的又不一样。
因此，从磁盘的固定目录读取配置文件，不是一个好的办法。
有没有路径无关的读取文件的方式呢？
* 我们知道，Java存放.class的目录或jar包也可以包含任意其他类型的文件，例如：
	* 	配置文件，例如.properties；
	* 	图片文件，例如.jpg；
	* 	文本文件，例如.txt，.csv；
	* 	……
* 从classpath读取文件就可以避免不同环境下文件路径不一致的问题：如果我们把default.properties文件放到classpath中，就不用关心它的实际存放路径。
* 在classpath中的资源文件，路径总是以／开头，我们先获取当前的Class对象，然后调用getResourceAsStream()就可以直接从classpath读取任意的资源文件：
```java
try (InputStream input = getClass().getResourceAsStream("/default.properties")) {
    // TODO:
}
```
调用getResourceAsStream()需要特别注意的一点是，如果资源文件不存在，它将返回null。
因此，我们需要检查返回的InputStream是否为null，如果为null，表示资源文件在classpath中没有找到：
```java
try (InputStream input = getClass().getResourceAsStream("/default.properties")) {
    if (input != null) {
        // TODO:
    }
}
```
* 如果我们把默认的配置放到jar包中，再从外部文件系统读取一个可选的配置文件，就可以做到既有默认的配置文件，又可以让用户自己修改配置：
```java
Properties props = new Properties();
props.load(inputStreamFromClassPath("/default.properties"));
props.load(inputStreamFromFile("./conf.properties"));
```
这样读取配置文件，应用程序启动就更加灵活。
## 序列化
* 序列化是指把一个Java对象变成二进制内容，本质上就是一个byte[]数组。
* 为什么要把Java对象序列化呢？
因为序列化后可以把byte[]保存到文件中，或者把byte[]通过网络传输到远程，这样，就相当于把Java对象存储到文件或者通过网络传输出去了。
* 有序列化，就有反序列化，即把一个二进制内容（也就是byte[]数组）变回Java对象。
有了反序列化，保存到文件中的byte[]数组又可以“变回”Java对象，或者从网络上读取byte[]并把它“变回”Java对象。
* 我们来看看如何把一个Java对象序列化。
* 一个Java对象要能序列化，必须实现一个特殊的java.io.Serializable接口，它的定义如下：
```java
public interface Serializable {
}
```
Serializable接口没有定义任何方法，它是一个空接口。
我们把这样的空接口称为“标记接口”（Marker Interface），实现了标记接口的类仅仅是给自身贴了个“标记”，并没有增加任何方法。
### 序列化
* 把一个Java对象变为byte[]数组，需要使用ObjectOutputStream。
它负责把一个Java对象写入一个字节流：
```java
import java.io.*;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        try (ObjectOutputStream output = new ObjectOutputStream(buffer)) {
            // 写入int:
            output.writeInt(12345);
            // 写入String:
            output.writeUTF("Hello");
            // 写入Object:
            output.writeObject(Double.valueOf(123.456));
        }
        System.out.println(Arrays.toString(buffer.toByteArray()));
    }
}
```
```java
[-84, -19, 0, 5, 119, 11, 0, 0, 48, 57, 0, 5, 72, 101, 108, 108, 111, 115, 114, 0, 16, 106, 97, 118, 97, 46, 108, 97, 110, 103, 46, 68, 111, 117, 98, 108, 101, -128, -77, -62, 74, 41, 107, -5, 4, 2, 0, 1, 68, 0, 5, 118, 97, 108, 117, 101, 120, 114, 0, 16, 106, 97, 118, 97, 46, 108, 97, 110, 103, 46, 78, 117, 109, 98, 101, 114, -122, -84, -107, 29, 11, -108, -32, -117, 2, 0, 0, 120, 112, 64, 94, -35, 47, 26, -97, -66, 119] 
```
* ObjectOutputStream既可以写入基本类型，如int，boolean，也可以写入String（以UTF-8编码），还可以写入实现了Serializable接口的Object。
* 因为写入Object时需要大量的类型信息，所以写入的内容很大。
### 反序列化
* 和ObjectOutputStream 相反，ObjectInputStream 负责从一个字节流读取Java对象：
```java
try (ObjectInputStream input = new ObjectInputStream(...)) {
    int n = input.readInt();
    String s = input.readUTF();
    Double d = (Double) input.readObject();
}
```
* 除了能读取基本类型和String类型外，调用readObject()可以直接返回一个Object对象。
要把它变成一个特定类型，必须强制转型。
* readObject()可能抛出的异常有：
	* 	ClassNotFoundException：没有找到对应的Class；
	对于ClassNotFoundException，这种情况常见于一台电脑上的Java程序把一个Java对象，例如，Person对象序列化以后，通过网络传给另一台电脑上的另一个Java程序，但是这台电脑的Java程序并没有定义Person类，所以无法反序列化。
	* 	InvalidClassException：Class不匹配。
	对于InvalidClassException，这种情况常见于序列化的Person对象定义了一个int类型的age字段，但是反序列化时，Person类定义的age字段被改成了long类型，所以导致class不兼容。
	为了避免这种class定义变动导致的不兼容，Java的序列化允许class定义一个特殊的serialVersionUID静态变量，用于标识Java类的序列化“版本”，通常可以由IDE自动生成。如果增加或修改了字段，可以改变serialVersionUID的值，这样就能自动阻止不匹配的class版本：
```java
public class Person implements Serializable {
    private static final long serialVersionUID = 2709425275741743919L;
}
```
* 要特别注意反序列化的几个重要特点：
反序列化时，由JVM直接构造出Java对象，不调用构造方法，构造方法内部的代码，在反序列化时根本不可能执行。
### 安全性
* 因为Java的序列化机制可以导致一个实例能直接从byte[]数组创建，而不经过构造方法，因此，它存在一定的安全隐患。
* 一个精心构造的byte[]数组被反序列化后可以执行特定的Java代码，从而导致严重的安全漏洞。
* 实际上，Java本身提供的基于对象的序列化和反序列化机制既存在安全性问题，也存在兼容性问题。
* 更好的序列化方法是通过JSON这样的通用数据结构来实现，只输出基本类型（包括String）的内容，而不存储任何与代码相关的信息。
* Java的序列化机制仅适用于Java，如果需要与其它语言交换数据，必须使用通用的序列化方法，例如JSON。
## Reader
* Reader是Java的IO库提供的另一个输入流接口。
* 和InputStream的区别是，InputStream是一个字节流，即以byte为单位读取，而Reader是一个字符流，即以char为单位读取：
	* InputStream
		* 字节流，以byte为单位
		* 读取字节（-1，0~255）：int read()
		* 读到字节数组：int read(byte[] b)
	* Reader
		* 字符流，以char为单位 
		* 读取字符（-1，0~65535）：int read()
		* 读到字符数组：int read(char[] c)
* java.io.Reader是所有字符输入流的超类，它最主要的方法是：
```java
public int read() throws IOException;
```
这个方法读取字符流的下一个字符，并返回字符表示的int，范围是0~65535。如果已读到末尾，返回-1。
### FileReader
* FileReader是Reader的一个子类，它可以打开文件并获取Reader。
* 下面的代码演示了如何完整地读取一个FileReader的所有字符：
```java
public void readFile() throws IOException {
    // 创建一个FileReader对象:
    Reader reader = new FileReader("src/readme.txt"); // 字符编码是???
    for (;;) {
        int n = reader.read(); // 反复调用read()方法，直到返回-1
        if (n == -1) {
            break;
        }
        System.out.println((char)n); // 打印char
    }
    reader.close(); // 关闭流
}
```
* 如果我们读取一个纯ASCII编码的文本文件，上述代码工作是没有问题的。
* 但如果文件中包含中文，就会出现乱码，因为FileReader默认的编码与系统相关，例如，Windows系统的默认编码可能是GBK，打开一个UTF-8编码的文本文件就会出现乱码。
* 要避免乱码问题，我们需要在创建FileReader时指定编码：
```java
Reader reader = new FileReader("src/readme.txt", StandardCharsets.UTF_8);
```
* 和InputStream类似，Reader也是一种资源，需要保证出错的时候也能正确关闭，所以我们需要用try (resource)来保证Reader在无论有没有IO错误的时候都能够正确地关闭：
```java
try (Reader reader = new FileReader("src/readme.txt", StandardCharsets.UTF_8) {
    // TODO
}
```
* Reader还提供了一次性读取若干字符并填充到char[]数组的方法：
```java
public int read(char[] c) throws IOException
```
它返回实际读入的字符个数，最大不超过char[]数组的长度。
返回-1表示流结束。
利用这个方法，我们可以先设置一个缓冲区，然后，每次尽可能地填充缓冲区：
```java
public void readFile() throws IOException {
    try (Reader reader = new FileReader("src/readme.txt", StandardCharsets.UTF_8)) {
        char[] buffer = new char[1000];
        int n;
        while ((n = reader.read(buffer)) != -1) {
            System.out.println("read " + n + " chars.");
        }
    }
}
```
### CharArrayReader
* CharArrayReader可以在内存中模拟一个Reader ，它的作用实际上是把一个char[]数组变成一个Reader ，这和ByteArrayInputStream 非常类似：
```java
try (Reader reader = new CharArrayReader("Hello".toCharArray())) {
}
```
### StringReader
* StringReader可以直接把String作为数据源，它和CharArrayReader几乎一样：
```java
try (Reader reader = new StringReader("Hello")) {
}
```
### InputStreamReader
* Reader 和InputStream有什么关系？
* 除了特殊的CharArrayReader和StringReader，普通的Reader实际上是基于InputStream构造的
因为Reader需要从InputStream中读入字节流（byte），然后，根据编码设置，再转换为char就可以实现字符流。如果我们查看FileReader的源码，它在内部实际上持有一个FileInputStream。
* 既然Reader本质上是一个基于InputStream的byte到char的转换器，那么，如果我们已经有一个InputStream，想把它转换为Reader，是完全可行的。
* InputStreamReader就是这样一个转换器，它可以把任何InputStream转换为Reader。示例代码如下：
```java
// 持有InputStream:
InputStream input = new FileInputStream("src/readme.txt");
// 变换为Reader:
Reader reader = new InputStreamReader(input, "UTF-8");
```
构造InputStreamReader时，我们需要传入InputStream，还需要指定编码，就可以得到一个Reader对象。
* 上述代码可以通过try (resource)更简洁地改写如下：
```java
try (Reader reader = new InputStreamReader(new FileInputStream("src/readme.txt"), "UTF-8")) {
    // TODO:
}
```
上述代码实际上就是FileReader的一种实现方式。
使用try (resource) 结构时，当我们关闭Reader时，它会在内部自动调用
InputStream的close()方法，所以，只需要关闭最外层的Reader对象即可。
## Writer
* Reader是带编码转换器的InputStream，它把byte转换为char，而Writer就是带编码转换器的OutputStream，它把char转换为byte并输出。
* Writer和OutputStream的区别如下：
	* OutputStream
		* 字节流，以byte为单位
		* 写入字节（0~255）：void write(int b)
		* 写入字节数组：void write(byte[] b)
	* Writer
		* 字符流，以char为单位
		* 写入字符（0~65535）：void write(int c)
		* 写入字符数组：void write(char[] c)
		* 写入String：void write(String s)
* Writer是所有字符输出流的超类，它提供的方法主要有：
	* 	写入一个字符（0~65535）：void write(int c)；
	* 	写入字符数组的所有字符：void write(char[] c)；
	* 	写入String表示的所有字符：void write(String s)。
### FileWriter
* FileWriter就是向文件中写入字符流的Writer。它的使用方法和FileReader似：
```java
try (Writer writer = new FileWriter("readme.txt", StandardCharsets.UTF_8)) {
    writer.write('H'); // 写入单个字符
    writer.write("Hello".toCharArray()); // 写入char[]
    writer.write("Hello"); // 写入String
}
```
### CharArrayWriter
* CharArrayWriter可以在内存中创建一个Writer，它的作用实际上是构造一个缓冲区，可以写入char，最后得到写入的char[]数组，这和
ByteArrayOutputStream非常类似：
```java
try (CharArrayWriter writer = new CharArrayWriter()) {
    writer.write(65);
    writer.write(66);
    writer.write(67);
    char[] data = writer.toCharArray(); // { 'A', 'B', 'C' }
}
```
### StringWriter
* StringWriter也是一个基于内存的Writer，它和CharArrayWriter类似。
* 实际上，StringWriter在内部维护了一个StringBuffer，并对外提供了Writer接口。
### OutputStreamWriter
* 除了CharArrayWriter和StringWriter外，普通的Writer实际上是基于OutputStream构造的，它接收char，然后在内部自动转换成一个或多个byte，并写入OutputStream。
* 因此，OutputStreamWriter就是一个将任意的OutputStream转换为
Writer的转换器：
```java
try (Writer writer = new OutputStreamWriter(new FileOutputStream("readme.txt"), "UTF-8")) {
    // TODO:
}
```
上述代码实际上就是FileWriter的一种实现方式。
这和上一节的InputStreamReader是一样的。
## PrintStream && PrintWriter
### PrintStream
* PrintStream是一种FilterOutputStream，它在OutputStream的接口上，额外提供了一些写入各种数据类型的方法：
	* 写入int：print(int)
	* 写入boolean：print(boolean)
	* 写入String：print(String)
	* 写入Object：print(Object)，实际上相当于print(object.toString())
	* …
	以及对应的一组println()方法，它会自动加上换行符。
* 我们经常使用的System.out.println()实际上就是使用PrintStream打印各种数据。
其中，System.out是系统默认提供的PrintStream，表示标准输出：
```java
System.out.print(12345); // 输出12345
System.out.print(new Object()); // 输出类似java.lang.Object@3c7a835a
System.out.println("Hello"); // 输出Hello并换行
```
* System.err是系统默认提供的标准错误输出。
* PrintStream和OutputStream相比，除了添加了一组print()/println()方法，可以打印各种数据类型，比较方便外，它还有一个额外的优点，就是不会抛出IOException，这样我们在编写代码的时候，就不必捕获IOException。
### PrintWriter
* PrintStream最终输出的总是byte数据，而PrintWriter则是扩展了Writer接口，它的print()/println()方法最终输出的是char数据。
* 两者的使用方法几乎是一模一样的：
```java
public class Main {
    public static void main(String[] args)     {
        StringWriter buffer = new StringWriter();
        try (PrintWriter pw = new PrintWriter(buffer)) {
            pw.println("Hello");
            pw.println(12345);
            pw.println(true);
        }
        System.out.println(buffer.toString());
    }
}
```
## 使用Files
* 从Java 7开始，提供了Files和Paths这两个工具类，能极大地方便我们读写文件。
* 虽然Files和Paths是java.nio包里面的类，但他俩封装了很多读写文件的简单方法
* 例如，我们要把一个文件的全部内容读取为一个byte[]，可以这么写：
```java
byte[] data = Files.readAllBytes(Paths.get("/path/to/file.txt"));
```
* 如果是文本文件，可以把一个文件的全部内容读取为String：
```java
// 默认使用UTF-8编码读取:
String content1 = Files.readString(Paths.get("/path/to/file.txt"));
// 可指定编码:
String content2 = Files.readString(Paths.get("/path/to/file.txt"), StandardCharsets.ISO_8859_1);
// 按行读取并返回每行内容:
List<String> lines = Files.readAllLines(Paths.get("/path/to/file.txt"));
```
* 写入文件也非常方便：
```java
// 写入二进制文件:
byte[] data = ...
Files.write(Paths.get("/path/to/file.txt"), data);
// 写入文本并指定编码:
Files.writeString(Paths.get("/path/to/file.txt"), "文本内容...", StandardCharsets.ISO_8859_1);
// 按行写入文本:
List<String> lines = ...
Files.write(Paths.get("/path/to/file.txt"), lines);
```
* 此外，Files工具类还有copy()、delete()、exists()、move()等快捷方法操作文件和目录。
* 最后需要特别注意的是，Files提供的读写方法，受内存限制，只能读写小文件，例如配置文件等，不可一次读入几个G的大文件。
* 读写大型文件仍然要使用文件流，每次只读写一部分文件内容。











