# LinuxTips69--df命令

## 功能

Linux df（disk free）命令用于显示目前在Linux系统上的文件系统磁盘使用情况统计

## 语法

```
df [选项]... [FILE]...
```

* -a, --all : 包含所有的具有0 Blocks的文件系统
* -h : 以方便阅读的方式显示，计算方式1K=1024
* -H : 等于-h，但计算方式1K=1000
* -i : 显示inode信息
* -k : 区块为1024字节，以单位显示磁盘的使用情况
* -l : 只显示本地文件系统
* -T : 显示文件系统类型
* -t <文件系统类型> : 只显示指定文件系统类型的磁盘信息
* -x <文件系统类型> : 不显示选定文件系统的磁盘信息

## 示例

### 实例1：显示磁盘使用情况

```shell
[root@controller CMD_SGIN_EP]# df
Filesystem               1K-blocks       Used Available Use% Mounted on
/dev/mapper/centos-root 2305798116 1381400304 924397812  60% /
devtmpfs                  32835484          0  32835484   0% /dev
tmpfs                     32845932          0  32845932   0% /dev/shm
tmpfs                     32845932     107768  32738164   1% /run
tmpfs                     32845932          0  32845932   0% /sys/fs/cgroup
/dev/sda2                  2086912     134260   1952652   7% /boot
tmpfs                      6569188          0   6569188   0% /run/user/0
```

* 第1列是代表文件系统对应的设备文件的路径名（一般是硬盘上的分区）；

* 第2列给出分区包含的数据块（1024字节）的数目；

* 第3，4列分别表示已用的和可用的数据块数目。

* 用户也许会感到奇怪的是，第3，4列块数之和不等于第2列中的块数。
  这是因为缺省的每个分区都留了少量空间供系统管理员使用。

  即使遇到普通用户空间已满的情况，管理员仍能登录和留有解决问题所需的工作空间。

* Use% 列表示普通用户空间使用的百分比，即使这一数字达到100％，分区仍然留有系统管理员使用的空间。

* Mounted on列表示文件系统的挂载点。

### 实例2：以inode模式来显示磁盘使用情况

```shell
[root@controller CMD_SGIN_EP]# df -i
Filesystem                 Inodes  IUsed     IFree IUse% Mounted on
/dev/mapper/centos-root 461384896 232823 461152073    1% /
devtmpfs                  8208871    532   8208339    1% /dev
tmpfs                     8211483      1   8211482    1% /dev/shm
tmpfs                     8211483    766   8210717    1% /run
tmpfs                     8211483     13   8211470    1% /sys/fs/cgroup
/dev/sda2                 2097152    330   2096822    1% /boot
tmpfs                     8211483      1   8211482    1% /run/user/0
```

### 实例3：列出文件系统的类型

```shell
[root@controller CMD_SGIN_EP]# df -T
Filesystem              Type      1K-blocks       Used Available Use% Mounted on
/dev/mapper/centos-root xfs      2305798116 1381396640 924401476  60% /
devtmpfs                devtmpfs   32835484          0  32835484   0% /dev
tmpfs                   tmpfs      32845932          0  32845932   0% /dev/shm
tmpfs                   tmpfs      32845932     107832  32738100   1% /run
tmpfs                   tmpfs      32845932          0  32845932   0% /sys/fs/cgroup
/dev/sda2               xfs         2086912     134260   1952652   7% /boot
tmpfs                   tmpfs       6569188          0   6569188   0% /run/user/0
```



