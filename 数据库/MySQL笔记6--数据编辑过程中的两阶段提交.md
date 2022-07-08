# MySQL笔记6--数据编辑过程中的两阶段提交

## 情景

* MySQL 数据库中的两阶段提交发生在数据变更期间（更新、删除、新增等）。

* 两阶段提交过程中涉及到了 MySQL 数据库中的两个日志系统：redo 日志和 binlog 文件。

## binlog文件

* binlog 是 MySQL server 层提供的[二进制](https://so.csdn.net/so/search?q=二进制&spm=1001.2101.3001.7020)文件，因此所有的存储引擎都可以使用 binlog 功能

* binlog 是追加写的逻辑日志，记录了执行语句的原始逻辑，文件写到指定大小后会切换到下一个文件继续写，并不会覆盖以前写过的日志文件。

* binlog 日志文件主要用于数据恢复和集群环境下各服务器之间的数据同步

  在工作中，我们误删了数据或者表之类，如果需要恢复的话都是利用 binlog 日志来恢复的，所以 binlog 日志是 MySQL 数据库中比较重要的模块。

## MySQL数据库的两阶段提交过程

在进行INSERT,UPDATE,DELETE操作时都需要提交。

用一条更新命令来加以说明，更新语句如下：

```sql
mysql>update T set c=c+1 whereid=2;
```

假设未更新前 id=2 的这行数据 c 的值为 0，这条更新语句在 MySQL 数据库内部执行的流程图：

![MySQL笔记6-1](MySQL笔记6-1.png)

流程图中可以看出，在 InnoDB 存储引擎下，一条 update 语句在 MySQL 内部执行大概会经历下面五个步骤：

* 执行器先找引擎取 id=2 这一行数据，如果 ID=2 这一行所在的数据页本来就在内存中，就直接返回给执行器；否则，需要先从磁盘读入内存，然后再返回。
* 执行器拿到引擎给的行数据，把这个值加上 1，比如原来是 N，现在就是 N+1，得到新的一行数据，再调用引擎接口写入这行新数据。
* 引擎将这行新数据更新到内存中，同时将这个更新操作记录到 redo log 里面，此时 redo log 处于 prepare 状态。然后告知执行器执行完成了，随时可以提交事务。
* 执行器生成这个操作的 binlog，并把 binlog 写入磁盘。
* 执行器调用引擎的提交事务接口，引擎把刚刚写入的 redo log 改成提交（commit）状态，更新完成。

## 为何将redo日志拆分成两步提交？

保证binlog与redolog的数据一致性。

如果没有两阶段提交：

* 先写redolog，再写binlog：
  redolog写完，还没来得及写binlog，MySQL宕机。重启以后，redolog里有记录，MySQL判断事务提交成功，但binlog里没有记录，binlog与redolog出现数据不一致。由于binlog是追加写入日志，往后的时间里binlog会一直缺失这条数据。如果在以后使用binlog恢复这个时间点的数据，会出现数据丢失的情况。

* 先写binlog，再写redolog：
  binlog写完，还没来得及写redolog，MySQL宕机。重启以后，redolog中没有记录，MySQL判断事务提交失败，但是binlog中有记录，binlog与redolog出现数据不一致。如果以后使用binlog恢复数据，就多出了一个事务操作。

从这两个假设中，我们可以看出无论先提交那个日志文件都有可能出现数据不一致的现象