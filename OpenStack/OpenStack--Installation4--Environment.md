# OpenStack--Installation4--Environment

1. 安装须知

   + 必须使用有管理员权限的账户来配置每个节点

   + 作为root用户运行命令或者配置sudo应用程序

   + Note

     当服务使用SysV Init脚本而不是本机systemd文件时，在openSUSE上调用systemctl enable将输出警告信息；此警告可忽略

   + 支持验证环境的**最低要求**

     + Controller Node : 1 processor, 4GB memory, and 5GB storage
     + Compute Node : 1 processor, 2GB memory, and 10GB storage

     注：随着OpenStack服务和虚拟机的增加，升级为Hardware Requriement以保证最好的性能；如果在启用其他服务或者虚拟机后性能下降了，考虑在环境中添加硬件资源

   + 建议Linux发行版安装最小化安装，以最大程度减少混乱并为OpenStack提供更多资源；同时，必须在每个节点上安装发行版的64位版本

   + 每个节点上的单个磁盘分区适用于大多数基本安装；但是对于具有可选服务（如块存储）的安装，应考虑使用LVM（逻辑卷管理）

   + 对于首次安装和为了测试目的，许多用户选择将每个主机构建为虚拟机(VM)

     虚拟机的主要优势为：

     + 一个物理服务器可以支持多个节点，每个节点可以拥有任意数量的网络接口
     + 在整个安装过程进行定期“快照”(snap shots)，并在出现问题时“回滚”(roll back)到可工作的配置

     虚拟机的劣势：

     + 虚拟机会降低实例的性能，尤其是在虚拟机管理程序和/或处理器缺乏对嵌套VM的硬件加速的情况下

     Note

     + **如果选择在VMs上安装，确保虚拟机管理程序提供了一种在Provider Network的网络接口上禁用MAC地址过滤的方法**

   ---

2. Security

   + OpenStack服务支持多种安全方法，包括密码、策略和加密；此外，支持包括数据库服务器和支持密码安全的消息代理服务

   + 为简化安装过程，只在使用的情况下使用密码安全

   + 可以手动创建安全密码，但是在服务配置文件中的数据库连接字符串不能接受像'@'之类的特殊字符

   + 建议使用像pwgen的工具生成密码，或者运行下面的命令

     ```shell
     $ openssl rand -hex 10
     ```

   + 对于OpenStack服务，指南用SERVICE_PASS引用(reference)服务账户密码，用SERVICE_DBPASS引用数据库密码

   + 指南中需要密码的服务列表及其reference

     | Password name                       | Description                                          |
     | ----------------------------------- | ---------------------------------------------------- |
     | Database password(no variable used) | Root password for the database                       |
     | **ADMIN_PASS**                      | Passsword of user **admin**                          |
     | **CINDER_DBPASS**                   | Database password for the Block Storage service      |
     | **CINDER_PASS**                     | Password of Block Storage service user **cinder**    |
     | **DASH_PASS**                       | Database password for the Dashboard                  |
     | **DEMO_PASS**                       | Password of user demo                                |
     | **GLANCE_DBPASS**                   | Database password for Image service                  |
     | **GLANCE_PASS**                     | Password of Image service user **glance**            |
     | **KEYSTONE_DBPASS**                 | Database password of Identity service                |
     | **METADATA_SECRET**                 | Secret for the metadata proxy                        |
     | **NEUTRON_DBPASS**                  | Database password for the Networking service         |
     | **NEUTRON_PASS**                    | Password of Networking service user **neutron**      |
     | **NOVA_DBPASS**                     | Database password for Compute service                |
     | **NOVA_PASS**                       | Password of Compute service user **nova**            |
     | **PLACEMENT_PASS**                  | Password of the Placement service user **placement** |
     | **RABBIT_PASS**                     | Password of RabbitMQ user **openstack**              |

   + 在安装过程中，OpenStack和支持性服务需要管理权限
   + 在某些情况下，服务会对主机执行修改，这可能会干扰部署自动化工具（如Ansible,Chef和Rupput）
     
     + 例如，某些OpenStack服务向sudo中添加了根包装，这会干涉安全策略
   + Networing service 采用内核网络参数的默认值并修改防火墙规则
   + 为了避免在初始安装过程中出现过多问题，建议在主机上使用受支持的发行版的常规部署

   ---

