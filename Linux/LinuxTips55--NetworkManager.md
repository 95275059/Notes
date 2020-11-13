# LinuxTips55--NetworkManager

### 介绍

+ **网络管理器是检测网络、自动连接网络的程序**

+ **可以管理无线和有限网络**

  对于无线网络,网络管理器优先连接已知的网络并可以自动切换到最可靠的无线网络。利用网络管理器的程序可以自由切换在线和离线模式。

+ 网络管理器会**相对无线网络优先选择有线网络**，支持 VPN。网络管理器最初由 Redhat 公司开发，现在由 GNOME 管理。
+ NetworkManager由一个管理系统网络连接、并且将其状态通过D-BUS（是一个提供简单的应用程序 互相通讯的途径的自由软件项目，它是作为freedesktoporg项目的一部分来开发的。）进行报告的**后台服务**，以及一个**允许用户管理网络连接的客户端程序**。
+ NetworkManager是2004年RedHat启动的项目，旨在能够让Linux用户更轻松的处理现代网络需求，尤其是无线网络，能够自动发现网卡并配置IP地址。
+ **RHEL7上同时支持network.service和NetworkManager.service(简称NM)。默认情况下这2个服务都有开启，但是因为NetworkManager.service当时的兼容性不好，大部分人都会将其关闭。**
+ 但是在**RHEL 8/Centos 8上已废弃network.service（默认不安装），只能通过NetworkManager进行网络配置**。
+ NetworkManager主要管理2个对象： Connection（网卡连接配置） 和 Device（网卡设备），他们之间是多对一的关系，但是同一时刻只能有一个Connection对于Device才生效。
+ 在RHEL 8/Centos 8有三种方法配置网络
  + 通过nmcli connection add命令配置，会自动生成ifcfg文件
  + 手动配置ifcfg文件，通过nmcli connection reload来加载生效
  + 手动配置ifcfg文件，通过传统network.service来加载生效

### NetworkManager命令

nmcli命令是redhat7或者centos7之后的命令，该命令可以完成网卡上所有的配置工作，并且可以写入配置文件，永久生效

---

+ 语法

  ```bash
  [root@controller ~]# nmcli -h
  Usage: nmcli [OPTIONS] OBJECT { COMMAND | help }
  
  OPTIONS
    -o[verview]                                    overview mode (hide default values)
    -t[erse]                                       terse output
    -p[retty]                                      pretty output
    -m[ode] tabular|multiline                      output mode
    -c[olors] auto|yes|no                          whether to use colors in output
    -f[ields] <field1,field2,...>|all|common       specify fields to output
    -g[et-values] <field1,field2,...>|all|common   shortcut for -m tabular -t -f
    -e[scape] yes|no                               escape columns separators in values
    -a[sk]                                         ask for missing parameters
    -s[how-secrets]                                allow displaying passwords
    -w[ait] <seconds>                              set timeout waiting for finishing operations
    -v[ersion]                                     show program version
    -h[elp]                                        print this help
  
  OBJECT
    g[eneral]       NetworkManager's general status and operations
    n[etworking]    overall networking control
    r[adio]         NetworkManager radio switches
    c[onnection]    NetworkManager's connections
    d[evice]        devices managed by NetworkManager
    a[gent]         NetworkManager secret agent or polkit agent
    m[onitor]       monitor NetworkManager changes
  ```

  OBJECT和COMMAND可以用全称也可以用简称，最少可以只用一个字母，建议用头三个字母

  ---

