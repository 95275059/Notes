# OpenStackTips16--安装LBaaS

### 参考官网https://docs.openstack.org/mitaka/networking-guide/config-lbaas.html

### 安装LBaaS

```bash
yum install -y openstack-neutron-lbaas haproxy
```

### 添加LBaaS服务(控制节点)

Add the LBaaS v2 service plug-in to the `service_plugins` configuration directive in `/etc/neutron/neutron.conf`. The plug-in list is comma-separated

```bash
[DEFAULT]
service_plugins = router,neutron_lbaas.services.loadbalancer.plugin.LoadBalancerPluginv2
```

### 配置LBaaS(网络节点)

+ Add the LBaaS v2 service provider to the `service_provider` configuration directive within the `[service_providers]` section in `/etc/neutron/neutron_lbaas.conf`(网络节点)

  ```bash
  [service_providers]
  service_provider = LOADBALANCERV2:Haproxy:neutron_lbaas.drivers.haproxy.plugin_driver.HaproxyOnHostPluginDriver:default
  ```

+ Select the driver that manages virtual interfaces in `/etc/neutron/lbaas_agent.ini`

  Replace `INTERFACE_DRIVER` with the interface driver that the layer-2 agent in your environment uses. For example, `openvswitch` for Open vSwitch
  
   or `linuxbridge` for Linux bridge.
  
+ OVS
  
    ```bash
    [DEFAULT]
    interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver
    ```
  
  + Linuxbridge
  
    ```bash
    [DEFAULT]
    interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver
    ```

### 在控制节点更新Neutron数据库

```
neutron-db-manage --subproject neutron-lbaas upgrade head
```

### 开启LBaaS v2 agent

```bash
systemctl enable neutron-lbaasv2-agent
systemctl start neutron-lbaasv2-agent
systemctl restart neutron-server
```

### 安装Dashboard for LBaaS V2

+ git源码

  ```bash
  https://opendev.org/openstack/neutron-lbaas-dashboard/
  ```

  没有mitaka版本🙄

+ 安装

  ```bash
  git clone https://git.openstack.org/openstack/neutron-lbaas-dashboard -b stable/mitaka
   
  cd  neutron-lbaas-dashboard
  python setup.py install
   
  cp neutron_lbaas_dashboard/enabled/_1481_project_ng_loadbalancersv2_panel.py  /usr/share/openstack-dashboard/openstack_dashboard/local/enabled/
  ```

+ 重新启动httpd

  ```bash
  systemctl restart httpd
  ```

  

