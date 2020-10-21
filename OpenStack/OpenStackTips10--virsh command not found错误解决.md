# OpenStackTips10--virsh command not found错误解决

### 环境

Vmware下用CentOS7搭建完OpenStack后，无法使用virsh命令

```bash
[root@compute ~]# virsh list
-bash: virsh: command not found
```

已保证虚拟机支持虚拟化嵌套

### 原因

+ 检查libvirt是否安装

  ```bash
  rpm -q libvirt
  ```

+ 安装libvirt

  ```bash
  yum install -y libvirt
  ```

+ 查看libvirt服务状态，确保该服务已打开

  ```bash
  systemctl status libvirtd
  ```





