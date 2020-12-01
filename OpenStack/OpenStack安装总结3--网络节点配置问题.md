# OpenStack安装总结3--网络节点配置问题

### 三节点（控制，网络，计算）

控制节点一个网卡；管理网卡

网络节点两个网卡；外部网卡，管理网卡

计算节点两个网卡；外部网卡，管理网卡

---

### 控制节点

  + 数据库

    + mysql -u root -p

    + ```shell
      CREATE DATABASE neutron;
      ```

    + ```shell
      GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' IDENTIFIED BY 'NEUTRON_DBPASS';
      > GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' IDENTIFIED BY 'NEUTRON_DBPASS';
      ```

  + 创建neutron用户、分配admin权限、创建neutron服务实体

    ```shell
    $ source admin-openrc
    ```

    ```shell
    $ openstack user create --domain default --password-prompt neutron
    User Password:
    Repeat User Password:
    +-----------+----------------------------------+
    | Field     | Value                            |
    +-----------+----------------------------------+
    | domain_id | e0353a670a9e496da891347c589539e9 |
    | enabled   | True                             |
    | id        | b20a6692f77b4258926881bf831eb683 |
    | name      | neutron                          |
    +-----------+----------------------------------+
    ```

    ```shell
    $ openstack role add --project service --user neutron admin
    ```

    ```shell
    $ openstack service create --name neutron --description "OpenStack Networking" network
    +-------------+----------------------------------+
    | Field       | Value                            |
    +-------------+----------------------------------+
    | description | OpenStack Networking             |
    | enabled     | True                             |
    | id          | f71529314dab4a4d8eca427e701d209e |
    | name        | neutron                          |
    | type        | network                          |
    +-------------+----------------------------------+
    ```

  + 创建neutron服务API endpoints

    ```shell
    $ openstack endpoint create --region RegionOne network public http://controller:9696
    +--------------+----------------------------------+
    | Field        | Value                            |
    +--------------+----------------------------------+
    | enabled      | True                             |
    | id           | 85d80a6d02fc4b7683f611d7fc1493a3 |
    | interface    | public                           |
    | region       | RegionOne                        |
    | region_id    | RegionOne                        |
    | service_id   | f71529314dab4a4d8eca427e701d209e |
    | service_name | neutron                          |
    | service_type | network                          |
    | url          | http://controller:9696           |
    +--------------+----------------------------------+
    ```

    ```shell
    $ openstack endpoint create --region RegionOne network internal http://controller:9696
    +--------------+----------------------------------+
    | Field        | Value                            |
    +--------------+----------------------------------+
    | enabled      | True                             |
    | id           | 09753b537ac74422a68d2d791cf3714f |
    | interface    | internal                         |
    | region       | RegionOne                        |
    | region_id    | RegionOne                        |
    | service_id   | f71529314dab4a4d8eca427e701d209e |
    | service_name | neutron                          |
    | service_type | network                          |
    | url          | http://controller:9696           |
    +--------------+----------------------------------+
    ```

    ```shell
    $ openstack endpoint create --region RegionOne network admin http://controller:9696
    +--------------+----------------------------------+
    | Field        | Value                            |
    +--------------+----------------------------------+
    | enabled      | True                             |
    | id           | 1ee14289c9374dffb5db92a5c112fc4e |
    | interface    | admin                            |
    | region       | RegionOne                        |
    | region_id    | RegionOne                        |
    | service_id   | f71529314dab4a4d8eca427e701d209e |
    | service_name | neutron                          |
    | service_type | network                          |
    | url          | http://controller:9696           |
    +--------------+----------------------------------+
    ```

  + 安装组件

    openstack-neutron 

    openstack-neutron-ml2 

    python-neutronclient

    ```shell
    # yum install openstack-neutron openstack-neutron-ml2 python-neutronclient which ebtables
    ```

  + 编辑/etc/neutron/neutron.conf

    ```shell
    [DEFAULT]
    ...
    core_plugin = ml2
    service_plugins = router
    allow_overlapping_ips = True
    rpc_backend = rabbit
    auth_strategy = keystone
    notify_nova_on_port_status_changes = True
    notify_nova_on_port_data_changes = True
    
    [database]
    ...
    connection = mysql+pymysql://neutron:NEUTRON_DBPASS@controller/neutron
    
    [oslo_messaging_rabbit]
    ...
    rabbit_host = controller
    rabbit_userid = openstack
    rabbit_password = RABBIT_PASS
    
    [keystone_authtoken]
    ...
    auth_uri = http://controller:5000
    auth_url = http://controller:35357
    memcached_servers = controller:11211
    auth_type = password
    project_domain_name = default
    user_domain_name = default
    project_name = service
    username = neutron
    password = NEUTRON_PASS
    
    [nova]
    ...
    auth_url = http://controller:35357
    auth_type = password
    project_domain_name = default
    user_domain_name = default
    region_name = RegionOne
    project_name = service
    username = nova
    password = NOVA_PASS
    
    [oslo_concurrency]
    ...
    lock_path = /var/lib/neutron/tmp
    ```

  + 编辑 /etc/neutron/plugins/ml2/ml2_conf.ini

    ```shell
    [ml2]
    ...
    type_drivers = flat,vlan,gre,vxlan
    tenant_network_types = gre
    mechanism_drivers = openvswitch,l2population
    extension_drivers = port_security
    
    [ml2_type_flat]
    ...
    flat_networks = provider
    
    [ml2_type_gre]
    ...
    tunnel_id_ranges = 1:200000
    
    [securitygroup]
    ...
    enable_ipset = True
    ```

  + 编辑 /etc/nova/nova.conf

    ```shell
    [neutron]
    ...
    url = http://controller:9696
    auth_url = http://controller:35357
    auth_type = password
    project_domain_name = default
    user_domain_name = default
    region_name = RegionOne
    project_name = service
    username = neutron
    password = NEUTRON_PASS
    
    service_metadata_proxy = True
    metadata_proxy_shared_secret = METADATA_SECRET
    ```

  + 创建链接

    ```shell
    # ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini
    ```

  + 同步数据库

    ```shell
    # su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron
    ```

  + 重启nova服务

    ```shell
    # systemctl restart openstack-nova-api.service
    ```

  + 启动neutron-server服务

    ```shell
    # systemctl enable neutron-server.service
    # systemctl start neutron-server.service
    ```

