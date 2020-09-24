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

+ 在另外一台机器上，使用ping命令，向当前机器发送报文

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

+ 实操

  ```bash
  [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
  Chain INPUT (policy ACCEPT 15 packets, 1096 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  2           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
  3           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  [root@promote ~]# iptables -t filter -D INPUT 2
  [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
  Chain INPUT (policy ACCEPT 6 packets, 428 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  2           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  [root@promote ~]# iptables -t filter -I INPUT 2 -s 192.168.200.4 -j DROP
  [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
  Chain INPUT (policy ACCEPT 6 packets, 428 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  2           0        0 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
  3           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0
  ```

---

### 删除规则

+ 两种方法
  + 根据规则的编号去删除规则
  + 根据具体的匹配条件与动作删除规则

##### 方法一：根据规则的编号去删除规则

+ ```bash
  iptables -t filter -D INPUT 3
  ```

  + -D : delete 删除指定链中的某条规则
  + -D INPUT 3 : 删除INPUT链中的第三条规则

+ 实操

  + 查看CentOS -1 iptables 

    ```bash
    [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
    Chain INPUT (policy ACCEPT 10 packets, 708 bytes)
    num      pkts      bytes target     prot opt in     out     source               destination         
    1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
    2           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
    3           0        0 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0
    ```

  + 删除INPUT链的第三条规则

    ```bash
    [root@promote ~]# iptables -t filter -D INPUT 3
    [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
    Chain INPUT (policy ACCEPT 6 packets, 428 bytes)
    num      pkts      bytes target     prot opt in     out     source               destination         
    1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
    2           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0 
    ```

##### 方法二：根据具体的匹配条件与动作删除规则

+ ```bash
  iptables -t filter -D INPUT -s 192.168.200.4 -j ACCEPT
  ```

  删除源地址为192.168.200.4，动作为ACCEPT的规则

+ 实操

  ```bash
  [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
  Chain INPUT (policy ACCEPT 6 packets, 428 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           4      336 ACCEPT     all  --  *      *       192.168.200.4        0.0.0.0/0           
  2           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0           
  [root@promote ~]# iptables -t filter -D INPUT -s 192.168.200.4 -j ACCEPT
  [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
  Chain INPUT (policy ACCEPT 10 packets, 692 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0 
  ```

##### 删除指定表表中某条链中的所有规则

```bash
iptables -t filter -F INPUT
```

+ -F : flush 冲刷指定的链，即删除指定链中的所有规则
+ 此规则相当于删除操作，在没有保存iptables规则的情况下，请慎用

##### 清空整个表中所有链的规则

```bash
iptables -t filter -F
```

+ 在没有保存iptables规则时，请勿随便清空链或者表中的规则，除非你明白你在干什么

---

### 修改规则

```bash
[root@promote ~]# iptables -t filter --line-number -nxvL INPUT
Chain INPUT (policy ACCEPT 10 packets, 692 bytes)
num      pkts      bytes target     prot opt in     out     source               destination         
1           8      672 DROP       all  --  *      *       192.168.200.4        0.0.0.0/0
```

##### 方法一：使用-R选项修改指定链中的规则

+ ```bash
  iptables -t filter -R INPUT 1 -s 192.168.200.4 -j REJECT
  ```

  + -R : 修改制定的链

  + -R INPUT 1 : 修改INPUT链的第一条规则

  + 注：-s选项以及对应的源地址不可省略，即使我们已经指定了规则对应的编号，**但是在使用-R选项修改某个规则时，必须指定规则对应的原本的匹配条件（如果有多个匹配条件，都需要指定）**

    如果上例中的命令没有使用-s指定对应规则中原本的源地址，那么在修改完成后，你修改的规则中的源地址会自动变为0.0.0.0/0（此IP表示匹配所有网段的IP地址），而此时，-j对应的动作又为REJECT，所以在执行上述命令时如果没有指明规则原本的源地址，那么所有IP的请求都被拒绝了（因为没有指定原本的源地址，当前规则的源地址自动变为0.0.0.0/0），如果你正在使用ssh远程到服务器上进行iptables设置，那么你的ssh请求也将会被阻断

