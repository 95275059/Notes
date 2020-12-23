# Python14--面向对象程序设计-类的继承和多态

### 类的继承

> class 派生类名(基类名):
>
>  派生类成员

+ 在Python2.7中使用继承时，务必在定义父类时在括号内指定object

+ 派生类可以继承父类的公有成员，但不能继承其私有成员

+ 基类的构造函数不会被自动调用，需要在派生类的构造中专门调用

  + 基类名.\__init__(self[,其他参数])

  + super().\__init__(其他参数)

    基类（父类），也称为超类（superclass）

    + python2.7

      super(基类名,self).\__init__(其他参数)

+ 在派生类中调用基类的方法

  + 基类名.方法名()

    需要加上基类的类名前缀，且需要带上self参数变量，而在类中调用普通函数时不需要带self

  + 使用super()实现

    + python2.7

      super(基类名,self).基类方法

    + python 3

      super().基类方法

+ Python总是先在本类中查找要调用的方法，找不到才去基类中找

+ 判断类之间的关系/某对象实例是哪个类的对象：

  issubclass(sub,sup):布尔函数，判断类sub是否是类sup的子类或者子孙类

  isinstance(obj,Class):布尔函数，判断对象obj是否是Class类或者Class子类的实例

  type(obj):返回对象obj数据类型(类)

+ 

---

### 类的多继承

> class SubClassName(ParentClass1[,ParentClass2,...]):
>
> 派生类成员

---

### 方法重写--多态性

 重写必须发生在继承中，指在派生类中重写基类的方法。

 子类和父类都存在相同的方法func()时，子类的func()覆盖了父类的func()。

---

### 多态

+ 在继承关系中，若一个实例的数据类型是某个子类，那它的数据类型也可以被看作是父类。
+ 而反之不成立：若一个实例的数据类型是某个父类，其子类不是它的数据类型

```python
class Anmial:
    def run(self):
        print("Animal is running...")
class Cat(Anmial):
    def run(self):
        print("Cat is running...")
class Dog(Anmial):
    def run(self):
        print("Dog is running...")

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Anmial())
run_twice(Cat())
run_twice(Dog())
```

+ 对于一个变量，只要知道它是Animal类型，无须确切知道它的子类型，就可以放心调用run()方法，而具体调用的run()方法是作用在Animal,Dog,Cat对象上，由运行时该对象的确切类型决定。
+ 调用方只管调用，不管细节。当新增一种Animal子类时，只需要确保run()方法编写正确，不用管原来的代码是如何调用的

+ 开闭原则
  + 对拓展开放：允许新增Animal子类
  + 对修改封闭：不需要修改以来Animal类型的run_twice()等函数

### 运算符重载

+ 通过运算符重载实现对象之间的运算。

+ 常用有的运算符与函数方法的对应关系：

  | 方法       | 运算  |
  | ---------- | ----- |
  | \__add__() | +     |
  | \__lt__()  | <     |
  | \__or__()  | 或    |
  | \__sub__() | -     |
  | \__eq__()  | =     |
  | \__mul__() | *     |
  | \__len__() | 长度  |
  | \__div__() | /     |
  | \__str__() | print |


```python
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):      #重写print()方法
        return ('Vector(%d,%d)'%(self.a,self.b))
    def __add__(self, other):    #重写加法运算符
        return Vector(self.a+other.a,self.b+other.b)
    def __sub__(self, other):    #重写减法运算符
        return Vector(self.a-other.a,self.b-other.b)

v1=Vector(2,10)
v2=Vector(5,-2)
print(v1+v2)
```











 