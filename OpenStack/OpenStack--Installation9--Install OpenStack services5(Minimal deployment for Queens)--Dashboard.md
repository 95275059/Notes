# OpenStack--Installation9--Install OpenStack services5(Minimal deployment for Queens)--Dashboard

1. Overview

   + **在控制节点安装**
   + Dashboard所需的唯一核心服务是身份服务
   + 可以将Dashboard与其他服务结合使用，例如镜像、计算和网络服务；也可以在具有独立服务（例如对象存储）的环境中使用Dashboard
2. System Requirements

   + 依赖

     + Python 2.7

     + Django 1.11

       + 还支持Django 1.8到1.10；它们的支持将在Rocky版本中删除

     + 可访问的keystone endpoint

     + 所有其他服务是可选的

       + 如果配置了服务的keystone的端点，horizon将检测到它并自动启用其支持

       + Horizon支持Queens版本的以下服务
         + cinder : Block Storage
         + glance : Image Management
         + neutron : Networking
         + nova : Compute
         + swift : Object Storage
         + Horizon通过组件也支持许多其他的OpenStack服务
           + For more information, see the [Plugin Registry](https://docs.openstack.org/horizon/queens/install/plugin-registry.html#install-plugin-registry)
3. Install from Packages
   + **在控制节点安装**
   + Install and configure
     + for CentOS
       + https://docs.openstack.org/horizon/queens/install/install-rdo.html
     + for Ubuntu
       + https://docs.openstack.org/horizon/queens/install/install-ubuntu.html
   + Verify Openration 
     + for Ubuntu / CentOS
       + https://docs.openstack.org/horizon/queens/install/verify-ubuntu.html
   + Next Steps
     + 为用户提供IP地址，用户名和密码，以便他们能通过浏览器访问dashboard
       + 如果发生任何SSL证书连接问题，请将服务器IP地址指向域名，然后授予用户访问权限
       + 自定义dashboard
         + For details, see [Customize and configure the Dashboard](https://docs.openstack.org/horizon/queens/admin/customize-configure.html).
       + 设置会话存储
         + For derails, see [Set up session storage for the Dashboard](https://docs.openstack.org/horizon/queens/admin/sessions.html).
       + 将VNC客户端与dashboard一起使用，浏览器必须支持HTML5 Canvas和HTML5 WebSockets
         + For details about browsers that support noVNC, see [README](https://github.com/novnc/noVNC/blob/master/README.md) and [browser support](https://github.com/novnc/noVNC/wiki/Browser-support).
4. Install from Source
   + Manual installation
     + 指南介绍了了生产环境下Horizon的基本安装
     + If you are looking for a developer environment(开发人员环境), see [Quickstart](https://docs.openstack.org/horizon/queens/contributor/quickstart.html#quickstart).
     + https://docs.openstack.org/horizon/queens/install/from-source.html
5. Horizon plugins
   + 有一些为许多有用特点而开发的horizon插件
   + 可以通过安装相应的horizon插件来获取dashboard支持
   + https://docs.openstack.org/horizon/queens/install/plugin-registry.html

