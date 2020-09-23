# LinuxTips47--Iptables3-规则管理

### Iptables规则

+ **匹配条件**

  源IP，目的IP，源端口，目标端口等

+ **处理动作**在iptables中被称为target，动作也可以分为基本动作和扩展动作

  + 常用动作

    **ACCEPT**：允许数据包通过

    **DROP**：直接丢弃数据包，不给任何回应信息，这时候客户端会感觉自己的请求泥牛入海了，过了超时时间才会有反应

    **REJECT**：拒绝数据包通过，必要时会给数据发送端一个响应的信息，客户端刚请求就会收到拒绝的信息

    **SNAT**：源地址转换，解决内网用户用同一个公网地址上网的问题

    **MASQUERADE**：是SNAT的一种特殊形式，适用于动态的、临时会变的ip上

    **DNAT**：目标地址转换

    **REDIRECT**：在本机做端口映射

    **LOG**：在/var/log/messages文件中记录日志信息，然后将数据包传递给下一条规则，也就是说除了记录以外不对数据包做任何其他操作，仍然让下一条规则去匹配

### 实操准备（以filter表中的INPUT链为例）

+ 实操环境

  + 虚拟机CentOS -1：192.168.200.3（测试用机）

  + 虚拟机CentOS -2 ：192.168.200.4

+ 查看filter表中的INPUT链的规则

  ```bash
  [root@localhost ~]# iptables -t filter --line-number -vnxL INPUT
  Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1         961    80461 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
  2          97     7092 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0           
  3          26     5777 INPUT_direct  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
  4          26     5777 INPUT_ZONES_SOURCE  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
  5          26     5777 INPUT_ZONES  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
  6           0        0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID
  7          25     5725 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            reject-with icmp-host-prohibited
  ```

+ 清空filter表中的INPUT链的规则，以准备一个从零开始的环境来进行试验

  ```bash
  [root@localhost ~]# iptables -F INPUT
  [root@localhost ~]# iptables -t filter --line-number -vnxL INPUT
  Chain INPUT (policy ACCEPT 16 packets, 1124 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination
  ```

  清空INPUT链后，filter表中的INPUT链已经不存在任何规则，但是INPUT链的默认策略仍是ACCEPT。即，INPUT链默认“放行”所有发往本机的报文，当没有任何规则时，会接受所有报文，当报文没有被任何规则匹配到时，也会放行报文

+ 在另外一台机器上，使用ping命令，想当前机器发送报文

  ```bash
  [root@promote ~]# ping -c 4 192.168.200.3
  PING 192.168.200.3 (192.168.200.3) 56(84) bytes of data.
  64 bytes from 192.168.200.3: icmp_seq=1 ttl=64 time=0.363 ms
  64 bytes from 192.168.200.3: icmp_seq=2 ttl=64 time=2.85 ms
  64 bytes from 192.168.200.3: icmp_seq=3 ttl=64 time=1.20 ms
  64 bytes from 192.168.200.3: icmp_seq=4 ttl=64 time=0.305 ms
  
  --- 192.168.200.3 ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3004ms
  rtt min/avg/max/mdev = 0.305/1.182/2.854/1.029 ms
  ```

---

### 增加规则

##### 在CentOS -1(192.168.200.3)虚拟机上配置一条规则，拒绝CentOS -2(192.168.200.4)上所有报文访问

+ 匹配条件

  源地址：192.168.200.4

+ 动作

  拒绝报文

+ 命令

  ```bash
  iptables -t filter -I INPUT -s 192.168.200.4 -j DROP
  ```

  + -t : table 指定要操作的表
  + -I : insert 在指定链的首部插入规则
  + -s : source 指明匹配条件中的源地址
  + -j : 指明当匹配条件被满足时，所对应的动作(target)

+ 实操

  ```bash
  [root@localhost ~]# iptables -t filter -I INPUT -s 192.168.200.4 -j DROP
  [root@localhost ~]# iptables -t filter --line-number -nvxL INPUT
  Chain INPUT (policy ACCEPT 6 packets, 428 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           0        0 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0 
  ```

  + 在CentOS -2(192.168.200.4) ping CentOS -1(192.168.200.3)

    ```bash
    [root@promote ~]# ping -c 4 192.168.200.3
    PING 192.168.200.3 (192.168.200.3) 56(84) bytes of data.
    
    --- 192.168.200.3 ping statistics ---
    4 packets transmitted, 0 received, 100% packet loss, time 3002ms
    ```

  + 在CentOS -1上查看iptables规则

    ```bash
    [root@localhost ~]# iptables -t filter --line-number -nvxL INPUT
    Chain INPUT (policy ACCEPT 13 packets, 984 bytes)
    num      pkts      bytes target     prot opt in     out     source               destination         
    1           4      336 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0 
    ```

    可以见到，有四个packet已经被对应的该规则匹配到，总计大小336bytes

