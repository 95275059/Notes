# LinuxTips9--firewalld常用命令

+ 配置文件说明

  firewalld配置文件存放在：/usr/lib/firewalld 和 /etc/firewalld

  /usr/lib/firewalld 存放了一些默认文件

  /etc/firewalld 存放用户自定义的数据，自己添加的service和rule都在该目录进行

  service 文件夹存储服务数据，即一组定义好的规则

  zones 存储区域规则

  firewalld.conf 默认配置文件，可以设置默认使用的区域，默认区域为public，对应zones目录下的public.xml

1. 启动

   systemctl start firewalld

2. 停止

   systemctl stop firewalld

3. 重启

   systemctl restart firewalld.service

4. 查看状态

   systemctl status firewalld

5. 开机自启动

   systemctl enable firewalld.service

6. 停止开机自启动

   systemctl disable firewalld

7. 查看是否开机自启动

   systemctl is-enabled firewalld.service

8. 查看启动失败的服务列表

   systemctl --failed

9. 查看版本

   firewall-cmd --version

10. 查看帮助

    firewall-cmd --help

11. 显示状态

    firewall-cmd --state

12. 查看所有打开的端口

    firewall-cmd --zone=public --list-ports

13. **更新防火墙规则**

    **firewall-cmd --reload**

14. 查看区域信息

    firewall-cmd --get-active-zones

15. 查看指定接口所属区域

    firewall-cmd --get-zone-of-interface=ens33

16. 拒绝所有包

    firewall-cmd --panic-on

17. 取消拒绝状态

    firewall-cmd --panic-off

18. 查看是否拒绝

    firewall-cmd --query-panic

19. 开放80端口（允许任意IP访问）

    firewall-cmd --zone=public --add-port=80/tcp --permanent   

    ​													 (--permanent永久生效,会将配置存储到配置文件，否则重启后失效)

20. 查看80端口

    firewall-cmd --zone=public --query-port=80/tcp

21. 删除80端口（允许任意IP访问的端口）

    firewall-cmd --zone=public --remove-port=80/tcp --permanent

22. 发放端口区间

    firewall-cmd --zone=public --add-port=8080-9999/tcp --permanent

23. 查看所有配置

    firewall-cmd --list-all

24. 查看允许指定IP访问端口的规则

    firewall-cmd --zone=public --list-rich-rules

25. 开放指定端口（只允许指定IP访问）

    firewall-cmd --add-rich-rule="rule family="ipv4" source address="192.168.1.1" port protocol="tcp" \

    port="3306" accept" --permanent

26. 移除规则（只允许指定IP访问的端口）

    firewall-cmd --remove-rich-rule="rule family="ipv4" source address="192.168.1.1 port portocol="tcp" \

    port="3306" accept" --permanent

27. 添加一个服务

    firewall-cmd --add-service=xxx --permanent

    使目标服务可以通过

27. 移除默认的ssh服务

    ==移除默认ssh服务前，先确认是否已经额外开放了22端口，否则会导致无法使用ssh远程连接==

    firewall-cmd --remove-service=ssh --permanent