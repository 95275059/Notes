# Python笔记44--内置函数int

## 描述

* int函数用于将一个字符串或数字转换为整型

## 语法

```python
class int(x, base=10)
```

+ x : 字符串或者数字

+ base : 进制数，默认10进制

  注意：当x为字符串时，可用base参数；但是当x为数字时，不可使用base参数

  + 当x为字符串且存在base参数时，将x看做base型数字，并将其转换为10进制数字

+ 返回值 : 返回整型数据

## 实例

```python
a = "10"
print(int(a, base=2))
```

```python
2
```

