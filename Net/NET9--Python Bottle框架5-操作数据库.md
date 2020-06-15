# NET9--Python Bottle框架5-操作数据库

1. Python的数据库接口

   + Python标准数据库接口为Python DB-API。

   + Python 数据库接口支持非常多的数据库：GadFly、mSQL、MySQL、PostgreSQL、Microsoft SQL Server 2000、Informix、Interbase、Oracle、Sybase。
   + 不同的数据库需要下载不同的DB-API模块。
   + DB-API是一个规范，它定义了一系列必须的对象和数据库存取方式，以便为各种底层数据库系统和多种多样的数据库接口程序提供一致的访问接口
   + Python的DB-API，为大多数的数据库实现了接口，使用它连接各数据库后，就可以用相同的方式操作各个数据库。
   + Python DB-API使用流程：
     + 引入API模块
     + 获取与数据库的连接
     + 执行SQL语句和存储过程
     + 关闭数据库连接

2. MySQLdb

   MySQLdb是用于Python连接Mysql数据库的接口，它实现了Python数据库API规范V2.0，基于MySQL C API上建立的。

3. 安装MySQLdb

   yum install -y MySQL-python

1. 实例

   Mysql_study.py

   ```python
   #!/usr/bin/python
   # -*- coding:UTF-8 -*-
   
   import MySQLdb
   #打开数据库连接
   db = MySQLdb.connect("192.168.1.161","root","123456","TESTDB",charset="utf8")
#使用cursor()方法获取操作游标
   cursor=db.cursor()
   #使用execute()方法执行SQL语句
   cursor.execute("SELECT VERSION()")
   #使用 fetchone()方法获取一条数据
   data = cursor.fetchone()
   
   print("Database version : %s"%data)
#关闭数据库
   db.close()
   
   ```
   
   + MySQLdb.connect():连接数据库
   
     参数：
   
     + host：数据库主机名。默认是本地主机
     + user：数据库登录名。默认是当前用户
     + passwd：数据库登录user的密码。默认为空
     + db：要使用的数据库名。无默认值
     + port：MySQL服务使用的TCP端口。默认是3306
     + charset：数据库编码
     + unix_socket：指定mysql的socket路径。
   
     ```python
     db = MySQLdb.connect(host = '192.168.1.161',
                                  user = 'root',
                                  passwd = '123456',
                                  db = 'TESTDB',
                                  charset = 'utf8')
     ```
   
   + db.close():关闭数据库
   
   + cursor游标对象
   
      执行SQL语句前要获得一个指定连接的Cursor对象，由Cursor对象执行SQL查询并获取结果。 
   
     + 获得cursor
   
       cursor=db.cursor()
   
     + 关闭cursor
   
        执行SQL结束后正常要关闭cursor对象 
   
       cursor.close()
   
   + 增删改除操作
   
     cursor提供了 execute方法用于执行SQL操作 
   
     + execute(query[,parameters])
   
       + query: SQL字符串 
       +  parameters：一个序列或映射，返回值是所影响的记录数 
   
       例如：
   
       + cursor.execute( "select * from user where name = %s and age = %s" , {'name':'drfdai', 'age':30}  ) 
   
         这里和字符串的格式化操作类似，但不管参数是什么类型，都要用'%s' 
   
     + executemany( query [, parametersequence] )
   
       query是一个查询字符串，parametersequence是一个参数序列。这一序列的每一项都是一个序列或映射象。但executemany只适合插入、更新或删除操作，而不适用于查询操作。 
   
       例如：
   
       + cur.execute("insert user(name, age) values(%s, %s)", (('drf', 31), ('jiang', 21))) 
   
   + 获取结果
   
     获取结果集有三种方法，fetchone、fetchall和fetchmany，返回结果是一个tuple（元组）对象，tuple中的每一个元素对应查询结果中的一条记录。 
   
     +  fetchone()返回结果集中的一条记录 
     +  fetchall()返回结果集中的所有记录 
     +  fetchmany([N])返回结果集中N条记录 
   
   + 提交
   
     mysql现在一般会默认InnoDB作为默认引擎，InnoDB引擎执行插入、更新、删除操作后要进行提交，才会更新数据库，因此需要用commit()提交后，才会生效执行的SQL 
   
     +  cur.commit() 
   
   + 回滚
   
     如果在执行事务SQL时，需要回滚的话，就用rollback() 。
   
     可以回退INSERT,UPDATE和DELETE语句。
   
     不能回退SELECT语句。
     
     不能回退CREATE和DROP操作。
     
     + db.rollback()

---

---

---

==python mysql的代码查看MySQLStudy项目==







