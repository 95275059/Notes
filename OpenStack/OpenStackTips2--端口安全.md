# OpenStackTips2--端口安全

1. 创建虚拟机不需要设置安全组

   ping&ssh安全组意义不明，不用理

2. 如果虚拟机ping不通外网，可能就是安全组没有删

   + 不要手动去编辑虚拟机，不然ssh都连不上

   + 控制节点

     ```shell
     [root@controller ~]# curl -x POST http://192.168.1.11:4501/v1.0/phys/iptables/delete/fa:16:3e:3b:31:ae
     ```

     + fa:16:3e:3b:31:ae 为端口的mac地址

       + 点进虚拟机所在网络，查看端口，点进虚拟机IP对应的端口名称

         ![](.\Tips2-1.png)

       + MAC地址

         ![](.\Tips2-2.png)

   + 若在控制节点删除端口安全出现以下问题

     ```shell
     [root@controller ~]# curl -x POST http://192.168.1.11:4501/v1.0/phys/iptables/delete/fa:16:3e:3b:31:ae
     
     curl: (7) Failed connect to 192.168.1.11:4501;拒绝连接
     ```

     + 解决方法:**控制节点运行**

       ```shell
       [root@controller ~]# python physcfg.pyc
       ```

       

     

