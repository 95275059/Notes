# OpenStack命令2--neutron命令

### 设置环境变量

```shell
source /root/admin-openrc
```

或

```shell
source .admin_openrc.sh
```

### agent

+ 显示agent列表

  ```bash
  neutron agent-list
  ```


### net

+ 显示已有网路列表

  ```bash
  neutron net-list
  ```

+ 显示某网络详细信息

  ```bash
  neutron net-show *net-id*
  ```
  
  ```bash
  [root@controller etc]# neutron net-show 41afadee-ab80-4b2a-86a9-f22fedcbb203
  +---------------------------+--------------------------------------+
  | Field                     | Value                                |
  +---------------------------+--------------------------------------+
  | admin_state_up            | True                                 |
  | availability_zone_hints   |                                      |
  | availability_zones        | nova                                 |
  | created_at                | 2020-10-20T02:25:21                  |
  | description               |                                      |
  | id                        | 41afadee-ab80-4b2a-86a9-f22fedcbb203 |
  | ipv4_address_scope        |                                      |
  | ipv6_address_scope        |                                      |
  | mtu                       | 1500                                 |
  | name                      | first_local_net                      |
  | port_security_enabled     | True                                 |
  | provider:network_type     | local                                |
  | provider:physical_network |                                      |
  | provider:segmentation_id  |                                      |
  | router:external           | False                                |
  | shared                    | False                                |
  | status                    | ACTIVE                               |
  | subnets                   | 535e2a92-3512-4781-a48b-c62ae900c2fa |
  | tags                      |                                      |
  | tenant_id                 | 6edfacbf5a83466281538f9baa05c81b     |
  | updated_at                | 2020-10-20T02:25:21                  |
  +---------------------------+--------------------------------------+
  ```
  
+ 删除网络

  ```bash
  neutron net-delete *net-id*
  ```

### port

+ 显示已有端口列表

  neutron port-list

+ 新建端口

  + 不指定IP

    neutron port-create *net_id*

  + 指定IP

    neutron port-create --fixed-ip subnet_id=*subnet_id*,ip_address=*IP* *net_id*

+ 删除端口

  neutron port-delete *port_id*

### ip netns

+ 列出所有namespace

  ```bash
  ip netns list
  ```

+ namespace管理

  ```bash
  ip netns exec *network_namespace* *command*
  ```

  + 查看某网络的ns配置

    ```bash
    [root@controller ~]# ip netns exec qdhcp-65362856-ce53-46ed-90f1-6cef22029541 ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
           valid_lft forever preferred_lft forever
    2: ns-9894fdef-df@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether fa:16:3e:af:c2:07 brd ff:ff:ff:ff:ff:ff link-netnsid 0
        inet 172.16.1.101/24 brd 172.16.1.255 scope global ns-9894fdef-df
           valid_lft forever preferred_lft forever
        inet 169.254.169.254/16 brd 169.254.255.255 scope global ns-9894fdef-df
           valid_lft forever preferred_lft forever
        inet6 fe80::f816:3eff:feaf:c207/64 scope link 
           valid_lft forever preferred_lft forever
    ```

  




