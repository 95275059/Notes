# LinuxTips53--查看文件大小

### stat命令

+ 功能

  用于显示incode内容

  stat以文字的格式来显示inode的内容

+ 语法

  ```bash
  stat [文件或目录]
  ```

+ 实例

  ```bash
  root@controller:/home/cxy_tdyt/images# stat tdyth.qcow2 
    File: 'tdyth.qcow2'
    Size: 1380843520	Blocks: 2696968    IO Block: 4096   regular file
  Device: 801h/2049d	Inode: 4722812     Links: 1
  Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
  Access: 2020-10-10 19:20:50.287088987 +0800
  Modify: 2020-10-10 19:20:00.134603392 +0800
  Change: 2020-10-10 19:20:00.134603392 +0800
   Birth: -
  ```

---

### wc命令

+ 功能

  用于计算字数

  利用wc命令可以计算文件的Byte数、字数、或是列数

  若不指定文件名称、或是所给予的文件名为"-"，则wc指令会从标准输入设备读取数据

+ 语法

  ```bash
  wc [-clw][--help][--version][文件...]
  ```

  | 选项                     | 说明          |
  | ------------------------ | ------------- |
  | -c 或 --bytes 或 --chars | 只显示Bytes数 |
  | -l 或 --lines            | 只显示行数    |
  | -w 或 --words            | 只显示字数    |
  | --help                   | 在线帮助      |
  | --version                | 显示版本信息  |

+ 实例

  + 实例1

    ```bash
    root@controller:/home/cxy_tdyt/images# wc tdyth.qcow2 
      11204055   48832226 1380843520 tdyth.qcow2
    ```

    3 个数字分别表示testfile文件的行数、单词数，以及该文件的字节数

  + 实例2:同时统计多个文件的信息

    ```bash
    root@controller:/home/cxy_tdyt/images# wc cxy.qcow2 cxy1.img 
       1653344    9414191  459669504 cxy.qcow2
      11279857   48319145 1221066752 cxy1.img
      12933201   57733336 1680736256 total
    ```

---

### du命令

+ 功能

  du （英文全拼：disk usage）命令用于显示目录或文件的大小

  du 会显示指定的目录或文件所占用的磁盘空间

+ 语法

  ```bash
  du [-abcDhHklmsSx][-L <符号连接>][-X <文件>][--block-size][--exclude=<目录或文件>][--max-depth=<目录层数>][--help][--version][目录或文件]
  ```

  | 选项                                    | 说明                                                         |
  | --------------------------------------- | ------------------------------------------------------------ |
  | -a 或 -all                              | 显示目录中所有文件的大小                                     |
  | -b 或 -bytes                            | 显示目录或文件大小时，以byte为单位                           |
  | -c 或 --total                           | 除了显示所有目录或文件的大小外，同时也显示所有目录或文件的总和 |
  | -D 或 --dereference-args                | 显示指定符号连接的源文件大小                                 |
  | **-h 或 --human-readable**              | 以K，M，G为单位，提高信息的可读性                            |
  | -H 或 --si                              | 与-h参数相同；但是K，M，G是以1000为换算单位                  |
  | **-k 或 --kilobytes**                   | 以1024 bytes为单位                                           |
  | -l 或 --count-links                     | 重复计算硬件连接的文件                                       |
  | -L<符号连接> 或 --dereference<符号连接> | 显示选项中所指定符号连接的源文件大小                         |
  | **-m 或 --megabytes **                  | 以1MB为单位                                                  |
  | **-s 或 --summarize**                   | 仅显示总计                                                   |
  | -S 或 --separate-dirs                   | 显示个别目录的大小时，并不含其子目录的大小                   |
  | -x 或 --one-file-xystem                 | 以一开始处理时的文件系统为准，若遇上其它不同的文件系统目录则略过 |
  | -X<文件> 或 --exclude-from=<文件>       | 在<文件>指定目录或文件                                       |
  | --exclude=<目录或文件>                  | 略过指定的目录或文件                                         |
  | --max-depth=<目录层数>                  | 超过指定层数的目录后，予以忽略                               |
  | --help                                  | 显示帮助                                                     |
  | --version                               | 显示版本信息                                                 |