3. Host Networking

   + 建议禁用所有自动网络管理工具，手动编辑适当的配置文件

   + 所有节点都需要Internet访问以进行管理，例如软件包安装、安全更新、DNS、NTP

   + 在大多数情况下，节点应通过管理网络(management network)接口获得Internet访问

   + 为强调网络分离的重要性，示例架构使用专用地址空间(private address space)用于管理网络，并假定物理网络基础结构通过NAT或其他方式提供Internet访问

   + 示例的Provider Network网络体系架构，使用可路由的IP地址空间，并假定物理网络基础架构提供直接的Internet访问

   + 在Provider Network体系架构中，所有实例可直接连接到provider network；在Self-service (private) network体系架构中，实例可以连接到自服务网络或provider网络

   + 自服务网络完全驻留在OpenStack或者通过provider网络使用NAT提供某种程度的外部网络访问

   + 示例网络体系架构

     ![Installation4-1](E:\Notes\OpenStack\Installation4-1.png)

     + 网络

       + Management Network

         + 使用网关10.0.0.1在10.0.0.0/24上进行管理

         + 该网络需要网关来提供所有节点的Internet访问，以进行管理，例如程序包安装、安装更新、DNS、NTP

       + Provider Network 

         + 203.0.113.0/24上的网关203.0.113.1

         + 该网络需要网关来提供OpenStack环境中实例的Internet访问

     + 网卡

       + 网卡名字因发布而异

       + 传统上，网卡使用eth后加序列号命名

       + 指南将编号最小的接口称为第一个接口，将编号最大的接口称为第二个接口

       + Note

         Ubuntu改变了网络接口的命名概念

         参考：https://askubuntu.com/questions/767786/changing-network-interfaces-name-ubuntu-16-04

     + 域名解析

       + 每个节点除了提供IP地址外，还必须按名称解析其他节点

         即，controller名称必须解析为10.0.0.11，即controller节点上管理网络的接口IP地址

     + 注意

       + 网络接口的重新配置会中断网络连接，建议在本地终端会话进行这些操作
       + **RHEL、CentOS 和SUSE发行版本默认启用了限制性的防火墙(firewall)；Ubuntu没有启用**
         + 在安装过程，如果不更改或者禁用防火墙，某些步骤会失败

     + 控制节点网络配置

       https://docs.openstack.org/install-guide/environment-networking-controller.html

     + 计算节点网络配置

       https://docs.openstack.org/install-guide/environment-networking-compute.html

     + 块存储节点(可选)网络配置

       https://docs.openstack.org/install-guide/environment-networking-storage-cinder.html

     + 测试连通性
       + 测试节点到网络，及各个节点之间的连通性
       + https://docs.openstack.org/install-guide/environment-networking-verify.html

   ---

4. Network Time Protocol(NTP)

   + 为在各个节点间正确同步服务，需要安装Chrony，一种NTP的实现方法。
+ 配置方式
   
  + 控制节点指向更准确(更低层)的服务器
     + 其他节点指向控制节点
   + Controller node

     + https://docs.openstack.org/install-guide/environment-ntp-controller.html
  + NTP_SERVER : time1.aliyun.com（网络参考）
   + Other nodes
     + 其他节点指向控制节点来进行时钟同步
  + https://docs.openstack.org/install-guide/environment-ntp-other.html
   + 验证NTP操作
  + 节点需要几分钟时间进行同步，尤其是指向控制节点的节点
     + https://docs.openstack.org/install-guide/environment-ntp-verify.html

   ---

