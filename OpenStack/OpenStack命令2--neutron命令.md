# OpenStack命令2--neutron命令

1. 设置环境变量

   ```shell
   source /root/admin-openrc
   ```

   或

   ```shell
   source .admin_openrc.sh
   ```

2. net

   + 显示已有网路列表

     ```bash
     neutron net-list
     ```

3. port

   + 显示已有端口列表

     neutron port-list

   + 新建端口

     + 不指定IP

       neutron port-create *net_id*

     + 指定IP

       neutron port-create --fixed-ip subnet_id=*subnet_id*,ip_address=*IP* *net_id*

   + 删除端口

     neutron port-delete *port_id*


