# OpenStack安装总结5--Dashboard报错

1. 报错：登录OpenStack 出现“无法连接keystone端点”

   + 原因：/etc/openstack-dashboard/local_settings中OPENSTACK_HOST设置拼写错误

   + 解决

     ```bash
     OPENSTACK_HOST = "cntroller"   
     OPENSTACK_KEYSTONE_URL = "http ://%s:5000/v2.0" % OPENSTACK_HOST
     OPENSTACK_KEYSTONE_DEFAULT_ROLE = "user"
     ```

     #OPENSTACK_HOST controller拼写错误

     + systemctl restart httpd.service memcached.service

