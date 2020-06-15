# OpenStackTips4--为实例增加网卡

1. 通过OpenStack添加

   **这种方式，不仅会增加一个虚拟网卡，还会自动分配IP**

   实例：将test_cxy3和test_cxy2相连，处于net_cxy_test2网络中。test_cxy3已经在net_cxy_test2网络中

   在net_cxy_test2网络中加一块网卡，然后把新网卡绑定到test_cxy2上

   + 设置环境变量

     ```shell
     source /root/admin-openrc
     ```

   + 查找网络

     neutron net-list | grep *net_name*

     ```shell
     [root@controller ~]# neutron net-list | grep net_cxy_test2
     | ce59735e-69a2-4568-a9d0-491cb1bc976d | net_cxy_test2  | 19290ef3-3757-40aa-9ce3-b825ab35b134 223.223.222.0/24 |
     ```

   + 增加网络端口

     + 不指定IP 

       neutron port-create *net_id* 

       ```shell
       [root@controller ~]# neutron port-create ce59735e-69a2-4568-a9d0-491cb1bc976d
       Created a new port:
       +-----------------------+--------------------------------------------------------------------------------------+
       | Field                 | Value                                                                                |
       +-----------------------+--------------------------------------------------------------------------------------+
       | admin_state_up        | True                                                                                 |
       | allowed_address_pairs |                                                                                      |
       | binding:host_id       |                                                                                      |
       | binding:profile       | {}                                                                                   |
       | binding:vif_details   | {}                                                                                   |
       | binding:vif_type      | unbound                                                                              |
       | binding:vnic_type     | normal                                                                               |
       | created_at            | 2020-06-04T02:47:37                                                                  |
       | description           |                                                                                      |
       | device_id             |                                                                                      |
       | device_owner          |                                                                                      |
       | dns_name              |                                                                                      |
       | extra_dhcp_opts       |                                                                                      |
       | fixed_ips             | {"subnet_id": "19290ef3-3757-40aa-9ce3-b825ab35b134", "ip_address": "223.223.222.6"} |
       | id                    | 7a32be07-4096-49b4-8bbe-bc033da3e82e                                                 |
       | mac_address           | fa:16:3e:89:c6:85                                                                    |
       | name                  |                                                                                      |
       | network_id            | ce59735e-69a2-4568-a9d0-491cb1bc976d                                                 |
       | port_security_enabled | True                                                                                 |
       | security_groups       | 82accba2-c713-4b41-84d7-bd1832c632c2                                                 |
       | status                | DOWN                                                                                 |
       | tenant_id             | f2e64bde168f41358b47ca3f1e1caea1                                                     |
       | updated_at            | 2020-06-04T02:47:37                                                                  |
       +-----------------------+--------------------------------------------------------------------------------------+
       ```

     + 指定IP

       neutron port-create --fixed-ip subnet_id=*subnet_id*,ip_address=*IP* *net_id*

       ```shell
       [root@controller ~]# neutron port-create --fixed-ip subnet_id=19290ef3-3757-40aa-9ce3-b825ab35b134,ip_address=223.223.222.4 ce59735e-69a2-4568-a9d0-491cb1bc976d
       Created a new port:
       +-----------------------+--------------------------------------------------------------------------------------+
       | Field                 | Value                                                                                |
       +-----------------------+--------------------------------------------------------------------------------------+
       | admin_state_up        | True                                                                                 |
       | allowed_address_pairs |                                                                                      |
       | binding:host_id       |                                                                                      |
       | binding:profile       | {}                                                                                   |
       | binding:vif_details   | {}                                                                                   |
       | binding:vif_type      | unbound                                                                              |
       | binding:vnic_type     | normal                                                                               |
       | created_at            | 2020-06-04T02:46:05                                                                  |
       | description           |                                                                                      |
       | device_id             |                                                                                      |
       | device_owner          |                                                                                      |
       | dns_name              |                                                                                      |
       | extra_dhcp_opts       |                                                                                      |
       | fixed_ips             | {"subnet_id": "19290ef3-3757-40aa-9ce3-b825ab35b134", "ip_address": "223.223.222.4"} |
       | id                    | 6071ee53-020b-448e-b171-074a57e50e65                                                 |
       | mac_address           | fa:16:3e:18:ee:cb                                                                    |
       | name                  |                                                                                      |
       | network_id            | ce59735e-69a2-4568-a9d0-491cb1bc976d                                                 |
       | port_security_enabled | True                                                                                 |
       | security_groups       | 82accba2-c713-4b41-84d7-bd1832c632c2                                                 |
       | status                | DOWN                                                                                 |
       | tenant_id             | f2e64bde168f41358b47ca3f1e1caea1                                                     |
       | updated_at            | 2020-06-04T02:46:05                                                                  |
       +-----------------------+--------------------------------------------------------------------------------------+
       ```

   + 查找实例

     nova list --all | grep *instance_name*

     ```shell
     [root@controller ~]# nova list --all | grep test_cxy2
     /usr/lib/python2.7/site-packages/keyring/backends/Gnome.py:6: PyGIWarning: GnomeKeyring was imported without specifying a version first. Use gi.require_version('GnomeKeyring', '1.0') before import to ensure that the right version gets loaded.
       from gi.repository import GnomeKeyring
     WARNING: Option "--all_tenants" is deprecated; use "--all-tenants"; this option will be removed in novaclient 3.3.0.
     | ceaeb58e-c67a-4595-b15f-c0835f800433 | test_cxy2             | f2e64bde168f41358b47ca3f1e1caea1 | ACTIVE  | -          | Running     | net_cxy_test=223.223.223.13  
     ```

   + 为实例增加端口=增加虚拟网卡

     nova interface-attach --port-id *port_id* *instance_id*

     ```shell
     [root@controller ~]# nova interface-attach --port-id 6071ee53-020b-448e-b171-074a57e50e65 ceaeb58e-c67a-4595-b15f-c0835f800433
     /usr/lib/python2.7/site-packages/keyring/backends/Gnome.py:6: PyGIWarning: GnomeKeyring was imported without specifying a version first. Use gi.require_version('GnomeKeyring', '1.0') before import to ensure that the right version gets loaded.
       from gi.repository import GnomeKeyring
     ```

   + 查看实例详情