+ device和connection

  + device叫网络接口，是物理设备

    ```bash
    [root@controller ~]# nmcli dev -h
    Usage: nmcli device { COMMAND | help }
    
    COMMAND := { status | show | set | connect | reapply | modify | disconnect | delete | monitor | wifi | lldp }
    
      status
    
      show [<ifname>]
    
      set [ifname] <ifname> [autoconnect yes|no] [managed yes|no]
    
      connect <ifname>
    
      reapply <ifname>
    
      modify <ifname> ([+|-]<setting>.<property> <value>)+
    
      disconnect <ifname> ...
    
      delete <ifname> ...
    
      monitor <ifname> ...
    
      wifi [list [ifname <ifname>] [bssid <BSSID>]]
    
      wifi connect <(B)SSID> [password <password>] [wep-key-type key|phrase] [ifname <ifname>]
                             [bssid <BSSID>] [name <name>] [private yes|no] [hidden yes|no]
    
      wifi hotspot [ifname <ifname>] [con-name <name>] [ssid <SSID>] [band a|bg] [channel <channel>] [password <password>]
    
      wifi rescan [ifname <ifname>] [[ssid <SSID to scan>] ...]
    
      lldp [list [ifname <ifname>]]
    ```

  + connection是连接，偏重于逻辑设置

    ```bash
    [root@controller ~]# nmcli con -h
    Usage: nmcli connection { COMMAND | help }
    
    COMMAND := { show | up | down | add | modify | clone | edit | delete | monitor | reload | load | import | export }
    
      show [--active] [--order <order spec>]
      show [--active] [id | uuid | path | apath] <ID> ...
    
      up [[id | uuid | path] <ID>] [ifname <ifname>] [ap <BSSID>] [passwd-file <file with passwords>]
    
      down [id | uuid | path | apath] <ID> ...
    
      add COMMON_OPTIONS TYPE_SPECIFIC_OPTIONS SLAVE_OPTIONS IP_OPTIONS [-- ([+|-]<setting>.<property> <value>)+]
    
      modify [--temporary] [id | uuid | path] <ID> ([+|-]<setting>.<property> <value>)+
    
      clone [--temporary] [id | uuid | path ] <ID> <new name>
    
      edit [id | uuid | path] <ID>
      edit [type <new_con_type>] [con-name <new_con_name>]
    
      delete [id | uuid | path] <ID>
    
      monitor [id | uuid | path] <ID> ...
    
      reload
    
      load <filename> [ <filename>... ]
    
      import [--temporary] type <type> file <file to import>
    
      export [id | uuid | path] <ID> [<output file>]
    ```

  +  多个connection可以应用到同一个device，但同一时间只能启用其中一个connection。这样的好处是针对一个网络接口，我们可以设置多个网络连接，比如静态IP和动态IP，再根据需要up相应connection

  ---

