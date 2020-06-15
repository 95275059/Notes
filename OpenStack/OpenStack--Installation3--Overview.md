# OpenStack--Installation3--Overview

1. 示例架构

   + 启动一个基础虚拟机或实例，需要至少两个节点（主机）

   + 示例架构是一个最低配置(minimum configuration)，不适用生产系统的安装

   + 示例架构和最小生产体系(minimal production architecture)

     + 网络代理驻留在控制器节点上，而不是一个或多个专用网络节点上（不需要网络节点）
     + 自服务网络的覆盖（隧道）流量通过**管理网络**，而不是专用网络（适用内部网络）

   + 硬件要求

     ![Installation3-1](E:\Notes\OpenStack\Installation3-1.png)

   + 控制节点(Controller)
     + 控制节点运行身份服务(Identity service)、镜像服务(Image service)、安置服务?(Placement service)、计算节点的管理部分、网络节点的管理部分、各种网络代理、仪表板(Dashboard)。
     + 还包括支持性服务,如SQL数据库，消息队列，NTP
     + 可选地，控制节点课运行块存储(Block Storage)、对象存储(Object Storage)、编排(orchestration)和遥测(Telemetry)服务的部分内容
     + 计算节点至少需要两个网络接口
   + 计算节点(Compute)
     + 计算节点运行操作实例的计算节点的管理程序部分
     + 默认情况下，计算节点使用KVM管理程序
     + 计算节点也运行网络服务代理，使实例连接到虚拟网络
     + 通过安全组为实例提供防火墙服务
     + 可以部署多个计算节点；每个节点至少需要两个网络接口
   + 块存储(Block Storage)
     + 块存储节点不是必须的
     + 块存储节点包括块存储和共享文件系统服务提供给实例的磁盘
     + 为简单起见，计算节点与该节点之间的服务流量使用管理网络
     + 生产环境下应实现单独的存储网络以提高性能和安全性
     + 可以部署多个块存储节点；每个节点至少需要一个网络接口
   + 对象存储(Object Storage)
     + 对象存储节点不是必须的
     + 对象存储节点包括对象存储服务用于存储账户、容器和对象的磁盘
     + 生产环境下应该实现单独的存储网络以提高性能和安全性
     + 该服务至少需要两个节点；每个节点至少需要一个网卡

2. 网络

   + 选择一：Provider networks

     ![Installation3-2](E:\Notes\OpenStack\Installation3-2.png)

     + 主要通过第二层（bridging/switching）服务和网络的VLAN分段，使用最简单的方法部署OpenStack网络服务
     + 本质上，它将虚拟网络**桥接**到物理网络，并依赖于物理网络基础结构来进行第三层（路由）服务
     + DHCP服务向实例提供IP地址
     + 这一选择缺乏对自服务（private）网络、第三层(routing)服务以及高级服务（如LBaaS和FWaas）的支持；如果需要这些功能，考虑第二种选择（自服务网络）
     + OpenStack用户需要了解底层网络基础设施信息来创建与基础结构完全匹配的虚拟网络

   + 选择二：Self-service networks

     ![Installation3-3](E:\Notes\OpenStack\Installation3-3.png)

     + 提供第三层(routing)服务，增强了Provider networks
       + 使用诸如VXLAN的覆盖分段方法启用自服务网络
     + 本质上，使用**NAT**将虚拟网络连接到物理网络
     + 这一选择为高级服务，如LBaaS和FWaaS提供了基础
     + OpenStack用户无需了解数据网络上的底层架构即可创建虚拟网络
     + 如果配置了第二层插件，该方案也包含VLAN网络

   

   

   