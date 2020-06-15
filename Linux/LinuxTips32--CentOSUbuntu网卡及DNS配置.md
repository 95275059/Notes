# LinuxTips32--CentOS/Ubuntu网卡及DNS配置

### CentOS 7

1. 修改IP地址

   + 临时修改

     ```shell
     # ifconfig eth0 192.168.1.80
     ```

     + 重新启动系统或网卡之后，还是会变回原来的地址，这种修改方式只适用于需要临时做IP修改

   + 永久修改

     + 编辑 **/etc/sysconfig/network-scripts/ifcfg-eth0**

       ```shell
       # vi  /etc/sysconfig/network-scripts/ifcfg-eth0
       
       DEVICE=eth0 #描述网卡对应的设备别名
       BOOTPROTO=static #设置网卡获得ip地址的方式，选项可以为为static，dhcp或bootp
       BROADCAST=192.168.44.255 #对应的子网广播地址
       HWADDR="00:0C:29:6B:2E:7B"#对应的网卡物理地址
       IPADDR=192.168.44.137 #只有网卡设置成static时，才需要此字段
       NETMASK=255.255.255.0 #网卡对应的网络掩码
       NETWORK=192.168.44.0 #网卡对应的网络地址，也就是所属的网段
       ONBOOT=yes #系统启动时是否设置此网络接口，设置为yes时，系统启动时激活此设备
       ```

     + 顺便加了网关和DNS服务器（连接外网）

       + GATEWAY=...
       + DNS1=8.8.8.8
       + DNS2=4.2.2.2

       ==注：这里如果加了DNS，后面/etc/resolv.conf里面自动加了DNS，就不用再改/etc/resolv.conf文件了==

     + 重启网卡

       + service network restart

2. 修改网关

   + 临时修改

     ```shell
     # route add default gw 192.168.1.1 dev eth0
     ```

     + 重新启动系统或网卡之后，还是会变回原来的网关

   + 永久修改

     + 编辑 **/etc/sysconfig/network**

       ```shell
       # vi  /etc/sysconfig/network
       
       NETWORKING=yes #表示系统是否使用网络，一般设置为yes。如果设为no，则不能使用网络。
       HOSTNAME=centos #设置本机的主机名，这里设置的主机名要和/etc/hosts中设置的主机名对应
       GATEWAY=192.168.1.1 #设置本机连接的网关的IP地址。
       ```

     + 重启网卡
       
       + **service network restart** 

3. 修改DNS

   修改完IP和网关后，ping一个域名是肯能不通，但ping对应的IP地址是同的。这就需要加DNS

   + 方法一：直接在网卡配置文件里加，看1

   + f方法二：编辑 **/etc/resolv.conf**

     ```shell
     nameserver 8.8.8.8 #google域名服务器 
     nameserver 8.8.4.4 #google域名服务器
     ```

---

### Ubuntu16.04

1. 查看网卡信息

   ```shell
   root@cxytest:/etc# ifconfig
   ens3      Link encap:Ethernet  HWaddr fa:16:3e:cd:3c:c7  
             inet addr:222.222.222.7  Bcast:222.222.222.255  Mask:255.255.255.0
             inet6 addr: fe80::f816:3eff:fecd:3cc7/64 Scope:Link
             UP BROADCAST RUNNING MULTICAST  MTU:1458  Metric:1
             RX packets:2625 errors:0 dropped:0 overruns:0 frame:0
             TX packets:2622 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000 
             RX bytes:221188 (221.1 KB)  TX bytes:235011 (235.0 KB)
   
   lo        Link encap:Local Loopback  
             inet addr:127.0.0.1  Mask:255.0.0.0
             inet6 addr: ::1/128 Scope:Host
             UP LOOPBACK RUNNING  MTU:65536  Metric:1
             RX packets:160 errors:0 dropped:0 overruns:0 frame:0
             TX packets:160 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1 
             RX bytes:11840 (11.8 KB)  TX bytes:11840 (11.8 KB)
   
   ```

2. 配置网卡文件/etc/network/interfaces，修改ip及网关

   + ```shell
     sudo vi /etc/network/interfaces
     ```

     + 默认的文件内容

       ```shell
       auto lo 
       iface lo inet loopback
       ```

   + 静态ip

     注意修改网卡名称为ifconfig结果中的网卡名称

     ```shell
     auto ens3
     iface ens3 inet static
     address 222.222.222.5
     netmask 255.255.255.0
     gateway 222.222.222.1
     ```

   + 动态ip

     ```shell
     auto ens3
     iface ens3 inet dhcp
     ```

3. 修改DNS服务器地址

   + 方法一：/etc/network/interfaces**==(测试改了没用)==**

     ```shell
     dns-nameservers 8.8.8.8
     ```

     重启后DNS就会生效，/etc/resolv.conf里面也会自动加好

   + 方法二：/etc/resolvconf/resolv.conf.d/目录下的base文件

     ```shell
     nameserver 8.8.8.8
     ```

4. 重启网卡

   ```shell
   sudo systemctl networking
   ```





