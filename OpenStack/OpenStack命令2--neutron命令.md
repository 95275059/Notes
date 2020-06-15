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

   neutron net-list

3. port

   + neutron port-list
+ neutron port-create *net_id*
   + neutron port-create --fixed-ip subnet_id=*subnet_id*,ip_address=*IP* *net_id*
   + neutron port-delete *port_id*

   

   