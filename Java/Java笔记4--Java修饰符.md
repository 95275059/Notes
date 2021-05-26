# Java笔记4--Java修饰符
## 介绍
* Java语言提供了很多修饰符，主要分为以下两类
	* 访问修饰符
	* 非访问修饰符
* 修饰符用来定义类，方法或者变量，通常放在语句的最前端
```java
public class className{
    // ...
} 
private boolean myFlag;
static final double weeks = 9.5;
protected static final int BOXWIDTH =42;
public static void main(String[] arguments){
    // ...
}
```
## 访问控制修饰符
* Java中，可以使用访问控制符来保护对类，变量，方法和构造方法的访问
* Java支持四种不同的访问权限
	* default
	默认的，在同一包内可见，不使用任何修饰符
	* private
	私有的，在同一类内可见
	* public
	共有的，对所有类可见
	* protected
	受保护的，对同一包内的类和所有子类可见
### 默认访问修饰符
* 不使用任何关键字
* 使用默认访问修饰符声明的变量和方法，对同一个包内的类是可见的。
* 接口里的变量都隐式声明为public static final（常量？）
* 接口里的方法默认情况下访问权限为public
```java
String version = “1.5.1”;
boolean processOrder() {
    return true;
}
```
### 私有访问修饰符
* 私有访问修饰符是最严格的访问级别
* 被声明为private的方法，变量和构造方法只能被所属类访问
* 类和接口不能声明为private
* 声明为私有访问类型的变量只能通过类中公共的getter方法被外部类访问
* private访问修饰符的使用主要用来隐藏类的实现谢姐和保护类的数据
```java
public class Logger {
    private String format;
    public String getFormat() {
        return this.format;
    }
    public void setFormat(String format) {
        this.format = format;
    }
}
```
### 公有访问修饰符
* 被声明为public的类，方法，构造方法和接口能够被任何其他类访问
* 如果几个相互访问的public类分布在不同的包中，则需要导入相应public类所在的包
* 由于类的继承性，类所有的公有方法和变量都能被其子类继承
* Java程序的main()方法必须设置成公有的，否则，Java解释器将不能运行该类
```java
public static void main(String[] arguments) {
    // ...
}
```
### 受保护的访问修饰符
* 被声明为protected的变量，方法和构造方法能够被同一个包中的任何其他类访问，也能够被不同包中的子类访问
* 类和接口不能声明为protected， 方法和成员变量能够声明为protected，但是接口的成员变量和成员方法不能声明为protected
* 子类能访问protected修饰符声明的方法和变量
这样就能够保护不相关的类使用这些方法和变量
```java
class AudioPlayer {
    protected boolean openSpeaker(Speaker sp) {
        // ...
    }
}
class StreamingAudioPlayer {
    boolean openSpeaker(Speaker sp) {
        // ...
    }
}
```
	* 父类AudioPlayer的openSpeaker方法使用了protected修饰符，子类重载了父类的openSpeaker方法
	* 如果把openSpeaker()方法声明为private，那么除了AudioPlayer之外的类将不能访问该方法
	* 如果把openSpeaker()方法声明为public，那么所有的类都能访问该方法
	* 如果把openSpeaker()方法声明为protected，那么只有AudioPlayer 及其子类
### 访问控制和继承
* 父类中声明为public的方法在子类中也必须为public
* 父类中声明为protected的方法在子类中要么声明为protected，要么声明为public。不能声明为private
* 父类中声明为private的方法，不能被继承
## 非访问修饰符
### static修饰符
* 用来创建类方法和类变量
* 静态变量
	* static关键字用来声明独立于对象的静态变量，无论一个类实例化多少对象，它的静态变量只有一份拷贝
	* 静态变量也被称为类变量
	* 局部变量不能被声明为static变量
* 静态方法
	* static关键字用来声明独立于对象的静态方法
	* 静态方法不能使用类的非静态变量
	* 静态方法从参数列表得到数据，然后计算这些数据
* 对于类变量和方法的访问可以直接使用classname.variablename和classname.methodname的方式访问
* 示例
```java
public class InstanceCounter {
    private static int numInstances = 0;
    protected static int getCount(){
        return numInstances;
    }
    private static void addInstance() {
        numInstances ++;
    }
    InstanceCounter() {
        InstanceCounter.addInstance();
    }
    public static void main(String[] arguments) {
        System.out.println(“Starting with” + InstanceCounter.getCount() + “ instances”);
        for (int i = 0;i < 500; ++i){
            new InstanceCounter(); 
        }
        System.out.println(“Created ” + InstanceCounter.getCount() + “ instances”);
    } 
}
```
```java
Started with 0 instances
Created 500 instances
```
### final修饰符
* 用来修饰类，方法和变量
* final修饰的类不能够被继承
	* 没有类能够继承final类的任何特性
```java
public final class Test {
    // ...
}
```
* final修饰的方法可以被子类继承，但不能被子类类重新定义
	* 声明final方法的主要目的是防止该方法的内容被修改
