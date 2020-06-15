# OpenStack--Installation6--Install OpenStack services2(Minimal deployment for Queens)--Image service

1. Overview

   + 镜像服务使得用户能够发现，注册并检索虚拟机镜像

   + 它提供了一个REST API，使你可以查询虚拟机镜像元数据并检索实际镜像

   + 可以将通过镜像服务提供的虚拟机镜像存储在从简单文件系统(simple file systems)到对象存储系统(object-storage systems)(如，OpenStack Object Storage)的各种位置

   + 注意

     + 为简单起见，该指南介绍了将Image服务配置为使用file后端(back end)的方法，该后端会将其上传并存储在托管Image服务的控制节点上的目录中
     + 默认情况下，该目录为***/var/lib/glance/images**
     + 在继续之前，请确保控制节点在此目录中至少有几个GB的可用空间
     + 由于file后端通常位于控制节点本地，因此通常不适合多节点glance部署

   + OpenStack镜像服务对于基础架构即服务(Infrastructure-as-a-Service(IaaS))至关重要

   + 镜像服务接收来自磁盘或者服务器镜像的API请求，以及来自终端用户或者OpenStack计算组件的元数据定义；还支持在各种存储库类型(包括OpenStack对象存储)上存储磁盘或者服务器镜像

   + OpenStack镜像服务上运行许多定期进程以支持缓存

     + Replication services确保整个群集的一致性和可用性
     + 其他定期进程包括：auditors（审核员）、updaters（更新者）、reapers（收割者）

   + OpenStack镜像服务包括以下组件

     + glance-api

       + 接收用于镜像发现、检索和存储的Image API调用

       + Notes

         Pike版本中的OpenStack社区目标是[通过WSGI部署Control Plane API端点](https://governance.openstack.org/tc/goals/pike/deploy-api-in-wsgi.html)。但是，按照目前的构成，glance-api **不适合**在这种配置下运行。相反，我们建议以传统方式将Glance作为独立服务运行。有关更多信息，请参阅Pike和Queens版本的[Glance发行说明](https://docs.openstack.org/releasenotes/glance/index.html)的“已知问题”部分。

     + glance-registry

       + 存储，处理和检索镜像的元数据
       + 元数据包括大小和类型等项目

       + Warning

         + 注册表是供OpenStack 镜像服务使用的私有内部服务，不要讲此服务提供给用户

       + Note

         **Queens版本中已经弃用Glance Registry Service及其API**，并且遵循OpenStack标准弃用策略，在“S”开发周期开始时将其删除

     + Database
       + 存储镜像元数据
       + 可以根据喜好选择数据库
       + 大多数部署使用MySQL或者SQLite
     + Storage repository for image files
       + 支持各种存储库类型，包括普通文件系统(normal file systems)(或挂载在控制节点glance-api上的任何文件系统)，Object Storage,RADOS block devices,VMware datasotre,and HTTP.
       + 注意，一些存储库只支持只读用法
     + Metadata definition service
       + 供应商(vendors)、管理员(admins)、服务(services)和用户(users)的通用API，可以有意义地定义他们自己的自定义元数据。此元数据可用于不同类型的资源，例如images,artifacts,volumes,flavors和aggregates
       + 定义包括新属性的键，描述，约束和可以与之关联的资源类型

   ---

2. Install and configure

   + **安装在控制节点**
   + 为简单起见，此次配置将镜像存储在本地文件系统
   + for Red Hat
     + https://docs.openstack.org/glance/queens/install/install-rdo.html
   + for Ubuntu
     + https://docs.openstack.org/glance/queens/install/install-ubuntu.html

   ---

3. Verify operation

   + 使用CirrOS（一个小型Linux镜像，可帮助您测试OpenStack的部署）来验证镜像服务的运行

   + **在控制节点验证**

   + https://docs.openstack.org/glance/queens/install/verify.html

   + 有关如何下载和构建镜像的更多信息

     + see [OpenStack Virtual Machine Image Guide](https://docs.openstack.org/image-guide/).

   + 有关如何管理镜像的信息

     + see the [OpenStack End User Guide](https://docs.openstack.org/user-guide/common/cli-manage-images.html).

   + 有关OpenStack镜像创建参数的信息

     + see [Create or update an image (glance)](https://docs.openstack.org/user-guide/common/cli-manage-images.html#create-or-update-an-image-glance) in the `OpenStack User Guide`.

   + 有关镜像的磁盘和容器格式的信息

     + see [Disk and container formats for images](https://docs.openstack.org/image-guide/image-formats.html) in the `OpenStack Virtual Machine Image Guide`.

       

   