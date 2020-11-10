# OpenStack安装总结6--多计算节点不同provider环境下neutron配置

### 参考

https://docs.openstack.org/mitaka/install-guide-rdo/

https://www.cnblogs.com/zhijian1574/tag/OpenStack/

### 环境说明

+ 网络环境
+ 管理网络/外部网络/API网络 : 192.168.200.0/24
+ 租户网络 : 192.168.100.0/24
+ 节点构成
  + 控制节点controller
    + eth1 : 192.168.200.10
    
      VMnet8 Nat模式，网关192.168.200.2 
    
    + eth0 : 192.168.100.10(租户网络)
    
      VMnet1 仅主机模式
    
    + eth2 : 192.168.1.233(外部网络)
    
      VMnet0 桥接模式，桥接到192.168.1.0/24对应的网卡上
  + 计算节点compute
    + eth1 : 192.168.200.20
    
      VMnet8 Nat模式，网关192.168.200.2 
    
    + eth0 : 192.168.100.20
    
      VMnet1 仅主机模式
  + 计算节点compute2
    + eth1 : 192.168.200.21
    
      VMnet8 Nat模式，网关192.168.200.2 
    
    + eth0 : 192.168.100.21
    
      VMnet1 仅主机模式

---

### 控制节点

+ 数据库相关操作按官方文档来

  https://docs.openstack.org/mitaka/install-guide-rdo/neutron-controller-install.html

  Prerequisites部分

+ 安装组件

  ```bash
  yum install openstack-neutron openstack-neutron-ml2 python-neutronclient which openstack-neutron-linuxbridge ebtables openstack-neutron-openvswitch
  ```

+ Configure the server component

+ Configure the Modular Layer 2 (ML2) plug-in

  The ML2 plug-in uses the Linux bridge ==and OVS== mechanism to build layer-2 (bridging and switching) virtual networking infrastructure for instances.

  + Edit the `/etc/neutron/plugins/ml2/ml2_conf.ini` file and complete the following actions

    + ==In the `[ml2]` section, enable flat, VLAN, and VXLAN networks==

      ```bash
      [ml2]
      ...
      type_drivers = flat,vlan,vxlan,gre
      ```

    + ==In the `[ml2]` section, enable VXLAN self-service networks==

      ```bash
      [ml2]
      ...
      tenant_network_types = vxlan,gre
      ```

    + ==In the `[ml2]` section, enable the Linux bridge and layer-2 population mechanisms==

      ```bash
      [ml2]
      ...
      mechanism_drivers = linuxbridge,openvswitch,l2population
      ```

    + In the `[ml2]` section, enable the port security extension driver

      ```bash
      [ml2]
      ...
      extension_drivers = port_security
      ```

    + In the `[ml2_type_flat]` section, configure the provider virtual network as a flat network

      ```bash
      [ml2_type_flat]
      ...
      flat_networks = provider
      ```

    + In the `[ml2_type_vxlan]` section, configure the VXLAN network identifier range for self-service networks

      ```bash
      [ml2_type_vxlan]
      ...
      vni_ranges = 1:1000
      ```

    + In the `[ml2_type_gre]` section, configure the gre network identifier range for self-service networks

      ```bash
      [ml2_type_gre]
      ...
      tunnel_id_ranges = 1:1000
      ```

    + In the `[securitygroup]` section, enable [*ipset*](https://docs.openstack.org/mitaka/install-guide-rdo/common/glossary.html#term-ipset) to increase efficiency of security group rules

      ```bash
      [securitygroup]
      ...
      enable_ipset = True
      ```

+ Configure the Linux bridge agent

  The Linux bridge agent builds layer-2 (bridging and switching) virtual networking infrastructure for instances and handles security groups.

  + Edit the `/etc/neutron/plugins/ml2/linuxbridge_agent.ini` file and complete the following actions

    + In the `[linux_bridge]` section, map the provider virtual network to the provider physical network interface

      ```bash
      [linux_bridge]
      physical_interface_mappings = provider:PROVIDER_INTERFACE_NAME
      ```

      Replace `PROVIDER_INTERFACE_NAME` with the name of the underlying provider physical network interface.

      See [*Host networking*](https://docs.openstack.org/mitaka/install-guide-rdo/environment-networking.html#environment-networking) for more information.

      ==即处于租户网络的eth0==

    + In the `[vxlan]` section, enable VXLAN overlay networks, configure the IP address of the physical network interface that handles overlay networks, and enable layer-2 population

      ```bash
      [vxlan]
      enable_vxlan = True
      local_ip = OVERLAY_INTERFACE_IP_ADDRESS
      l2_population = True
      ```

      ==即处于租户网络的192.168.100.10==

    + In the `[securitygroup]` section, enable security groups and configure the Linux bridge [*iptables*](https://docs.openstack.org/mitaka/install-guide-rdo/common/glossary.html#term-iptables) firewall driver

      ```bash
  [securitygroup]
      ...
  enable_security_group = True
      firewall_driver = neutron.agent.linux.iptables_firewall.IptablesFirewallDriver
      ```
  
+ Configure the openvswitch agent

  + 编辑 **/etc/neutron/plugins/ml2/openvswitch_agent.ini**文件

    ```bash
    [ovs]
    ...
    local_ip = TUNNEL_INTERFACE_IP_ADDRESS
    bridge_mappings = provider:br-ex
    
    [agent]
    ...
    tunnel_types = gre
    l2_population = true
    prevent_arp_spoofing = true
    
    [securitygroup]
    ...
    enable_security_group = true
    firewall_driver=neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver
    ```

    替换**TUNNEL_INTERFACE_IP_ADDRESS**为用于隧道网的网卡地址
  
    ==(即，处于租户网络的192.168.100.10)==

+ Configure the layer-3 agent

  + 按照官方文档来

  + 但只能对应一种network provider

    [DEFAULT] section的interface_driver是最重要的配置选项，用来指定mechanism driver，neutron支持三种interface_driver，具体配置项如下：

    + 使用openvswitch

      ```bash
    [DEFAULT]
      interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver
    external_network_bridge = br-ex
      ```

    + 使用linuxbridge

      ```bash
      [DEFAULT]
      interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver
      external_network_bridge = br-ex
      ```
    
    + 使用null
    
      interface_driver = neutron.agent.linux.interface.NullDriver

+ Configure the DHCP agent

  + 按照官方文档来
  
  + 但只能对应一种network provider，同layer-3 agent的对于interface_driver的配置方案一样
  
    + 使用openvswitch
  
      ```bash
      [DEFAULT]
      ...
      interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver
      dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
      enable_isolated_metadata = True
      ```
  
    + 使用linuxbridge
  
      ```bash
      [DEFAULT]
      ...
      interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver
      dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
      enable_isolated_metadata = True
      ```

+ **关于OVS和linuxbirdge之间的切换**

  各个计算节点的配置不用变，但是网络节点的DHCP和L3层服务都需要切换driver

  然后重启neutron-dhcp-agent和neutron-l3-agent即可

  如果是多网络节点，一个网络节点driver为linuxbridge，一个网络节点driver为openvswitch。就不用切换了吧（猜测）

---

### 计算节点

+ 根据计算节点加载的network provider进行不同的安装

+ 若加载linux bridge，根据官方文档来

  https://docs.openstack.org/mitaka/install-guide-rdo/neutron-compute-install.html

+ 若加载ovs，根据操作文档《OpenStack,M版安装过程，OVS》来











