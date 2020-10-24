# LinuxTips54--网络服务重启失败

### Failed to start LSB

+ ```bash
  systemctl stop NetworkManager
  ```

+ ```bash
  systemctl disable NetworkManager
  ```

+ ```bash
  systemctl restart network
  ```

+ network和NetworkManager

  在CentOS系统上，目前有NetworkManager和network两种网络管理工具。如果两种都配置会引起冲突，而且NetworkManager在网络断开的时候，会清理路由，如果一些自定义的路由，没有加入到NetworkManager的配置文件中，路由就被清理掉，网络连接后需要自定义添加上去。

  目前在CentOS上的NetworkManager版本比较低，而且比较适合有桌面环境的系统，所以服务器上保留network服务即可，将NetworkManager关闭，并且禁止开机启动。

+ 生产环境下 我们一般都是手动配置网络，以静态地址为主不需要系统的网络管理工具，往往会出现在KDE环境中，因此，我们就会将NetworkManager禁用掉

