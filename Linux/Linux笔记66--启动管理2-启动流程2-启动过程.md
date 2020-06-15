# Linux笔记66--启动管理2-启动流程2-启动过程

1. initramfs内存文件系统

   在/boot/目录下，通过启动引导程序，initramfs被加载到内核中，然后加载启动过程中所需要的内核模块（如，USB,SATA,SCSI硬盘的驱动和LVM,RAID文件系统的驱动）

2. 查看initramfs内容

   centos7 内核默认的initramfs与原生linux不一致，包含一个cpio格式的early_cpio头和一个gzip压缩的cpio格式的initramfs rootfs。前面的early_cpio头是centos7内核独有的

   + cd /boot

   +  file initramfs-3.10.0-862.el7.x86_64.img

     输出：initramfs-3.10.0-862.el7.x86_64.img: ASCII cpio archive (SVR4 with no CRC)

     注：查看file类型
   
   + cd /home/cxy/initramfs/
   
   + cp /boot/initramfs-3.10.0-862.el7.x86_64.img /home/cxy/initramfs
   
   + mkdir early_cpio
   
   + mkdir rootfs_cpio
   
   + cd early_cpio
   
   + cpio -idm < /home/cxy/initramfs/initramfs-3.10.0-862.el7.x86_64.img
   
     #解包early_cpio
   
   + cd /home/cxy/rootfs_cpio
   + /usr/lib/dracut/skipcpio /home/cxy/initramfs/initramfs-3.10.0-862.el7.x86_64.img | zcat | cpio -id

3. 打包initramfs rootfs
   + cd /home/cxy/initramfs/early_cpio
   + find . -print0 | cpio --null -o -H newc --quiet > ../early_cpio.img
   + cd /home/cxy/initramfs/rootfs_cpio
   + find . | cpio -o -H newc | gzip > ../rootfs_cpio.img
   + cd /home/cxy/initramfs
   + cat early_cpio.img rootfs_cpio.img > newInitramfs.img

4. 启动流程

   ![笔记66-1](E:\notes\Linux\笔记66-1.jpg)

   + /sbin/init是根进程

   + /etc/init/rcS.conf配置文件

     主要功能

     + 先调用/etc/rc.d/rc.sysinit，由/etc/rc.d/rc.sysinit配置文件进行Linux系统初始化
     + 然后调用/etc/inittab，由/etc/inittab配置文件确定系统的默认运行级别

   + /etc/rc.d/rc[0-6].d/文件

     + /etc/rc3.d/k??开头的文件(??是数字)，关机时会按照数字顺序依次关闭
     + /etc/rc3.d/S??开头的文件(??是数字)，开机时会按照数字顺序依次启动

     

   