# DockerTips4--WARNING: Your kernel does not support swap limit capabilities or the cgroup

### WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.

### 原因

这是在ubuntu或其他基于Debian的系统上才会出现的问题，原因是系统默认未开启swap限制。

开启后会使系统内存占用多1%,性能下降约10%,即使没有运行docker

### 解决方案

+ 修改系统的/etc/default/grub 文件

  ```bash
  GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
  ```

+ 更新系统grub

  ```bash
  update-grub
  ```

+ 重启

  ```bash
  reboot
  ```

  