2. 通过python API添加

   ```python
   import sys
   import MySQLdb
   sys.path.append('/home/cxy_tdyt/tdyt_openstack')
   import credentials
   neutron_client = credentials.get_neutron_client(credentials.get_nova_creds())
   
   def get_net_id(net):
       db = MySQLdb.connect(host='192.168.1.11',
                            user='root',
                            passwd='123456',
                            db='neutron',
                            charset='utf8')
       sql = "select id from networks where name=\'%s\'"%(str(net))
       cursor = db.cursor()
       try:
           cursor.execute(sql)
           net_id = cursor.fetchone()
           db.commit()
       except Exception, e:
           db.rollback()
           print e
           net_id = ['']
       cursor.close()
       db.close()
       return list(net_id)[0]
   
   def set_body_value(net_id):
       body_value = {
           "port": {
               "admin_state_up": True,
               "network_id": net_id
           }
       }
       return body_value
   
   def create_port(net_name):
       net_id = get_net_id(net_name)
       body_value = set_body_value(net_id)
       res = neutron_client.create_port(body=body_value)
       return res
   
   if __name__=='__main__':
       res = create_port('net_cxy_test2')
       print res
       res_port = res['port']
       print res_port
       port_id_new = res_port['id']
       print port_id_new
       fixed_ips = res_port['fixed_ips'][0]
       print fixed_ips
       ip_address = fixed_ips['ip_address']
       print ip_address
   ```

   输出：

   ```shell
   [root@controller test]# python port_create_test.py 
   {u'port': {u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2020-06-04T03:21:45', u'device_owner': u'', u'binding:profile': {}, u'port_security_enabled': True, u'fixed_ips': [{u'subnet_id': u'19290ef3-3757-40aa-9ce3-b825ab35b134', u'ip_address': u'223.223.222.9'}], u'id': u'b679542a-c1df-4c94-8232-1658e98c4757', u'security_groups': [u'82accba2-c713-4b41-84d7-bd1832c632c2'], u'binding:vif_details': {}, u'binding:vif_type': u'unbound', u'mac_address': u'fa:16:3e:4c:2a:de', u'status': u'DOWN', u'binding:host_id': u'', u'description': u'', u'device_id': u'', u'name': u'', u'admin_state_up': True, u'network_id': u'ce59735e-69a2-4568-a9d0-491cb1bc976d', u'dns_name': None, u'created_at': u'2020-06-04T03:21:45', u'binding:vnic_type': u'normal', u'tenant_id': u'f2e64bde168f41358b47ca3f1e1caea1'}}
   {u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2020-06-04T03:21:45', u'device_owner': u'', u'binding:profile': {}, u'port_security_enabled': True, u'fixed_ips': [{u'subnet_id': u'19290ef3-3757-40aa-9ce3-b825ab35b134', u'ip_address': u'223.223.222.9'}], u'id': u'b679542a-c1df-4c94-8232-1658e98c4757', u'security_groups': [u'82accba2-c713-4b41-84d7-bd1832c632c2'], u'binding:vif_details': {}, u'binding:vif_type': u'unbound', u'mac_address': u'fa:16:3e:4c:2a:de', u'status': u'DOWN', u'binding:host_id': u'', u'description': u'', u'device_id': u'', u'name': u'', u'admin_state_up': True, u'network_id': u'ce59735e-69a2-4568-a9d0-491cb1bc976d', u'dns_name': None, u'created_at': u'2020-06-04T03:21:45', u'binding:vnic_type': u'normal', u'tenant_id': u'f2e64bde168f41358b47ca3f1e1caea1'}
   b679542a-c1df-4c94-8232-1658e98c4757
   {u'subnet_id': u'19290ef3-3757-40aa-9ce3-b825ab35b134', u'ip_address': u'223.223.222.9'}
   223.223.222.9
   ```

