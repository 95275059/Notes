# OpenStack笔记2--OpenFlow

1. SDN(Software Defined Network)

   + 基于OpenFlow实现
     + 实现了数据转发层和控制层的分离
       + OpenFlow在OpenFlow交换机上实现数据转发，而在控制器上实现数据的转发控制
   + 交换设备的数据转发层和控制层是分离的
     + 因此，网络协议和交换策略的升级只需要改动控制层
   + 在网络中实现了软硬件的分离以及底层硬件的虚拟化，为网络的发展提供了一个了良好的发展平台

2. OpenFlow

   + OpenFlow的原理和基本架构

     ![OpenStack笔记2-1](E:\Notes\OpenStack\OpenStack笔记2-1.jpg)

   + OpenFlow规范

     + OpenFlow端口(Port)

       + 将Switch上的端口分为三类

         + 物理端口

           设备上物理可见的端口

         + 逻辑端口

           在物理端口基础上由Switch设备抽象出来的逻辑端口

           如，为tunnel或者聚合等功能而实现的逻辑端口

         + OpenFlow定义的端口
           + OpenFlow目前总共定义了八种端口
             + ALL；CONTROLLER；TABLE；IN_PORT；ANY；LOCAL；NORMAL；FLOOD
             + 后三种不是必须的端口，只在混合型的OpenFlow Switch(OpenFlow-hybrid Swtich，即同时支持传统网络协议栈和OpenFlow协议的Switch设备)中存在

       + OpenFlow的FlowTable

         + OpenFlow通过用户定义的或者预设的规则来匹配和处理网络包

         + 一条OpenFlow的规则由匹配域(Match Fields)、优先级(Priority)、处理指令(Instructions)和统计数据(如Counters)等字段组成

           ![OpenStack笔记2-2](E:\Notes\OpenStack\OpenStack笔记2-2.jpg)

           

         

         