+ 实例

  + 实例1

    ```bash
    root@controller:/home/cxy_tdyt# du
    16	./SGIN-Stack/Figure10
    32	./SGIN-Stack
    160	./cy/openstack
    16	./cy/study
    16	./cy/log
    16	./cy/config_file
    640	./cy/topology
    1020	./cy
    192	./tdyth_test
    3776308	./images
    572	./tdyt_openstack/scene_file
    4	./tdyt_openstack/.svn/tmp
    20	./tdyt_openstack/.svn/pristine/c7
    12	./tdyt_openstack/.svn/pristine/05
    12	./tdyt_openstack/.svn/pristine/52
    24	./tdyt_openstack/.svn/pristine/8d
    8	./tdyt_openstack/.svn/pristine/5d
    20	./tdyt_openstack/.svn/pristine/88
    8	./tdyt_openstack/.svn/pristine/bc
    12	./tdyt_openstack/.svn/pristine/73
    8	./tdyt_openstack/.svn/pristine/75
    8	./tdyt_openstack/.svn/pristine/74
    16	./tdyt_openstack/.svn/pristine/ef
    40	./tdyt_openstack/.svn/pristine/97
    8	./tdyt_openstack/.svn/pristine/79
    8	./tdyt_openstack/.svn/pristine/f6
    12	./tdyt_openstack/.svn/pristine/c0
    28	./tdyt_openstack/.svn/pristine/ab
    96	./tdyt_openstack/.svn/pristine/04
    8	./tdyt_openstack/.svn/pristine/15
    120	./tdyt_openstack/.svn/pristine/98
    120	./tdyt_openstack/.svn/pristine/91
    96	./tdyt_openstack/.svn/pristine/13
    8	./tdyt_openstack/.svn/pristine/16
    20	./tdyt_openstack/.svn/pristine/7e
    28	./tdyt_openstack/.svn/pristine/5f
    48	./tdyt_openstack/.svn/pristine/bd
    28	./tdyt_openstack/.svn/pristine/be
    12	./tdyt_openstack/.svn/pristine/64
    8	./tdyt_openstack/.svn/pristine/fc
    136	./tdyt_openstack/.svn/pristine/e4
    56	./tdyt_openstack/.svn/pristine/a0
    68	./tdyt_openstack/.svn/pristine/f2
    24	./tdyt_openstack/.svn/pristine/55
    12	./tdyt_openstack/.svn/pristine/b7
    20	./tdyt_openstack/.svn/pristine/70
    84	./tdyt_openstack/.svn/pristine/0d
    8	./tdyt_openstack/.svn/pristine/0f
    8	./tdyt_openstack/.svn/pristine/80
    8	./tdyt_openstack/.svn/pristine/a1
    8	./tdyt_openstack/.svn/pristine/2b
    88	./tdyt_openstack/.svn/pristine/61
    8	./tdyt_openstack/.svn/pristine/92
    4	./tdyt_openstack/.svn/pristine/da
    20	./tdyt_openstack/.svn/pristine/b1
    8	./tdyt_openstack/.svn/pristine/e6
    12	./tdyt_openstack/.svn/pristine/e5
    20	./tdyt_openstack/.svn/pristine/bf
    12	./tdyt_openstack/.svn/pristine/5e
    20	./tdyt_openstack/.svn/pristine/66
    20	./tdyt_openstack/.svn/pristine/0b
    36	./tdyt_openstack/.svn/pristine/cd
    12	./tdyt_openstack/.svn/pristine/e3
    8	./tdyt_openstack/.svn/pristine/32
    8	./tdyt_openstack/.svn/pristine/af
    8	./tdyt_openstack/.svn/pristine/e1
    20	./tdyt_openstack/.svn/pristine/6c
    8	./tdyt_openstack/.svn/pristine/18
    20	./tdyt_openstack/.svn/pristine/c3
    8	./tdyt_openstack/.svn/pristine/c6
    8	./tdyt_openstack/.svn/pristine/ee
    16	./tdyt_openstack/.svn/pristine/43
    8	./tdyt_openstack/.svn/pristine/68
    36	./tdyt_openstack/.svn/pristine/4b
    1680	./tdyt_openstack/.svn/pristine
    1764	./tdyt_openstack/.svn
    16	./tdyt_openstack/sygkxml
    108	./tdyt_openstack/.idea
    64	./tdyt_openstack/tools
    2708	./tdyt_openstack
    28	./network_node/vm
    56	./network_node
    52	./test
    4104	./tools
    64	./compute_node
    32	./monitor
    40	./bandwidth
    3784792	.
    ```

  + 实例2

    ```bash
    root@controller:/home/cxy_tdyt# du images/
    3776308	images/
    ```

  + 实例3

    ```bash
    root@controller:/home/cxy_tdyt# du -h images/
    3.7G	images/
    ```

---

### ls命令

+ ```bash
  root@controller:/home/cxy_tdyt# ls -l network_node/
  total 28
  -rw-r--r-- 1 root root  798 Jul 11 16:23 monitor_create_xml.py
  -rw-r--r-- 1 root root 4931 Jul 11 16:26 monitor_network_plugin.py
  -rw-r--r-- 1 root root 8035 Jul 23 09:42 monitor_network_plugin_v1.py
  drwxr-xr-x 2 root root 4096 Jul 23 09:58 vm
  -rw-r--r-- 1 root root 3900 Jul 23 10:00 vm_file_transmission.py 
  ```

  第五行为文件或目录字节数

+ ```bash
  root@controller:/home/cxy_tdyt# ls -lh network_node/
  total 28K
  -rw-r--r-- 1 root root  798 Jul 11 16:23 monitor_create_xml.py
  -rw-r--r-- 1 root root 4.9K Jul 11 16:26 monitor_network_plugin.py
  -rw-r--r-- 1 root root 7.9K Jul 23 09:42 monitor_network_plugin_v1.py
  drwxr-xr-x 2 root root 4.0K Jul 23 09:58 vm
  -rw-r--r-- 1 root root 3.9K Jul 23 10:00 vm_file_transmission.py
  ```

  human-readable



