# LinuxTips46--Iptables2-实操之规则查询

### 以filter表为例

+ filter表功能

  + 过滤功能

    允许哪些IP地址访问，拒绝哪些IP地址访问

    允许访问哪些端口，拒绝访问哪些端口

+ 查看表中规则

  + ```bash
    iptables -t filter -L
    ```

    + -t 指定表
    + -L : list 列出规则

  + ```bash
    iptables -t nat -L
    ```

  + ```bash
    ipatables -t mangle -L
    ```

  + ```bash
    iptables -t raw -L
    ```

  + ```bash
    iptables -L
    ```

    + iptables默认表为filter，该命令会列出filter表中的所有规则

  + 实操

    ```bash
    [root@localhost ~]# iptables -t filter -L
    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination         
    ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
    ACCEPT     all  --  anywhere             anywhere            
    INPUT_direct  all  --  anywhere             anywhere            
    INPUT_ZONES_SOURCE  all  --  anywhere             anywhere            
    INPUT_ZONES  all  --  anywhere             anywhere            
    DROP       all  --  anywhere             anywhere             ctstate INVALID
    REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited
    
    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination         
    ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
    ACCEPT     all  --  anywhere             anywhere            
    FORWARD_direct  all  --  anywhere             anywhere            
    FORWARD_IN_ZONES_SOURCE  all  --  anywhere             anywhere            
    FORWARD_IN_ZONES  all  --  anywhere             anywhere            
    FORWARD_OUT_ZONES_SOURCE  all  --  anywhere             anywhere            
    FORWARD_OUT_ZONES  all  --  anywhere             anywhere            
    DROP       all  --  anywhere             anywhere             ctstate INVALID
    REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited
    
    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination         
    OUTPUT_direct  all  --  anywhere             anywhere            
    
    Chain FORWARD_IN_ZONES (1 references)
    target     prot opt source               destination         
    FWDI_public  all  --  anywhere             anywhere            [goto] 
    FWDI_public  all  --  anywhere             anywhere            [goto] 
    
    Chain FORWARD_IN_ZONES_SOURCE (1 references)
    target     prot opt source               destination         
    
    Chain FORWARD_OUT_ZONES (1 references)
    target     prot opt source               destination         
    FWDO_public  all  --  anywhere             anywhere            [goto] 
    FWDO_public  all  --  anywhere             anywhere            [goto] 
    
    Chain FORWARD_OUT_ZONES_SOURCE (1 references)
    target     prot opt source               destination         
    
    Chain FORWARD_direct (1 references)
    target     prot opt source               destination         
    
    Chain FWDI_public (2 references)
    target     prot opt source               destination         
    FWDI_public_log  all  --  anywhere             anywhere            
    FWDI_public_deny  all  --  anywhere             anywhere            
    FWDI_public_allow  all  --  anywhere             anywhere            
    ACCEPT     icmp --  anywhere             anywhere            
    
    Chain FWDI_public_allow (1 references)
    target     prot opt source               destination         
    
    Chain FWDI_public_deny (1 references)
    target     prot opt source               destination         
    
    Chain FWDI_public_log (1 references)
    target     prot opt source               destination         
    
    Chain FWDO_public (2 references)
    target     prot opt source               destination         
    FWDO_public_log  all  --  anywhere             anywhere            
    FWDO_public_deny  all  --  anywhere             anywhere            
    FWDO_public_allow  all  --  anywhere             anywhere            
    
    Chain FWDO_public_allow (1 references)
    target     prot opt source               destination         
    
    Chain FWDO_public_deny (1 references)
    target     prot opt source               destination         
    
    Chain FWDO_public_log (1 references)
    target     prot opt source               destination         
    
    Chain INPUT_ZONES (1 references)
    target     prot opt source               destination         
    IN_public  all  --  anywhere             anywhere            [goto] 
    IN_public  all  --  anywhere             anywhere            [goto] 
    
    Chain INPUT_ZONES_SOURCE (1 references)
    target     prot opt source               destination         
    
    Chain INPUT_direct (1 references)
    target     prot opt source               destination         
    
    Chain IN_public (2 references)
    target     prot opt source               destination         
    IN_public_log  all  --  anywhere             anywhere            
    IN_public_deny  all  --  anywhere             anywhere            
    IN_public_allow  all  --  anywhere             anywhere            
    ACCEPT     icmp --  anywhere             anywhere            
    
    Chain IN_public_allow (1 references)
    target     prot opt source               destination         
    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh ctstate NEW
    
    Chain IN_public_deny (1 references)
    target     prot opt source               destination         
    
    Chain IN_public_log (1 references)
    target     prot opt source               destination         
    
    Chain OUTPUT_direct (1 references)
    target     prot opt source               destination     
    ```

    即：INPUT链、FORWARD链、OUTPUT链都拥有"过滤"的能力

    所以，当我们要定义某条"过滤"的规则时，我们会在filter表中定义

    但是具体在哪条"链"上定义规则则取决于我们的工作场景

    + 比如，我们需要禁止某个IP地址访问我们的主机，我们则需要在INPUT链上定义规则

      报文发往本机时，会经过PREROUTING链与INPUT链，所以，如果我们想要禁止某些报文发往本机，我们只能在PREROUTING链和INPUT链中定义规则，但是PREROUTING链并不存在于filter表中，换句话说就是，PREROUTING关卡天生就没有过滤的能力，所以，我们只能在INPUT链中定义

    + 如果是其他工作场景，可能需要在FORWARD链或者OUTPUT链中定义过滤规则