```java
public class Test {
    public final void changeName() {
        // ...
    } 
}
```
* final修饰的变量为常量，是不可修改的
	* final变量能被显式地初始化并且只能初始化一次
	* 被声明为final的对象的引用不能指向不同的对象
	* 但是final对象里的数据可以改变
	* 即，final对象的引用不能改变，但里面的值可以改变
	* final修饰符通常和static修饰符一起使用来创建类常量
```java
public class Test {
    final int value = 10;
    public static final int BOXWIDTH = 6;
    static final String TITLE = “Manager”;
    public void changeValue() {
        value = 12; //将输出一个错误，因为final变量不可修改
    }
}
```
```java
public class FinalDemo {
    static final Integer[] arr = new Integer[]{1, 2, 3};
    public static void main(String[] args) {
    System.out.println(“arr原来的数组内容：” + Arrays.toString(arr));
    System.out.println(“arr原来的内存地址：” + arr.hashCode());
    arr[0] = 4;  //final对象里的数据可以改变
    arr[1] = 5;
    arr[2] = 6;
    System.out.println(“修改后arr的数组内容：” + Arrays.toString(arr));
    System.out.println(“修改后arr的内存地址：” + arr.hashCode());  //final对象的引用不会改变
    arr = new Integer[]{7, 8, 9}; // 会报错，因为final对象内容可变但引用不可变，即不能被重新赋值
    }   
}
```
### abstract修饰符
* 用来创建抽象类和抽象方法
* 抽象类
	* 在面向对象的概念中，所有的对象都是通过类来描绘的，但是反过来，并不是所有的类都是用来描绘对象的，如果一个类中没有包含足够的信息来描绘一个具体的对象，这样的类就是抽象类
	* 抽象类除了不能实例化对象之外，类的其他功能依然存在，成员变量，成员方法和构造方法的访问和普通类一样
	* 抽象类不能用来实例化对象，声明抽象类的唯一目的是为了将来对该类进行扩充
	* 由于抽象类不能实例化对象，所以抽象类必须被继承，才能使用
	* 父类包含了子类集合的常见方法，但是由于父类本身是抽象的，所以不能使用这些方法
	* 一个类只能继承一个抽象类，而一个类却可以实现多个接口
	* 一个类不能同时被abstract和final修饰
	* 如果一个类包含抽象方法，那么该类一定要声明为抽象类，否则将出现编译错误
	* 抽象类可以包含抽象方法和非抽象方法
```java
abstract class Caravan {
    private double price;
    private String model;
    private String year;
    public abstract void goFast();  //抽象方法
    public abstract void changeColor();
}
```
* 抽象方法
	* 抽象方法是一种没有任何实现的方法，该方法的具体实现由子类提供
	* 抽象方法不能被声明为final和static
	* 任何继承抽象类的子类必须实现父类的所有抽象方法，除非该子类也是抽象类
	* 如果一个类包含若干个抽象方法，那么该类必须声明为抽象类
	* 抽象类可以不包含抽象方法
	* 抽象方法的声明以分号结尾
	例如：public abstract sample();
```java
public abstract class SuperClass {
    abstract void m(); //抽象方法 
}
class SubClass extends SuperClass {
    //实现抽象方法
    void m() {
        // ...
    }
}
```
### synchronized修饰符
* synchronized关键字声明的方法同一时间只能被一个线程访问
* synchronized修饰符可以应用于全部四个访问修饰符
```java
public synchronized void showDetails() {
    // ...
}
```
### transient修饰符
* 序列化的对象包含被transient修饰的实例变量时，Java虚拟机（JVM）跳过该特定的变量
* 即，如果用transient声明一个实例变量，当对象存储时，它的值不需要维持
* 即，用transient关键字标记的成员变量不参与序列化过程
* 作用：
Java的serialization提供了一种持久化对象实例的机制。当持久化对象时，可能有一个特殊的对象数据成员，我们不想用serialization机制来保存它。为了在一个特定对象的一个域上关闭serialization，可以在这个域前加上关键字transient。
* 该修饰符包含在定义变量的语句中，用来预处理类和变量的数据类型
```java
public transient int limit = 55;  //
public int b;
```
### volatile修饰符
* volatile修饰的成员变量在每次被线程访问时，都强迫从共享内存中重读该成员变量的值
* 而且，当成员变量发生变化时，强迫线程将变化值回写到共享内存
* 这样，在任何时刻，两个不同的线程总是看到某个成员变量的同一个值
* 一个volatile对象引用可能是null
```java
public class MyRunnable implements Runnable {
    private volatile boolean active;
    public void run() {
        active = true;
        while (active){  // line 1
            // ...
        }
    }
    public void stop() {
        active = false; // line 2
    }
}
```
一般地，在一个线程中调用run()方法，在另一个线程中调用stop()方法
如果line 1中的active位于缓冲区的值被使用，那么当把line 2中的active设置成false时，循环也不会停止
