# 重启OpenStack的整个服务

~~~
openstack-service restart
~~~

# 重启dashboard

~~~
service httpd restart
service memcached restart
~~~

# 重启Nova服务

## 控制节点

~~~
service openstack-nova-api restart
service openstack-nova-consoleauth restart
service openstack-nova-scheduler restart
service openstack-nova-conductor restart
service openstack-nova-novncproxy restart
~~~

## 计算节点

~~~
service libvirtd restart
service openstack-nova-compute restart
~~~

# 重启neutron服务

## 控制节点

~~~
service openstack-nova-api restart
service openstack-nova-scheduler restart
service openstack-nova-conductor restart
service neutron-server restart
~~~

##  网络节点

~~~
service openvswitch restart
service neutron-openvswitch-agent restart
service neutron-l3-agent restart
service neutron-dhcp-agent restart
service neutron-metadata-agent restart
~~~

## 计算节点

~~~
service neutron-openvswitch-agent restart
service openvswitch restart
~~~

# 重启rabbitmq服务

~~~
systemctl restart rabbitmq-server
~~~



* 参考

  https://blog.csdn.net/chengqiuming/article/details/79597787
  
  https://www.cnblogs.com/weijie0717/p/8641515.html