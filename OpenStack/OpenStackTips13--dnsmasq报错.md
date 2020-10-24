# OpenStackTips13--dnsmasq报错

### 查看dnsmasq日志

```bash
grep -ri --exclude-dir=dist_upgrade dnsmasq /var/log
```



### 错误：dnsmasq: failed to create listening socket for port 53: Address already in use

+ 查看端口

  ```bash
  [root@controller cfbcaac6-e374-4156-a586-74957e7e553a]# netstat -tupln | grep dnsmasq
  tcp        0      0 192.168.122.1:53        0.0.0.0:*               LISTEN      9704/dnsmasq        
  udp        0      0 192.168.122.1:53        0.0.0.0:*                           9704/dnsmasq        
  udp        0      0 0.0.0.0:67              0.0.0.0:*                           9704/dnsmasq  
  ```

+ 方案

  重启dhcp服务

  ```bash
  systemctl restart neutron-dhcp-agent
  ```