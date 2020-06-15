# LinuxTips2--关于ifconfig未找到的解决方法 

yum install ifconfig 命令提示没有可用软件包ifconfig

1. 搜索ifconfig相关信息

   yum search ifconfig   

   ifconfig匹配net-tools.x86_64包

   ![Tips2-1](E:\notes\Linux\Tips2-1.PNG)

2. 安装net-tools.x86_64包

   yum install -y net-tools.x86_64

   