# OpenStack命令3--openstack命令

### openstack命令就是以前老版的keystone命令

---

### 查看openstack已安装的组件分类

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

### 查看OpenStack所有角色(Role)

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

### 查看OpenStack所有用户（User）

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

### 查看服务的endpoints

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

### openstack flavor

+ openstack flavor create

  + Create new flavor

  + 语法

    ```bash
    openstack flavor create [OPTIONS] flavor-name
    ```

    | 选项                   | 说明                                                   |
    | ---------------------- | ------------------------------------------------------ |
    | --id <id>              | Unique flavor ID; 'auto' creates a UUID (default:auto) |
    | --ram <size-mb>        | Memory size in MB (default 256M)                       |
    | --disk <size-gb>       | Disk size in GB (default 0G)                           |
    | --ephemeral <size-gb>  | Ephemeral disk(临时盘) size in GB (default 0G)         |
    | --swap <size-gb>       | Swap space size in GB (default 0G)                     |
    | --vcpus <vcpus>        | Number of vcpus (default 1)                            |
    | --rxtx-factor <factor> | RX/TX factor (default 1)                               |
    | --public               | Flavor is available to other projects (default)        |
    | --private              | Flavor is not available to other projects              |

  + 实例

    ```bash
    [root@controller cy]# openstack flavor create --id 6 --vcpus 1 --ram 1024 --disk 10 1_1_10
    +----------------------------+--------+
    | Field                      | Value  |
    +----------------------------+--------+
    | OS-FLV-DISABLED:disabled   | False  |
    | OS-FLV-EXT-DATA:ephemeral  | 0      |
    | disk                       | 10     |
    | id                         | 6      |
    | name                       | 1_1_10 |
    | os-flavor-access:is_public | True   |
    | ram                        | 1024   |
    | rxtx_factor                | 1.0    |
    | swap                       |        |
    | vcpus                      | 1      |
    +----------------------------+--------+
    ```

+ openstack flavor delete

  + Delete flavor

  + 语法

    ```bash
    openstack flavor delete <flavor>
    ```

    + <flavor>    Flavor to delete (name or ID)

+ openstack flavor list

  + List flavors

  + 语法

    ```bash
    openstack flavor list [OPTIONS]
    ```

    | 选项              | 说明                                        |
    | ----------------- | ------------------------------------------- |
    | --public          | List only public flavors (default)          |
    | --private         | List only private flavors                   |
    | --all             | List all flavors, whether public or private |
    | --long            | List additional fields in output            |
    | --marker <marker> | The last flavor ID of the previous page     |
    | --limit <limit>   | Maximum number of flavors to display        |

  + 实例

    ```bash
    [root@network ~]# openstack flavor list
    +----+-----------+-------+------+-----------+-------+-----------+
    | ID | Name      |   RAM | Disk | Ephemeral | VCPUs | Is Public |
    +----+-----------+-------+------+-----------+-------+-----------+
    | 1  | m1.tiny   |   512 |    1 |         0 |     1 | True      |
    | 2  | m1.small  |  2048 |   20 |         0 |     1 | True      |
    | 3  | m1.medium |  4096 |   40 |         0 |     2 | True      |
    | 4  | m1.large  |  8192 |   80 |         0 |     4 | True      |
    | 5  | m1.xlarge | 16384 |  160 |         0 |     8 | True      |
    | 6  | 1_1_10    |  1024 |   10 |         0 |     1 | True      |
    +----+-----------+-------+------+-----------+-------+-----------+
    ```

+ openstack flavor set

  + Set flavor properties

  + 语法

    ```bash
    openstack flavor set [OPTIONS] <flavor>
    ```

    + <flavor>    Flavor to modify (name or ID)

    | 选项                   | 说明                                                         |
    | ---------------------- | ------------------------------------------------------------ |
    | --property <key=value> | Property to add or modify for this flavor (repeat option to set multiple properties) |

+ openstack flavor show

  + Display flavor details

  + 语法

    ```bash
    openstack flavor show [OPTIONS] <flavor>
    ```

    + flavor : Flavor to display (name or ID)

  + 实例

    ```bash
    [root@controller cy]# openstack flavor show 1_1_10
    +----------------------------+--------+
    | Field                      | Value  |
    +----------------------------+--------+
    | OS-FLV-DISABLED:disabled   | False  |
    | OS-FLV-EXT-DATA:ephemeral  | 0      |
    | disk                       | 10     |
    | id                         | 6      |
    | name                       | 1_1_10 |
    | os-flavor-access:is_public | True   |
    | properties                 |        |
    | ram                        | 1024   |
    | rxtx_factor                | 1.0    |
    | swap                       |        |
    | vcpus                      | 1      |
    +----------------------------+--------+
    ```

+ openstack flavor unset

  + Unset flavor properties

  + 语法

    ```bash
    openstack flavor unset [OPTIONS] <flavor>
    ```

    + <flavor>    Flavor to modify (name or ID)

    | 选项                   | 说明                                                         |
    | ---------------------- | ------------------------------------------------------------ |
    | --property <key=value> | Property to add or modify for this flavor (repeat option to set multiple properties) |