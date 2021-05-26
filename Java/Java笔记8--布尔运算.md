# Java笔记8--布尔运算
* 对于布尔类型boolean，永远只有true和false两个值
## 分类
* 布尔运算是一种关系运算
	* 比较运算符
	>, >=, <, <=, ==, !=
	* 与运算
	&&
	* 或运算
	|| 
	* 非运算
	!
* 示例
```java
boolean isGreater = 5 >3; //true
int age = 12;
boolean isZero = age == 0; //false
boolean isNonZero = !isZero //true
boolean isAdult = age >= 18; //false
boolean isTeenager = age > 6 && age < 18; //true
```
## 优先级
从高到低：
* !
* >, >=, <, <=
* ==, !=
* &&
* ||
## 短路运算
* 布尔运算的一个重要特点是短路运算
* 如果一个布尔运算的表达式能提前确定结果，则后续的计算不再执行，直接返回结果
* false && x 的结果总是false
* true || x 的结果总是true
* 示例
```java
public class Main{
    public static void main(String[] args) {
        boolean b = 5 < 3;
        boolean result = b && (5/0 > 0);
        System.out.println(result);
    }
}
```
如果没有短路运算，&&后面的表达式会由于除数为0而报错，但实际并没有报错
如果b的值为true，则因为无法短路运算，运行会报错
## 三元运算符
* Java提供一个三元运算符 `b?x:y`,它根据第一个布尔表达式的结果，分别返回后续两个表达式之一的计算结果
如果b为true，则返回x的计算结果
如果b为false，则返回y的计算结果
* 示例
```java
public class Main {
    public static void main(String[] args) {
        int n = -100;
        int x = n >= 0 ? n : -n;
        System.out.println(x);
    }
}
```
	* 这是一个求绝对值的表达式
* 三元元算 `b?x:y`会首先计算b，如果b为true，则只计算x，否则只计算y
* x和y的类型必须相同，因为返回值不是boolean，而是x和y之一