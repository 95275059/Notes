# OpenStackTips15--安装FWaaS

### 参考https://www.cnblogs.com/zhouxyuuuuu/p/6097584.html

### 安装FWaaS

```bash
yum -y install openstack-neutron-fwaas
```

### 添加FWaaS服务（控制节点）

+ vim /etc/neutron/neutron.conf

  ```bash
  [DEFAULT]
  service_plugins = router,firewall
  ```

### 配置FWaaS（网络节点）

+ vim /etc/neutron/fwaas_driver.ini

  ```bash
  [fwaas]
  driver = neutron_fwaas.services.firewall.drivers.linux.iptables_fwaas.IptablesFwaasDriver
  enabled = True
  ```

### Dashboard启用FWaaS

+ vim /usr/share/openstack-dashboard/openstack_dashboard/local/local_settings.py

  ```bash
OPENSTACK_NEUTRON_NETWORK = {
      ...
      'enable_firewall': True,
      ...
  }
  ```
  
  ```bash
  OPENSTACK_NEUTRON_NETWORK = {
      'enable_router': True,
      'enable_quotas': True,
      'enable_ipv6': True,
      'enable_distributed_router': False,
      'enable_ha_router': False,
      'enable_lb': True,
      'enable_firewall': True,
      'enable_vpn': True,
      'enable_fip_topology_check': True,
  
      # Neutron can be configured with a default Subnet Pool to be used for IPv4
      # subnet-allocation. Specify the label you wish to display in the Address
      # pool selector on the create subnet step if you want to use this feature.
      'default_ipv4_subnet_pool_label': None,
  
      # Neutron can be configured with a default Subnet Pool to be used for IPv6
      # subnet-allocation. Specify the label you wish to display in the Address
      # pool selector on the create subnet step if you want to use this feature.
      # You must set this to enable IPv6 Prefix Delegation in a PD-capable
      # environment.
      'default_ipv6_subnet_pool_label': None,
  
      # The profile_support option is used to detect if an external router can be
      # configured via the dashboard. When using specific plugins the
      # profile_support can be turned on if needed.
      'profile_support': None,
      #'profile_support': 'cisco',
  
      # Set which provider network types are supported. Only the network types
      # in this list will be available to choose from when creating a network.
      # Network types include local, flat, vlan, gre, and vxlan.
      'supported_provider_types': ['*'],
  
      # Set which VNIC types are supported for port binding. Only the VNIC
      # types in this list will be available to choose from when creating a
      # port.
      # VNIC types include 'normal', 'macvtap' and 'direct'.
      # Set to empty list or None to disable VNIC type selection.
      'supported_vnic_types': ['*'],
  }
  ```

+ ```bash
  systemctl restart httpd
  ```

### 数据库建表

```bash
neutron-db-manage --subproject neutron-fwaas upgrade head
```

### 重启服务

```bash
systemctl restart neutron-server.service
systemctl restart neutron-l3-agent.service
```



