# LinuxTips51--netstat命令

### 功能

+ netstat命令用于显示网络状态

### 语法

```bash
netstat [-acCeFghilMnNoprstuvVwx] [-A<网络类型>][--ip]
```

+ 选项

  | 选项                          | 说明                                     |
  | ----------------------------- | ---------------------------------------- |
  | **-a 或 -all**                | 显示所有连线中的Socket                   |
  | -A<网络类型> 或 --<网络类型>  | 列出该网络类型连线中的相关地址           |
  | -c 或 --continuous            | 持续列出网络状态                         |
  | -C 或 --cache                 | 显示路由器配置的快取信息                 |
  | -e 或 --extend                | 显示网络其他相关信息                     |
  | -F 或 --fib                   | 显示FIB                                  |
  | -g 或 --groups                | 显示多重广播功能群组组员名单             |
  | -h 或 --help                  | 在线帮助                                 |
  | **-i 或 --interfaces**        | 显示网络界面信息表单                     |
  | **-l 或 --listening**         | 显示监控中的服务器的Socket               |
  | -M 或 --masquerade            | 显示伪装的网络连线                       |
  | **-n 或 --numeric**           | 直接使用IP地址，而不通过域名服务器       |
  | -N 或 --netlink 或 --symbolic | 显示网络硬件外围设备的符号连接名称       |
  | -o 或 --timers                | 显示计时器                               |
  | **-p 或 --programs**          | 显示正在使用Socket的程序识别码和程序名称 |
  | **-r 或 --route**             | 显示Routing Table                        |
  | -s 或 --statistics            | 显示网络工作信息统计表                   |
  | **-t 或 --tcp**               | 显示TCP传输协议的连线状况                |
  | **-u 或 --udp**               | 显示UDP传输协议的连线状况                |
  | -v 或 --verbose               | 显示指令执行过程                         |
  | -V 或 --version               | 显示版本信息                             |
  | -w 或 --raw                   | 显示RAW传输协议的连线状况                |
  | -x 或 --unix                  | 参数的效果和指定"-A unix"参数相同        |
  | --ip 或 --inet                | 此参数的效果和指定"-A inet"参数相同      |

### 实例

+ 查看本机监听的端口

  ```bash
  [root@compute6 html]# netstat -tuln
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State      
  tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN     
  tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN     
  tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
  tcp6       0      0 ::1:25                  :::*                    LISTEN     
  tcp6       0      0 :::111                  :::*                    LISTEN     
  tcp6       0      0 :::80                   :::*                    LISTEN     
  tcp6       0      0 :::22                   :::*                    LISTEN     
  udp        0      0 0.0.0.0:111             0.0.0.0:*                          
  udp        0      0 127.0.0.1:323           0.0.0.0:*                          
  udp        0      0 0.0.0.0:846             0.0.0.0:*                          
  udp6       0      0 :::111                  :::*                               
  udp6       0      0 ::1:323                 :::*                               
  udp6       0      0 :::846                  :::* 
  ```

