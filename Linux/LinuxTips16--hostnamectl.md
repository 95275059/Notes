# LinuxTips16--hostnamectl

1. hostname

   hostname三种状态：static(静态)；transient(瞬态)；pretty(灵活)

   + static

     静态主机名也称为内核主机名，是系统在启动时从/etc/hostname自动初始化的主机名

     遵从作为互联网域名同样的字符限制规则

   + transient

     瞬态主机名是在系统运行时临时分配的主机名

     例如，通过DHCP或mDNS服务器分配

     遵从作为互联网域名同样的字符限制规则

   + pretty

     灵活主机名则允许使用自由形式（包括特殊、空白字符）的主机名，展示给终端用户

2. 查看主机名
   + hostname
   + hostnamectl
   + hostnamectl status
   + cat /etc/hostname

3. 只查看静态、瞬态或灵活主机名
   + hostnamectl --static
   + hostnamectl --transient
   + hostnamectl --pretty

4. 修改主机名

   + hostnamectl set-hostname [主机名]

     #会同时修改静态、瞬态和灵活主机名

     注意：在修改静态/瞬态主机名时，任何特殊字符或空白字符会被移除，而提供的参数中的所有大写字母会自动转化为小写。

     注意：直接修改/etc/hostname文件，可以保证大小写不变

     注意：一旦修改了静态主机名，/etc/hostname会被自动更新，但是/etc/hosts不会更新

     注意：==**一旦修改了静态主机名，一定要手动更新/etc/hosts，然后重启系统(reboot)**==

     注意：静态主机名是小写的，就算修改了大写的，也只会显示小写

     ````bash
     [root@cxy-centos7-1 ~]# hostnamectl
        Static hostname: cxy-centos7-1
        Pretty hostname: CXY-Centos7-1
              Icon name: computer-vm
                Chassis: vm
             Machine ID: c86fdb2ad56d49498b782143376d1947
                Boot ID: 9658bd89615e4defa3bb43340fc3382e
         Virtualization: vmware
       Operating System: CentOS Linux 7 (Core)
            CPE OS Name: cpe:/o:centos:centos:7
                 Kernel: Linux 3.10.0-957.el7.x86_64
           Architecture: x86-64
     ````

     + 手动更新/etc/hosts

       ```bash
       127.0.0.1   cxy-centos7-1
       #127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
       ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
       ```

   + hostname [主机名]

     这条命令不会更改/etc/hostname文件中的静态主机名（static hostname），它更改的只是临时主机名（transient hostname）。所以重启计算机后会回到旧的主机名。

   + 只修改特定主机名
     + hostnamectl --static sethostname [主机名]
     + hostnamectl --transient sethostname [主机名]
     + hostnamectl --pretty sethostname [主机名]