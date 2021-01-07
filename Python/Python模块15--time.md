# Python模块15--time

### 简介

用于格式化转换日期和时间

时间间隔是**以秒为单位**的**浮点小数**

每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示

时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年

---

### 时间元组

很多Python函数用一个元组装起来的9组数字（struct_time元组）处理时间:

| 序号 | 字段         | 值                                   |
| :--- | :----------- | :----------------------------------- |
| 0    | 4位数年      | 2008                                 |
| 1    | 月           | 1 到 12                              |
| 2    | 日           | 1到31                                |
| 3    | 小时         | 0到23                                |
| 4    | 分钟         | 0到59                                |
| 5    | 秒           | 0到61 (60或61 是闰秒)                |
| 6    | 一周的第几日 | 0到6 (0是周一)                       |
| 7    | 一年的第几日 | 1到366 (儒略历)                      |
| 8    | 夏令时       | -1, 0, 1, -1是决定是否为夏令时的旗帜 |

struct_time元组的结构属性

| 序号 | 属性     | 值                                   |
| :--- | :------- | :----------------------------------- |
| 0    | tm_year  | 2008                                 |
| 1    | tm_mon   | 1 到 12                              |
| 2    | tm_mday  | 1 到 31                              |
| 3    | tm_hour  | 0 到 23                              |
| 4    | tm_min   | 0 到 59                              |
| 5    | tm_sec   | 0 到 61 (60或61 是闰秒)              |
| 6    | tm_wday  | 0到6 (0是周一)                       |
| 7    | tm_yday  | 1 到 366(儒略历)                     |
| 8    | tm_isdst | -1, 0, 1, -1是决定是否为夏令时的旗帜 |

---

### 获取当前时间

```python
import time

print(time.time())
localtime = time.localtime(time.time())
print("本地时间为：", localtime)
```

```python
1607264870.6710033
本地时间为： time.struct_time(tm_year=2020, tm_mon=12, tm_mday=6, tm_hour=22, tm_min=27, tm_sec=50, tm_wday=6, tm_yday=341, tm_isdst=0)
```

---

### 获取格式化的时间

+ 最简单的获取可读的时间模式的函数是asctime()

  ```python
  import time
  
  print(time.time())
  localtime = time.localtime(time.time())
  print("本地时间为：", localtime)
  asctime = time.asctime(localtime)
  print("格式化时间后为", asctime)
  ```

  ```python
  1607265011.782272
  本地时间为： time.struct_time(tm_year=2020, tm_mon=12, tm_mday=6, tm_hour=22, tm_min=30, tm_sec=11, tm_wday=6, tm_yday=341, tm_isdst=0)
  格式化时间后为 Sun Dec  6 22:30:11 2020
  ```

---

### 格式化日期

+ 使用strftime方法格式化日期

  ```python
  time.strftime(format[, t])
  ```

+ 使用mktime方法将格式字符串日期转换为日期

  ```python
  time.mktime(str_time, format)
  ```

+ 时间日期格式化符号

  | 符号 | 含义                                      |
  | ---- | ----------------------------------------- |
  | %y   | 两位数的年份表示（00-99）                 |
  | %Y   | 四位数的年份表示（000-9999）              |
  | %m   | 月份（01-12）                             |
  | %d   | 月内中的一天（0-31）                      |
  | %H   | 24小时制小时数（0-23）                    |
  | %I   | 12小时制小时数（01-12）                   |
  | %M   | 分钟数（00-59）                           |
  | %S   | 秒（00-59）                               |
  | %a   | 本地简化星期名称                          |
  | %A   | 本地完整星期名称                          |
  | %b   | 本地简化的月份名称                        |
  | %B   | 本地完整的月份名称                        |
  | %c   | 本地相应的日期表示和时间表示              |
  | %j   | 年内的一天（001-366）                     |
  | %p   | 本地A.M.或P.M.的等价符                    |
  | %U   | 一年中的星期数（00-53）星期天为星期的开始 |
  | %w   | 星期（0-6），星期天为星期的开始           |
  | %W   | 一年中的星期数（00-53）星期一为星期的开始 |
  | %x   | 本地相应的日期表示                        |
  | %X   | 本地相应的时间表示                        |
  | %Z   | 当前时区的名称                            |
  | %%   | %号本身                                   |

---

### 获取秒级、毫秒级、微妙级时间戳

```python
import time
print("原始时间数据：", time.time())
print("秒级时间戳：", int(time.time()))
print("毫秒级时间戳：",int(round(time.time()*1000)))
print("微妙级时间戳：", int(round(time.time()*1000000)))
```

```python
原始时间数据： 1607341410.326192
秒级时间戳： 1607341410
毫秒级时间戳： 1607341410326
微妙级时间戳： 1607341410326192
```

---

### 实例

```python
import time

print(time.time())
localtime = time.localtime(time.time())
print("localtime (本地时间): ", localtime)
asctime = time.asctime(localtime)
print("asctime : ", asctime)

# 格式化成2016-03-20 11:45:39形式
strftime1 = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print("strftime1 : ", strftime1)
# 格式化成Sat Mar 28 22:24:24 2016形式
strftime2 = time.strftime("%a %b %d %H:%M:%S %Y", localtime)
print("strftime2 : ", strftime2)
strftime3 = time.strftime("%a %b %d %H:%M:%S %Y")
print("strftime3 : ", strftime3)
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
time_stamp = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print("time_stamp : ", time_stamp)
```





