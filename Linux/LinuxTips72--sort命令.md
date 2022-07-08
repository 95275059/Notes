# LinuxTips72--sort命令

## 功能

Linux sort 命令用于将文本文件内容加以排序。

sort 可针对文本文件的内容，以行为单位来排序。

## 语法

```shell
sort [-bcdfimMnr][-o<输出文件>][-t<分隔字符>][+<起始栏位>-<结束栏位>][--help][--verison][文件][-k field1[,field2]]
```

- -b 忽略每行前面开始出的空格字符。
- -c 检查文件是否已经按照顺序排序。
- -d 排序时，处理英文字母、数字及空格字符外，忽略其他的字符。
- -f 排序时，将小写字母视为大写字母。
- -i 排序时，除了040至176之间的ASCII字符外，忽略其他的字符。
- -m 将几个排序好的文件进行合并。
- -M 将前面3个字母依照月份的缩写进行排序。
- -n 依照数值的大小排序。
- -u 意味着是唯一的(unique)，输出的结果是去完重了的。
- -o<输出文件> 将排序后的结果存入指定的文件。
- -r 以相反的顺序来排序。
- -t<分隔字符> 指定排序时所用的栏位分隔字符。
- +<起始栏位>-<结束栏位> 以指定的栏位来排序，范围由起始栏位到结束栏位的前一栏位。
- --help 显示帮助。
- --version 显示版本信息。
- **[-k field1[,field2]] 按指定的列进行排序。**

## 示例

### 实例1：按文件大小排序

```shell
[root@controller CMD_SGIN_EP]# du | sort -nr
6216	.
6044	./log
108	./common
52	./openstack_controller
20	./common/shell
8	./common/shell/__pycache__
```

### 实例2：查看磁盘占用情况并降序排序

```shell
[root@controller CMD_SGIN_EP]# df | sort -nr -k 3
/dev/mapper/centos-root 2305798116 1381397688 924400428  60% /
/dev/sda2                  2086912     134260   1952652   7% /boot
tmpfs                     32845932     107640  32738292   1% /run
tmpfs                      6569188          0   6569188   0% /run/user/0
tmpfs                     32845932          0  32845932   0% /sys/fs/cgroup
tmpfs                     32845932          0  32845932   0% /dev/shm
Filesystem               1K-blocks       Used Available Use% Mounted on
devtmpfs                  32835484          0  32835484   0% /dev
```



