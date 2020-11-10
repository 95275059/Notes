# OpenStackTips12--实例没有ip

### 检查dhcp agent日志

+ /var/log/neutron/dhcp-agent.log

+ ![OpenStackTips12-1](E:\Notes\OpenStack\OpenStackTips12-1.png)

+ **错误：Unable to enable dhcp for  + Permission denied: '/var/lib/neutron/dhcp/.....'** 

+ 原因

  /var/lib/neutron/dhcp目录所有者为root,应该是neutron

  ```bash
  [root@controller dhcp]# ls -lrt
  total 0
  drwxr-xr-x 2 root root 90 Oct 20 23:46 41afadee-ab80-4b2a-86a9-f22fedcbb203
  ```

+ 解决

  ```bash
  [root@controller dhcp]# chown -R neutron:neutron /var/lib/neutron/dhcp
  ```

  ```bash
  [root@controller neutron]# ll
  total 0
  d-wx--x--x 3 neutron neutron  50 Oct 20 23:16 dhcp
  drwxr-xr-x 3 neutron neutron  18 Oct 19 22:25 external
  drwxr-xr-x 2 neutron neutron   6 Jun  9 10:03 ha_confs
  srwxr-xr-x 1 neutron neutron   0 Oct 20 21:55 keepalived-state-change
  srw-r--r-- 1 neutron neutron   0 Oct 20 21:54 metadata_proxy
  drwxr-xr-x 2 neutron neutron 161 Oct 19 22:25 tmp
  ```

+ 参考

  https://ask.openstack.org/en/question/30078/unable-to-enable-dhcp-for-network-id-error/

### 检查计算节点的linuxbridge日志

+ /var/log/neutron/linuxbirdge.log

+ ![OpenStackTips12-1](E:\Notes\OpenStack\OpenStackTips12-2.jpg)

+ 在网络节点配置

  + vim /etc/sysctl.conf

    ```bash
    net.ipv4.ip_forward=1
    
    net.ipv4.conf.all.rp_filter=0
    
    net.ipv4.conf.default.rp_filter=0
    
    net.bridge.bridge-nf-call-arptables=1
    
    net.bridge.bridge-nf-call-iptables=1
    
    net.bridge.bridge-nf-call-ip6tables=1
    ```

  + ```bash
    sysctl -p
    ```

    + 报错

      ```bash
      sysctl: cannot stat/proc/sys/net/bridge/bridge-nf-call-arptables: No such file or directory
      
      sysctl: cannot stat/proc/sys/net/bridge/bridge-nf-call-iptables: No such file or directory
      
      sysctl: cannot stat/proc/sys/net/bridge/bridge-nf-call-ip6tables: No such file or directory
      ```

    + 解决

      ```bash
      [root@controller etc]# sysctl -p
      net.ipv4.ip_forward = 1
      net.ipv4.conf.all.rp_filter = 0
      net.ipv4.conf.default.rp_filter = 0
      sysctl: cannot stat /proc/sys/net/bridge/bridge-nf-call-arptables: No such file or directory
      sysctl: cannot stat /proc/sys/net/bridge/bridge-nf-call-iptables: No such file or directory
      sysctl: cannot stat /proc/sys/net/bridge/bridge-nf-call-ip6tables: No such file or directory
      [root@controller etc]# modprobe bridge
      [root@controller etc]# sysctl -p
      net.ipv4.ip_forward = 1
      net.ipv4.conf.all.rp_filter = 0
      net.ipv4.conf.default.rp_filter = 0
      sysctl: cannot stat /proc/sys/net/bridge/bridge-nf-call-arptables: No such file or directory
      sysctl: cannot stat /proc/sys/net/bridge/bridge-nf-call-iptables: No such file or directory
      sysctl: cannot stat /proc/sys/net/bridge/bridge-nf-call-ip6tables: No such file or directory
      [root@controller etc]# modprobe br_netfilter
      [root@controller etc]# sysctl -p
      net.ipv4.ip_forward = 1
      net.ipv4.conf.all.rp_filter = 0
      net.ipv4.conf.default.rp_filter = 0
      net.bridge.bridge-nf-call-arptables = 1
      net.bridge.bridge-nf-call-iptables = 1
      net.bridge.bridge-nf-call-ip6tables = 1
      ```

+ 在计算节点配置

  + vim /etc/sysctl.conf

    ```bash
    net.ipv4.conf.all.rp_filter=0
    
    net.ipv4.conf.default.rp_filter=0
    
    net.bridge.bridge-nf-call-arptables=1
    
    net.bridge.bridge-nf-call-iptables=1
    
    net.bridge.bridge-nf-call-ip6tables=1
    ```

  + ```
    sysctl -p
    ```

    ```bash
    [root@compute2 neutron]# sysctl -p
    net.ipv4.conf.all.rp_filter = 0
    net.ipv4.conf.default.rp_filter = 0
    net.bridge.bridge-nf-call-arptables = 1
    net.bridge.bridge-nf-call-iptables = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    ```

### local网络

local网络类型下的虚拟机，如果建在计算节点上，不会被分配到ip的。因为DHCP服务在控制节点上

### vlan网络

虚拟机启动日志

![OpenStackTips12-1](E:\Notes\OpenStack\OpenStackTips12-5.jpg)

+ 参考网址
  + https://www.aboutyun.com/forum.php?mod=viewthread&tid=16420
  + https://blog.csdn.net/quqi99/article/details/17483883
  + https://blog.csdn.net/happyteafriends/article/details/48263537
  + https://my.oschina.net/xiaozhublog/blog/677238
  + https://ask.openstack.org/en/question/30339/dnsmasq-unknown-interface/
  
+ 配置问题

  + 控制节点  /etc/nova/nova.conf

    ![OpenStackTips12-1](E:\Notes\OpenStack\OpenStackTips12-3.jpg)

    注意后面根据官方文档更新计算服务数据库和重启相关服务

  + 控制节点和计算节点 /etc/neutron/plugins/ml2/linuxbridge_agent.ini

    ![OpenStackTips12-1](E:\Notes\OpenStack\OpenStackTips12-4.jpg)

    注意后面根据官方文档更新网络服务数据库和重启相关服务

+ 可能的原因

  租户网络网卡设置混杂模式

  ip link set eth1 promisc on

  





 