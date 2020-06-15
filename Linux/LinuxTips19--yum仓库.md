# LinuxTips19--yum仓库

1. yum仓库

   yum仓库就是使用yum命令下载软件的镜像地址

   通常使用yum install 命令来在线安装linux系统的软件, 这种方式可以自动处理依赖性关系，并且一次安装所有依赖的软体包,但是经常会遇到从国外镜像下载速度慢,无法下载的情况.那么此时我们就需要把我们的yum 源改为国内的镜像。

2. yum仓库命令

   + yum repolist   列出yum仓库

   + yum clean all   清理yum仓库

     yum会把下载的软件包和header存储在cache中，而不会自动删除。

     如果觉得占用磁盘空间，可以使用yum clean指令进行清除

     yum clean headers   清除header

     yum clean packages   清除下载的rpm包

     yum clean all   全部清除

   + yum makecache   缓存yum仓库

     将服务器的报信息下载到本地电脑缓存起来，makecache建立一个缓存，以后用install时就在缓存中搜索，提高了速度。

   + yum list   显示服务器所有可用yum包列表