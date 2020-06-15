# OpenStackTips1--ssh

1. 在网络节点ssh连接虚拟机

   ```shell
   [root@network ~]# ip netns exec qdhcp-8e91cab1-1091-41e8-b25e-e5d52a1e005a ssh root@222.222.222.5
   ```

   + qdhcp后加虚拟机222.222.222.5所在的网络的ID

2. 

