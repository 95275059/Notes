# Linux笔记16--网络命令

1. write

   命令所在路径：/usr/bin/write

   执行权限：所有与洪湖

   语法：write [用户名]

   功能：给**在线**用户发送消息，以Ctrl+==D(大写)==保存结束  

   **注：前提是所有用户都需要登录在同一服务器上**

   注：在编辑文件时，删除：Ctrl+退格键||DELETE

   注：在接收方最后的EOF代表Ctrl+D的结束符

   ---

2. wall(write all)

   命令所在路径：/usr/bin/wall

   执行权限：所有用户

   语法：wall [message]

   功能：发广播消息给在线的所有用户

   注：发送信息若有>，则包括>在内的之后所有信息都无法发送

   ---

3. ping

   命令所在路径：/bin/ping

   执行权限：所有用户

   语法：ping [选项] [IP地址]

   ​					-c   指定发送次数

   功能：测试网络连通性

   ​			给远程主机发送一个ICMP信息请求包，检测是否有回复

   例：ping -c 4 192.168.117.2   只ping4次

   ---

4. ifconfig(interface configure)

   命令所在路径：/sbin/ifconfig

   执行权限：root

   语法：ifconfig [网卡名称] [IP地址]

   功能描述：查看和设置网卡信息

   **注：ifconfig ens33 192.168.177.128   只是临时更改IP地址**

   ---

5. mail

   命令所在路径：/bin/mail

   执行权限：所有用户

   语法：mail [用户名]

   功能：查看发送电子邮件（接收方无需在线）

   发送邮件：mail [用户名]

   ​				   依次输入主题(Subject)和内容后Ctrl+D(大写)保存结束

   接受邮件：mail

   ​					会显示邮件列表 

   ![笔记16-1](E:\notes\Linux\笔记16-1.PNG)

   ​						注：N：即NEW，未读；1：邮件序列号；root：邮件发送人；

   ​						help：查看mail交互模式下的各种命令格式

   ​						![笔记16-1](E:\notes\Linux\笔记16-1.PNG)

   ​						1：查看序列号为1的邮件的内容

   ​						h：查看邮件列表

   ​						d 1 ：删除序列号为1的邮件

   ​						quit ：退出

   ---

6. last

   命令所在路径：/usr/bin/last

   执行权限：所有用户

   语法：last

   功能：列出目前与过去登入系统的用户信息

   注：该命令还能查看该机的重启时间

   ---

7. lastlog

   命令所在路径：/usr/bin/lastlog

   执行权限：所有用户

   语法：lastlog

   ​						-u [用户的uid||用户名]

   功能：检查某用户（或所有用户）上次登录时间

   ---

8. traceroute

   命令所在路径：/bin/traceroute

   执行权限：所有用户

   语法：traceroute [IP地址或者DNS域名]

   功能：显示数据包到主机间的路径

   ---

9. netstat

   命令所在路径：/bin/netstat

   执行权限：所有用户

   语法：netstat [选项]

   功能：显示网络相关信息

   |  -t  |      TCP协议       |
   | :--: | :----------------: |
   |  -u  |      UDP协议       |
   |  -l  |        监听        |
   |  -r  |        路由        |
   |  -n  | 显示IP地址和端口号 |

   netstat -tuln   查看本机监听的端口            只能查询监听

   netstat -an      查看本机所有网络连接        能够查询正在连接的网络程序（ESTABLISHED）

   netstat -rn       查看本机路由表

   ---

10. setup（只在redhat中有）

    命令所在路径：/usr/bin/setup

    执行权限：root

    语法：setup

    功能描述：配置网络（永久生效）

    注：配完后service network restart

    注：yum install -y setuptool 

    ​		yum install -y ntsysv   安装系统服务管理

    ​		yum install -y iptables   安装防火墙以及setup中配套的防火墙设置、网络设置

    ​		yum install -y system-config-securitylevel-tui   安装setup中配套的防火墙设置

    ​		yum install -y system-config-network-tui    安装setup中配套的网络设置

    注：cenOS7 中setup已经没有网络设置功能，使用nmtui命令进行网络设置。

    ---

11. mount

    命令所在路径：/bin/mount

    执行权限：所有用户

    语法：mount [-t 文件系统] 设备文件名 挂载点

    例：mount -t iso9660 /dev/sr0 /mnt/cdrom       

    ​        **CD-ROM光盘标准文件系统iso9660    redhat中设备文件名默认为/dev/sr0**

    注：用完后执行==卸载==命令：umount /dev/sr0

    ​		卸载出错提示：device is busy   =>退出挂载目录后重试

    ​		卸载后 /mnt/cdrom目录变空 