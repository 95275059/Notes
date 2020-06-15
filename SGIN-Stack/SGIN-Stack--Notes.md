# SGIN-Stack--Notes

1. SGIN

   + 大规模时变网络
   + 高度异构的复杂网络
   + 组成
     + 天基骨干网络
     + 天基接入网络
     + 地基骨干网络
   + 特点
     + 可变延时和BER
     + 卫星之间不稳定的端到端路径
     + 卫星操纵
     + 安全问题
       + 接入控制
       + 身份认证
       + 隐私保护
       + 恶意软件和攻击检测

   ---

2. SGIN-Stack

   + 实现了OpenStack 和STK的无缝高效链接，从而实现了对SGIN动态，精确，实时的网络仿真
     + OpenStack生成的仿真网络能够被STK计算的准确的数据动态地驱动
     + 仿真网络的任何动态变化（如，卫星轨道操纵和姿态调整）可以促使STK实时地重新计算数据
   + SGIN-Stack不仅整合了TC工具和SDN，也在OpenStack中集成了动态查分补偿技术和随机数算法
     + 实现对可变延时、BER、卫星间不稳定的端到端路径的更加精准地仿真
   + **主要优势**
     + 实现了OpenStack 和STK的无缝高效链接
       + 对SGIN的真实仿真
       + 对SGIN动态变化的实时仿真
         + 如，不稳定的端到端路径和卫星操作
     + 动态差分补偿技术和随机数算法
       + 提高了卫星链路仿真精度
     + 采用了两种虚拟化方法（KVM,Docker），以利用两种虚拟化方法的独特优势
       + 天机骨干卫星节点和网关站节点采用KVM
         + 满足天机骨干卫星链路的高吞吐量要求
       + 天机卫星接入节点采用Docker
         + 实现物理资源的快速部署和有效利用

   ---

3. Section 1--Introduction

   + 基于云平台和虚拟化技术的网络仿真
     + 基于商品云平台的网络协议仿真平台CloudNet（然后引出OpenStack）
       + 采用名为LXC容器的轻量级虚拟化技术，可实现上千个节点的仿真网络
     + 基于Opensatck的网络仿真平台EmuStack
       + 实现对DTN（Delay tolerant Networks）的实时网络仿真和对卫星网络特征（bandwidth,delay,BER）的时变仿真
       + 忽略了卫星操纵的功能，这需要实时仿真SGIN的动态变化（如，卫星的实时管理策略）（然后引出SGIN-Stack）
   + SGIN-Stack
     + 基于OpenStack，结合SDN,KVM,Docker技术，SGIN-Stack实现了SGIN节点的高逼真仿真和SGIN链路的高吞吐量和灵活性
     + SGIN-Stack的仿真源数据（卫星轨道数据，大气将于衰减模型和卫星链路的通信计算）由STK计算

   ---

4. Section 2--Related work

   + STK

     + 可用于各种卫星性能分析的商用软件包
       + 测试新的理论方法的有效性
       + 航天器仿真的详细动画
       + 网络拓扑的设计
       + 卫星操纵的评估
     + 特点
       + 在卫星网络的建模和分析方面很强
       + 缺乏网络性能分析机制
         + 无法对卫星网络中的网络协议，动态吞吐量和安全通信方法进行仿真

   + 弥补STK缺陷的相关工作

     + 文献33提出了一种在STK设计卫星星座拓扑然后将数据提取到ns-2离散时间模拟器中，以评估卫星网络的网络性能

       Topology design and performance analysis for networked earth observing small satellites

     + 文献36结合STK和QualNet网络模拟器对有Internet协议的通信进行建模

       Rf communication data model for satellite networks

     + 文献10和18基于离散事件模拟器（例如，OMNeT++,QualNet），评估了基于区块链的SGIN认证方案

   + 由于网络仿真难以模拟复杂的环境，提供更相关和更全面的细节，以及难以生成逼真的数据流，因此评估技术的趋势已从仿真变为实验性测试平台

   + 文献20通过应用SDN,虚拟化技术，提出了一个大规模，可重配置和灵活的用于仿真空间信息网络的仿真平台

     + 能够仿真卫星节点的物理特征（如，CPU频率，内存，操作系统等）
     + 能够仿真卫星节点之间的链路特征（如，通信速率，BER，延时等）
     + 能够仿真从STK获取的链路特征的源数据

     **SGIN-Stack不仅能仿真可变特征，还能够模拟卫星的操纵**

   + 文献8提出了基于OpenStack的DTN网络仿真平台EmuStack

     + 使用Docker实现大规模拓扑
     + 在OpenStack上集成TC和STK，以对卫星链路特征进行仿真

     **SGIN-Stack除了集成了TC和STK，还集成了动态差分补偿技术和随机数算法来提高卫星链路仿真的准确性**

     **SGIN-Stack比EmuStack在STK和OpenStack之间实现了更加无缝的链接，以仿真SGIN的动态变化，同时更有可能用于评估启动了区块链的SGIN**

   + 文献21设计了一个用于评估DTN的测试平台TUNIE
     + 使用虚拟化技术和SDN来实现一个真实可靠的DTN环境
     + 通过控制数据传输实现了时变比特率，错误率和传输延时
     + 但是，TUNIE需要集成更丰富的模型来仿真高度异构复杂SGIN

   ---

