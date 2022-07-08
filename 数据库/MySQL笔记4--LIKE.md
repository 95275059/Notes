# MySQL笔记4--LIKE

* LIKE运算符用于WHERE表达式中，以搜索匹配字段中的指定内容

* 语法如下：

  ```sql
  WHERE column LIKE pattern
  
  WHERE column NOT LIKE pattern
  ```

  在LIKE前面加上NOT运算符时，表示与LIKE相反的意思，即选择column不包含pattern的数据记录

* LIKE通常与通配符%一起使用，%表示通配pattern中出现的内容，而不加通配符%的LIKE语法，表示精确匹配，其实际效果等同于 = 等于运算符

* LIKE使用示例

  ```sql
  SELECT * FROM user WHERE username LIKE '小%'；
  ```

   上面这个例子是找出所有username以"小"开头的记录

  注意：小%表示以小开头，而后面可以是任意字符，同样，%小，表示以”小”结尾，而%小%则表示包含“小”这个字符(并一同包含"%小"和"小%"这两种情况)

* MySQL LIKE 大小写

  * MySQL LIKE 匹配字符的时候，默认情况下是不区分大小写的

  * 如果在需要区分大小写的时候，可以加入BINARY操作符：

    ```sql
    SELECT * FROM username WHERE LIKE BINARY '%azz%'
    
    SELECT * FROM username WHERE LIKE BINARY '%Azz%'
    ```

* MySQL LIKE 中文匹配

  由于数据存储编码问题，在某些情况下，MySQL进行LIKE搜索返回的数据除了符合要求的数据外，往往还会返回许多不相干的数据，这时候也需要在LIKE后面加上BINARY操作符进行二进制比较

  ```sql
  SELECT * FROM username WHERE LIKE BINARY '%小%'
  ```

  注意：当LIKE匹配时加上BINARY操作符之后，则会严格区分英文大小写，因此检索的内容中如果出现中英文混合且需要忽略英文大小写的时候，就会遇见问题，这个时候可以引入MySQL中的UPPER()和COUNT()函数：

  UPPER() ：将英文字符转成大写，同UCASE()

  CONCAT()：将多个字符串连接成一个字符串

  所以，当我们要进行中英文混合匹配检索且要忽略英文大小写时候，可以用下面的语句：

  ```sql
  SELECT * FROM username WHERE UPPER(username) LIKE BINARY CONCAT('%',UPPER('a中文b')，'%');
  ```

* LIKE 的效率

  LIKE运算符要对字段数据进行逐一扫描匹配，实际执行的效率比较差

