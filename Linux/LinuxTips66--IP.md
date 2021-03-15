# LinuxTips66--IP

### 功能

ip 命令与ifconfig命令类似，但比 ifconfig 命令更加强大，主要功能是用于显示或设置网络设备。

ip 命令是 Linux 加强版的的网络配置工具，用于代替 ifconfig 命令。

---

### 语法

```bash
ip [OPTIONS] OBJECT {COMMAND | help}
```

+ OBJECT为常用对象，值可以是以下几种：

  ```bash
  OBJECT={ link | addr | addrlabel | route | rule | neigh | ntable | tunnel | maddr | mroute | mrule | monitor | xfrm | token }
  ```
  + link : 网络设备
  + address : 设备上的协议（IP或IPv6）地址
  + addrlabel : 协议地址选择的标签配置
  + route : 路由表条目
  + rule : 路由策略数据库中的规则

+ OPTIONS常用选项，值可以是以下几种：

  ```bash
  OPTIONS={ -V[ersion] | -s[tatistics] | -d[etails] | -r[esolve] | -h[uman-readable] | -iec | -f[amily] { inet | inet6 | ipx | dnet | link } | -o[neline] | -t[imestamp] | -b[atch] [filename] | -rc[vbuf] [size] }
  ```

  + 常用选项的取值含义如下：
    + -V：显示命令的版本信息；
    + -s：输出更详细的信息；
    + -f：强制使用指定的协议族；
    + -4：指定使用的网络层协议是IPv4协议；
    + -6：指定使用的网络层协议是IPv6协议；
    + -0：输出信息每条记录输出一行，即使内容较多也不换行显示；
    + -r：显示主机时，不使用IP地址，而使用主机的域名。
    + help 为该命令的帮助信息。

---

### ip link

+ ```bash
  ip link show
  ```

  显示网络接口信息

+ ```shell
  ip link ls dev_name
  ```

  查看某块网卡信息。另外添加-s选项可以显示更加详细的信息

+ ```bash
  ip link set eth0 up/down
  ```

  开启/关闭网卡

+ ```bash
  ip link set eth0 promisc on/off
  ```

  开启/关闭网卡的混合模式

+ ```bash
  ip link set eth0 txqueuelen 1200
  ```

  设置网卡队列长度

+ ```bash
  ip link set eth0 mtu 1400
  ```

  设置网卡最大传输单元

---

### ip addr

+ ```bash
  ip addr show
  ```

  显示网卡IP信息

+ ```bash
  ip addr add/del 192.168.0.1/24 dev eth0 
  ```

  设置/删除eth0网卡的IP地址

---

### ip route

+ ```bash
  ip route show
  ```

  显示系统路由

+ ```设置系统默认路由
  ip route add default via 192.168.0.254
  ```

  设置系统默认路由

+ ```bash
  ip route list
  ```

  查看路由信息

+ ```bash
  ip route add 192.168.4.0/24 via 192.168.0.254 dev eth0
  ```

  设置192.168.4.0网段的网关为192.168.0.254,数据走eth0接口

+ ```bash
  ip route add default via  192.168.0.254  dev eth0
  ```

  设置默认网关为192.168.0.254

+ ```bash
  ip route del 192.168.4.0/24
  ```

  删除192.168.4.0网段的网关

+ ```bash
  ip route delete 192.168.1.0/24 dev eth0 
  ```

  删除路由





