# Linux笔记70--备份与恢复3-备份命令3-restore/xfsrestore

1. restore命令

   restore [模式选项] [选项]

   + 模式选项

     | 模式选项 | 说明                                     |
     | -------- | ---------------------------------------- |
     | -C       | 比较备份数据和实际数据的变化             |
     | -i       | 进入交互模式，手工选择要恢复的文件       |
     | -t       | 查看模式，用于查看备份文件中拥有哪些数据 |
     | -r       | 还原模式，用于数据还原                   |

   + 选项

     | 选项 | 说明                 |
     | ---- | -------------------- |
     | -f   | 指定备份文件的文件名 |

2. xfsrestore命令

   restore [选项] 恢复目录

   + 选项

     | 选项           | 说明                                                         |
     | -------------- | ------------------------------------------------------------ |
     | -I（大写i）    | 查询备份数据的信息                                           |
     | -f <备份文件>  | 指定要还原的备份文件                                         |
     | -L             | 可以通过-L标签值进行还原，或还原更加精确。这一项也可以不用加 |
     | -s <文件/目录> | 还原时只还原指定目录/文件，不是全部还原                      |
     |                | 进入交互模式，高级管理员使用，一般用不到                     |

   + 常见格式
     + xfsrestore -I
     + xfsrestore [-f 备份文件名] [-L S_label] [-s 目录/文件] 恢复目录
     + xfsrestore [-f 备份文件名] -r 恢复目录   (-r加不加都可以)

   + 注意
     + 文件系统还原后，只有同名文件会被覆盖，而原本备份之后由系统产生的新文件则保留

3. restore使用实例（未实验过）

   + 比较备份数据和实际数据的变化

     + mv /boot/vmlinuz-3.10.0-862.el7.x86_64 /boot/vmlinuz-3.10.0-862.el7.x86_64.bak

       #把/boot目录中内核镜像文件改个名字

       **#注：操作完一定要记得改回去，这是内核文件，否则下次重启找不到内核会没办法开机**

     + restore -C -f /root/boot.bak.bz2

       #restore发现内核镜像文件丢失

   + 查看模式
     + restore -t -f /root/boot.bak.bz2

   + 还原模式

     + 还原boot.bak.bz2分区备份

       + mkdir /home/cxy/boot_test

       + cd /home/cxy/boot_test

       + restore -r -f /root/boot.bak.bz2

         #先还原完全备份的数据

       + restore -r -f /root/boot.bak1.bz2

         #恢复增量备份数据

     + 还原/etc/目录的备份etc.dump.bz2

       + restore -r -f etc.dump.bz2

         #还原etc.dump.bz2备份

3. xfsrestore使用实例

   + 还原/boot目录到/home/cxy/xfsrestore_test/boot_xfsrestore_test/下

     + 先还原完全备份/home/cxy/xfsdump/boot_bak.dump

       xfsrestore -f /home/cxy/xfsdump_test/boot_bak.dump -r /home/cxy/xfsrestore_test/boot_xfsrestore_test/

     + 然后还原增量备份/home/cxy/xfsdump/boot_bak1.dump

       xfsrestore -f /home/cxy/xfsdump_test/boot_bak1.dump -r /home/cxy/xfsrestore_test/boot_xfsrestore_test/

   + 还原/etc目录到/home/cxy/xfsrestore_test/etc_xfsrestore_test/下

     xfsrestore -f /home/cxy/xfsdump_test/etc_bak.dump -r /home/cxy/xfsrestore_test/etc_xfsrestore_test/

   + 只还原/boot目录下的grub2目录到/home/cxy/xfsrestore_test/boot_grub2_xfsrestore_test/下

     xfsrestore -f /home/cxy/xfsdump_test/boot_bak.dump -s grub2 /home/cxy/xfsrestore_test/boot_grub2_xfsrestore_test/

