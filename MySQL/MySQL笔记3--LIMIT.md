# MySQL笔记3--LIMIT

+ 查询第一行记录

  ```mysql
  SELECT * FROM table LIMIT 1;
  ```

+ 查询第n行到第m行的记录

  ```mysql
  SELECT * FROM table LIMIT n-1,m-n+1;
  ```

+ 查询第n行的记录

  ```mysql
  SELECT * FROM table LIMIT n-1,1;
  ```

+ 查询前n行的记录

  ```mysql
  SELECT * FROM table LIMIT 0,n;
  ```

  ```mysql
  SELECT * FROM table LIMIT n;
  ```

+ 查询后n行的记录

  ```mysql
  SELECT * FROM table ORDER BY id desc LIMIT n;
  ```

  示例

  ```mysql
  SELECT * FROM objects ORDER BY id desc LIMIT 2;
  ```

  ![笔记3-1](E:\Notes\MySQL\笔记3-1.png)