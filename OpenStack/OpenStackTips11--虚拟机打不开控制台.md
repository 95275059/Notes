# OpenStackTips11--虚拟机打不开控制台

### 某一个计算节点上的虚拟机无法打开虚拟机控制台

+ 在该计算节点修改/etc/nova/nova.conf

  ```bash
  [vnc]
  enabled = True
  server_listen = 0.0.0.0
  server_proxyclient_address = $my_ip
  novncproxy_base_url = http://controller:6080/vnc_auto.html
  ```

  最后一行，将controller改为控制节点的ip（如192.168.1.211）

### 所有计算节点上的虚拟机都无法打开虚拟机控制台(不懂==)

+ 可以ping通控制节点的电脑，无法访问http://192.168.1.211:6080/vnc_auto.html。

+ 在控制节点（严格来说是配置VNC服务代理节点，TECS目前默认在控制节点上），查看openstack-nova-novncproxy是否运行。

  systemctl status openstack-nova-novncproxy

+ **参考**：https://www.sohu.com/a/167804954_468741                

