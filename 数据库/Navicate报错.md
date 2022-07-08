# Navicate报错

## 内存越界

![Navicate报错-1](Navicate报错-1.png)

### 原因

这是**内存越界**的问题，需要**重新注册Windows的动态链接库**。

### 解决

**运行 -> cmd**，然后在命令行中输入：**for %1 in (%windir%\system32\*.dll) do regsvr32.exe /s %1** ，最后**回车运行**

# 使用GROUP BY 时报错

```python
Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column ‘csdn.liulancsdnblog.id’ which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```

### 错误原因

MySQL 5.7.5及以上功能依赖检测功能。

如果启用了ONLY_FULL_GROUP_BY，SQL模式（默认情况下），MySQL将拒绝选择列表，HAVING条件或ORDER BY列表的查询引用在GROUP BY子句中既未命名的非集合列，也不在功能上依赖于它们。

5.7.5之前，MySQL没有检测到功能依赖关系，默认情况下不启用ONLY_FULL_GROUP_BY。

### 解决

* 查询当前的@@global.sql_mode;

  ```sql
  select @@global.sql_mode;
  ```

  ```ini
  ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
  ```

* 进入mysql安装目录，打开my.cnf文件，在[msqld]后面追加对sql_mode的配置，删掉ONLY_FULL_GROUP_BY

  ```ini
  [mysql]
  default-character-set=utf8
  [mysqld]
  port=3306
  basedir=E:\MySQL\mysql-8.0.26-winx64
  datadir=E:\MySQL\mysql-8.0.26-winx64/data
  max_connections=200
  character-set-server=utf8
  default-storage-engine=innodb
  sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
  ```

  

