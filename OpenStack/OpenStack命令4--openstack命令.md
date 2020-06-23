# OpenStack命令4--openstack命令

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

3. 