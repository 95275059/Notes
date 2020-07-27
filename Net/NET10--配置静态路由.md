# NET10--配置静态路由

1. 使用 route 命令添加

   使用route 命令添加的路由，机器重启或者网卡重启后路由就失效了

   + 添加到主机的路由

     ```bash
     route add –host 192.168.1.11 dev eth0
     route add –host 192.168.1.12 gw 192.168.1.1
     ```

   + 添加到网络的路由

     ```bash
     route add –net 192.168.1.11 netmask 255.255.255.0 eth0
     route add –net 192.168.1.11 gw 192.168.1.1 netmask 255.255.255.0 
     route add –net 192.168.1.0/24 eth1
     ```

   + 添加默认网关

     ```bash
     route add default gw 192.168.2.1
     ```

   + 删除路由

     ```bash
     route del –host 192.168.1.11 dev eth0
     ```

2. 在Linux下设置永久路由

   + 在/etc/rc.local中添加

     ```bash
     route add -net 192.168.3.0/24 dev eth0
     route add -net 192.168.2.0/24 gw 192.168.2.254
     ```

   + 在/etc/sysconfig/network里添加到末尾

     ```bash
     GATEWAY=gw-ip 或者 GATEWAY=gw-de
     ```

     