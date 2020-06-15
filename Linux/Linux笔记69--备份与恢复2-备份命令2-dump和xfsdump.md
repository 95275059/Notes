# Linux笔记69--备份与恢复2-备份命令dump/xfsdump

1. dump命令

   格式：dump [选项] 备份后的文件名 原文件或目录

   | 选项      | 说明                                                      |
   | --------- | --------------------------------------------------------- |
   | -level    | 0-9十个备份级别                                           |
   | -f 文件名 | 指定备份后的文件名                                        |
   | -u        | 备份成功后，把备份时间记录在/etc/dumpdates文件            |
   | -v        | 显示备份过程中更多的输出信息                              |
   | -j        | 调用bzlib库压缩备份文件，其实就是把备份文件压缩为.bz2格式 |
   | -W        | 显示允许被dump的分区的备份等级及备份时间                  |

   + 备份级别
     + 0   =>   完全备份
     + 1   =>   第一次增量备份
     + 2   =>   第二次增量备份
     + ....

2. xfsdump命令

   若使用dump命令时如果出现以下错误：**Bad magic number in super-block while opening filesystem**

   则应使用xfsdump进行备份，使用xfsrestore进行还原

   注：df -Th能够查看分区类型，根据这个命令查看分区的类型为xfs时，使用xfsdump和xfsrestore

   + xfsdump -f 备份后的文件名 原文件或目录

   + 选项

     | 选项               | 说明                                                         |
     | ------------------ | ------------------------------------------------------------ |
     | -l level           | 指定备份级别                                                 |
     | -L <session label> | 指定会话标签。填写针对此次文件系统备份的简易说明             |
     | -M <media label>   | 指定设备标签。填写此次文件系统备份的设备的简易说明           |
     | -s 文件路径        | 只对指定的文件或目录进行备份，-s指定时，路径写**相对路径**   |
     | -I                 | 列出/var/libxfsdump/inventory目录下目前备份的信息状态（大写的i） |

   + 注意事项

     + xfsdump只能备份xfs文件系统

     + xfsdump必须使用root的权限才可以操作

     + xfsdump备份备份下来的数据（文件/存储媒介）只能让xfsrestore解析。备份的文件名后缀为.dump

     + xfsdump 不支持没有挂载的文件系统备份，所以只能备份已挂载的文件系统

     + xfsdump是通过文件系统的UUID来辨别各备份文件，因此不能备份两个具有相同UUID的文件系统

     + xfsdump默认仅支持文件系统的备份,并不支持特定目录的备份

       即：/dev/sda1分区是xfs文件系统类型，挂载/boot目录，因此能够使用xfsdump对/boot进行备份

       ​        而/etc仅仅是一个目录，不是一个独立的文件系统，因此不能够使用xfsdump对/etc进行备份

       ​		但是通s选项可以只备份分区中某个目录，因此可以通过该选项从而备份/etc

3. dump备份分区：以备份boot分区为例(看个格式就行，boot是xfs文件类型)

   + dump -0uj -f /root/boot.bak.bz2 /boot/

     #先执行一次完全备份，并压缩和更新备份时间

   + cat /etc/dumpdates

     #查看备份时间文件

   + cp /home/cxy/orld /boot/

     #复制一个新文件到/boot分区

   + dump -1uj -f /root/boot.bak1.bz2 /boot/

     #增量备份/boot分区，并压缩

   + dump -W

     #查询分区的备份时间及备份级别

4. xfsdump备份分区/boot

   + cd /home/cxy/xfsdump_test/

   + 完全备份/boot

     + 会话模式

       xfsdump -f /home/cxy/xfsdump_test/boot_bak.dump /boot 

       回车后根据提示输入level和label

       ==注：写/boot/会出错，必须写/boot==

     + xfsdump -l 0 -L boot_bak -M sda1 -f /home/cxy/xfsdump_test/boot_bak.dump /boot

   + cp /home/cxy/orld /boot/orld

   + 增量备份

     xfsdump -l 1 -L boot_bak1 -M sda1 -f /home/cxy/xfsdump_test/boot_bak1.dump /boot

5. dump备份文件或目录

   以备份目录/etc为例(看个格式就行，备份/etc还是需要xfsdump)

   + dump -0j -f /root/etc.dump.bz2 /etc/

     #完全备份/etc/目录，只能使用0级别进行完全备份，而不再支持增量备份

6. xfsdump备份文件或目录

   xfsdump备份文件或目录时，需要知道该文件或目录所处的分区

   查找文件或目录所处分区：df -h 目录名

   例：备份/etc

   + cd /etc          #由于xfsdump -s必须使用相对路径，所以要先进入到/etc目录下
   + xfsdump -l 0 -L etc_bak -M /dev/mapper/centos-root -f /root/etc.dump.bz2 -s etc /dev/mapper/centos-root

   

