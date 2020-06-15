# OpenStack--Installation2--GetStarted with OpenStack

1. OpenStack 通过一组相互关联的服务提供了一种基础架构即服务(IaaS)的解决方案。每个服务都提供一个应用程序编程接口(API)来促进集成

2. 根据用户需求，可以安装部分或全部服务

3. OpenStack 概念架构

   ![Installation2-1](E:\Notes\OpenStack\Installation2-1.png)

4. OpenStack 逻辑架构

   ![Installation2-2](E:\Notes\OpenStack\Installation2-2.png)

   + OpenStack由几个独立的部分组成，成为OpenStack服务

     + 所有服务都通过公共身份服务(common Identity service)进行身份验证
     + 单独的服务通过公用APIs将各个服务联系起来，除非需要特权管理员命令

   + 在内部，OpenStack服务由几个进程组成

     + 所有服务都至少一个API进程，该进程侦听API请求，对其进行预处理，然后将其传递给服务的其他部分。
     + 除身份服务外，实际工作由不同的流程完成

   + 使用**AMQP信息代理**在一项服务的进程之间进行通信

     + 服务的状态存储在一个数据库中

     + 在部署和配置OpenStack云时，可以在一些信息代理和数据库方案中进行选择

       如，RabbitMQ, MySQL, MariaDB, and SQLite

   + 访问OpenStack的方式

     + 用户
       + 由Horizon Dashboard实现的基于Web的用户接口
       + 客户端命令行
       + 使用如浏览器插件或curl等工具发送API请求
     + 应用程序
       + 使用一些SDK
     + 所有的访问方式都通过发送REST API来调用各种OpenStack服务

     

   

