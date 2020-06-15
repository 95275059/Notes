# OpenStack--Installation8--Install OpenStack services4(Minimal deployment for Queens)--Networking service

1. OverView

   + For more information about the Networking service including virtual networking components, layout, and traffic flows, see the [OpenStack Networking Guide](https://docs.openstack.org/neutron/queens/admin/index.html).
   + OpenStack Networking(neutron)允许您创建由其他OpenStack服务管理的接口设备并将其连接到网络
   + 可以利用**插件(plug-ins)**来容纳不同的网络设备和软件，从而为OpenStack体系结构和部署提供灵活性
   + 组成
     + neutron-service
       + 接收API请求并将其路由到适当的OpenStack网络插件以采取措施
     + OpenStack Networking plug-ins and agents
       + 插入和拔出端口，创建网络或子网，提供IP地址
       + 这些插件和代理因特定云中使用的供应商(vendor)和技术而异
       + OpenStack Networking随附了用于思科虚拟和物理交换机，NEC OpenFlow产品，Open vSwitch,Linux bridging和VMware NSX产品的插件和代理
       + 通用代理是L3(layer 3)，DHCP(dynamic host IP addressing)和一个插件(plug-in)代理
     + Messaging queue
       + 大多数OpenStack Networking安装使用消息队列在neutron服务器和各种代理之间路由信息
       + 同时也作为一个存储特定插件的网络状态的数据库
   + OpenStack Networking 主要和OpenStack Compute进行交互，来为实例提供网络和连接

   ---

2. Networking(neutron) concepts

   + OpenStack Networking(neutron)在OpenStack环境中管理**虚拟网络基础架构(Virtual Networking Infrastructure)(VNI)**的所有网络面以及**物理网络基础结构(Physical Networking Infrastructure)(PNI)**的访问层面
   + 该服务使项目能够创建高级虚拟网络拓扑，其中可能包含防火墙(firewall)，负载平衡器(load balancer)和虚拟专用网络(virtual private network)(VPN)之类的服务
   + Networking包括网络，子网和作为对象抽象的路由器
     + 每种抽象都模仿其物理对应物的功能：网络包含子网，路由器在不同子网和网络之间路由流量
   + 任何给定的网络设置都至少具有一个**外部网络(external network)**
     + 不同于其他网络，外部网络不仅仅是虚拟定义的网络
     + 相反，它代表对OpenStack安装外部可访问的物理外部网络切片的视图
     + 外部网络上的任何人都可以物理访问外部网络上的IP地址
   + 除了外部网络，任何Networking设置有一个或多个**内部网络(internal network)**
     + 这些软件定义的网络直接连接到VMs
     + 只有在任何给定的内部网络上的VMs或者通过接口连接到类似的路由器的子网上的VMs，能够访问直接连接到该网络的VMs
   + 为了使外部网络访问VMs，反之亦然，需要网络之间的路由器
     + 每个路由器有一个连接到一个外部网络的网关和一个或多个连接到内部网络的接口
     + 类似物理路由器，子网能够访问连接在同一个路由器上的其他子网的计算机，并且计算机能够通过路由器的网关访问外部网络
   + 另外，可以将外部网络上的IP地址分配给内部网络上的端口
     + 只要有东西连接到子网，该连接就称为端口
     + 可以将外部网络IP地址与VM的端口关联，这样外部网络的实体可以访问VM
   + 网络服务也支持**安全组(security groups)**
     + 安全组使得管理员可以按组中定义防火墙规则
     + 一个VM可以属于一个或多个安全组
     + 网络服务会将安全组中的规则应用于来阻止或取消阻止该虚拟机的端口，端口范围或流量类型
   + 每个网络服务使用的插件有自己的概念(concepts)
     + 尽管对操作VNI和OpenStack环境并不重要，但了解这些概念可以帮助设置网络
     + 所有网络安装都使用核心插件和安全组插件（或仅使用No-Op安全组插件）
     + 此外，还提供了防火墙即服务(FWaaS)和负载均衡即服务(LBaaS)插件

   ---

3. Install and configure 

   + Networking options

     + Option 1: Provider network
       + 部署了最简单的架构
       + 该架构仅支持将实例附加到提供provider（外部）网络
       + 没有self-service（private）网络，路由器或浮动IP地址
       + 只有`admin`或其他特权用户可以管理provider network
     + Option 2 : Self-service network
       + 通过支持将实例附加到自服务网络的第3层服务增强了provider network
         + demo非特权用户或其他非特权用户可以管理自服务网络，包括在自服务网络和提供商网络之间提供连接的路由器
         + 此外，来自外部网络（例如Internet）的浮动IP地址使用自服务网络提供到实例的连接
       + 自服务网络通常使用覆盖网络
         + 诸如VXLAN之类的覆盖网络协议包括其他标头，这些标头增加了开销并减少了可用于有效负载或用户数据的空间
         + 在不了解虚拟网络基础结构的情况下，实例尝试使用默认的1500字节以太网最大传输单元（MTU）发送数据包
         + 网络服务会通过DHCP自动为实例提供正确的MTU值;但是，某些云镜像不使用DHCP或忽略DHCP MTU选项，而需要使用元数据或脚本进行配置
         + 自服务网络也支持将实例附加到provider network

   + **实验室的安装方案**

     + 使用自服务网络，即Option 2

     + 使用openswitch而不是Linux bridge

       需要网络搜索

   + for CentOS

     + Install and configure **controller node**
       + https://docs.openstack.org/neutron/queens/install/controller-install-rdo.html
     + Install and configure **compute node**
       + https://docs.openstack.org/neutron/queens/install/compute-install-rdo.html
     + verify operation
       + https://docs.openstack.org/neutron/queens/install/verify.html

   + for Ubuntu

     + Install and configure **controller node**

       + https://docs.openstack.org/neutron/queens/install/controller-install-ubuntu.html

     + Install and configure **compute node**

       + https://docs.openstack.org/neutron/queens/install/compute-install-ubuntu.html

     + verify operation

       + https://docs.openstack.org/neutron/queens/install/verify.html

         