---

### 网络节点

  + 安装组件

    ```shell
    # yum install openstack-neutron openstack-neutron-ml2 openstack-neutron-openvswitch
    ```

  + 配置/etc/neutron/neutron.conf   

    ```shell
    [DEFAULT]
    ...
    core_plugin = ml2
    service_plugins = router
    allow_overlapping_ips = True
    rpc_backend = rabbit
    auth_strategy = keystone
    
    [oslo_messaging_rabbit]
    ...
    rabbit_host = controller
    rabbit_userid = openstack
    rabbit_password = RABBIT_PASS
    
    [keystone_authtoken]
    ...
    auth_uri = http://controller:5000
    auth_url = http://controller:35357
    memcached_servers = controller:11211
    auth_type = password
    project_domain_name = default
    user_domain_name = default
    project_name = service
    username = neutron
    password = NEUTRON_PASS
    
    [oslo_concurrency]
    lock_path = /var/lib/neutron/tmp
    ```

    和控制节点一样，只是在[DEFAULT]少了最后两行

  + 配置 /etc/neutron/plugins/ml2/ml2_conf.ini

    ```shell
    [ml2]
    ...
    type_drivers = flat,vlan,gre,vxlan(11无，211有)
    tenant_network_types = gre(11无，211有)
    mechanism_drivers = openvswitch,l2population
    extension_drivers = port_security(11无，211有)
    
    [ml2_type_flat]
    ...
    flat_networks = provider(11无，211有)
    
    [ml2_type_gre]
    ...
    tunnel_id_ranges = 1:1000(11无，211有)
    
    [securitygroup]
    ...
    enable_ipset = true(11无，211有)
    ```

    和控制节点一样

    计算节点不配置这个文件

  + 配置/etc/neutron/plugins/ml2/openvswitch.ini

    ```
    [ovs]
    local_ip = TUNNEL_INTERFACE_IP_ADDRESS
    bridge_mappings = provider:br-ex
    
    [agent]
    tunnel_types = gre
    l2_population = true
    prevent_arp_spoofing = true
    
    [securitygroup]
    enable_security_group = true
    firewall_driver=neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver
    ```

    TUNNEL_INTERFACE_IP_ADDRESS : 该节点的租户网络

  + 配置/etc/neutron/l3_agent.ini

    ```shell
    [DEFAULT]
    ...
    interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver
    external_network_bridge = br-ex
    ```

  + 配置/etc/neutron/dhcp_agent.ini

    ```shell
    [DEFAULT]
    ...
    interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver
    dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
    enable_isolated_metadata = true
    ```

  + 配置 /etc/neutron/metadata_agent.ini

    ```shell
    [DEFAULT]
    ...
    nova_metadata_ip = controller
    metadata_proxy_shared_secret = METADATA_SECRET
    ```
    
     METADATA_SECRET：替换为metadata proxy密码
         

  + 创建链接

    ```shell
    ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini
    ```

  + 创建网桥

    ```shell
    # systemctl enable openvswitch.service
    # systemctl start openvswitch.service
      
    # ovs-vsctl add-br br-ex
    #ovs-vsctl add-port br-ex INTERFACE_NAME(enp4s0f1)(此步骤暂时不加，是基于双网卡配置)
    ```

       INTERFACE_NAME 为用于外部网络的网卡名

     + 启动各项服务

       ```shell
       # systemctl start neutron-openvswitch-agent.service neutron-l3-agent.service neutron-dhcp-agent.service neutron-metadata-agent.service
       # systemctl enable neutron-openvswitch-agent.service neutron-l3-agent.service neutron-dhcp-agent.service neutron-metadata-agent.service
       ```
