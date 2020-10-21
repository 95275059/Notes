# OpenStack命令3--openstack命令

+ openstack命令就是以前老版的keystone命令

1. 查看openstack已安装的组件分类

   **查看Endpoints**

   ```bash
   [root@controller cxy_tdyt]# openstack catalog list
   +----------+----------+--------------------------------------------------------------------------+
   | Name     | Type     | Endpoints                                                                |
   +----------+----------+--------------------------------------------------------------------------+
   | keystone | identity | RegionOne                                                                |
   |          |          |   public: http://controller:5000/v3                                      |
   |          |          | RegionOne                                                                |
   |          |          |   admin: http://controller:35357/v3                                      |
   |          |          | RegionOne                                                                |
   |          |          |   internal: http://controller:5000/v3                                    |
   |          |          |                                                                          |
   | nova     | compute  | RegionOne                                                                |
   |          |          |   public: http://controller:8774/v2.1/f2e64bde168f41358b47ca3f1e1caea1   |
   |          |          | RegionOne                                                                |
   |          |          |   admin: http://controller:8774/v2.1/f2e64bde168f41358b47ca3f1e1caea1    |
   |          |          | RegionOne                                                                |
   |          |          |   internal: http://controller:8774/v2.1/f2e64bde168f41358b47ca3f1e1caea1 |
   |          |          |                                                                          |
   | glance   | image    | RegionOne                                                                |
   |          |          |   admin: http://controller:9292                                          |
   |          |          | RegionOne                                                                |
   |          |          |   internal: http://controller:9292                                       |
   |          |          | RegionOne                                                                |
   |          |          |   public: http://controller:9292                                         |
   |          |          |                                                                          |
   | neutron  | network  | RegionOne                                                                |
   |          |          |   public: http://controller:9696                                         |
   |          |          | RegionOne                                                                |
   |          |          |   internal: http://controller:9696                                       |
   |          |          | RegionOne                                                                |
   |          |          |   admin: http://controller:9696                                          |
   |          |          |                                                                          |
   +----------+----------+--------------------------------------------------------------------------+
   ```

   ---

2. 查看OpenStack所有角色(Role)

   ```bash
   [root@controller cxy_tdyt]# openstack role list
   +----------------------------------+-------+
   | ID                               | Name  |
   +----------------------------------+-------+
   | 5eb5b2cfcb05410489756775155c2626 | user  |
   | cfc0aa1e33284fed8227d63c5d577dee | admin |
   +----------------------------------+-------+
   ```

   ---

3. 查看OpenStack所有用户（User）

   ```bash
   [root@controller cxy_tdyt]# openstack user list
   +----------------------------------+--------------+
   | ID                               | Name         |
   +----------------------------------+--------------+
   | 3e1d49649eef41f68994dee9f89c8307 | neutron      |
   | 63e5d9d7ee1a41cca5c16749dbd89bc8 | spinlt       |
   | 6837ba7dc4c74be3bc5b6d20067d37f9 | zgj          |
   | 78f3312fab9d47278ce2ea54f179a2e2 | db           |
   | 8943d3f104fe427185be6a6e6ec7540f | admin        |
   | 932b130648b6497c8cd641e916154831 | amber        |
   | a02cf69888a94f9783b4ba8bf7a60223 | nova         |
   | d9a61ffd09fc48e184b6081046a4cd15 | glance       |
   | dccdaf2487b04a4886bf9ae1e33abf30 | demo         |
   | f1505295a79e4b3b96c596cfd02616d6 | lihuayuliang |
   +----------------------------------+--------------+
   ```

   ---

4. 查看服务的endpoints

   openstack endpoint list --service *service_name*

   ```bash
   [root@controller test]# openstack endpoint list --service nova
   +----------------------------------+-----------+--------------+--------------+---------+-----------+-------------------------------------------+
   | ID                               | Region    | Service Name | Service Type | Enabled | Interface | URL                                       |
   +----------------------------------+-----------+--------------+--------------+---------+-----------+-------------------------------------------+
   | 6f2813c3d6574fd89dc369cea4925ecc | RegionOne | nova         | compute      | True    | public    | http://controller:8774/v2.1/%(tenant_id)s |
   | 7533b4c9f39b48afa15514773fecce71 | RegionOne | nova         | compute      | True    | admin     | http://controller:8774/v2.1/%(tenant_id)s |
   | a272e4577c374ad8ac66a07279aaf260 | RegionOne | nova         | compute      | True    | internal  | http://controller:8774/v2.1/%(tenant_id)s |
   +----------------------------------+-----------+--------------+--------------+---------+-----------+-------------------------------------------+
   ```

   + openstack endpoint show nova

     报错：More than one endpoint exists with the name 'nova'.

     这是因为每个服务有三个endpoint（admin,public,internal）

5. 