5. Section 3--Architecture of SGIN-Stack

   + SGIN-Stack架构是基于OpenStack的云架构

   + 整个平台架构采用SDN的设计思想

   + 采用多尺度集成的思想，结合全虚拟化和轻量级虚拟化技术

     + 天机骨干卫星节点和网关站节点采用全虚拟化技术KVM
       + 满足天机骨干卫星链路的高吞吐量要求
     + 天机卫星接入节点采用轻量级虚拟化技术Docker
       + 实现物理资源的快速部署和有效利用

   + 组成结构

     + 网络节点（Network node）
       + 充当控制平面（云平台）
     + STK仿真节点（STK simulation node）
       + 充当数据平面
     + 多个物理仿真节点（Physical emulation nodes）

     **所有节点采用NTP（Network Time Protocol）并且使用控制节点作为统一的时间轴，从而保证了SGIN-Stack中所有节点的实时操作和同步**

     ---

     ---

   + STK仿真节点（STK simulation node）

     + STK11

     + MATLAB R2013a

     + STKX模型（TCP/IPsocket）

       提供STK和MATLAB的双向通信

     + Coordinated control module(协调控制模块)
       
       + 负责根据来自仿真节点的反向链路控制模块的命令反向控制STK
     + STK reports acquisition module(STK报告获取模块)
       
       + 负责获取链路特征数据的报告然后实时地传输给链路性能控制模块
     + Topology monitor(拓扑监视模块)
       
       + 负责监视STK中拓扑的动态变化，然后拓扑链路控制模型相应的改变SGIN仿真网络

     ---

   + 物理仿真节点（Physical emulation node）

     + Topology linkage control module(拓扑链路控制模块)
       + 负责和STK中SGIN计算模型的拓扑保持一致
       + **举例：如果STK中添加了一颗卫星**
         + 该模块可以感知到这样的事件
         + 向OpenStack的nova调度程序服务发送创建请求
         + 向nova计算服务发送远程过程调用请求，从glance获取已创建节点的image，并在计算节点的hypervisor管理程序上启动该节点
         + 此后，网络服务neutron将向虚拟卫星节点分配一个硬件设备（例如网卡）和IP地址
     + Link characteristics linkage control module(链路性能控制模块)
       + **实时**动态地控制卫星链路的性能（如，间歇性，延时，BER和带宽）
     + Reverse linkage control module(反向链路控制模块)
       + 用于反向控制STK中SGIN计算模型
       + 同时在一些场合下适用
         + 控制轨道机动
         + 卫星姿态
         + 太阳能电池板

     ---

   + 网络节点（Network node）

     + 虚拟卫星节点在物理仿真节点上运行
     + OpenStack使用支持OpenFlow协议的OpenvSwitch(OVS)来提供与虚拟卫星节点的第二层链接
     + Neutron-plugin-agent
       + 负责管理逻辑网络
     + Neutron-l3-agent
       + 一个网络节点的Neutron-l3-agent向虚拟卫星节点提供了静态路由
     + Neutron-dhcp-agent
       + 实现了DHCP，向虚拟卫星节点提供IPs

   ---

