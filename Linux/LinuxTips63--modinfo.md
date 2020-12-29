# LinuxTips63--modinfo

### 功能

用于显示kernel模块的信息

modifo 会显示kernel模块的对象文件，以显示该模块的相关信息

### 语法

```bash
modinfo [-adhpV] [模块文件]
```

| 选项               | 说明                      |
| ------------------ | ------------------------- |
| -a 或 --author     | 显示模块开发人员          |
| -d 或 -description | 显示模块的说明            |
| -h 或 --help       | 显示modinfo的参数使用方法 |
| -p 或 --parameters | 显示模块所支持的参数      |
| -V 或 --version    | 显示版本信息              |

### 实例

```bash
[root@cxy-centos7-1 ~]# modinfo tun
filename:       /lib/modules/3.10.0-957.el7.x86_64/kernel/drivers/net/tun.ko.xz
alias:          devname:net/tun
alias:          char-major-10-200
license:        GPL
author:         (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
description:    Universal TUN/TAP device driver
retpoline:      Y
rhelversion:    7.6
srcversion:     A215175F959FA6FE8B76ECD
depends:        
intree:         Y
vermagic:       3.10.0-957.el7.x86_64 SMP mod_unload modversions 
signer:         CentOS Linux kernel signing key
sig_key:        B7:0D:CF:0D:F2:D9:B7:F2:91:59:24:82:49:FD:6F:E8:7B:78:14:27
sig_hashalgo:   sha256
```