##### 在CentOS -1(192.168.200.3)虚拟机上追加一条规则，接受所有来自CentOS -2(192.168.200.4)的报文访问

+ 匹配条件

  源地址：192.168.200.4

+ 动作

  允许报文访问

+ 命令

  ```bash
  iptables -t filter -A INPUT -s 192.168.200.4 -j ACCEPT
  ```

  + -A : append 在对应链中追加规则

+ 实操

  ```bash
  [root@localhost ~]# iptables -t filter -A INPUT -s 192.168.200.4 -j ACCEPT
  [root@localhost ~]# iptables -t filter --line-number -nvxL INPUT
  Chain INPUT (policy ACCEPT 10 packets, 724 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           4      336 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
  2           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0
  ```

  + 在CentOS -2(192.168.200.4) ping CentOS -1(192.168.200.3)

    ```bash
    [root@promote ~]# ping -c 4 192.168.200.3
    PING 192.168.200.3 (192.168.200.3) 56(84) bytes of data.
    
    --- 192.168.200.3 ping statistics ---
    4 packets transmitted, 0 received, 100% packet loss, time 3000ms
    ```

    ping不通

  + 在CentOS -1上查看iptables规则

    ```bash
    [root@localhost ~]# iptables -t filter --line-number -nvxL INPUT
    Chain INPUT (policy ACCEPT 17 packets, 1264 bytes)
    num      pkts      bytes target     prot opt in     out     source               destination         
    1           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
    2           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0
    ```

    可以看到 第一条规则匹配到了8个packet，而第二条规则没有匹配到规则

    即，**规则是逐条执行，有顺序的**

##### 在CentOS -1(192.168.200.3)虚拟机上添加一条规则，接受所有来自CentOS -2(192.168.200.4)的报文访问，该新规则添加在链首部

+ 匹配条件

  源地址：192.168.200.4

+ 动作

  允许报文访问

+ 命令

  ```bash
  iptables -t filter -I INPUT -s 192.168.200.4 -j ACCEPT
  ```

+ 实操

  ```bash
  [root@localhost ~]# iptables -t filter --line-number -nvxL INPUT
  Chain INPUT (policy ACCEPT 6 packets, 428 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  2           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
  3           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0
  ```

  + 在CentOS -2(192.168.200.4) ping CentOS -1(192.168.200.3)

    ```bash
    [root@promote ~]# ping -c 4 192.168.200.3
    PING 192.168.200.3 (192.168.200.3) 56(84) bytes of data.
    64 bytes from 192.168.200.3: icmp_seq=1 ttl=64 time=0.319 ms
    64 bytes from 192.168.200.3: icmp_seq=2 ttl=64 time=0.504 ms
    64 bytes from 192.168.200.3: icmp_seq=3 ttl=64 time=0.423 ms
    64 bytes from 192.168.200.3: icmp_seq=4 ttl=64 time=0.342 ms
    
    --- 192.168.200.3 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3002ms
    rtt min/avg/max/mdev = 0.319/0.397/0.504/0.072 ms
    ```

    ping的通

  + 在CentOS -1上查看iptables规则

    ```bash
    [root@localhost ~]# iptables -t filter --line-number -nvxL INPUT
    Chain INPUT (policy ACCEPT 11 packets, 800 bytes)
    num      pkts      bytes target     prot opt in     out     source               destination         
    1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
    2           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
    3           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0
    ```

    第一条规则成功匹配到

    **iptables会对报文按照规则顺序执行对应的操作。即使后面的规则也能匹配到当前报文，但很有可能已经没有机会再对报文执行相应的动作了**

    该实验可以看出，报文先被第一条规则匹配到了，于是当前报文被"放行"了，因为报文已经被放行了，所以，即使上图中的第二条规则即使能够匹配到刚才"放行"的报文，也没有机会再对刚才的报文进行丢弃操作了。这就是iptables的工作机制。

##### 可以在添加规则时，指定新增规则的编号，这样可以在任意位置插入规则

```bash
iptables -t filter -I INPUT 2 -s 192.168.200.4 -j DROP
```

+ -I INPUT 2 表示在INPUT链中新增规则，新增的规则编号为2





