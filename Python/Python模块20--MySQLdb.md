# Python模块20--MySQLdb

## 简介

Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口。

MySQLdb 是用于Python链接Mysql数据库的接口，它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。

## 安装

```python
import MySQLdb
```

+ 出现 No module named MySQLdb

  参考笔记：PythonTips1

## 使用

### 数据库连接

已知在数据库TESTDB下创建了表EMPLOYEE

EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。

连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123"

#### 基本连接操作

+ ```python
  db_conn = MySQLdb.connect(host,user,passwd,db,charset)
  ```

  connect方法建立一个与数据库的连接

+ ```python
  cursor = db_conn.cursor()
  ```

  创建一个游标对象

+ ```python
  cursor.exeute(sql)
  ```

  执行SQL语句，注意这里不返回结果，只是执行而已

+ ```
  db_conn.commit()
  ```

  提交到数据库执行

  **commit()方法需要跟在增（insert）、删（delete）、改（update）、查（select）的任何execute()语句后面。commit是把查询语句提交到数据库内，而不只是要向数据库提交增、添的数据。**

  commit 就是确定提交的意思，比如你用test账户登录数据库insert到表中一条记录，而不commit,那么别的账户在登录这个数据库时就查询不到你insert 的记录，且自己的账户在后续查询中国也查不到insert记录；而commit后则其他账户就能查询到你insert的记录了。

  COMMIT 是提交你的DML操作.

+ ```python
  res = cursor.fetchall()
  ```

  fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）

  ```python
  res = cursor.fetchone()
  while res:
      print res
      res = cursor.fetchone() 
  ```

  fetchone只给出一条数据，然后游标后移。

  游标移动过最后一行数据后再fetch就得到None

+ ```python
  db_conn.rollback()
  ```

  回滚操作

  在数据库里做修改后 （ update ,insert , delete）未commit 之前  使用rollback  可以恢复数据到修改之前。

  rollback就是回滚的意思，比如你用test账户登录数据库delete表中一条记录，这时你查询这个表时，则delete的记录不存在；再rollback后，你再查询你delete的记录时，发现被删除的记录又回来了。

  ROLLBACK 是取消你的DML操作.

+ ```python
  db_conn.close()
  ```

  断开连接

#### 使用DictCursor

python在使用MySQLdb库的时候，在默认情况下cursor方法返回的是BaseCursor类型对象，BaseCursor类型对象在执行查询后每条记录的结果是tuple结构。

如果我们以后更改数据表的字段顺序，那么我们必须要修改现有数据库代码，如何才能做到不修改代码呢，很简单，使用DictCursor，这样得到的结果集就是字典形式的了，我们可以用key去获取数据了。

如果要返回字典(dict)表示的记录，就要设置cursorclass参数为MySQLdb.cursors.DictCursor类。

```python
cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
```

### 关于commit和rollback

https://blog.csdn.net/xiaotom5/article/details/8133067?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control

https://blog.csdn.net/jack_ywj/article/details/52151975?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-3&spm=1001.2101.3001.4242





