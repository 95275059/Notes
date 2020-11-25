# LinuxTips62--IP Forwarding

一般情况下，我们的linux机器的ip forwarding选项都是关闭的。 但是如果我们的机器需要做网关，或路由器。那么这个就要打开了

### 检查是否打开了IP Forwarding

```bash
root@ubuntu16:~# sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 1
```

```bash
root@ubuntu16:~# cat /proc/sys/net/ipv4/ip_forward
1
```

如果上述文件中的值为0,说明禁止进行IP转发；如果是1,则说明IP转发功能已经打开。

### 打开IP Forwarding

+ 方法一：一次性

  ```bash
  sysctl -w net.ipv4.ip_forward=1
  ```

+ 方法二：一次性

  ```bash
  echo 1 > /proc/sys/net/ipv4/ip_forward
  ```

  上面的两种方法并没有保存对IP转发配置的更改，下次系统启动时仍会使用原来的值

+ 方法三：永久

  vim /etc/sysctl.conf

  ```bash
  net.ipv4.ip_forward = 1
  ```

  重启系统或者输入以下命令使生效

  ```bash
  sysctl -p /etc/sysctl.conf
  ```

  + 对于centos 7

    + ```bash
      vim /etc/sysctl.d/99-sysctl.conf 
      ...
      net.ipv4.ip_forward = 1
      ...
      ```

    + ```bash
      sysctl -p
      ```

      

