# OpenStack安装总结4--创建实例

具体参照：https://docs.openstack.org/mitaka/install-guide-rdo/launch-instance.html#launch-instance

1. Create virtual networks -- Provider network

   + ```bash
     . admin-openrc
     ```

   + 创建网络

     ```bash
     [root@controller ~]# neutron net-create --shared --provider:physical_network provider \
     >   --provider:network_type flat provider
     Created a new network:
     +---------------------------+--------------------------------------+
     | Field                     | Value                                |
     +---------------------------+--------------------------------------+
     | admin_state_up            | True                                 |
     | availability_zone_hints   |                                      |
     | availability_zones        |                                      |
     | created_at                | 2020-06-15T14:04:34                  |
     | description               |                                      |
     | id                        | 74afa9af-a695-4e5e-8511-2b4ba34dbea1 |
     | ipv4_address_scope        |                                      |
     | ipv6_address_scope        |                                      |
     | mtu                       | 1500                                 |
     | name                      | provider                             |
     | port_security_enabled     | True                                 |
     | provider:network_type     | flat                                 |
     | provider:physical_network | provider                             |
     | provider:segmentation_id  |                                      |
     | router:external           | False                                |
     | shared                    | True                                 |
     | status                    | ACTIVE                               |
     | subnets                   |                                      |
     | tags                      |                                      |
     | tenant_id                 | 6edfacbf5a83466281538f9baa05c81b     |
     | updated_at                | 2020-06-15T14:04:34                  |
     +---------------------------+--------------------------------------+
     ```

   + 创建子网

     模板：

     ```bash
     $ neutron subnet-create --name provider \
       --allocation-pool start=START_IP_ADDRESS,end=END_IP_ADDRESS \
       --dns-nameserver DNS_RESOLVER --gateway PROVIDER_NETWORK_GATEWAY \
       provider PROVIDER_NETWORK_CIDR
     ```

     Example：

     ```bash
     [root@controller ~]# neutron subnet-create --name provider --allocation-pool start=192.168.200.101,end=192.168.200.250 \
     > --dns-nameserver 8.8.8.8 --gateway 192.168.200.2 provider 192.168.200.0/24
     Created a new subnet:
     +-------------------+--------------------------------------------------------+
     | Field             | Value                                                  |
     +-------------------+--------------------------------------------------------+
     | allocation_pools  | {"start": "192.168.200.101", "end": "192.168.200.250"} |
     | cidr              | 192.168.200.0/24                                       |
     | created_at        | 2020-06-15T14:07:45                                    |
     | description       |                                                        |
     | dns_nameservers   | 8.8.8.8                                                |
     | enable_dhcp       | True                                                   |
     | gateway_ip        | 192.168.200.2                                          |
     | host_routes       |                                                        |
     | id                | 664c2a3e-f657-4139-bd15-5f3d332980ee                   |
     | ip_version        | 4                                                      |
     | ipv6_address_mode |                                                        |
     | ipv6_ra_mode      |                                                        |
     | name              | provider                                               |
     | network_id        | 74afa9af-a695-4e5e-8511-2b4ba34dbea1                   |
     | subnetpool_id     |                                                        |
     | tenant_id         | 6edfacbf5a83466281538f9baa05c81b                       |
     | updated_at        | 2020-06-15T14:07:45                                    |
     +-------------------+--------------------------------------------------------+
     ```

2. Create virtual networks -- Self-service network



