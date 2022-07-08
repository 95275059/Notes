# LinuxTips71--du命令

## 功能

Linux du （英文全拼：disk usage）命令用于显示目录或文件的大小。

du 会显示指定的目录或文件所占用的磁盘空间。

## 语法

```shell
du [-abcDhHklmsSx][-L <符号连接>][-X <文件>][--block-size][--exclude=<目录或文件>][--max-depth=<目录层数>][--help][--version][目录或文件]
```

* -a, -all : 显示目录下所有文件大小，包括子目录中的文件
* -h, --human-readable : 以K,M,G为单位，提高信息的可读性
* -H或--si : 与-h参数相同，但是K,M,G以1000为换算单位
* -s, --summarize : 仅显示总计 
* --max-depth=<目录层数> 超过指定层数的目录后，予以忽略
* --exclude=<目录或文件> : 略过指定的目录或文件

## 示例

### 实例1：显示目录下各个文件目录大小

```shell
[root@controller CMD_SGIN_EP]# du 
8	./common/shell/__pycache__
20	./common/shell
108	./common
6044	./log
52	./openstack_controller
6216	.
[root@controller CMD_SGIN_EP]# du -h
8.0K	./common/shell/__pycache__
20K	./common/shell
108K	./common
6.0M	./log
52K	./openstack_controller
6.1M	.
```

### 实例2：以文件大小降序排序

```shell
[root@controller CMD_SGIN_EP]# du | sort -nr
6216	.
6044	./log
108	./common
52	./openstack_controller
20	./common/shell
8	./common/shell/__pycache__
```