+ 查看本机所有网络连接

  ```bash
  [root@compute6 html]# netstat -an
  Active Internet connections (servers and established)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State      
  tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN     
  tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN     
  tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
  tcp        0      0 192.168.1.18:47156      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47148      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47150      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47142      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47154      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47146      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47152      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:22         192.168.1.11:38378      ESTABLISHED
  tcp        0      0 192.168.1.18:47164      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47140      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47138      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47144      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47158      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47162      192.168.1.11:5672       ESTABLISHED
  tcp        0      0 192.168.1.18:47160      192.168.1.11:5672       ESTABLISHED
  tcp6       0      0 ::1:25                  :::*                    LISTEN     
  tcp6       0      0 :::111                  :::*                    LISTEN     
  tcp6       0      0 :::80                   :::*                    LISTEN     
  tcp6       0      0 :::22                   :::*                    LISTEN     
  udp        0      0 0.0.0.0:111             0.0.0.0:*                          
  udp        0      0 127.0.0.1:323           0.0.0.0:*                          
  udp        0      0 0.0.0.0:846             0.0.0.0:*                          
  udp6       0      0 :::111                  :::*                               
  udp6       0      0 ::1:323                 :::*                               
  udp6       0      0 :::846                  :::*                               
  raw6       0      0 :::58                   :::*                    7          
  raw6       0      0 :::58                   :::*                    7          
  Active UNIX domain sockets (servers and established)
  Proto RefCnt Flags       Type       State         I-Node   Path
  unix  3      [ ]         DGRAM                    13571    /run/systemd/notify
  unix  2      [ ]         DGRAM                    13573    /run/systemd/cgroups-agent
  unix  2      [ ACC ]     STREAM     LISTENING     13581    /run/systemd/journal/stdout
  unix  6      [ ]         DGRAM                    13584    /run/systemd/journal/socket
  unix  19     [ ]         DGRAM                    13586    /dev/log
  unix  2      [ ACC ]     STREAM     LISTENING     28695    /run/systemd/private
  unix  2      [ ACC ]     STREAM     LISTENING     26916    /run/gssproxy.sock
  unix  2      [ ACC ]     STREAM     LISTENING     1584     /var/run/libvirt/virtlogd-sock
  unix  2      [ ACC ]     STREAM     LISTENING     1587     /var/run/libvirt/virtlockd-sock
  unix  2      [ ACC ]     STREAM     LISTENING     17204    /var/run/openvswitch/br-int.mgmt
  unix  2      [ ACC ]     STREAM     LISTENING     17206    /var/run/openvswitch/br-int.snoop
  unix  2      [ ACC ]     STREAM     LISTENING     24888    /var/run/docker/libnetwork/b450978cf01e7f86272a3c21801ca56f38bcf4a4b1ee44f76fcd85d283fa31ce.sock
  unix  2      [ ACC ]     STREAM     LISTENING     17208    /var/run/openvswitch/br-tun.mgmt
  unix  2      [ ACC ]     STREAM     LISTENING     17210    /var/run/openvswitch/br-tun.snoop
  unix  2      [ ACC ]     STREAM     LISTENING     44603    /var/run/openvswitch/db.sock
  unix  2      [ ACC ]     STREAM     LISTENING     49717    private/tlsmgr
  unix  2      [ ACC ]     STREAM     LISTENING     49720    private/rewrite
  unix  2      [ ACC ]     STREAM     LISTENING     44605    /var/run/openvswitch/ovsdb-server.1157.ctl
  unix  2      [ ACC ]     STREAM     LISTENING     49723    private/bounce
  unix  2      [ ACC ]     STREAM     LISTENING     52287    /var/run/docker/metrics.sock
  unix  2      [ ACC ]     STREAM     LISTENING     49706    public/pickup
  unix  2      [ ACC ]     STREAM     LISTENING     49710    public/cleanup
  unix  2      [ ACC ]     STREAM     LISTENING     16731    @ISCSID_UIP_ABSTRACT_NAMESPACE
  unix  2      [ ACC ]     STREAM     LISTENING     49713    public/qmgr
  unix  2      [ ]         DGRAM                    29771    /var/run/chrony/chronyd.sock
  unix  2      [ ACC ]     STREAM     LISTENING     49735    public/flush
  unix  2      [ ACC ]     STREAM     LISTENING     49750    public/showq
  unix  2      [ ACC ]     STREAM     LISTENING     29013    /run/lvm/lvmpolld.socket
  unix  2      [ ]         DGRAM                    29016    /run/systemd/shutdownd
  unix  2      [ ACC ]     STREAM     LISTENING     16729    /var/run/docker.sock
  unix  2      [ ACC ]     STREAM     LISTENING     16732    /run/dbus/system_bus_socket
  unix  2      [ ACC ]     STREAM     LISTENING     16735    /var/run/rpcbind.sock
  unix  2      [ ACC ]     STREAM     LISTENING     55561    /tmp/rootwrap-ywLoaO/rootwrap.sock
  unix  2      [ ACC ]     STREAM     LISTENING     26915    /var/lib/gssproxy/default.sock
  unix  2      [ ACC ]     STREAM     LISTENING     35982    /var/run/libvirt/libvirt-sock
  unix  2      [ ACC ]     STREAM     LISTENING     35984    /var/run/libvirt/libvirt-sock-ro
  unix  2      [ ACC ]     STREAM     LISTENING     35986    /var/run/libvirt/libvirt-admin-sock
  unix  2      [ ACC ]     STREAM     LISTENING     49726    private/defer
  unix  2      [ ACC ]     STREAM     LISTENING     53688    /run/containerd/containerd.sock
  unix  2      [ ACC ]     STREAM     LISTENING     49729    private/trace
  unix  2      [ ACC ]     STREAM     LISTENING     49732    private/verify
  unix  2      [ ACC ]     STREAM     LISTENING     1589     @ISCSIADM_ABSTRACT_NAMESPACE
  unix  2      [ ACC ]     STREAM     LISTENING     49738    private/proxymap
  unix  2      [ ACC ]     STREAM     LISTENING     29121    /run/lvm/lvmetad.socket
  unix  2      [ ACC ]     STREAM     LISTENING     49741    private/proxywrite
  unix  2      [ ACC ]     STREAM     LISTENING     49744    private/smtp
  unix  2      [ ACC ]     STREAM     LISTENING     49747    private/relay
  unix  2      [ ACC ]     STREAM     LISTENING     49753    private/error
  unix  2      [ ACC ]     STREAM     LISTENING     49756    private/retry
  unix  2      [ ACC ]     STREAM     LISTENING     49759    private/discard
  unix  2      [ ACC ]     STREAM     LISTENING     49762    private/local
  unix  2      [ ACC ]     STREAM     LISTENING     49765    private/virtual
  unix  2      [ ACC ]     STREAM     LISTENING     49768    private/lmtp
  unix  2      [ ACC ]     STREAM     LISTENING     49771    private/anvil
  unix  2      [ ACC ]     STREAM     LISTENING     49774    private/scache
  unix  2      [ ACC ]     STREAM     LISTENING     14031    /var/run/openvswitch/ovs-vswitchd.1244.ctl
  unix  2      [ ACC ]     SEQPACKET  LISTENING     35062    /run/udev/control
  unix  3      [ ]         STREAM     CONNECTED     49727    
  unix  2      [ ]         DGRAM                    7119813  
  unix  3      [ ]         STREAM     CONNECTED     27976    /run/containerd/containerd.sock
  unix  3      [ ]         STREAM     CONNECTED     33975    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     37066    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     33987    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     4249239  
  unix  3      [ ]         STREAM     CONNECTED     17927    
  unix  2      [ ]         DGRAM                    26581    
  unix  2      [ ]         DGRAM                    909      
  unix  3      [ ]         DGRAM                    21621    
  unix  3      [ ]         STREAM     CONNECTED     22592    
  unix  3      [ ]         STREAM     CONNECTED     49740    
  unix  3      [ ]         STREAM     CONNECTED     33979    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     26662    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49761    
  unix  3      [ ]         STREAM     CONNECTED     49746    
  unix  3      [ ]         STREAM     CONNECTED     22610    /run/dbus/system_bus_socket
  unix  3      [ ]         STREAM     CONNECTED     49705    
  unix  3      [ ]         STREAM     CONNECTED     26896    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49719    
  unix  3      [ ]         STREAM     CONNECTED     49775    
  unix  3      [ ]         STREAM     CONNECTED     33940    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     26880    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49736    
  unix  3      [ ]         STREAM     CONNECTED     49773    
  unix  3      [ ]         STREAM     CONNECTED     49758    
  unix  3      [ ]         STREAM     CONNECTED     15708    
  unix  3      [ ]         STREAM     CONNECTED     4249238  
  unix  3      [ ]         STREAM     CONNECTED     49707    
  unix  3      [ ]         STREAM     CONNECTED     14034    
  unix  3      [ ]         STREAM     CONNECTED     13996    
  unix  3      [ ]         STREAM     CONNECTED     22612    /run/dbus/system_bus_socket
  unix  2      [ ]         DGRAM                    54487    
  unix  3      [ ]         STREAM     CONNECTED     49769    
  unix  3      [ ]         STREAM     CONNECTED     49754    
  unix  3      [ ]         STREAM     CONNECTED     33223    
  unix  3      [ ]         STREAM     CONNECTED     49766    
  unix  3      [ ]         STREAM     CONNECTED     22608    
  unix  3      [ ]         STREAM     CONNECTED     49743    
  unix  3      [ ]         STREAM     CONNECTED     49728    
  unix  3      [ ]         STREAM     CONNECTED     55566    /tmp/rootwrap-ywLoaO/rootwrap.sock
  unix  3      [ ]         STREAM     CONNECTED     50244    
  unix  3      [ ]         STREAM     CONNECTED     54373    
  unix  3      [ ]         STREAM     CONNECTED     33981    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49749    
  unix  3      [ ]         STREAM     CONNECTED     7223427  /var/run/openvswitch/db.sock
  unix  3      [ ]         DGRAM                    21622    
  unix  3      [ ]         STREAM     CONNECTED     22593    
  unix  3      [ ]         STREAM     CONNECTED     49739    
  unix  3      [ ]         STREAM     CONNECTED     49724    
  unix  3      [ ]         STREAM     CONNECTED     49704    
  unix  3      [ ]         STREAM     CONNECTED     41247    
  unix  3      [ ]         STREAM     CONNECTED     49745    
  unix  3      [ ]         STREAM     CONNECTED     7054250  
  unix  3      [ ]         STREAM     CONNECTED     7213736  /var/run/docker.sock
  unix  3      [ ]         STREAM     CONNECTED     49712    
  unix  3      [ ]         STREAM     CONNECTED     7995521  
  unix  3      [ ]         STREAM     CONNECTED     17107    
  unix  3      [ ]         STREAM     CONNECTED     46696    
  unix  3      [ ]         STREAM     CONNECTED     49757    
  unix  3      [ ]         STREAM     CONNECTED     49776    
  unix  3      [ ]         STREAM     CONNECTED     26876    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49770    
  unix  2      [ ]         DGRAM                    54489    
  unix  3      [ ]         STREAM     CONNECTED     18173    
  unix  2      [ ]         DGRAM                    24728    
  unix  3      [ ]         STREAM     CONNECTED     49731    
  unix  3      [ ]         STREAM     CONNECTED     33955    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49742    
  unix  3      [ ]         STREAM     CONNECTED     44717    /run/dbus/system_bus_socket
  unix  3      [ ]         STREAM     CONNECTED     44739    
  unix  3      [ ]         STREAM     CONNECTED     54446    
  unix  3      [ ]         STREAM     CONNECTED     47067    
  unix  3      [ ]         STREAM     CONNECTED     49767    
  unix  3      [ ]         STREAM     CONNECTED     49752    
  unix  3      [ ]         STREAM     CONNECTED     49715    
  unix  3      [ ]         STREAM     CONNECTED     17766    
  unix  3      [ ]         STREAM     CONNECTED     7994534  /run/systemd/journal/stdout
  unix  2      [ ]         DGRAM                    22605    
  unix  3      [ ]         STREAM     CONNECTED     54652    
  unix  3      [ ]         STREAM     CONNECTED     45563    
  unix  3      [ ]         STREAM     CONNECTED     49763    
  unix  3      [ ]         STREAM     CONNECTED     49748    
  unix  3      [ ]         STREAM     CONNECTED     49725    
  unix  3      [ ]         STREAM     CONNECTED     49711    
  unix  3      [ ]         STREAM     CONNECTED     49486    
  unix  3      [ ]         STREAM     CONNECTED     17161    /run/dbus/system_bus_socket
  unix  3      [ ]         STREAM     CONNECTED     22609    
  unix  2      [ ]         DGRAM                    7919245  
  unix  3      [ ]         STREAM     CONNECTED     49734    
  unix  3      [ ]         STREAM     CONNECTED     26914    
  unix  3      [ ]         STREAM     CONNECTED     49760    
  unix  2      [ ]         DGRAM                    35976    
  unix  2      [ ]         DGRAM                    17175    
  unix  2      [ ]         DGRAM                    52318    
  unix  2      [ ]         DGRAM                    17932    
  unix  3      [ ]         STREAM     CONNECTED     49721    
  unix  3      [ ]         STREAM     CONNECTED     47300    /run/dbus/system_bus_socket
  unix  3      [ ]         STREAM     CONNECTED     41292    
  unix  3      [ ]         STREAM     CONNECTED     22616    /run/systemd/journal/stdout
  unix  2      [ ]         DGRAM                    13845    
  unix  3      [ ]         STREAM     CONNECTED     49751    
  unix  3      [ ]         STREAM     CONNECTED     44632    /var/run/openvswitch/db.sock
  unix  3      [ ]         STREAM     CONNECTED     12565    
  unix  3      [ ]         STREAM     CONNECTED     26568    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     49764    
  unix  2      [ ]         DGRAM                    22591    
  unix  3      [ ]         STREAM     CONNECTED     49730    
  unix  3      [ ]         STREAM     CONNECTED     53703    /run/containerd/containerd.sock
  unix  3      [ ]         STREAM     CONNECTED     49554    
  unix  3      [ ]         STREAM     CONNECTED     6634306  /var/run/docker.sock
  unix  3      [ ]         STREAM     CONNECTED     17168    /run/dbus/system_bus_socket
  unix  2      [ ]         DGRAM                    15760    
  unix  3      [ ]         STREAM     CONNECTED     24764    
  unix  3      [ ]         STREAM     CONNECTED     49714    
  unix  3      [ ]         STREAM     CONNECTED     26609    
  unix  3      [ ]         STREAM     CONNECTED     26572    /run/dbus/system_bus_socket
  unix  2      [ ]         DGRAM                    35769    
  unix  3      [ ]         STREAM     CONNECTED     17989    
  unix  3      [ ]         STREAM     CONNECTED     46415    
  unix  3      [ ]         STREAM     CONNECTED     26913    
  unix  3      [ ]         STREAM     CONNECTED     55397    
  unix  3      [ ]         STREAM     CONNECTED     49772    
  unix  2      [ ]         DGRAM                    17159    
  unix  2      [ ]         DGRAM                    26571    
  unix  3      [ ]         STREAM     CONNECTED     49737    
  unix  3      [ ]         STREAM     CONNECTED     49722    
  unix  2      [ ]         DGRAM                    7213738  
  unix  3      [ ]         STREAM     CONNECTED     49755    
  unix  2      [ ]         DGRAM                    13990    
  unix  3      [ ]         STREAM     CONNECTED     49708    
  unix  3      [ ]         STREAM     CONNECTED     26664    /run/systemd/journal/stdout
  unix  2      [ ]         DGRAM                    11500    
  unix  3      [ ]         STREAM     CONNECTED     22618    /run/systemd/journal/stdout
  unix  3      [ ]         STREAM     CONNECTED     22018    
  unix  2      [ ]         DGRAM                    7970872  
  unix  3      [ ]         STREAM     CONNECTED     49733    
  unix  3      [ ]         STREAM     CONNECTED     49718    
  unix  3      [ ]         STREAM     CONNECTED     33989    /run/systemd/journal/stdout
  ```

