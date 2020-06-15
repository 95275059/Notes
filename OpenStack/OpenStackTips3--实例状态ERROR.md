# OpenStackTips3--实例状态ERROR

+ 查看日志文档

  ```shell
  cd /var/log/nova/nova-compute.log
  ```

  错误：Instance failed network setup after 1 attempt(s)

### Failed to allocate the network(s),not rescheduling

![Tips3-1](.\Tips3-1.png)

![Tips3-2](.\Tips3-2.png)

+ 修改对应计算节点 /etc/nova/nova.conf

  ```shell
  #在[default]下面添加下面两行配置
  vif_plugging_is_fatal: false
  vif_plugging_timeout: 0
  ```

+ 重启各服务

  ```shell
  #误
  sudo service nova-api restart &&\
  sudo service neutron-server restart &&\
  sudo service neutron-linuxbridge-agent restart &&\
  sudo service neutron-dhcp-agent restart &&\
  sudo service neutron-metadata-agent restart
  ```
  
  ```shell
  cd /etc/init.d
  ./nova-compute restart
  ```



  