5. OpenStack packages

   + 发行版将OpenStack软件包作为发行版的一部分，或者由于其他发行计划而使用其他方法来发行。
   + **在所有节点安装**
   + 主机需包含可用于发行版的最新版本的基础安装包
   + 禁用或删除任何自动更服务，这些服务会影响OpenStack环境
   + for Ubuntu
     + Ubuntu随每个发行版一起发布OpenStack
     + 每两年发行一个Ubuntu LTS releases
     + Ubuntu临时发行版中的OpenStack软件包可以通过Ubuntu Cloud存档提供给先前的Ubuntu LTS
     + 可以直接使用Ubuntu 18.04 LTS 使用OpenStack Queens；直接使用Ubuntu 16.04 LTS使用OpenStack Mitaka，而无需启用Ubuntu Cloud Archive存储库
     + https://docs.openstack.org/install-guide/environment-packages-ubuntu.html
   + for CentOS
     + https://docs.openstack.org/install-guide/environment-packages-rdo.html

   ---

6. SQL database

   + 大多数OpenStack服务使用SQL数据库来存储信息
   + **数据库通常运行在控制节点**
   + 指南中基于发行版使用MariaDB或者MySQL
   + OpenStack服务也支持其他SQL数据库，包括PostgreSQL
   + 如果在OpenStack服务上看到“Too many connections”或者“Too many open files”的错误日志消息，确认连接设置的最大数量是否已正确应用到环境中
   + 在MariaDB中，您可能还需要更改“open_files_limit”配置
   + for Ubuntu
     + 对于Ubuntu16.04,MariaDB更改为使用**“unix_socket Authentication Plugin"**;现在使用**用户凭据(the user credentials(UID))**执行本地身份验证，并且默认情况下不再使用密码身份验证。这意味着，root用户不再使用密码来本地访问服务器
     + 从Ubuntu18.04开始，mariadb-server软件包无法再从默认存储库中获得；要成功安装，在Ubuntu中启用“Universe”库
     + https://docs.openstack.org/install-guide/environment-sql-database-ubuntu.html
   + for CentOS
     + https://docs.openstack.org/install-guide/environment-sql-database-rdo.html

   ---

7. Message queue

   + OpenStack使用消息队列来协调服务之间的操作和状态信息
   + **消息队列通常运行在控制节点**
   + OpenStack支持多种消息队列服务，包括RabbitMQ,Qpid,and ZeroMQ
   + 大多数打包OpenStack的发行版都支持特定的消息队列服务
   + 指南实现了RabbitMQ消息队列服务，因为大多发行版支持该服务
   + for Ubuntu
     + https://docs.openstack.org/install-guide/environment-messaging-ubuntu.html
   + for CentOS
     + https://docs.openstack.org/install-guide/environment-messaging-rdo.html

   ---

8. Memcached

   + 对服务的身份服务认证机制使用Memcached来缓存令牌(tokens)
   + **Memcached服务通常运行在控制节点**
   + 对于生产部署，建议启用防火墙、身份验证和加密的组合来保护其安全
   + for Ubuntu
     + https://docs.openstack.org/install-guide/environment-memcached-ubuntu.html
   + for CentOS
     + https://docs.openstack.org/install-guide/environment-memcached-rdo.html

   ---

9. Etcd

   + OpenStack服务可以使用Etcd(分布式可靠键值存储)，进行分布式键锁定，存储配置，跟踪服务活动性和其他情况

   + **Etcd服务运行在控制节点**

   + for Ubuntu

     + 对于Ubuntu18.04，默认存储库不再有etcd包;需要在Ubuntu中启用“Universe”存储库
     + https://docs.openstack.org/install-guide/environment-etcd-ubuntu.html

   + for CentOS

     + https://docs.openstack.org/install-guide/environment-etcd-rdo.html

     

     

   

   

   

   

   

   

   

   

