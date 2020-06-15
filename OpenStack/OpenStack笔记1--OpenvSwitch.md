# OpenStack笔记1--OpenvSwitch

1. OpenSwitch定义
   + 简称OVS
   + 一个虚拟机交换软件
     + 主要用于虚拟机VM环境，作为一个**虚拟交换机**
     + 支持Xen/XenServer;KVM;VirtualBox等多种虚拟化技术
     + 支持多个物理机的分布式环境
   + 使用开源Apache2.0协议，主要实现代码为可移植的C代码
   + 目的是让大规模网络自动化可以通过编程扩展，同时仍然支持标准的管理接口和协议（例如NetFlow, sFlow, SPAN, RSPAN, CLI, LACP, 802.1ag）
   + 在这种某一台物理机器的虚拟化环境中，一个**虚拟交换机(vswitch)**主要的作用
     + 传递虚拟机VM之间的流量
     + 实现VM和外界网络的通信
     + 