+ 既然**使用-R选项修改规则时，必须指明规则原本的匹配条件**，那么我们则**可以理解为，只能通过-R选项修改规则对应的动作了**，所以我觉得，**如果你想要修改某条规则，还不如先将这条规则删除，然后在同样位置再插入一条新规则**，这样更好，当然，**如果你只是为了修改某条规则的动作，那么使用-R选项时，不要忘了指明规则原本对应的匹配条件**

+ 实操

  ```bash
  [root@promote ~]#  iptables -t filter -R INPUT 1 -s 192.168.200.4 -j REJECT
  [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
  Chain INPUT (policy ACCEPT 10 packets, 692 bytes)
  num      pkts      bytes target     prot opt in     out     source               destination         
  1           0        0 REJECT     all  --  *      *       192.168.200.4        0.0.0.0/0            reject-with icmp-port-unreachable
  ```

  + 在CentOS -2(192.168.200.4) ping CentOS -1(192.168.200.3)

    ```bash
    [root@promote ~]# ping -c 4 192.168.200.3
    PING 192.168.200.3 (192.168.200.3) 56(84) bytes of data.
    From 192.168.200.3 icmp_seq=1 Destination Port Unreachable
    From 192.168.200.3 icmp_seq=2 Destination Port Unreachable
    From 192.168.200.3 icmp_seq=3 Destination Port Unreachable
    From 192.168.200.3 icmp_seq=4 Destination Port Unreachable
    
    --- 192.168.200.3 ping statistics ---
    4 packets transmitted, 0 received, +4 errors, 100% packet loss, time 3002ms
    ```

    **REJECT 表示拒绝， DROP表示丢弃**

    **用REJECT，ping的时候是unreachable，目标不可达**

    **用DROP，ping的时候直接被丢包，没有返回**

  + 在CentOS -1上查看iptables规则

    ```bash
    [root@promote ~]# iptables -t filter --line-number -nxvL INPUT
    Chain INPUT (policy ACCEPT 15 packets, 1064 bytes)
    num      pkts      bytes target     prot opt in     out     source               destination         
    1           4      336 REJECT     all  --  *      *       192.168.200.4        0.0.0.0/0            reject-with icmp-port-unreachable
    ```

    可以看到，第一条规则匹配到了四个packet

##### 方法二：修改制定链的默认策略

+ 每张表的每条链中，都有自己的默认策略（动作）

+ 当报文没有被链中的任何规则匹配到时，或者，当链中没有任何规则时，防火墙会按照默认动作处理报文

+ 修改指定链的默认策略

  ```bash
  iptables -t filter -P FORWARD DROP
  ```

  + -P : 指定要修改的链
  + -P FORWARD DROP : 表示将表中FORWARD链的默认策略改为DROP