6. Section 4--Implementation of SGIN-Stack

   + Topology linkage control module

     +  负责使OpenStack中SGIN的仿真拓扑和STK中SGIN计算模型的拓扑保持一致
     + MATLAB是监听者的角色
       + 接收STK中SGIN的拓扑
       + 在STK中的拓扑变化时，指导OpenStack调整SGIN网络拓扑
     + 在接收到来自MATLAB的拓扑监听模块发来的**连接矩阵**后，拓扑连接控制模块在仿真过程中动态地改变拓扑
     + 动态改变SGIN仿真拓扑的原理
       + 通过配置OpenStack中的OVS流表来实现
       + 该模块获取虚拟卫星节点在OVS上的设备头(device tap)的对应信息
         + MAC address
         + VLAN label
         + IP address
       + **当卫星链路从正常通信状态变为中断状态**
         + 设备头和OVS的虚拟链路可以通过OpenStack的‘del-port‘ 接口来断开
         + 相应的VLAN标签和流表规则被删除
         + 最后该条链路无法传输任何数据
       + **当卫星链路从中断状态变为正常的通信状态**
         + 通过OpenStack的’add-port‘接口来重建一条链路
         + 该模块创建一个与ARP和IP数据包匹配的流表规则

     ---

   + 链路性能控制模块

     + 带宽和延时控制

       + 卫星链路的延时是动态变化的
         + 因为链路的长度是持续变化的
         + 延时的变化导致了吞吐量的动态变化
       + 在SGIN-Stack,有两个位置可以设置带宽和延时
         + 虚拟节点中的NIC驱动
           + 由于要向虚拟节点发送命令来限制速率，所以花费时间更久；同时这些时间会影响延时的仿真
         + OVS上的设备头（device tap）
           + 比起NIC驱动，控制设备头设置带宽和延时更加高效
         + **因此，选择第二种方法设置带宽和延时**
       + 卫星链路是定向的
         + 链路A-B和链路B-A是不同的
       + **举例:基于OVS的一条链路“sate1-sate2”**
         + 使用TC在OVS的设备头上添加HTB规则，以限制虚拟卫星链路的带宽
         + 需要发送的数据包在虚拟卫星sate1的内核控件的发送缓冲区中
         + 被发送到虚拟卫星sate2的数据包将首先被iptables过滤
         + 当数据包到达OVS的设备头2，内核中的’dev_queue_xmit‘函数释放数据包，将其放入Qdisc缓冲区进行整形
           + 该模块调用Linux内核中的Netem模块，以动态地限制设备头的带宽
           + 整个设备头的队列类似一个树结构
           + 数据包首先通过设备头的根队列然后进入根分类
           + 一个分类可以有多个子分类
           + 该模块添加HTB队列规则像Netem规则一样限制带宽
         + 然后，'hard_start_xmit'将数据包发送到NIC驱动

       ---

     + 延时补偿

       + SGIN-Stack中的卫星链路
     
         + 主机内虚拟链路（intra-host virtual link）
           + 一条链路的两个虚拟卫星在同一物理仿真节点
           + 存在一个物理仿真节点的传输延时
         + 跨主机虚拟链路（cross-host virtual link）
           + 一条链路的两个虚拟卫星在不同的物理仿真节点
         + 存在在两个物理仿真节点之间的基础物理链路的传输延时
           + 这种情况造成的传输延迟更加严重

         **这两种链路都会降低卫星链路延时仿真的准确性**
     
       + 动态可配置的延时差分补偿方法
         + 可以通过获取开始时间T1和到达时间Tn来实现传输延时的差分补偿
         + 具体方法
           + 在虚拟链路上设置一个消息发送队列用于发送由源卫星生成的数据包
           + 在数据包被源卫星网卡发送后，队列自动匹配从源卫星到目的卫星的数据包
           + 合格的信息将发送到NFQUEUE发送队列，然后队列获取当前的时间戳T1，以用户模式截获信息并将T1分装在数据包的尾部
           + 目的卫星创建一个消息NFQUEUE接收队列；在数据包进入目的卫星的网卡后，队列自动匹配并截获从源卫星发送来的数据包，并且对数据包的数据部分进行解析，以获得T1；然后获取当前时间戳；
           + 然后动态地补偿链路传输延迟以提高卫星延时仿真的准确性
       
       ---
       
     + BER控制
     
       + SGIN-Stack通过丢弃数据包来对BER进行仿真
     
       + BER控制原理
     
         + 符合指定匹配约束的数据包进入指定队列，并且不同的卫星链路具有不同的约束。当分组进入队列时，产生随机数。分组是被丢弃还是被接收取决于随机数和BER的比较。
     
         + 当数据包被发送者发送，链路性能控制模块会生成一个随机数
         + 该随机数会和当前虚拟卫星链路的BER相比较
         + 如果随机数在在BER的范围内，那么就假定在这个包里面会发生比特错误（误码），则该包就会被丢弃，那个这个分组不会进入缓冲队列；否则该包会进入缓冲队列
         + 因此，正确控制BER的关键是有一个好的随机数生成算法
     
       + 计算机生成的伪随机数具有一定的相关性
     
       + 随机数生成算法
     
         + 改进了线性同余生成器（Linear Congruential Generator）(LCG)
     
         + 过程
     
           + 对LCG进行初始化
     
           + 提供两个参数：'lower_limit','upper_limit'
     
           + 设置不过大过小的阈值(threshold)
     
             + 随着随机数的相关性下降，阈值的提高会使随机数的生成时间提高
     
             + 测试表明，随机数生成算法生成的随机数在阈值为10时，有良好的随机性
     
           + 之后，使用LCG生成10个随机数然后把他们放入一个名为Random_set的数组
     
           + 最后，由LCG生成在‘lower_limit’和'upper_limit'之间的随机数，以及在“随机”集中具有相应索引的数字是最终的随机数
     
       ---
     
     + 反向链路控制模块
     
       + 卫星轨道机动，卫星太阳能电池板，卫星姿态和星载摄像机的仿真对于一些SGIN方案（例如基于天地的接入网）至关重要。
       + 尽管OpenStack不提供任何支持以上行为的服务，但是STK能够完全弥补这一缺陷
       + 卫星根据控制系统的要求改变轨道，进行轨道机动
       + 将卫星从高轨道转移到低轨道，反之亦然，以及根据用户需求调整卫星监视区域，需要进行轨道操纵
       + STK的姿态控制模块解决了在STK的3维图形窗口控制对象姿态的问题
       + 正因为有姿态控制模块，STK中的三位对象不再是一个恒定的模型，而是一个有多重作用（例如随时间旋转）的对象
       + **反向链路控制过程**
         + OpenStack中的虚拟地面站节点向虚拟卫星节点发送命令以要求卫星改变其轨道，，调整太阳能电池板或者姿态，或者拍摄照片
         + 虚拟卫星节点在收到命令后，将命令发送到反向链路控制模块，然后该命令将被发送到STK仿真节点中的协同控制模块
         + MATLAB调用适当的接口函数来调节STK中的SGIN计算模型
         + STK中相应的卫星仿真节点的轨道，太阳能电池板和姿态会根据指示进行调整
         + 最后，OpenStack中相应的虚拟链路的链路性能会被改变
       + **以轨道机动控制为例**
         + 反向链路控制模块收到参数调整的指令
         + MATLAB使用主函数'stkSetPropClassical'来控制STK计算模型中相关卫星的轨道机动
         + 最后，SGIN-Stack基于STK中新的计算模型更新SGIN仿真网络，OpenStack中相应的网络拓扑和虚拟卫星链路将被更新
       + 卫星轨道的六个参数
         + 半长轴(semimajor axis)
         + 偏心率(eccentricity)
         + 近地点中心角(perigee central angle)
         + 上升节点的右上角(right ascension of the ascending node)
         + 轨道倾角(orbital inclination)
         + 近点角(near-point angle)
       + **STK提供标准的姿势定义或外部输入的手势文件，以启用各种分析工具来计算姿态变化对其他参数的影响**

   ---

