# Python笔记40--内置函数max

### 描述

max方法返回给定参数的最大值，参数可以为序列

### 语法

```python
max(x,y,z[,key=fun])
```

+ x , y , z : 数值表达式
+ key : 可选参数，经过key处理后再进行比较
+ 返回值 : 返回给定参数最大值

### 实例

```python
eth_ip = {'1':44,'2':33,'3':22,'4':11}
router_id1 = max(eth_ip)
print(router_id1)
print(type(router_id1))
router_id2 = max(eth_ip, key=eth_ip.get)
print(router_id2)
print(type(router_id2))
```

```python
4
<class 'str'>
1
<class 'str'>
```

+ router_id1 ，没有使用key参数，默认直接比较字典的键
+ router_id2，指定key = eth_ip.get，则比较字典的值
+ 返回都是字典的键