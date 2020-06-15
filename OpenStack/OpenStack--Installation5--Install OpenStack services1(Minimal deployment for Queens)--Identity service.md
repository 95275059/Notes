# OpenStack--Installation5--Install OpenStack services1(Minimal deployment for Queens)--Identity service

1. **安装在控制节点**

2. 基于可扩展的目的，指南的配置部署了Fernet令牌和Apache HTTP服务来处理请求

3. Overview

   + OpenStack Identity服务提供了一个集成点，用于管理身份验证、授权和服务目录
   + 身份服务通常是用户接触的第一个服务
     + 身份验证成功后，用户可以使用其身份去访问其他OpenStack服务
     + 同样，其他OpenStack服务利用身份服务来确保用户是他们所说的人，并且发现其他服务在部署中的位置
     + 身份服务也能和某些外部用户管理系统(如,LDAP)集成
   + 用户和服务可以使用由身份服务管理的**服务目录**来查找其他服务
     + 服务目录是OpenStack部署中可用服务的集合
     + 每个服务可以具有一个或多个**端点(endpoints)**，并且每个端点可以是一下三种类型之一：admin、internal、public
       + 在生产环境中，处于安全原因，不同的端点类型可能驻留在暴露给不同类型的用户的单独的网络上
         + 例如，**public API**网络可能在Internet上可见，因此客户可以管理其云
         + **admin API**网络可能仅限于管理云基础架构的组织内的运营商
         + **internal API**网络可能仅限于包含OpenStack服务的主机
     + OpenStack支持多个**区域**以实现可扩展性
     + 为简单起见，指南对所有端点类型和默认的“RegionOne”区域使用管理网络
     + 身份服务中创建的区域(regions)、服务(services)和端点(endpoints)共同构成了部署的服务目录
     + 部署中的每个OpenStack服务需要一个存储在身份服务中的有相应端点的服务条目；这可以在安装和配置了身份服务之后完成
   + 身份服务包含如下组成部分
     + Server
       + 集中式服务器使用RESTful接口，提供验证和验证服务
     + Drivers
       + Drivers或者服务后端(service back end)已集成到集中式服务器；它们用于访问OpenStack外部存储库中的身份信息，并且可能已经存在于部署OpenStack的基础架构中(如，SQL数据库或者LDAP服务器)
     + Modules
       + 中间件模块(middleware modules)在使用身份服务的OpenStack组件的地址空间中运行
       + 这些模块拦截服务请求，提取用户凭据，并将其发送到集中式服务器进行授权
       + 中间件模块和OpenStack组件之间的集成使用Python Web服务器网关接口

   ---

4. for Ubuntu

   + Abstract

     + 指南将根据"Canonical's Ubuntu Cloud"档案库为Ubuntu 16.04(LTS)提供的可用安装包逐步介绍安装过程

     + 包括配置选项和示例配置文件的说明

     + Note

       Training Labs脚本提供了一种自动方式，可以将本安装指南中介绍的群集部署到VirtualBox或KVM VM中;需要具有至少8 GB内存和20 GB可用存储空间的台式机或笔记本电脑，并运行Linux，MaOS或Windows

   + Install and configure

     + https://docs.openstack.org/keystone/queens/install/keystone-install-ubuntu.html

   + Create a domain,projects,users,and roles

     + 身份服务为每个OpenStack服务提供验证服务
     + 验证服务使用域(domains)、项目(projects)、用户(users)和角色(roles)的组合
     + https://docs.openstack.org/keystone/queens/install/keystone-users-ubuntu.html

   + Verify operation

     + 在安装其他服务前，验证身份服务的操作
     + **在控制节点执行命令**
     + https://docs.openstack.org/keystone/queens/install/keystone-verify-ubuntu.html

   + Create OpenStack client environment scripts

     + 前面讲到使用环境变量和命令选项的组合，以通过openstack客户端与Identity Service进行交互
     + 为了提高客户端操作的效率，OpenStack支持简单的客户端环境脚本，也称为OpenRC files；
     + 这些脚本通常包含所有客户端的通用选项，但是也支持唯一的选项
     + https://docs.openstack.org/keystone/queens/install/keystone-openrc-ubuntu.html

   ---

5. for CentOS

   + Abstract

     + 指南将展示如何通过RDO存储库使用Red Enterprise Linux 7提供的安装包安装Keystone

     + 包括配置选项和示例配置文件的说明

     + Note

       Training Labs脚本提供了一种自动方式，可以将本安装指南中介绍的群集部署到VirtualBox或KVM VM中;需要具有至少8 GB内存和20 GB可用存储空间的台式机或笔记本电脑，并运行Linux，MaOS或Windows

   + Install and configure

     + 在Queens发行之前，keystone需要在两个单独的端口上运行，以适应Identity v2 API，通常在端口35357上运行单独的仅管理员服务;删除v2 API后，keystone可以在同一端口上运行所有接口。

     + https://docs.openstack.org/keystone/queens/install/keystone-install-rdo.html

   + Create a domain,projects,users,and roles

     + 身份服务为每个OpenStack服务提供验证服务
     + 验证服务使用域(domains)、项目(projects)、用户(users)和角色(roles)的组合
     + https://docs.openstack.org/keystone/queens/install/keystone-users-rdo.html

   + Verify operation

     + 在安装其他服务前，验证身份服务的操作
     + **在控制节点执行命令**
     + https://docs.openstack.org/keystone/queens/install/keystone-verify-rdo.html

   + Create OpenStack client environment scripts

     + 前面讲到使用环境变量和命令选项的组合，以通过openstack客户端与Identity Service进行交互

     + 为了提高客户端操作的效率，OpenStack支持简单的客户端环境脚本，也称为OpenRC files；

     + 这些脚本通常包含所有客户端的通用选项，但是也支持唯一的选项

     + https://docs.openstack.org/keystone/queens/install/keystone-openrc-rdo.html

       









