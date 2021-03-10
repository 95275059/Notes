# LinuxTips38--ifconfig

## 简介

Linux ifconfig 命令用于显示或设置网络设备

## 安装

```shell
yum install -y net-tools
```

## 语法

```bash
ifconfig [网络设备][down up -allmulti -arp -promisc][add<地址>][del<地址>][<hw<网络设备类型><硬件地址>][io_addr<I/O地址>][irq<IRQ地址>][media<网络媒介类型>][mem_start<内存地址>][metric<数目>][mtu<字节>][netmask<子网掩码>][tunnel<地址>][-broadcast<地址>][-pointopoint<地址>][IP地址]
```

| 参数                        | 说明                                                 |
| --------------------------- | ---------------------------------------------------- |
| add<地址>                   | 设置网络设备IPv6的IP地址                             |
| del<地址>                   | 删除网络设备IPv6的IP地址                             |
| down                        | 关闭指定的网络设备                                   |
| up                          | 启动指定的网络设备                                   |
| <hw<网络设备类型><硬件地址> | 设置网络设备的类型与硬件地址                         |
| io_addr<I/O地址>            | 设置网络设备的I/O地址                                |
| irq<IRQ地址>                | 设置网络设备的IRQ                                    |
| media<网络媒介类型>         | 设置网络设备的媒介类型                               |
| mem_start<内存地址>         | 设置网络设备在主内存所占用的起始地址                 |
| metric<数目>                | 指定在计算数据包的转送次数时，所要加上的数目         |
| mtu<字节>                   | 设置网络设备的MTU                                    |
| netmask<子网掩码>           | 设置网络设备的子网掩码                               |
| tunnel<地址>                | 建立IPv4与IPv6之间的隧道通信地址                     |
| -broadcast<地址>            | 将要送往指定地址的数据包当成广播数据包来处理         |
| -pointopoint<地址>          | 与指定地址的网络设备建立直接连线，此模式具有保密功能 |
| -promisc                    | 关闭或启动指定网络设备的promiscuous模式              |
| [IP地址]                    | 指定网络设备的IP地址                                 |
| [网络设备]                  | 指定网络设备的名称                                   |

3. 实例

   + 查看所有网卡信息(不包括down状态的网卡)

     ```bash
     [root@mysql ~]# ifconfig
     eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
             inet 192.168.0.111  netmask 255.255.255.0  broadcast 192.168.0.255
             inet6 fe80::8c18:4c0c:35b:f89c  prefixlen 64  scopeid 0x20<link>
             ether 00:0c:29:bf:7a:4b  txqueuelen 1000  (Ethernet)
             RX packets 396  bytes 43132 (42.1 KiB)
             RX errors 0  dropped 0  overruns 0  frame 0
             TX packets 189  bytes 25028 (24.4 KiB)
             TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
     
     
     # eth0：网卡名称
     # Link encap：网卡的接口类型，这里是以太网
     # HWaddr：网卡的硬件地址，俗称的MAC地址
     # inet addr：IPv4地址，如果是IPv6会写成inet6 addr
     # Bcast：广播地址
     # Mask：子网掩码
     # UP：表示网卡是开启状态
     # BROADCAST：表示网卡支持广播
     # RUNNING：表示网卡的网线已经被接上
     # MULTICAST：表示网卡支持组播
     # MTU：网络最大传输单元
     # Metric：到达网关的度量值，参考：http://m.chinabyte.com/network/191/12287691_gfh.shtml
     # RX packets：网络从启动到现在为止接收的数据包大小，单位是字节，error 发生错误的数据包，dropped 被丢弃的数据包
     # TX packets：网络从启动到现在为止发送的数据包大小，单位是字节，error 发生错误的数据包，dropped 被丢弃的数据包
     # collisions：发生碰撞的数据包，如果发生太多次,表明网络状况不太好
     # txqueuelen：传输数据的缓冲区的储存长度
     # RX bytes：总接收字节总量
     # TX bytes：总发送字节总量
     # Memory：网卡硬件的内存地址
     ```

   + 查看所有网卡信息（包括down状态的网卡）

     ```bash
     ifconfig -a
     ```

   + 查看指定网卡信息

     ```bash
     ifconfig eth0
     ```

   + 启动或关闭指定网卡

     ```bash
     # ifconfig eth0 down    ##等同于ifdown eth0
     # ifconfig eth0 up      ##等同于ifup eth0
     ```

   + 