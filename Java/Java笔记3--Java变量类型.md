# Java笔记3--Java变量类型
## 三种变量类型
* 在Java语言中，所有的变量在使用前必须声明
```java
type identifier [ = value][, identifier [ = value] ...]
```
	* type 为Java数据类型
	* identifier 是变量名
	* 可以使用逗号隔开来声明多个同类型变量
* Java语言支持的变量类型
	* 局部变量：类的方法中的变量
	* 实例变量：独立于方法之外的变量，不过没有static修饰
	* 类变量（静态变量）：独立于方法之外的变量，用static修饰
```java
public class Variable{
    static int allClicks = 0; //类变量
    String str = “hello world”;  //实例变量
    public void method(){
	      int I = 0;  //局部变量
    }
}
```
## 局部变量
### 特点
* 局部变量声明在方法，构造方法或者语句块中
* 局部变量在方法，构造方法或者语句块被执行的时候创建，当它们执行完成后，变量将会被销毁
* 而在语句块中定义的局部变量，它有一个作用域，就是从定义处开始，到语句块结束。超出了作用域引用这些变量，编译器会报错。
* 访问修饰符不能用于局部变量
* 局部变量值在声明它的方法，构造方法或者语句块中可见
* 局部变量是在栈上分配的
* 局部变量没有默认值，所以局部变量被声明后，必须经过初始化，猜可以使用
### 实例
```java
public class Test{
    public void pupAge(){
        int age = 0;
        age = age + 7;
        System.out.println(“Puppy age is : ” + age);
    }
	  public static void main(String args[]){
        Test test = new Test();
        test.pupAge();
    }
}
```
* age是一个局部变量，定义在pupAge()方法中，它的作用域就限制在这个方法中
## 实例变量
### 特点
* 实例变量声明在一个类中，但在方法，构造方法和语句块之外
* 当一个对象被实例化之后，每个实例变量的值就跟着确定
* 实例变量在对象创建的时候创建，在对象被销毁的时候销毁
* 实例变量的值应该至少被一个方法，构造方法或者语句块引用，是的外部能够通过这些方法获取实例变量信息
* 实例变量可以声明在使用前或者使用后
* 访问修饰符可以修饰实例变量
* 实例变量对于类中的方法，构造方法或者语句块是可见的
一般情况下应该把实例变量设为私有
通过使用访问修饰符可以使实例变量对自类可见
* 实例变量具有默认值
	* 数值型变量的默认值是0
	* 布尔型变量的默认值是false
	* 引用类型变量的默认值是null
* 变量的值可以在声明时指定，也可以在构造方法中指定
* 实例变量可以直接通过变量名访问，但在静态方法以及其他类中，就应该使用完全限定名：ObjectReference.VariableName
### 实例
```java
import java.io.*;
public class Employee{
   // 这个成员变量对子类可见
   public String name;
   // 私有变量，仅在该类可见
   private double salary;
   //在构造器中对name赋值
   public Employee (String empName){
       name = empName;
   }
   //设定salary的值
   public void setSalary(double empSal){
       salary = empSal;
   }  
   // 打印信息
   public void printEmp(){
       System.out.println("name  : " + name );
       System.out.println("salary :" + salary);
   }

   public static void main(String args[]){
       Employee empOne = new Employee("Ransika");
       empOne.setSalary(1000);
       empOne.printEmp();
   }
}
```
## 类变量（静态变量）
### 特点
* 类变量也称为静态变量，在类中以static关键字声明，但必须在方法，构造方法和语句块之外
* 无论一个类创造了多少个对象，类只拥有类变量的一份拷贝
* 静态变量除了被声明为常量外很少使用
？常量是指声明为public/private，final和static类型的变量
常量初始化后不可改变
* 静态变量存储在静态存储区
经常被声明为常量，很少单独使用static声明变量
* 静态变量在程序开始时创建，在程序结束时销毁
* 静态变量与实例变量具有相似的可见性
但为了对类的使用者可见，大多数静态按量声明为public 类型
* 静态变量的有默认值，和实例变量类似
	* 数值型变量的默认值是0
	* 布尔型变量的默认值是false
	* 引用类型变量的默认值是null
* 静态变量的值可以在声明的时候指定，也可以在构造方法中指定。此外，静态变量还可以在静态语句块中初始化
* 静态变量可以通过：ClassName.VariableName的方式访问
* 静态变量被声明为public static final 类型时，静态变量名称必须使用大写字母。其他情况下，其命名方式与实例变量以及局部变量的命名方式一致
### 实例
```java
import java.io.*;
public class Employee{
   //salary是静态的私有变量
   private static double salary;
   // DEPARTMENT是一个常量
   public static final String DEPARTMENT = "Development ";
   public static void main(String args[]){
       salary = 1000;
       System.out.println(DEPARTMENT+"average salary:"+salary);
   }
}
```
其他类如果想要访问变量DEPARTMENT，可以：Employee.DEPARTMENT
