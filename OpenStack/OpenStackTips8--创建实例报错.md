# OpenStackTips8--创建实例报错

### 云主机 "cirros-vm1" 执行所请求操作失败，云主机处于错误状态。: 请稍后再试 [错误: Build of instance 542a8a93-66d6-4b90-900c-ee0d3feddf24 aborted: Failed to allocate the network(s), not rescheduling.].

+ 在创建实例用的计算节点上修改/etc/nova/nova.conf

  在[default]下面添加如下两行配置

  ```bash
  vif_plugging_is_fatal: false
  vif_plugging_timeout: 0
  ```

+ 重启nova服务

  ```bash
  service openstack-nova-compute restart
  ```

+ 参考

  https://www.jianshu.com/p/d148f6ad2622

### 云主机 "cirros-vm1" 执行所请求操作失败，云主机处于错误状态。: 请稍后再试 [错误: No valid host was found. There are not enough hosts available.].

+ 原因：对应的计算节点内存不够，增大内存