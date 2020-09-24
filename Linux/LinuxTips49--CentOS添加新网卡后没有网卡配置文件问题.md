# LinuxTips49--CentOS添加新网卡后没有网卡配置文件问题

### 为虚拟机添加新网卡后，多了ens37的网卡信息，但是在/etc/sysconfig/network-scripts下没有对应的ifcfg-ens37配置文件

```bash
[root@promote network-scripts]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:0e:0e:63 brd ff:ff:ff:ff:ff:ff
    inet 192.168.200.3/24 brd 192.168.200.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::d94c:ed0d:52ca:1b84/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: ens37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:0e:0e:6d brd ff:ff:ff:ff:ff:ff
    inet6 fe80::b749:1bbf:b944:b603/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

### 解决方法1

##### 添加网卡配置信息

+ 使用nmcli con show查看网卡的设备名称（Device）

  ```bash
  [root@promote network-scripts]# nmcli con show
  NAME                UUID                                  TYPE      DEVICE 
  ens33               4fc12b23-8106-401a-b7c0-c5c27eb981ca  ethernet  ens33  
  Wired connection 1  d98e0ae2-f616-3bde-9715-9fb2d40ad8e0  ethernet  ens37 
  ```

+ 添加网卡信息，会自动生成一个ifcfg-ens37配置文件

  ```bash
  [root@promote network-scripts]# nmcli con add con-name ens37 type ethernet ifname ens37
  Connection 'ens37' (3265a71d-939c-4471-8d9f-e2e280a52a18) successfully added.
  ```

  此时/etc/sysconfig/network-scripts下自动生成了ifcfg-ens37配置文件

##### 修改ifcfg-ens37配置

+ 设置静态IP,网关等

+ ```bash
  TYPE=Ethernet
  PROXY_METHOD=none
  BROWSER_ONLY=no
  BOOTPROTO=static
  IPADDR=192.168.200.30
  NETMASK=255.255.255.0
  GATEWAY=192.168.200.2
  DNS1=8.8.8.8
  DEFROUTE=yes
  IPV4_FAILURE_FATAL=no
  IPV6INIT=yes
  IPV6_AUTOCONF=yes
  IPV6_DEFROUTE=yes
  IPV6_FAILURE_FATAL=no
  IPV6_ADDR_GEN_MODE=stable-privacy
  NAME=ens37
  UUID=3265a71d-939c-4471-8d9f-e2e280a52a18
  DEVICE=ens37
  ONBOOT=yes
  ```

##### 重启网络服务

+ ```bash
  service network restart
  ```

---

### 解决方法2

##### 使用nmcli con show命令，查看网卡UUID信息

+ ```bash
  [root@promote network-scripts]# nmcli con show
  NAME                UUID                                  TYPE      DEVICE 
  ens33               4fc12b23-8106-401a-b7c0-c5c27eb981ca  ethernet  ens33  
  Wired connection 1  d98e0ae2-f616-3bde-9715-9fb2d40ad8e0  ethernet  ens37
  ```

##### 使用ip addr命令查看网卡信息，查看ens37网卡的MAC地址

+ ```bash
  [root@promote network-scripts]# ip addr
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
      link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      inet 127.0.0.1/8 scope host lo
         valid_lft forever preferred_lft forever
      inet6 ::1/128 scope host 
         valid_lft forever preferred_lft forever
  2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
      link/ether 00:0c:29:0e:0e:63 brd ff:ff:ff:ff:ff:ff
      inet 192.168.200.3/24 brd 192.168.200.255 scope global noprefixroute ens33
         valid_lft forever preferred_lft forever
      inet6 fe80::d94c:ed0d:52ca:1b84/64 scope link noprefixroute 
         valid_lft forever preferred_lft forever
  3: ens37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
      link/ether 00:0c:29:0e:0e:6d brd ff:ff:ff:ff:ff:ff
      inet6 fe80::b749:1bbf:b944:b603/64 scope link noprefixroute 
         valid_lft forever preferred_lft forever
  ```

##### 将ifcfg-ens33文件复制一份，改名为ifcfg-ens37

##### 修改ifcfg-ens37配置文件

+ ```bash
  [root@promote network-scripts]# vim ifcfg-ens37
  
  TYPE=Ethernet
  PROXY_METHOD=none
  BROWSER_ONLY=no
  BOOTPROTO=static
  IPADDR=192.168.200.30
  NETMASK=255.255.255.0
  GATEWAY=192.168.200.2
  DNS1=8.8.8.8
  DEFROUTE=yes
  IPV4_FAILURE_FATAL=no
  IPV6INIT=yes
  IPV6_AUTOCONF=yes
  IPV6_DEFROUTE=yes
  IPV6_FAILURE_FATAL=no
  IPV6_ADDR_GEN_MODE=stable-privacy
  NAME=ens37
  UUID=d98e0ae2-f616-3bde-9715-9fb2d40ad8e0
  DEVICE=ens37
  ONBOOT=yes
  HWADDR=00:0c:29:0e:0e:6d
  ```

+ **修改UUID**
+ **添加HWADDR**
+ **丢该NAME,DEVICE**
+ 按需修改IPADDR,NETMASK,GATEWAY,DNS等

##### 重启网卡

+ ```bash
  service network restart
  ```

  