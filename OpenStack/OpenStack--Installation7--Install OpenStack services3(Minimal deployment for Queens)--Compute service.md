# OpenStack--Installation7--Install OpenStack services3(Minimal deployment for Queens)--Compute service

1. Overview

   + 使用OpenStack Compute托管和管理云计算系统
   + OpenStack Compute是基础设施即服务(Infrastructure-as-a-Service(IaaS))系统的主要组成部分
   + 主要的模块用Python实现的
   + OpenStack Compute和身份服务交互以进行身份验证；和镜像服务交互获取磁盘和服务器镜像；和Dashboard交互获取用户和管理员接口；
     + 镜像访问受项目、用户的限制
     + 每个项目都限制配额(例如，实例数)
     + OpenStack Compute可以再标准硬件上水平扩展，并下载镜像以启动实例
   + 组成
     + nova-api service
       + 接收并响应来自终端用户计算API调用
       + 该服务支持OpenStack Compute API
       + 它执行一些策略并启动大多数编排活动，例如运行实例
     + nova-api-metadata service
       + 接收来自实例的元数据请求
       + 在用户在使用nova-network安装时以多主机模式运行时，通常会使用该服务
       + For details, see [Metadata service](https://docs.openstack.org/nova/queens/admin/networking-nova.html#metadata-service) in the Compute Administrator Guide.
     + nova-compute service
       + 一个通过管理程序API创建和终止虚拟机实例的守护程序，例如:
         + 适用于XenServer/XCP的XenAPI
         + 适用于KVM或者QEMU的libvirt
         + 适用于VMware的VMwareAPI
       + 进程是非常复杂的
       + 基本上，守护程序接收从队列接收操作，并运行一系列系统命令(例如，启动KVM实例并更新其数据库中的状态)
     + nova-placement-api service
       + 跟踪每个provider的库存和使用情况
       + For details, see [Placement API](https://docs.openstack.org/nova/queens/user/placement.html).
     + nova-scheduler service
       + 从队列中获取虚拟机实例请求，并确定它在哪台计算服务器主机上运行
     + nova-conductor module
       + nova-compute服务和数据库之间交互的中介
       + 该模块消除了nova-compute服务对云数据库的直接访问
       + 该模块水平缩放
       + **但是，不要将这个模块部署在nova-compute服务运行的节点上**
       +  For more information, see the `conductor` section in the [Configuration Options](https://docs.openstack.org/nova/queens/configuration/config.html).
     + nova-consoleauth daemon
       + 由控制台代理提供给用户的授权令牌
       + 参照nova-novncproxy和nova-xvpvncproxy
       + 该服务必须为控制台代理运行工作
       + 可以在集群配置中针对单个nova-consoleauth服务运行这两种类型的代理
       + For information, see [About nova-consoleauth](https://docs.openstack.org/nova/queens/admin/remote-console-access.html#about-nova-consoleauth).
     + nova-novncproxy daemon
       + 提供用于通过VNC连接访问正在运行的实例的代理
       + 支持基于浏览器的novnc客户端
     + nova-spicehtmlSproxy daemon
       + 提供用于通过SPICE连接访问正在运行的实例的代理
       + 支持基于浏览器的HTML5客户端
     + nova-xvpvncproxy daemon
       + 提供用户通过VNC连接访问正在运行的实例的代理
       + 支持特定于OpenStack的Java客户端
     + The queue
       + 在守护程序之间传递消息的中央中心
       + 通常使用RabbitMQ实现，也可以使用其他AMQP消息队列(例如ZeroMQ)实现
     + SQL数据库
       + 存储云基础架构的大多数构建时和运行时状态，包括
         + 可用实例类型
         + 使用中的实例
         + 可用网络
         + 项目(Projects)
       + 理论上来讲，OpenStack Compute可以支持任何SQLAlchemy支持的数据库；常见的数据库是用于测试和开发工作的SQLite3和MySQL,MariaDB和PostgreSQL

   ---

2. Install and configure **controller node**

   + for Ubuntu
     + https://docs.openstack.org/nova/queens/install/controller-install-ubuntu.html
   + for CentOS
     + https://docs.openstack.org/nova/queens/install/controller-install-rdo.html

   ---

3. Install and configure a **compute node**

   + Compute service支持多个虚拟机管理程序以部署实例或虚拟机实例（VMs）
   + 为简单起见，此配置在支持虚拟机硬件加速的计算节点上使用带有基于内核的VM（KVM）扩展的Quick EMUlator(QEMU)管理程序；在旧硬件上，此配置使用通用QEMU管理程序
   + 可以对这些说明进行少量修改，以通过其他计算节点水平扩展您的环境

   + for Ubuntu
     + https://docs.openstack.org/nova/queens/install/compute-install-ubuntu.html
   + for CentOS
     + https://docs.openstack.org/nova/queens/install/compute-install-rdo.html

   ---

4. Verify operation

   + **在控制节点运行**
   + https://docs.openstack.org/nova/queens/install/verify.html

   

