# OpenStack笔记3--日志位置

### Nova日志

OpenStack计算服务日志位于**/var/log/nova**，默认权限拥有者是nova用户。需要注意的是，并不是每台服务器上都包含所有的日志文件,例如nova-compute.log仅在计算节点生成

+ **nova-compute.log**：虚拟机实例在启动和运行中产生的日志；仅在计算节点生成
+ nova-network.log：关于网络状态、分配、路由和安全组的日志
+ nova-manage.log：运行nova-manage命令时产生的日志
+ nova-scheduler.log：有关调度的，分配任务给节点以及消息队列的相关日志
+ nova-objectstore.log：镜像相关的日志
+ nova-api.log：用户与OpenStack交互以及OpenStack组件间交互的消息相关日志
+ nova-cert.log：nova-cert过程的相关日志
+ nova-console.log：关于nova-console的VNC服务的详细信息
+ nova-consoleauth.log：关于nova-console服务的验证细节
+ nova-dhcpbridge.log：与dhcpbridge服务相关的网络信息

### Dashboard

Dashboard是一个DJango的web应用程序，默认运行在Apache服务器上，相应的运行日志也都记录在Apache的日志中，用户可以在**/var/log/apache2/**中查看。

### Swift

对象存储Swift默认日志写到syslog中，在Ubuntu系统中，可以通过**/var/log/syslog**查看，在其他系统中，可能位于**/var/log/messages**中。

### Cinder

默认存放在**/var/log/cinder**目录中 

+ cinder-api.log：关于cinder-api服务的细节 
+ cinder-scheduler.log：关于cinder调度服务的操作的细节 
+ cinder-volume.log：与cinder卷服务相关的日志项

### Keystone

在**/var/log/keystone/keystone.log**中

### Glance

默认存放在**/var/log/glance**目录中

根据日志配置的不同，会保存诸如元信息更新和访问记录这些信息。

+ api.log：Glance API相关的日志 
+ registry.log：Glance registry服务相关的日志 

### Neutron

网络服务Neutron的日志默认存放在**/var/log/neutron**目录中 

+ dhcp-agent.log：关于dhcp-agent的日志 
+ l3-agent.log：与l3代理及其功能相关的日志 
+ metadata-agent.log：通过neutron代理给Nova元数据服务的相关日志 
+ openvswitch-agent.log：与openvswitch相关操作的日志项，在具体实现OpenStack网络时，如果使用了不同的插件，就会有相应的日志文件名 
+ server.log：与Neutron API服务相关的日志

### dnsmasq

```bash
[root@controller log]# grep -ir --exclude-dir=dist-upgrade dnsmasq /var/log
```



