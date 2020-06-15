# LinuxTips17--设置FQDN

1. FQDN(Fully Qualified Name)

   完整域名

   例：一台机器主机名（hostname）是www，域后缀（domain）是example.com，那么该主机的FQDN应该是www.example.com。

   其实FQDN最后是以“.”来结尾的，但是大部分应用和服务器都允许忽略最后这个点

2. 设置FQDN

   + 修改主机名为elk

     vim /etc/hostname

   + 修改FQDN

     + vim /etc/hosts

       在/etc/hosts文件中增加一行主机记录，第一个字段是该主机的IP地址，第二个字段是你希望设置的FQDN

       ```
       [root@localhost ~]# vi /etc/hosts
       
       127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
       ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
       192.168.7.27 elk.server.com elk
       ```

3. 查看主机名，FQDN，域名

   + 查看主机名

     hostname

   + 查看域名

     dnsdomainname

   + 查看FQDN

     hostname -f

     hostname -f -v

     



