# OpenStack命令3--virsh虚拟机管理命令

更多的使用命令参考：https://www.cnblogs.com/cyleon/p/9816989.html

1. 确认CPU是否支持虚拟化

   ```shell
   # egrep -o '(vmx|svm)' /proc/cpuinfo
   ```

   如果有输出vmx或svm，就说明当前的CPU支持KVM

2. 安装包

   ```shell
   # yum install -y qemu-kvm qemu-system libvirt-bin virt-manager bridge-utils vlan
   ```

3. 查看宿主机上赈灾运行的虚拟机

   ```shell
   # virsh list
   ```

4. 查看虚拟机上所有的虚拟机

   ```shell
   # virsh list --all
   ```

5. 查看当前Linux Bridge 配置

   ```shell
   # brctl show
   ```

5. 启动虚拟机

   ```shell
   # virsh start VM_name
   ```

6. 查看虚拟机网卡配置信息

   ```shell
   # virsh domiflist VM_name
   ```

7. 关闭虚拟机

   ```shell
   # virsh shutdown VM_name
   ```

8. 虚拟机强制断电

   ```shell
   # virsh destroy VM_name
   ```

9. 挂起虚拟机

   ```shell
   # virsh suspend VM_name
   ```

10. 恢复挂起的虚拟机

    ```shell
    # virsh resume VM_name
    ```

11. 删除虚拟机，慎用

    ```shell
    # virsh undefine VM_name
    ```

12. 查看虚拟机配置信息

    ```shell
    # virsh dominfo VM_name
    ```

13. 查看虚拟机磁盘位置

    ```shell
    # virsh domblklist VM_name
    ```

14. 修改虚拟机的xml配置文件

    ```shell
    # virsh edit VM_name
    ```

15. 查看虚拟机当前配置

    ```shell
    # virsh dumpxml VM_name
    ```

16. 备份虚拟机的xml文件，原文件默认路径/etc/libvirt/qemu/VM_name.xml

    ```shell
    # virsh dumpxml VM_name > VM_name.bak.xml 
    ```

17. KVM物理机开机自启动虚拟机VM_name，配置后会在此目录生成配置文件/etc/libvirt/qemu/autostart/VM_name.xml

    ```shell
    # virsh autostart VM_name
    ```

18. 取消开机自启动

    ```shell
    # virsh autostart --disable VM_name
    ```

---

20. 查看实例disk文件属性

    ```bash
    [root@compute16 instances]# qemu-img info /var/lib/nova/instances/00d779d3-da63-45f5-9fa3-f377b44acfb7/disk
    image: /var/lib/nova/instances/00d779d3-da63-45f5-9fa3-f377b44acfb7/disk
    file format: qcow2
    virtual size: 10G (10737418240 bytes)
    disk size: 277M
    cluster_size: 65536
    backing file: /var/lib/nova/instances/_base/8808c0df4eb3a7cf2d5988de180a0a563022aae6
    Format specific information:
        compat: 1.1
        lazy refcounts: false
    ```

21. 查看KVM节点（服务器）信息

    ```bash
    # virsh nodeinfo 
    ```

    