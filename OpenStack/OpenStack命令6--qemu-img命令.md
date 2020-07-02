# OpenStack命令6--qemu-img命令

1. 安装

   + Ubuntu

     ```bash
     $ apt-get install qemu-utils
     ```

   + CentOS

     ```bash
     $ yum install qemu-img
     ```

2. 转换镜像格式

   ```bash
   $ qemu-img convert -f qcow2 -O raw centos.qcow2 centos.raw
   ```

   + -f 的参数值为源镜像文件的格式
   + -O 的参数值为目标镜像格式、源镜像文件名和目标文件名
   + 转换完成后，目标文件会出现在源镜像文件所在目录

3. 创建镜像文件

   ```bash
   $ qemu-img create [-f fmt] [-o options] filename [size]
   ```

   + 创建一个格式为*fmt*大小为*size*文件名为*filename*的镜像文件。
   + 根据文件格式*fmt*的不同，还可以添加一个或多个选项（*options*）来附加对该文件的各种功能设置，可以使用“-o ?”来查询某种格式文件支持那些选项，在“-o”选项中各个选项用逗号来分隔。
   + 如果“-o”选项中使用了backing_file这个选项来指定其**后端镜像**文件，那么这个创建的镜像文件仅记录与后端镜像文件的差异部分。后端镜像文件不会被修改，除非在QEMU monitor中使用“commit”命令或者使用“qemu-img commit”命令去手动提交这些改动。这种情况下，size参数不是必须需的，其值默认为后端镜像文件的大小。另外，直接使用“-b *backfile*”参数也与“-o backing_file=*backfile*”效果相同。

   ```bash
   $ qemu-img create -f qcow2 -o backing_file=/var/lib/nova/instances/_base/*image_id*/
   ```

4. 查看镜像文件属性

   ```bash
   $ qemu-img info [-f fmt] filename
   ```

   + 如果文件是使用稀疏文件的存储方式，也会显示出它的本来分配的大小以及实际已占用的磁盘空间大小。
   + 如果文件中存放有客户机快照，快照的信息也会被显示出来。

   ```bash
   $ qemu-img info /var/lib/nova/instances/*image_file_id*/disk
   ```

   ```bash
   [root@compute1 instances]# qemu-img info /var/lib/nova/instances/013e0029-af6f-49c8-844e-175960b05395/disk
   image: /var/lib/nova/instances/013e0029-af6f-49c8-844e-175960b05395/disk
   file format: qcow2
   virtual size: 10G (10737418240 bytes)
   disk size: 130M
   cluster_size: 65536
   backing file: /var/lib/nova/instances/_base/ede66a66d3148b6edecb1139e03a43149b7a0996
   Format specific information:
       compat: 1.1
       lazy refcounts: false
   ```

   