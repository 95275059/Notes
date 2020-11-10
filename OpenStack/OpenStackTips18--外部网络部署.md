# OpenStackTips18--外部网络部署

### 环境

+ Controller
  + eth0   192.168.100.10   租户网络
  + eth1   192.168.200.10   管理网络，API网络
  + eth2   192.168.1.1.233   外部网络

+ Compute (ovs)
  + eth0   192.168.100.20   租户网络
  + eth1   192.168.200.20   管理网络，API网络
+ Compute2 (linuxbridge)
  + eth0   192.168.100.21   租户网络
  + eth1   192.168.200.21   管理网络，API网络

### Linuxbridge

**具体参考每天五分钟OpenStackP296-300**

外部网络为flat类型

+ 配置Controller节点

  + vim /etc/neutron/plugins/ml2/ml2_conf.ini

    ```bash
    [ml2_type_flat]
    flat_networks = external
    ```

  + vim /etc/neutron/plugins/ml2/linuxbridge_agent.ini

    ```bash
    [linux_bridge]
    physical_interface_mappings = external:eth2
    ```

+ 创建外网ext_net

  | ext_net参数           |                    |
  | --------------------- | ------------------ |
  | Name                  | ext_net            |
  | Project               | admin              |
  | Provider Network Type | Flat               |
  | Physical Network      | external           |
  | Admin State           | up                 |
  | Shared                | :x:                |
  | External Network      | :heavy_check_mark: |

  | subnet_192_168_1_0参数 |                    |
  | ---------------------- | ------------------ |
  | Subnet Name            | subnet_192_168_1_0 |
  | Network Address        | 192.168.1.0/24     |
  | IP Version             | IPv4               |
  | Gateway IP             | 192.168.1.1        |
  | Disable Gateway        | :x:                |
  | Enable DHCP            | :x:                |

+ 将ext_net连接到router

  Set Gateway

  External Network : ext_net

+ 测试

  + 镜像：cirros

  + ping 114.114.114.114 可以ping通

  + DNS设置

    + vi /etc/resolv.conf(重启后失效)

      ```bash
      nameserver 114.114.114.114
      ```

    + 重启网卡

      ```bash
      ifdown eth0
      ifup eth0 
      ```

    + ping www.baidu.com 可以ping通

### Openvswitch

**具体参考每天五分钟OpenStackP404-408**

外部网络为flat类型

+ 创建br-ex网桥
  + ovs-vsctl add-br br-ex

+ 将eth2添加到br-ex网桥
  + ovs-vsctl add-port br-ex eth2

+ 配置Controller节点

  + vim /etc/neutron/plugins/ml2/ml2_conf.ini

    ```bash
    [ml2_type_flat]
    flat_networks = external
    ```

  + vim /etc/neutron/plugins/ml2/openvswitch_agent.ini

    ```bash
    [ovs]
    bridge_mappings = external:br-ex
    ```

+ 创建外网ext_net

  同linuxbridge步骤

+ 将ext_net连接到router

  同linuxbridge步骤

+ 测试

  同linuxbridge步骤



