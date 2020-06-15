# OpenStack安装总结2--Glance报错

1. 创建glance镜像报错HTTP403

   ```shell
   [root@controller ~]# openstack image create "cirros" --file cirros-0.5.1-x86_64-disk.img --disk-format qcow2 --container-format bare --public
   403 Forbidden: You are not authorized to complete this action. (HTTP 403)
   ```

   **错误：**403 Forbidden: You are not authorized to complete this action. (HTTP 403)

   **原因：**配置文件中flavor=keystone没有写

   **解决：**进入两个配置文件：/etc/glance/glance-api.conf 和 /etc/glance/glance-registry.conf:

   查看两个配置文件glance.api与glance.registry中[paste_deploy]是否有误

   ```shell
   [paste_deploy]
   flavor = keystone
   ```

   