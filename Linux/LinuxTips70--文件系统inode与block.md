# LinuxTips70--文件系统inode与block

## block

* 文件存储在硬盘上

* 硬盘的**最小存储单位**叫**扇区Sector**，每个扇区存储512字节
* 操作系统读取硬盘的时候，不会一个一个扇区地读取，这样效率太低，而是一次性连续读取多个扇区，即一次性读取一个**块block**
* 块由多个扇区组成，是**文件存取的最小单位**，块大小常见为4KB，即连续8个扇区组成一个block

* 文件数据存储在块中，文件元信息（文件创建者，创建日期，文件 大小等）存储在**inode索引节点中，也叫作i节点**。
* 一个文件必须占用一个inode，至少占用一个block

## inode

### inode内容

* inode中包含文件元信息，包含：字节数，属主UserID，数组GroupID，读写执行权限，时间戳等。但不包含文件名
* 文件名存放在目录中
* Linux系统内部不适用文件名，而是使用inode号码识别文件

#### 查看inode信息

```shell
[root@controller CMD_SGIN_EP]# stat SGIEN.conf 
  File: ‘SGIEN.conf’
  Size: 1772      	Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d	Inode: 1033865     Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2021-09-16 14:25:38.870693997 +0800
Modify: 2021-04-29 17:29:28.000000000 +0800
Change: 2021-04-30 12:24:15.654955029 +0800
 Birth: -
```

* 三个主要的时间属性

  * ctime : change time 是最后一次改变文件或目录（属性）的时间

    如执行chmod，chown命令

  * atime : access time 是最后一次访问文件或目录的时间
  * mtime : modify time 是最后一次修改文件或目录（内容）的时间

#### 查看文件类型

```shell
[root@controller CMD_SGIN_EP]# file SGIEN.conf 
SGIEN.conf: C source, ASCII text, with CRLF line terminators
[root@controller CMD_SGIN_EP]# file common
common: directory
```

#### inode号码

* 用户通过文件名打开文件的过程，系统内部分为三步实现：
  * 系统找到文件名对应的inode号码
  * 通过inode号码，获取inode信息
  * 根据inode信息，查看和用户是否有访问权限，有继续下一步，没有的话就返回权限拒绝
  * 根据inode信息，找到文件数据所在block，并读出数据

#### 查看inode号码

* ls -i

  ```shell
  [root@controller CMD_SGIN_EP]# ls -i SGIEN.conf 
  1033865 SGIEN.conf
  ```

* stat

  ```shell
  [root@controller CMD_SGIN_EP]# stat SGIEN.conf 
    File: ‘SGIEN.conf’
    Size: 1772      	Blocks: 8          IO Block: 4096   regular file
  Device: fd00h/64768d	Inode: 1033865     Links: 1
  Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
  Access: 2021-09-16 14:25:38.870693997 +0800
  Modify: 2021-04-29 17:29:28.000000000 +0800
  Change: 2021-04-30 12:24:15.654955029 +0800
   Birth: -
  ```

#### inode大小

* inode同样会消耗硬盘空间，因此格式化的时候，操作系统自动将硬盘分成两个区域。
* 一个是数据区，存放文件数据。
* 另一个是inode区，存放inode所包含的信息
* 每个inode大小一般是128字节或者256字节。
* 通常情况下不需要关注单个inode大小，而是需要重点关注inode总数。
* inode总数在格式化的时候就确定了

#### 查看inode总数和已使用情况

```shell
[root@controller CMD_SGIN_EP]# df -i
Filesystem                 Inodes  IUsed     IFree IUse% Mounted on
/dev/mapper/centos-root 461384896 232823 461152073    1% /
devtmpfs                  8208871    532   8208339    1% /dev
tmpfs                     8211483      1   8211482    1% /dev/shm
tmpfs                     8211483    726   8210757    1% /run
tmpfs                     8211483     13   8211470    1% /sys/fs/cgroup
/dev/sda2                 2097152    330   2096822    1% /boot
tmpfs                     8211483      1   8211482    1% /run/user/0c
```

### 特殊现象

由于`inode`号码与文件名分离，导致一些`Unix/Linux`系统具备以下几种特有的现象。

* 文件名包含特殊字符，可能无法正常删除。这时直接删除`inode`，能够起到删除文件的作用；

  ```
  find ./* -inum 节点号 -delete
  ```

* 移动文件或重命名文件，只是改变文件名，不影响`inode`号码；

* 打开一个文件以后，系统就以`inode`号码来识别这个文件，不再考虑文件名。

  这种情况使得软件更新变得简单，可以在不关闭软件的情况下进行更新，不需要重启。

  因为系统通过`inode`号码，识别运行中的文件，不通过文件名。

  更新的时候，新版文件以同样的文件名，生成一个新的`inode`，不会影响到运行中的文件。

  等到下一次运行这个软件的时候，文件名就自动指向新版文件，旧版文件的`inode`则被回收。

### inode耗尽故障

* 由于硬盘分区的`inode`总数在格式化后就已经固定，而每个文件必须有一个`inode`，因此就有可能发生`inode`节点用光，但硬盘空间还剩不少，却无法创建新文件。
* 同时这也是一种攻击的方式，所以一些公用的文件系统就要做磁盘限额，以防止影响到系统的正常运行。
* 至于修复，很简单，只要找出哪些大量占用`i节点`的文件删除就可以了。

## 软连接与硬链接

### 硬链接

* 通过文件系统的`inode`链接来产生的新的文件名，而不是产生新的文件，称为硬链接。

* 一般情况下，每个`inode`号码对应一个文件名，但是`Linux`允许多个文件名指向同一个`inode`号码。意味着可以使用不同的文件名访问相同的内容。

* ```shell
  ln 源文件 目标
  ```

  运行该命令以后，源文件与目标文件的`inode`号码相同，都指向同一个`inode`。

  `inode`信息中的链接数这时就会增加`1`。

* 当一个文件拥有多个硬链接时，对文件内容修改，会影响到所有文件名；

* 但是删除一个文件名，不影响另一个文件名的访问。

  删除一个文件名，只会使得`inode`中的链接数减`1`。

* 需要注意的是不能对目录做硬链接。
* 通过`mkdir`命令创建一个新目录，其硬链接数应该有`2`个，因为常见的目录本身为`1`个硬链接，而目录下面的隐藏目录`.（点号）`是该目录的又一个硬链接，也算是`1`个连接数。

### 软链接

* 类似于Windows的快捷方式功能的文件，可以快速连接到目标文件或目录，称为软链接。

* ```shell
  ln -s 源文件或目录 目标文件或目录
  ```

* 软链接就是再创建一个独立的文件，而这个文件会让数据的读取指向它连接的那个文件的文件名。

  例如，文件`A`和文件`B`的`inode`号码虽然不一样，但是文件`A`的内容是文件`B`的路径。

  读取文件`A`时，系统会自动将访问者导向文件`B`。

  这时，文件`A`就称为文件`B`的软链接`soft link`或者符号链接`symbolic link`。

  这意味着，文件`A`依赖于文件`B`而存在，如果删除了文件`B`，打开文件`A`就会报错。

* 这是软链接与硬链接最大的不同：文件`A`指向文件`B`的文件名，而不是文件`B`的`inode`号码，文件`B`的`inode`链接数不会因此发生变化。

* 