+ 查看本机路由表

  ```bash
  [root@compute6 html]# netstat -rn
  Kernel IP routing table
  Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
  0.0.0.0         192.168.1.1     0.0.0.0         UG        0 0          0 em1
  10.1.1.0        0.0.0.0         255.255.255.0   U         0 0          0 em2
  172.17.0.0      0.0.0.0         255.255.0.0     U         0 0          0 docker0
  192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 em1
  ```

+ 显示网卡列表

  ```bash
  [root@compute6 html]# netstat -i
  Kernel Interface table
  Iface             MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
  docker0          1500        0      0      0 0             0      0      0      0 BMU
  em1              1500  2547970      0      2 0        176790      0      0      0 BMRU
  em2              1500  2567084      0      2 0            15      0      0      0 BMRU
  em3              1500        0      0      0 0             0      0      0      0 BMU
  em4              1500        0      0      0 0             0      0      0      0 BMU
  lo              65536   104633      0      0 0        104633      0      0      0 LRU
  ```

+ 显示网络统计信息

  ```bash
  [root@compute6 html]# netstat -s
  Ip:
      302851 total packets received
      0 forwarded
      0 incoming packets discarded
      234534 incoming packets delivered
      257617 requests sent out
      4 dropped because of missing route
  Icmp:
      104633 ICMP messages received
      51989 input ICMP message failed.
      ICMP input histogram:
          destination unreachable: 104633
      104967 ICMP messages sent
      0 ICMP messages failed
      ICMP output histogram:
          destination unreachable: 104967
  IcmpMsg:
          InType3: 104633
          OutType3: 104967
  Tcp:
      52061 active connections openings
      4 passive connection openings
      52047 failed connection attempts
      0 connection resets received
      15 connections established
      52919 segments received
      122877 segments send out
      52166 segments retransmited
      0 bad segments received.
      747 resets sent
  Udp:
      214 packets received
      676 packets to unknown port received.
      0 packet receive errors
      820 packets sent
      0 receive buffer errors
      0 send buffer errors
  UdpLite:
  TcpExt:
      2 TCP sockets finished time wait in fast timer
      3663 delayed acks sent
      20802 packet headers predicted
      1122 acknowledgments not containing data payload received
      29159 predicted acknowledgments
      23 times recovered from packet loss by selective acknowledgements
      TCPLostRetransmit: 18
      179 fast retransmits
      51986 other TCP timeouts
      TCPLossProbes: 1
      TCPLossProbeRecovery: 1
      TCPSackShifted: 475
      TCPSackMerged: 265
      TCPSackShiftFallback: 33
      TCPDeferAcceptDrop: 3
      IPReversePathFilter: 67843
      TCPRcvCoalesce: 4138
      TCPSpuriousRtxHostQueues: 78304
      TCPAutoCorking: 4886
      TCPSynRetrans: 51986
      TCPOrigDataSent: 50711
      TCPHystartTrainDetect: 1
      TCPHystartTrainCwnd: 16
  IpExt:
      InBcastPkts: 76092
      InOctets: 104732017
      OutOctets: 60241596
      InBcastOctets: 15785574
      InNoECTPkts: 335428
  ```

+ 