3. 直接用KVM方式增加

   这种方式只增加一个虚拟网口，如果需要配置ip，需要进入虚拟机增加ip

   + 查看实例

     nova list --all | grep *instance_name*

     ```shell
     [root@controller ~]# nova list --all | grep test_cxy2
     /usr/lib/python2.7/site-packages/keyring/backends/Gnome.py:6: PyGIWarning: GnomeKeyring was imported without specifying a version first. Use gi.require_version('GnomeKeyring', '1.0') before import to ensure that the right version gets loaded.
       from gi.repository import GnomeKeyring
     WARNING: Option "--all_tenants" is deprecated; use "--all-tenants"; this option will be removed in novaclient 3.3.0.
     | ceaeb58e-c67a-4595-b15f-c0835f800433 | test_cxy2             | f2e64bde168f41358b47ca3f1e1caea1 | ACTIVE  | -          | Running     | net_cxy_test2=223.223.222.4; net_cxy_test=223.223.223.13        
     ```

   + 查看实例详情

     这一步确定计算节点名称和实例名称，看OS-EXT-SRV-ATTR:hypervisor_hostname 和 OS-EXT-SRV-ATTR:instance_name   

     nova show *instance_id*

     ```shell
     [root@controller ~]# nova show ceaeb58e-c67a-4595-b15f-c0835f800433
     /usr/lib/python2.7/site-packages/keyring/backends/Gnome.py:6: PyGIWarning: GnomeKeyring was imported without specifying a version first. Use gi.require_version('GnomeKeyring', '1.0') before import to ensure that the right version gets loaded.
       from gi.repository import GnomeKeyring
     +--------------------------------------+----------------------------------------------------------+
     | Property                             | Value                                                    |
     +--------------------------------------+----------------------------------------------------------+
     | OS-DCF:diskConfig                    | AUTO                                                     |
     | OS-EXT-AZ:availability_zone          | compute6                                                 |
     | OS-EXT-SRV-ATTR:host                 | compute6                                                 |
     | OS-EXT-SRV-ATTR:hostname             | test-cxy2                                                |
     | OS-EXT-SRV-ATTR:hypervisor_hostname  | compute6                                                 |
     | OS-EXT-SRV-ATTR:instance_name        | instance-0000b90e                                        |
     | OS-EXT-SRV-ATTR:kernel_id            |                                                          |
     | OS-EXT-SRV-ATTR:launch_index         | 0                                                        |
     | OS-EXT-SRV-ATTR:ramdisk_id           |                                                          |
     | OS-EXT-SRV-ATTR:reservation_id       | r-do7dzcgg                                               |
     | OS-EXT-SRV-ATTR:root_device_name     | /dev/vda                                                 |
     | OS-EXT-SRV-ATTR:user_data            | -                                                        |
     | OS-EXT-STS:power_state               | 1                                                        |
     | OS-EXT-STS:task_state                | -                                                        |
     | OS-EXT-STS:vm_state                  | active                                                   |
     | OS-SRV-USG:launched_at               | 2020-05-28T11:18:57.000000                               |
     | OS-SRV-USG:terminated_at             | -                                                        |
     | accessIPv4                           |                                                          |
     | accessIPv6                           |                                                          |
     | config_drive                         |                                                          |
     | created                              | 2020-05-28T11:18:53Z                                     |
     | description                          | test_cxy2                                                |
     | flavor                               | 1_1_10 (1310bb10-ff4e-4d92-9193-0cce450dab43)            |
     | hostId                               | 5c38cb836b564527b9eeafde558d6222f128b246f5c4ab91ea34c399 |
     | host_status                          | UP                                                       |
     | id                                   | ceaeb58e-c67a-4595-b15f-c0835f800433                     |
     | image                                | mini-router-ospf (6f1796a8-f84e-438a-a48b-eedcb4a0a693)  |
     | key_name                             | -                                                        |
     | locked                               | False                                                    |
     | metadata                             | {}                                                       |
     | name                                 | test_cxy2                                                |
     | net_cxy_test network                 | 223.223.223.13                                           |
     | net_cxy_test2 network                | 223.223.222.4                                            |
     | os-extended-volumes:volumes_attached | []                                                       |
     | progress                             | 0                                                        |
     | security_groups                      | default                                                  |
     | status                               | ACTIVE                                                   |
     | tenant_id                            | f2e64bde168f41358b47ca3f1e1caea1                         |
     | updated                              | 2020-05-28T11:18:57Z                                     |
     | user_id                              | 8943d3f104fe427185be6a6e6ec7540f                         |
     +--------------------------------------+----------------------------------------------------------+
     ```

   + 登录对应的计算节点

   + 查看kvm实例

     virsh list --all | grep *instance_name*

     ```shell
     [root@compute6 ~]# virsh list --all | grep instance-0000b90e
      178   instance-0000b90e              running
     ```

   + 查看网络接口

     virsh domiflist *instance_name*

     ```shell
     [root@compute6 ~]# virsh domiflist instance-0000b90e
     Interface  Type       Source     Model       MAC
     -------------------------------------------------------
     tap232324e0-00 bridge     qbr232324e0-00 virtio      fa:16:3e:9a:1a:b6
     tap6071ee53-02 bridge     qbr6071ee53-02 virtio      fa:16:3e:18:ee:cb
     ```

   + 增加网络接口

     virsh attach-interface *instance_name* --type bridge --source qbr232324e0-00 --current

     这一步没有操作，推测是在compute6的网桥 qbr232324e0-00上再加一个端口，和MAC地址为 fa:16:3e:9a:1a:b6的端口所处的网段一致

     