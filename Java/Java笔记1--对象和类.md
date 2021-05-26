# Java笔记1--对象和类
## 对象
* 对象是类的一个实例，有状态和行为
	* 状态：属性
	* 行为：方法
## 类
* 创建对象的模版
* 类型变量
	* 局部变量
	在方法，构造方法或者语句块中定义的变量
	变量声明和初始化都在方法中，方法结束后，变量就会自动销毁
	* 成员变量
	成员变量是定义在类中，方法体之外的变量。
	这种变量在创建对象的时候实例化
	成员变量可以被类中方法，构造方法和特定类的语句块访问
	* 类变量
	类变量也声明在类中，方法体之外
	但必须声明为static类型
* 构造方法
	* 每个类都有一个构造方法
	* 如果没有显式地为类定义构造方法，Java编译器将会为该类提供一个默认构造方法
	* 在创建一个对象的时候，至少要调用一个构造方法
	* 构造方法的名称必须与类同名
	* 一个类可以有多个构造方法
## 创建对象
* 使用关键字new来创建一个新的对象
* 创建对象需要三步
	* 声明：声明一个对象，包括对象名称和对象类型
	* 实例化：使用关键字new来创建一个对象
	* 初始化：使用new创建对象时，会调用构造方法初始化对象
* 实例
	```java
	public class Puppy{
		int puppyAge;
		public Puppy(String name){
			//这个构造器仅有一个参数：name
			System.out.println("Puppy Name is :" + name ); 
		}
		public void setAge(int age){
			puppyAge = age
		}
		public int getAge(){
			System.out.println(“Puppy’s age is : ” + puppyAge);
			return puppyAge;
		}
		public static void main(String []args){
			// 下面的语句将创建一个Puppy对象
			Puppy myPuppy = new Puppy( "tommy" );
			myPuppy.setAge(2);
			myPuppy.getAge();
			System.out.println(“Variable Value : ” + myPuppy.puppyAge);
		}
}
	```
	
	注：Java规定，某个类定义的`public static void main(String[] args)`是Java程序的固定入口方法，因此，Java程序总是从`main`方法开始执行。
## 源文件声明规则
当在一个源文件中定义多个类，并且还有import语句和package语句时，要特别注意这些规则
	* 一个源文件中只能有一个public类
	* 一个源文件可以有多个非public类
	* 源文件的名称应该和public类的类名保持一致
	* 如果一个类定义在某个包中，那么package语句应该在源文件的首行
	* 如果源文件包含import语句，那么应该放在package语句和类定义之间。如果没有package语句，那么import语句应该在源文件中最前面
	* import语句和package语句对源文件中定义的所有类都有效
	在同一源文件中，不能给不同的类不同的包声明
## Java包
包主要用来对类和接口进行分类
* import语句
在Java中，需要给出一个完整的限定名，包括包名和类名，这样Java编译器就能很容易的定位到源代码或者类
import语句就是用来提供一个合理的路径，使得编译器可以找到某个类
	* 实例
		```java
		import java.I’m.*;
		```
	该命令行将会命令编译器载入java_installation_java_io路径下的所有类

	
