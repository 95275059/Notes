# MySQL笔记5--三值逻辑，NULL

## 三值逻辑

### NULL有两种：未知（unknown）和不适用（inapplicable）

* 未知

  不知道戴眼镜的人眼睛是什么颜色，就是未知。只要不摘掉眼睛，就不知道，但是这个人眼睛肯定有颜色的。

* 不适用

  不知道冰箱的眼睛是什么颜色。这就是不适用，这个属性不适用于冰箱。冰箱是没有眼睛的。

### 现在DBMS都将这两种类型NULL归为了一类，并采用三值逻辑

* True
* False
* UNKNOWN

### MySQL提供IS NULL和IS NOT NULL两种操作来对NULL特殊判断

### 为什么是IS NULL 而不是=NULL

SQL的保留字中，很多都被归类为谓词一类，例如>,<>,= 等比较谓词，以及BETWEEN, LIKE, IN, IS NULL等。总结，谓词是一种特殊的函数，返回值是真值。(前面提到的这个谓词，返回值都是true, false, unknown,SQL是三值逻辑，所以有三种真值）

因为查询结果只会包含WHERE子句里的判断结果为true的行！不包含判断结果为false和unknown的行。且不仅是等号，对NULL使用其他比较谓词（比如> NULL），结果也都是unknown。

重点理解：
NULL不是值，所以不能对其使用谓词，如果使用谓词，结果是unknown。
可以认为**它只是一个没有值的标记,而比较谓词只适用于比较值**。因此对非值的NULL使用比较谓词是没有意义的

### 如何理解IS NULL?是两个单词？IS空格NULL?

"NULL值" 和 "列的值为NULL"这个说法是错误的。**NULL不属于关系型数据库中的某种类型**。
我们为什么会误认为NULL是一个值？
可能因为混淆了别的语言，在一些语言中NULL是一个常量。还有个重要原因是IS NULL是两个单词，所以我以前也把IS当作谓词，比如IS-A,所以误认为NULL是一个值。特别是SQL里有IS TRUE, IS FALSE。在讲解SQL标准的书里提醒人那么样，我们应该把IS NULL看作一个谓词，如果可以IS_NULL或许更合适。

### 三值逻辑运算

unknown小写，是第三个真值。与作为NULL的一种UNKNOWN(未知)是不同的东西。小写是明确的布尔类型的真值，后者大写的既不是值也不是变量。为了对比不同：看x=x的情况。

```
unknown = unknown -> true
UNKNOWN = UNKNOWN ->unknown
```


重点：【三值逻辑运算】

```
NOT unknown => unknown
```

```
true OR unknown => true
unknown OR unknown => unknown
false OR unknown => unknown
```

```
true AND unknown => unknown
unknown AND unknown => unknown
false AND unknown => false
```

记忆：优先级：
AND:    false > unknown > true
OR:       true > unknown > false