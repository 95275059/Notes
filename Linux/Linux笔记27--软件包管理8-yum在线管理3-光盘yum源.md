# Linux笔记27--软件包管理8-yum在线管理3-光盘yum源

1. 光盘yum源搭建步骤

   + 挂载光盘

     mount /dev/sr0 /mnt/cdrom/

   + 让网络yum源文件失效

     cd /etc/yum.repos.d/

     mv CentOS-Base.repo CentOS-Base.repo.bak    #改名，使文件不再是.repo，从而使该yum源文件失效

     mv CentOS-CR.repo CentOS-CR.repo.bak       #改名

     mv CentOS-Debuginfo.repo CentOS-Debuginfo.repo.bak            #改名

     mv CentOS-fasttrack.repo CentOS-fasttrack.repo.bak            #改名 

     mv CentOS-Sources.repo CentOS-Sources.repo.bak            #改名 

     mv CentOS-Vault.repo CentOS-Cault.repo.bak            #改名

   + 修改光盘yum源文件

     vim CentOS-Media.repo

     + baseurl=file:///mnt/cdrom         **第三个/代表根目录**

       baseurl写自己的光盘挂载地址，注释掉其他两个无用多余的baseurl地址

     + enabled=1

       让该yum源配置文件生效

     **注：yum源文件的修改格式非常严格，不要乱加注释和空格，否则会导致命令不能正常使用**

     ​		**注释顶头改，不要输入多余字符**