+ 实操

  ```bash
  [root@promote ~]# iptables -t filter -P FORWARD DROP
  [root@promote ~]# iptables -nvL
  Chain INPUT (policy ACCEPT 32 packets, 2112 bytes)
   pkts bytes target     prot opt in     out     source               destination         
      4   336 REJECT     all  --  *      *       192.168.200.4        0.0.0.0/0            reject-with icmp-port-unreachable
  
  Chain FORWARD (policy DROP 0 packets, 0 bytes)
   pkts bytes target     prot opt in     out     source               destination         
      0     0 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
      0     0 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0           
      0     0 FORWARD_direct  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FORWARD_IN_ZONES_SOURCE  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FORWARD_IN_ZONES  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FORWARD_OUT_ZONES_SOURCE  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FORWARD_OUT_ZONES  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID
      0     0 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            reject-with icmp-host-prohibited
  
  Chain OUTPUT (policy ACCEPT 17 packets, 1628 bytes)
   pkts bytes target     prot opt in     out     source               destination         
   1344  137K OUTPUT_direct  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
  
  Chain FORWARD_IN_ZONES (1 references)
   pkts bytes target     prot opt in     out     source               destination         
      0     0 FWDI_public  all  --  ens33  *       0.0.0.0/0            0.0.0.0/0           [goto] 
      0     0 FWDI_public  all  --  +      *       0.0.0.0/0            0.0.0.0/0           [goto] 
  
  Chain FORWARD_IN_ZONES_SOURCE (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FORWARD_OUT_ZONES (1 references)
   pkts bytes target     prot opt in     out     source               destination         
      0     0 FWDO_public  all  --  *      ens33   0.0.0.0/0            0.0.0.0/0           [goto] 
      0     0 FWDO_public  all  --  *      +       0.0.0.0/0            0.0.0.0/0           [goto] 
  
  Chain FORWARD_OUT_ZONES_SOURCE (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FORWARD_direct (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FWDI_public (2 references)
   pkts bytes target     prot opt in     out     source               destination         
      0     0 FWDI_public_log  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FWDI_public_deny  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FWDI_public_allow  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 ACCEPT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0           
  
  Chain FWDI_public_allow (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FWDI_public_deny (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FWDI_public_log (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FWDO_public (2 references)
   pkts bytes target     prot opt in     out     source               destination         
      0     0 FWDO_public_log  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FWDO_public_deny  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 FWDO_public_allow  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
  
  Chain FWDO_public_allow (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FWDO_public_deny (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain FWDO_public_log (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain INPUT_ZONES (0 references)
   pkts bytes target     prot opt in     out     source               destination         
      1    52 IN_public  all  --  ens33  *       0.0.0.0/0            0.0.0.0/0           [goto] 
      0     0 IN_public  all  --  +      *       0.0.0.0/0            0.0.0.0/0           [goto] 
  
  Chain INPUT_ZONES_SOURCE (0 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain INPUT_direct (0 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain IN_public (2 references)
   pkts bytes target     prot opt in     out     source               destination         
      1    52 IN_public_log  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      1    52 IN_public_deny  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      1    52 IN_public_allow  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      0     0 ACCEPT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0           
  
  Chain IN_public_allow (1 references)
   pkts bytes target     prot opt in     out     source               destination         
      1    52 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:22 ctstate NEW
  
  Chain IN_public_deny (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain IN_public_log (1 references)
   pkts bytes target     prot opt in     out     source               destination         
  
  Chain OUTPUT_direct (1 references)
   pkts bytes target     prot opt in     out     source               destination
  ```

---

### 保存规则

+ 在默认情况下，我们对防火墙所做的修改都是临时的，即，当重启iptables服务或者重启服务器以后，我们添加的规则或者对规则所做的修改都将消失。为了防止这种情况的发生，我们需要将规则保存

##### CentOS6

+ ```bash
  service iptables save
  ```

  规则默认保存在/etc/sysconfig/iptables文件汇总

+ 刚装完CentOS6时，刚打开使用iptables会发现filter表中会有一些默认的规则，这些默认提供的规则就保存在/etc/sysconfig/iptables中

+ ```bash
  service iptables restart
  ```

  重启iptables后，规则会再次回到上次保存在/etc/sysconfig/iptables文件中的样子

##### CentOS7

+ 不再使用init风格的脚本启动服务，而是使用unit文件

  所以，在centos7中已经不能再使用类似service iptables start这样的命令了，所以service iptables save也无法执行，

+ 在CentOS7中，用firewall替代了原来的iptables service

+ 安装iptables-services(iptables一般会被默认安装)

  ```bash
  yum install -y iptables-services
  ```

  ```bash
  #停止firewalld
  # systemctl stop firewalld
  #禁止firewalld自动启动
  # systemctl disable firewalld
  #启动iptables
  # systemctl start iptables
  #将iptables设置为开机自动启动，以后即可通过iptables-service控制iptables服务
  # systemctl enable iptables
  ```

##### 其他通用方法

+ 使用iptables-save命令

  使用iptables-save**并不能保存当前的iptables规则**，但是可以将当前的iptables规则以"保存后的格式"输出到屏幕上

+ 可以使用iptables-save命令，配合重定向，将规则重定向到/etc/sysconfig/iptables文件中即可

  ```bash
  iptables-save > /etc/sysconfig/iptables
  ```

##### 重新载入规则

+ 将/etc/sysconfig/iptables中的规则重新载入为当前的iptables规则

  ```bash
  iptables-restore < /etc/sysconfig/iptables
  ```

+ **未保存入/etc/sysconfig/iptables文件中的修改将会丢失或者被覆盖**

  













