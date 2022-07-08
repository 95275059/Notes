# OpenStackTips22--自动部署任务过多报错

OpenStack默认网络端口部署任务堵塞的时候，会让一连串的任务直接报错

计算节点nova.conf

```shell
vif_plugging_is_fatal=false
vif_plugging_timeout=0
```

