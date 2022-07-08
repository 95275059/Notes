# LinuxTips74--开机自启动脚本

* 自启动脚本 : /root/startup

* 开启脚本可执行权限

  chmod +x /root/startup

* 修改/etc/rc.local

  在exit 0 前 加入执行脚本命令 /root/startup

* systemctl enable rc-local

* systemctl start rc-local

  