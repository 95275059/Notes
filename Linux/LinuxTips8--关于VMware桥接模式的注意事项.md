# LinuxTips8--关于VMware桥接模式的注意事项

1. 编辑->虚拟网络编辑器

   ![Tips8-1](E:\notes\Linux\Tips8-1.PNG)

   2. 虚拟机一定要设置成静态IP，同时设置网关，DNS

      ![Tips8-2](E:\notes\Linux\Tips8-2.PNG)

      网关、DNS要和主机网关、DNS一致

      主机命令行下ipconfig /all能查主机网关和DNS

   3. 出现虚拟机能ping通网关，百度（外网）；主机能ping通虚拟机；但是虚拟机不能ping通主机的问题

      **原因：主机防火墙没关**

      控制面板->系统和安全->Windows Defender防火墙->启用或关闭Windows Defender防火墙->关闭专用网络和公用网络的防火墙

      