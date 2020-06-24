# OpenStackTips1--ssh&&scp远程操作

1. 在网络节点ssh连接虚拟机

   ```shell
   [root@network ~]# ip netns exec qdhcp-8e91cab1-1091-41e8-b25e-e5d52a1e005a ssh root@222.222.222.5
   ```

   + qdhcp后加虚拟机222.222.222.5所在的网络的ID

2. ssh/scp免手工输入yes

   + 方法一：连接时加入StrictHostKeyChecking=no

     ```bash
     $ ssh -o "StrictHostKeyChecking no" username@hostname
     ```

     ```bash
     $ ssh -o StrictHostKeyChecking=no username@hostname
     ```

   + 方法二：修改/etc/ssh/ssh_config配置文件，添加：

     ```
     StrictHostKeyChecking no
     ```

3. sshpass

   + 一个用于非交互的ssh密码验证工具

   + 使用前需要先安装

     ```bash
     $ yum install sshpass
     ```

   + 使用方法

     ```bash
     $ sshpass -p *password* ssh -o StrictHostKeyChecking=no username@hostname
     ```

4. 在网络节点向虚拟机传输远程命令

   ```bash
   [root@network ~]# ip netns exec qdhcp-*net_id* ssh username@hostname "cmd1 && cmd2"
   ```

   + 运行多条命令用&&连接即可

   + sshpass方式

     ```bash
     [root@network ~]# ip netns exec qdhcp-*net_id* sshpass -p *password* ssh username@hostname "cmd1 && cmd2"
     ```

5. 在网络节点向虚拟机传输文件

   ```bash
   [root@network ~]# ip netns exec qdhcp-*net_id* scp *directory and filename of the file waiting to be transferred* username@hostname:*target directory of the remote host*
   ```

   + sshpass方式

     ```bash
     [root@network ~]# ip netns exec qdhcp-*net_id* sshpass -p *password* scp -o StrictHostKeyChecking=no *directory and filename of the file waiting to be transferred* username@hostname:*target directory of the remote host*
     ```

   + 例：

     ```bash
     [root@network ~]# ip netns exec qdhcp-8e91cab1-1091-41e8-b25e-e5d52a1e005a sshpass -p 123456 scp -o StrictHostKeyChecking=no /home/cxy_tdyt/netperf-netperf-2.7.0.tar.gz root@222.222.222.5:/root
     ```

     

   