---

### 计算节点

+ 安装组件

  ```bash
  yum install openstack-neutron openstack-neutron-ml2 openstack-neutron-openvswitch
  ```

+ 配置/etc/neutron/neutron.conf

  ```shell
  [DEFAULT]
  ...
  rpc_backend = rabbit
  auth_strategy = keystone
  
  [oslo_messaging_rabbit]
  rabbit_host = controller （controller的管理网络IP）
  rabbit_userid = openstack
  rabbit_password = RABBIT_PASS
  
  [keystone_authtoken]
  ...
  auth_uri = http://controller:5000
  auth_url = http://controller:35357
  memcached_servers = controller:11211
  auth_type = password
  project_domain_name = default
  user_domain_name = default
  project_name = service
  username = neutron
  password = NEUTRON_PASS
  
  [oslo_concurrency]
  ...
  lock_path = /var/lib/neutron/tmp
  ```

  将[DEFAULT]中的关于连接数据库部分都注释掉！！！

 + 配置/etc/neutron/plugins/ml2/openvswitch_agent.ini
   
   ```shell
[ovs]
   ...
local_ip = TUNNEL_INTERFACE_IP_ADDRESS
   
   [agent]
   ...
   tunnel_types = gre
   l2_population = true
   
   [securitygroup]
   ...
   firewall_driver = neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver
   enable_security_group = true
   ```
   
   TUNNEL_INTERFACE_IP_ADDRESS : 该节点的租户网络
   
 + 配置/etc/nova/nova.conf
   
   ```shell
[neutron]
   ...
url = http://controller:9696
   auth_url = http://controller:35357
auth_type = password
   project_domain_name = default
   user_domain_name = default
   region_name = RegionOne
   project_name = service
   username = neutron
   password = NEUTRON_PASS
   ```

 + 启用各项服务
   
   ```shell
   # systemctl restart openstack-nova-compute.service
   # systemctl enable neutron-openvswitch-agent.service
   # systemctl start neutron-openvswitch-agent.service
   ```
