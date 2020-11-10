# OpenStackTips19--OVS 下 vxlan或gre配置

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

### 具体参考每天五分钟OpenStack P411-413

### 在ML2配置中enable vxlan network

+ 控制节点

  + vim /etc/neutron/plugins/ml2/ml2_conf.ini

    ```bash
    [DEFAULT]
    ...
    tenant_network_types = gre,vxlan
    extension_drivers = port_security
    type_drivers = local,flat,vlan,gre,vxlan
    mechanism_drivers = l2population,openvswitch
    ...
    [ml2_type_vxlan]
    vni_ranges = 1001:2000(指定普通用户在自己组合里创建vxlan network的范围)
    ```

  + vim /etc/neutron/plugins/ml2/openvswitch_agent.ini

    ```bash
    [agent]
    ...
    tunnel_types = vxlan,gre
    l2_population = true
    ...
    [ovs]
    tunnel_bridge = br-tun
    bridge_mappings = external:br-ex(部署外部网络用)
    local_ip = 192.168.100.10(租户网络)
    ```

+ 计算节点

  + vim /etc/neutron/plugins/ml2/openvswitch_agent.ini

    ```bash
    [agent]
    ...
    tunnel_types = vxlan,gre
    l2_population = true
    ...
    [ovs]
    tunnel_bridge = br-tun
    bridge_mappings = 
    local_ip = 192.168.100.20(租户网络)
    ```

    