# LinuxTips60--chrony同步失败

### 检查客户端和服务端的chrony包版本是否一致

```bash
rpm -qa chrony
```

### 关闭selinux和firewalld

```bash
systemctl stop selinux
systemctl disable selinux
systemctl stop firewalld
systemctl disable firewalld
```

### 客户端和服务端重启chronyd

```bash
systemctl restart chronyd
```

