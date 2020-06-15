# LinuxTips3--CentOS7改网卡为ethx

+ https://www.cnblogs.com/Wolf-Dreams/p/9090577.html
+ 下面的不知道什么东西

安装CentOS7没有ip，使用ifconfig指令查看网络配置，发现如下图所示：

 ![](https://img-blog.csdn.net/20180926170544574?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 配置中没有eth0，但是有ens33

 马上进入磁盘路径 cd /etc/sysconfig/network-scripts/，发现空空如也，

 ![](https://img-blog.csdn.net/20180926170553919?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 创建网卡eth0可以将ens33文件重命名为mv ifcfg-ens33 ifcfg-eth0

 ![](https://img-blog.csdn.net/20180926171345832?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 编辑vi ifcfg-eth0文件

 ![](https://img-blog.csdn.net/20180926171832597?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 编辑加载启动项的配置 vi /etc/default/grub

 ![](https://img-blog.csdn.net/20180926172650846?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 运行命令grub2-mkconfig -o /boot/grub2/grub.cfg 更新环境参数

 ![](https://img-blog.csdn.net/20180926172655283?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 重启网卡:systemctl restart network

 再次查询ip :ifconfig

 ![](https://img-blog.csdn.net/20180926172846746?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 ping一下百度

 ![](https://img-blog.csdn.net/20180926172901885?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NtZDI1NzU2MjQ1NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 成功

   
