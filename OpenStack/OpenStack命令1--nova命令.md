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

   + 列出所有已有实例

     nova list --all

     显示每个实例的ID，名称，租户（项目）ID，状态，任务状态，电池状态，网络

     注：WARNING: Option "--all_tenants" is deprecated; use "--all-tenants"; this option will be removed in novaclient 3.3.0.即，在nova3.3.0中--all将被移除，使用--all-tenants.

   + 查看nova子服务信息

     ```bash
     [root@controller images]# nova service-list
     +----+------------------+-----------------------+-------------+---------+-------+----------------------------+-----------------+
     | Id | Binary           | Host                  | Zone        | Status  | State | Updated_at                 | Disabled Reason |
     +----+------------------+-----------------------+-------------+---------+-------+----------------------------+-----------------+
     | 1  | nova-conductor   | controller            | internal    | enabled | up    | 2020-06-23T02:59:54.000000 | -               |
     | 9  | nova-consoleauth | controller            | internal    | enabled | up    | 2020-06-23T02:59:48.000000 | -               |
     | 10 | nova-scheduler   | controller            | internal    | enabled | up    | 2020-06-23T02:59:48.000000 | -               |
     | 16 | nova-compute     | compute3              | compute3    | enabled | up    | 2020-06-23T02:59:46.000000 | -               |
     | 17 | nova-compute     | compute4              | compute4    | enabled | down  | 2019-09-12T13:54:10.000000 | -               |
     | 19 | nova-compute     | compute5              | compute5    | enabled | down  | 2020-05-06T09:00:24.000000 | -               |
     | 20 | nova-compute     | compute6              | compute6    | enabled | up    | 2020-06-23T02:59:45.000000 | -               |
     | 21 | nova-compute     | compute7              | compute7    | enabled | up    | 2020-06-23T02:59:53.000000 | -               |
     | 22 | nova-compute     | compute8              | compute8    | enabled | up    | 2020-06-23T02:59:47.000000 | -               |
     | 23 | nova-compute     | localhost.localdomain | nova        | enabled | down  | 2019-07-13T05:39:14.000000 | -               |
     | 27 | nova-compute     | compute11             | d_compute11 | enabled | up    | 2020-06-23T02:59:51.000000 | -               |
     | 28 | nova-compute     | compute12             | compute12   | enabled | up    | 2020-06-23T02:59:48.000000 | -               |
     | 29 | nova-compute     | compute13             | compute13   | enabled | down  | 2020-01-03T05:25:28.000000 | -               |
     | 30 | nova-compute     | compute14             | compute14   | enabled | down  | 2019-08-01T07:59:57.000000 | -               |
     | 31 | nova-compute     | compute1              | compute1    | enabled | up    | 2020-06-23T02:59:46.000000 | -               |
     | 32 | nova-compute     | compute2              | compute2    | enabled | down  | 2020-01-07T08:04:18.000000 | -               |
     | 33 | nova-compute     | compute15             | compute15   | enabled | down  | 2019-08-02T02:52:17.000000 | -               |
     | 34 | nova-compute     | compute16             | compute16   | enabled | up    | 2020-06-23T02:59:47.000000 | -               |
     | 36 | nova-compute     | compute18             | compute18   | enabled | up    | 2020-06-23T02:59:51.000000 | -               |
     | 37 | nova-compute     | compute20             | compute20   | enabled | up    | 2020-06-23T02:59:45.000000 | -               |
     +----+------------------+-----------------------+-------------+---------+-------+----------------------------+-----------------+
     ```

   + 列出实例详情

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

   ---

3. interface

   + 给实例添加端口

     nova interface-attach --port-id *port_id* *instance_id*

   + 删除实例某端口

     nova interface-detach *instance_id* *port_id*

     + 端口若一开始就直接绑定在实例上，删除实例端口会直接把端口删除掉
     + 端口若是先建在某个网络中（不论指不指定IP），删除实例端口不会把端口删除掉

   ---

4. reset

   + 将虚机状态重置为active

     nova reset-state *instance_id* --active
     
     将虚机状态重置为active，对于部分error虚机无法删除时，运行该命令再删除一般能将虚机删除

   ---

5. delete

   + 删除实例

     nova delete *instance_id*

   ---

6. 

