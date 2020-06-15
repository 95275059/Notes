---
title: Linux笔记--远程登录管理工具
date: 2019-04-15 20:54:41
tags: CSDN迁移
---
 [ ](http://creativecommons.org/licenses/by-sa/4.0/) 版权声明：本文为博主原创文章，遵循[ CC 4.0 by-sa ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。  本文链接：[https://blog.csdn.net/zhaandzha/article/details/89316436](https://blog.csdn.net/zhaandzha/article/details/89316436)   
    
   1.虚拟机网络配置

 **桥接模式**：虚拟机用真实网卡和真实PC连接。

 好处：只要虚拟机IP地址和PC机/其他机处于同一网段，虚拟机就可以和真实机连接；操作简单；

 坏处：会占用网段的一个IP，可能会出现IP地址冲突

 **NAT模式**：虚拟机通过一块虚拟网卡进行通信。 --对应虚拟网卡VMnet8

 虚拟机只能和自己的真实机通信，不能和局域网中的其他PC机通信。

 不会占用真实的IP地址；若真实机能够访问互联网，虚拟机也可以访问互联网

 **Host-only(仅主机模式)**:虚拟机通过一块虚拟网卡进行通信。 --对应虚拟网卡VMnet1

 虚拟机只能和自己的真实机通信，不能和局域网中的其他PC机通信。

 不会占用真实的IP地址；

 2.ip addr :查看网卡情况

 loopback(环回网卡)(lo):所有操作系统都有；主要用来做本机通信和测试；127.0.0.1

 **3.激活网卡**

 (1)切换路径:cd /etc/sysconfig/network-scripts

 (2)查看该路径下文件:ls

 ![](https://img-blog.csdnimg.cn/20190415201340286.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70)

 (3)编辑(第一个)文件:vi ifcfg-ens33

 ![](https://img-blog.csdnimg.cn/20190415201815339.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70)

 将ONBOOT=no 改为ONBOOT=yes;

 esc:wq保存修改后退出

 (4)重启网卡服务：service network restart

 

 4.设置虚拟机IP地址

 保证虚拟机IP地址同真实机下的虚拟网卡VMnet1的IP地址处于同一网段，同样需要在ifcfg-ens33文件中进行修改

 例如若使用仅主机模式，则查询VMnet1的IP地址后得知为192.168.216.1 则设置虚拟机IP地址为192.168.216.2

 若使用NAT模式，则查询VMnet8的IP地址后得知为192.168.58.1 则设置虚拟机IP地址为192.168.58.2

 **设置centOS7静态IP**

 (1)进入ifcfg-ens33修改

 需要手动修改或添加的有：

 BOOTPROTO=static

 IPADDR=192.168.216.2

 NETWORK=255.255.255.0

 保存后退出：esc:wq

 ![](https://img-blog.csdnimg.cn/20190415210149255.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70)

 (2)重启网卡服务：service network restart

 

 注：桥接模式下，虚拟机的IP地址和真实机的IP地址处于同一网段。此时可能出现ping不通的情况，原因可能是，若真实机是有线连接(无线连接)，虚拟机可能桥接到无线连接(有线连接)上。此时需要打开虚拟网络编辑器，手动修改桥接到的真实机的网络连接。

 5.SSH远程连接管理工具:finalshell或者Xshell5

 6.文件拷贝工具:Winscp

   