7. Section 5--Experiments

   + 实验一

     + 在一个SGIN下对链路的间歇性、带宽、延时和BER进行实时仿真，以表示SGIN-Stack的高逼真度

   + 实验二

     + 构建了一个包含卫星轨道机动、姿态和太阳能电池面板的仿真场景，以证明SGIN-Stack能够执行SGIN的动态实时网络仿真

   + 典型场景拓扑

     + 组成结构
       + 一个天基接入网络
         + 66个LEO卫星(LEO:低轨道卫星)
           + 6个轨道平面
           + 地面用户可以连接到SGIN以拨打卫星电话，并可以通过天基接入网络在任何地方使用导航服务
       + 一个天基骨干网络
         + 6个GEO卫星（GEO:位于赤道上方35800km的对地同步卫星）
           + 一个轨道
           + 负责长距离通信和信息交换
       + 一个地面网络

     + DOP(dilution of precision)（精度稀释因子或误差放大因子）
       + 几何精度稀释（GDOP）、位置精度稀释（PDOP）、垂直精度稀释（VDOP）、水平精度稀释（HDOP）与时间精度稀释（TDOP）
       + 常常用于卫星导航，量化位置测量精度的影响
       + GDOP(Geometric DOP)
         + 用于确定测量误差将如何影响卫星的最终估计状态
         + 理想的GDOP值是1，该值表示对精度的高置信度
     + STK具有内置的DOP品质因数（FOM）
       + 用于测量卫星的几何形状和覆盖质量
       + 有一些DOP可供选择，包括GDOP，它可以测量整个导航解决方案（具有与位置和时钟相关的组件）精度的稀释因子
     + GDOP测试结果(Fig.7)
       + GDOP的形状变化，在短的时间迁移下，在同一纬度线上相似
       + 经度的变化对卫星的可见度和GDOP的影响很小
       + 由三个高纬度地区的GDOP平均值低于2，可以得出结论，天基接入网可以满足高纬度地区的通信和定位的需求
     + GEO星座覆盖率(Fig.8)
       + 天基骨干接入网络能够覆盖全球，满足设计要求

     ---

   + 在SGIN-Stack上的仿真

     + 实验环境
       + OpenStack Mitaka
         + 一个计算节点
         + 一个网络节点
         + 两个物理仿真节点
           + 硬件：Dell PowerEdge R830服务器
           + 两个Inter(R) Xeon(R) E5-4620 v4处理器
           + 64GB of RAM
         + 物理仿真节点通过10吉比特（Gigabit）交换机连接
         + 四个物理节点运行CentOS 7 Linux
         + 实验显示一个Dell PowerEdge R830服务器能够承载17个KVM虚拟卫星节点和几百个Docker虚拟卫星节点

       ---
       
     + SGIN的仿真拓扑

       + 一个物理仿真节点使用Docker方法部署天基接入网络
         + 6个轨道平面，每个轨道11颗LEO卫星
       + 另一个物理仿真节点采用KVM模式部署天基骨干网络
         + 六个GEO卫星
         + 一个地面站SHStation
       + 仿真网络共包含268条卫星链路
         + **inter-satellite links(ISL) 卫星间链路**
           + 指在同一高度的轨道上的两颗卫星之间的链接
           + 它可以分为**平面间链路（inter-plane link）**和**平面内链路（intra-plane link）**
           + 对于ISL并且intra-plane link，卫星之间是相对静止的
         + **inter-orbital links(IOL)**
           + 指在不同高度的轨道上的两颗卫星之间的链接
         + **gateway-satellite links(GWL)**
           + 指在卫星和地面站之间的链路
       + 仿真平台中的链路仿真模块基于多线程，并使用多线程从内存中获取所有链路的链接仿真数据，并动态控制所有虚拟链路的链路特性

       ---

     + 延时仿真

       + Fig.10(Comparision of theoretical delay and actual delay)

         + 比较了五个典型卫星链路在仿真平台中延时的实际值和STK中的理论值
         + 时间从10 Aug 2018 08:00:00到10 Aug 2018 08:40:00
         + 链路是单向的，即延时是一个方向的
         + 链路LEOA1-LEOA2和GEO1-GEO2是ISL,并且是平面内链路（intra-plane link）
           + 链路的延时曲线几乎是直线
         + 链路LEOA1-LWOB1是ISL，并且是平面间链路（inter-plane link）
         + 链路LEOA1-GEO1是IOL
         + 链路LEOA1-SHStation是GWL
           + 在8:24中断，因为卫星LEOA1不可见
         + 实验数据结果表明，仿真平台中的延时和STK中的理论延时非常相近
       + Fig.11(Comparison of delay emulation on EmuStack and SGIN-Stack)
         + EmuStack
           + 使用TC在源卫星的网卡创建Netem queue
           + 不考虑虚拟和物理链路的传输延迟
           + EmuStack无法动态补偿传输延迟
         + EmuStack的精确度不如SGIN-Stack高
         + 比较实验
           + Fig.11(a) IOL
             + LEOA3 and GEO3
           + Fig.11(b) ISL
             + LEOA1 and LEOA3
           + Fig.11(c) ISL
             + GEO1 and GEO3
           + 每个测试使用100个延迟的数据
           + SGIN-Stack上延迟仿真的平均错误约为0.1ms
           +  EmuStack的最大误差约为0.44ms，总误差波动约0.4ms

       ---

     + BER仿真

       + Fig.12(Emulation of BER)
         + LEOA1 and LEOA2
         + 预定的BER值在5%到50%
         + 每次评估发送100个包
         + 实验结果显示随机数生成算法是可行的

       ---

     + 带宽和间歇性仿真

       + LEOA1 and SHStation
       + Fig.13(Access times between LEOA1 and SHStation)
         + 仿真阶段从10 Aug 2018 00:00:00 到 11 Aug 2018 00:00:00
         + 共五次访问时间，每次访问时间持续大约20分钟
       + Table 2(Link characteristics parameters of link LEOA1-SHStation)
       + Fig.14(Bandwidth and intermittence of link LEOA1-SHStation)
         + 显示在SGIN-Stack上的带宽和访问时间
         + 理论带宽200KB/s
         + SGIN-Stack的吞吐量是一分钟的平均值，而延时导致了吞吐量的下降；
         + SGIN-Stack中吞吐量在200KB/s以下，但是分接近200KB/s
         + 实验结果表明，SGIN-Stack中链路的吞吐量和间歇性和STK中的结果较为匹配

       ---

     + 反向链路控制仿真实例

       + 以卫星'test'和'test1'为例
       + 卫星轨道参数
         + 以大约192 km的近地点高度送入轨道，其远地点的高度大约为570 km
         + Table 3(Initial state of satellite 'test' and 'test1')
       + 卫星'test'最初遵循固定的运行轨道，而卫星'test1'始终遵循固定的运行轨道
       + 'test'和'test1'之间的链路'test-test1'
       + **实验1：对'test'的轨道机动命令**
         + Fig.15(satellite 'test'. (a) Orbit maneuver. (b) LLA Position)
           + 描述了其从椭圆形轨道变为圆形轨道的轨道操纵的过程
           + Fig.15(a) : 椭圆轨道--青色 ; 圆形轨道--红色
           + Fig.15(b)
             + 大约在6:45 a.m.进行了轨道空中
             + 'test'卫星的动量发生了积极变化，轨道从椭圆形轨道变为半径约570公里的圆形轨道
         + Fig.16(Delay of satellite link test-test1 on SGIN-Stack)
           + 6:45之前，链路延时的曲线比较平缓
           + 6:45之后，链路延时的曲线突然增大
             + 因为卫星'test'处于轨道操纵的过程，而test-test1的链路长度越来越长
         + Fig.17(Deployment of solar panels and attitude angle of coordinate system. (a)(b)(c) ψ=20°,θ=7°,Φ=7°. (d) ψ=0°,θ=2°,Φ=2°)
           + 卫星体坐标系相对于轨道坐标系的姿态角为ψ=20°,θ=7°,Φ=7°
           + 卫星太阳能滑浪风帆展开后，卫星的姿态角变为ψ=0°,θ=2°,Φ=2°
         + 可以看出，SGIN-Stack在STK中实现了SGIN计算模型的轨道操纵，姿态和太阳板的链接控制

       

       

       

     

     

