# Linux笔记25--软件包管理6-yum在线管理1-网络yum源

1. 网络yum源

   网络yum源保存在/etc/yum.repos.d/CentOS-Base.repo

   能联网默认用CentOS-Base.repo；不联网，让光盘生效作为yum源用CentOS-Media.repo

   + 软件池：

     | 字符       | 含义                                                         |
     | ---------- | ------------------------------------------------------------ |
     | [base]     | 容器名称，一定要放在[]中。一般不改，默认什么是什么           |
     | name       | 容器说明，可以自己随便写                                     |
     | mirrorlist | 站点镜像，可以注释掉（用mirrorlist或者baseurl都可以，推荐用baseurl。其实都一样） |
     | baseurl    | 我们的yum源服务器地址。默认是CentOS官方的yum源服务器，是可以使用的，如果觉得慢可以改成其他的yum源地址 |
     | enabled    | 此容器是否生效，如果不写或者写成enable=1都是生效，写成enable=0是不生效 |
     | gpgcheck   | 如果是1是指RPM的数字证书生效，如果是0则不生效                |
     | gpgkey     | 数字证书的公钥文件保存位置。不用修改                         |

     