+ 网络连接管理

  nmcli connection

  偏重于逻辑设置

  + 显示连接

    + 显示所有连接

      ```bash
      nmcli con show
      ```

      ```bash
      [root@network network-scripts]# nmcli con show
      NAME                UUID                                  TYPE      DEVICE 
      em1                 a7f87045-9e56-4af1-a9b4-252678aa3920  ethernet  em1    
      em2                 a3b34706-0284-4818-8768-c70b0dcf2d5b  ethernet  em2    
      p6p1                ea2efdba-e254-417c-bffd-a1726cfd528b  ethernet  --     
      p6p2                dbf96d98-8cc3-43a3-bd65-c26f7c2adae9  ethernet  --     
      Wired connection 1  7d5bf18c-d796-3c7a-b83a-fc1235f02b8b  ethernet  --   
      ```

      + NAME : 网卡配置文件中定义的NAME内容，修改配置文件NAME项，可以更改名称，记得重启网卡（systemctl restart network）或重读配置文件（nmcli connection reload）

        “Wired connection 1”为一个有线连接，由于DEVICE选项为空，没有与网卡绑定，使其并未生效

    + 显示所有活动连接

      ```bash
      nmcli con show -active
      ```

    + 显示网络连接配置

      ```bash
      nmcli con show "Wired connection 1"
      ```

  + 创建连接

    **创建连接的意思，相当于在/etc/sysconfig/network-scripts/目录下创建了一个ifcfg-${con-name}文件，创建多个连接，则会同时创建多个文件**

    + 创建动态(DHCP)获取ip地址的连接

      ```bash
      nmcli con add con-name dhcp-em3 type ethernet ifname em3 autoconnect no
      ```

      + con-name : 创建连接的名字
      + type : 设备类型
      + ifname : 物理设备，网络接口
      + autoconnect ： 是否开机自启动

    + 创建静态ip地址连接

      ```bash
      nmcli con add con-name static-em3 type ethernet ifname em3 ip4 223.223.223.5/24 gw 223.223.223.1
      ```

    创建连接后，直接生成配置文件，但是网卡没有绑定，即，没有生效。需要启动连接

    ```bash
    nmcli con up static-em3
    ```

  + 修改连接

    | nmcli con mod                                       | 对应的配置文件参数                                       |
    | --------------------------------------------------- | -------------------------------------------------------- |
    | ipv4.method manual                                  | BOOTPROTO=none                                           |
    | ipv4.method auto                                    | BOOTPROTO=dhcp                                           |
    | connection.id eth0                                  | NAME=eth0                                                |
    | (ipv4.addresses<br/>“192.0.2.1/24<br/>192.0.2.254”) | IPADDR0=192.0.2.1<br/>PREFIX0=24<br/>GATEWAY=192.0.2.254 |
    | ipv4.dns 8.8.8.8                                    | DNS=8.8.8.8                                              |
    | pv4.dns-search example.com                          | DOMAIN=example.com                                       |
    | pv4.ignore-auto-dns true                            | PEERDNS=no                                               |
    | connection.autoconnect yes                          | ONBOOT=yes                                               |
    | connection.interface-name eth0                      | DEVICE=eth0                                              |
    | 802-3-ethernet.mac-address ...                      | HWADDR=...                                               |

    + 修改IP地址

      ```bash
      nmcli con mod static-em3 ip4 223.223.223.6/24
      ```

    + 修改IP地址时静态还是DHCP

      ```bash
      nmcli con mod static-em3 ip4.method manual|dhcp
      ```

    + 修改默认网关

      ```bash
      nmcli con mod static-em3 ip4.gateway 223.223.223.1
      ```

    + 修改IP地址以及网关

      ```bash
      nmcli con mod static-em3 ip4.addresses "223.223.223.6/24 223.223.223.1"
      ```

    + 修改连接是否为自启（默认自启）

      ```bash
      nmcli con mod static-em3 connection.autoconnect no
      ```

      检测

      ```bash
      grep ONBOOT /etc/sysconfig/network-scripts/ifcfg-static-em3
      ```

    + 修改连接dns

      ```bash
      nmcli con modify static-em3 ipv4.dns 114.114.114.114
      ```

    + 为连接添加dns**(添加其他的同理)**

      ```bash
      nmcli con modify static-em3 +ipv4.dns 114.114.114.114
      ```

    **修改连接后，需要重新激活连接方可生效**

    ```bash
    nmcli con up static-em3
    ```

  + 删除网络连接的配置文件

    ```bash
    nmcli con delete static-em3
    ```

  + 激活连接

    ```bash
    nmcli con up static-em3
    ```

  + 停用网络连接(可被自动激活)

    ```bash
    nmcli con down static-em3
    ```

  + 重新加载网络配置文件

    ```bash
    nmcli con reload
    ```

  + 启用/关闭所有的网络连接

    ```bash
    nmcli net on/off
    ```

  ---

+ 网络设备管理

  nmcli device

  + 显示设备

    + 显示所有设备

      ```bash
      nmcli dev show
      ```

    + 显示设备状态

      ```bash
      nmcli dev status
      ```

    + 显示指定网络设备属性

      ```bash
      nmcli dev show em3
      ```

  + 禁用网卡，防止被激活

    ```bash
    nmcli dev dis em3
    ```

    

  

### 