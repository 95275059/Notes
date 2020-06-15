# Linux笔记26--软件包管理7-yum在线管理2-yum命令

1. 常用yum命令

   + 查询

     yum list                             查询服务器所有可用软件包列表

     yum search 关键字          搜索服务器上所有和关键字相关的包

   + 安装

     yum -y install 包名

   + 升级

     yum -y update 包名

     yum -y update     =>升级所有软件包，包括Linux内核；Linux内核升级后需要在本地完成一些配置才能使用，但由于远程升级，所以升级完成后服务器无法开机，直接崩溃  ==慎重==

   + 卸载

     yum -y remove 包名           

     **由于软件包的依赖性问题存在，某些软件包依赖于其他包或者某些问系统文件等，卸载软件包时可能出现系统崩溃，系统某些重要功能不能使用等问题**   **==尽量不要卸载==**

   ---

2. YUM软件组管理命令
   + yum grouplist                                     列出所有可用的软件组列表
   + yum groupinstall 软件组名               安装指定软件组，组名可以由grouplist查询出来（如果软件组名有空格，需要用“ “把软件组名括起来）
   + yum groupremove 软件组名            卸载指定软件组
   
3. yum常用命令2

   + yum clean

     yum会将下载下来的包文件rpm和头文件header存盘在本地机器的硬盘缓存中，这将占用硬盘空间，可以将这些内容清除掉，以释放磁盘空间

     + yum clean headers   释放头文件
     + yum clean packages   清除包文件
     + yum clean all   清除所有

   + yum makecache

     把服务器的包信息下载到本地电脑缓存起来，makecache建立一个缓存，以后用install时就在缓存中搜索，提高了速度

     配合 yum search 使用

   