+ 验证是否安装成功

  ```shell
  source admin-openrc
  $ neutron ext-list
 +---------------------------+-----------------------------------------------+
  | alias                     | name                                          |
 +---------------------------+-----------------------------------------------+
  | default-subnetpools       | Default Subnetpools                           |
  | network-ip-availability   | Network IP Availability                       |
  | network_availability_zone | Network Availability Zone                     |
  | auto-allocated-topology   | Auto Allocated Topology Services              |
  | ext-gw-mode               | Neutron L3 Configurable external gateway mode |
  | binding                   | Port Binding                                  |
  | agent                     | agent                                         |
  | subnet_allocation         | Subnet Allocation                             |
  | l3_agent_scheduler        | L3 Agent Scheduler                            |
  | tag                       | Tag support                                   |
  | external-net              | Neutron external network                      |
  | net-mtu                   | Network MTU                                   |
  | availability_zone         | Availability Zone                             |
  | quotas                    | Quota management support                      |
  | l3-ha                     | HA Router extension                           |
  | provider                  | Provider Network                              |
  | multi-provider            | Multi Provider Network                        |
  | address-scope             | Address scope                                 |
  | extraroute                | Neutron Extra Route                           |
  | timestamp_core            | Time Stamp Fields addition for core resources |
  | router                    | Neutron L3 Router                             |
  | extra_dhcp_opt            | Neutron Extra DHCP opts                       |
  | dns-integration           | DNS Integration                               |
  | security-group            | security-group                                |
  | dhcp_agent_scheduler      | DHCP Agent Scheduler                          |
  | router_availability_zone  | Router Availability Zone                      |
  | rbac-policies             | RBAC Policies                                 |
  | standard-attr-description | standard-attr-description                     |
  | port-security             | Port Security                                 |
  | allowed-address-pairs     | Allowed Address Pairs                         |
  | dvr                       | Distributed Virtual Router                    |
  +---------------------------+-----------------------------------------------+
  
  $ neutron agent-list
  +--------------------------------------+--------------------+----------+-------------------+-------+----------------+---------------------------+
  | id                                   | agent_type         | host     | availability_zone | alive | admin_state_up | binary                    |
  +--------------------------------------+--------------------+----------+-------------------+-------+----------------+---------------------------+
  | 250ffcfd-afb1-43ed-b23b-77297cdf842b | L3 agent           | network  | nova              | :-)   | True           | neutron-l3-agent          |
  | 2cc4f859-cf2f-4238-9053-210583ed96d5 | DHCP agent         | network  | nova              | :-)   | True           | neutron-dhcp-agent        |
  | 7382d15a-8a75-405b-b829-748d5a93dd94 | Metadata agent     | network  |                   | :-)   | True           | neutron-metadata-agent    |
  | 8d504da9-5d70-4fd9-b8f6-5520fa7c7a5f | Open vSwitch agent | network  |                   | :-)   | True           | neutron-openvswitch-agent |
  | a09e5522-a4fc-4d21-be9a-968826386f3c | Open vSwitch agent | compute1 |                   | :-)   | True           | neutron-openvswitch-agent |
  +--------------------------------------+--------------------+----------+----
  ```

---

### 双节点（控制、计算）

---

控制节点：两个网卡；管理网卡，外部网卡

计算节点：两个网卡；管理网卡，外部网卡

neutron服务搭在控制节点上

---

控制节点上直接安装openstack-neutron-openvswitch，不安装python-neutronclient

控制节点的安装和三节点中控制节点的安装一样

三节点中网络节点上的操作都操作在控制节点上