+ 查看表中某条链的规则

  + ```bash
    iptables -L INPUT
    ```

    + 实操

      ```bash
      [root@localhost ~]# iptables -L INPUT
      Chain INPUT (policy ACCEPT)
      target     prot opt source               destination         
      ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
      ACCEPT     all  --  anywhere             anywhere            
      INPUT_direct  all  --  anywhere             anywhere            
      INPUT_ZONES_SOURCE  all  --  anywhere             anywhere            
      INPUT_ZONES  all  --  anywhere             anywhere            
      DROP       all  --  anywhere             anywhere             ctstate INVALID
      REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited
      ```

  + ```bash
    iptables -vL INPUT
    ```

    + -v : 即verbose，查看更多更详细的信息

    + 实操

      ```bash
      [root@localhost ~]# iptables -vL INPUT
      Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
       pkts bytes target     prot opt in     out     source               destination         
        341 30168 ACCEPT     all  --  any    any     anywhere             anywhere             ctstate RELATED,ESTABLISHED
         97  7092 ACCEPT     all  --  lo     any     anywhere             anywhere            
          2   281 INPUT_direct  all  --  any    any     anywhere             anywhere            
          2   281 INPUT_ZONES_SOURCE  all  --  any    any     anywhere             anywhere            
          2   281 INPUT_ZONES  all  --  any    any     anywhere             anywhere            
          0     0 DROP       all  --  any    any     anywhere             anywhere             ctstate INVALID
          1   229 REJECT     all  --  any    any     anywhere             anywhere             reject-with icmp-host-prohibited
      ```

      + 规则属性

        + pkts : 对应规则匹配到的报文的个数
        + bytes : 对应规则匹配到的报文包的大小总和
        + target : 规则对应的target，往往表示规则对应的动作，即规则匹配成功后需要采取的规则
        + prot : 表示规则对应的协议，是否只针对某些协议应用此规则
        + opt : option 表示规则对应的选项
        + in : 表示数据包由哪个接口（网卡）流入，我们可以设置通过哪块网卡流入的报文需要匹配当前规则
        + out : 表示数据包由哪个接口（网卡）流出，我们可以设置通过哪块网卡流出的报文需要匹配当前规则
        + source : 表示规则对应的源头地址，可以是一个IP，也可以是一个网段
        + destination : 表示规则对应的目标地址，可以是一个IP，也可以是一个网段

      + iptables默认进行了地址解析，但是在规则非常多的情况下如果进行名称解析，效率会比较低，所以，在没有此需求的情况下，可以使用-n选项，表示不对IP地址进行名称反解，直接显示IP地址

      + **(policy ACCEPT 0 packets, 0 bytes)**

        + policy : 当前链的默认策略

          + policy ACCEPT表示INPUT链的默认动作为ACCEPT，也就是说，默认接受通过INPUT链的所有请求

            所以在配置INPUT链的具体规则时，应该将需要拒绝的请求配置到规则中，即‘黑名单机制’。默认所有人都能通过，只有指定的人不能通过

        + packets : 当前链默认策略匹配到的包的数量，0 packets表示默认策略匹配到0个包

        + bytes : 表示当前链默认策略匹配到的所有包的大小总和

        + 可以把pckets和bytes称作‘计数器’，计数器只会在使用-v选项时才会显示出来

        + 当被匹配到的包达到一定数量时，计数器会自动将匹配到的包的大小转换为可读性较高的单位

        + 如果想查看精确的计数值，而不是经过可读性优化过的计数值，则可以使用**-x选项**，表示显示精确的计数值

          ```bash
          iptables -vxL INPUT
          ```

        + 每张表中的每条链都有自己的计数器，链中的每个规则也都有自己的计数器，就是每条规则对应的pkts字段与bytes字段的信息

  + ```bash
    iptables -nvL INPUT
    ```

    + -n : numeric 不对IP地址进行名称反解，直接显示IP地址

    + 实操

      ```bash
      [root@localhost ~]# iptables -nvL INPUT
      Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
       pkts bytes target     prot opt in     out     source               destination         
        421 36028 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
         97  7092 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0           
          4   739 INPUT_direct  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
          4   739 INPUT_ZONES_SOURCE  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
          4   739 INPUT_ZONES  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
          0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID
          3   687 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            reject-with icmp-host-prohibited
      ```

  + ```bash
    iptables --line-number -nvL INPUT
    ```

    + --line-number显示规则编号

      --line-number选项并没有对应的短选项

      centos中的iptables可以识别--line

      此选项为长选项，不能与其他短选项合并，不过此选项可以在centos中简写为--line，注意，简写后仍然是两条横杠，仍然是长选项

    + 实操

      ```bash
      [root@localhost ~]# iptables --line-number -nvL INPUT
      Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
      num   pkts bytes target     prot opt in     out     source               destination         
      1      539 44662 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
      2       97  7092 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0           
      3        5   968 INPUT_direct  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      4        5   968 INPUT_ZONES_SOURCE  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      5        5   968 INPUT_ZONES  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
      6        0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID
      7        4   916 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            reject-with icmp-host-prohibited
      ```

    

  