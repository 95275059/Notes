# OpenStack命令1--nova命令

1. 设置环境变量

   ```shell
   source /root/admin-openrc
   ```

   或

   ```shell
   source .admin_openrc.sh
   ```

2. list

   + nova list --all

     列出所有实例，显示每个实例的ID，名称，租户（项目）ID，状态，任务状态，电池状态，网络

     注：WARNING: Option "--all_tenants" is deprecated; use "--all-tenants"; this option will be removed in novaclient 3.3.0.即，在nova3.3.0中--all将被移除，使用--all-tenants.

   + nova show *instance_id*

     列出实例详情

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

   ---

3. interface

   + nova interface-attach --port-id *port_id* *instance_id*
   + nova interface-detach *instance_id* *port_id*

   ---

4. reset

   + nova reset-state *instance_id* --active

     将虚机状态重置为active，对于部分error虚机无法删除时，运行该命令再删除一般能将虚机删除

   ---

5. delete

   + nova delete *instance_id*

   ---

6. 

