# Linux笔记65--启动管理1-启动流程1-运行级别

### 运行级别

##### centos7之前

+ 在centos7之前inittab的配置文件是这样的

  vim /etc/inittab

  ```shell
  # inittab is only used by upstart for the default runlevel.
  #
  # ADDING OTHER CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
  #
  # System initialization is started by /etc/init/rcS.conf
  #
  # Individual runlevels are started by /etc/init/rc.conf
  #
  # Ctrl-Alt-Delete is handled by /etc/init/control-alt-delete.conf
  #
  # Terminal gettys are handled by /etc/init/tty.conf and /etc/init/serial.conf,
  # with configuration in /etc/sysconfig/init.
  #
  # For information on how to write upstart event handlers, or how
  # upstart works, see init(5), init(8), and initctl(8).
  #
  # Default runlevel. The runlevels used are:
  #   0 - halt (Do NOT set initdefault to this)
  #   1 - Single user mode
  #   2 - Multiuser, without NFS (The same as 3, if you do not have networking)
  #   3 - Full multiuser mode
  #   4 - unused
  #   5 - X11
  #   6 - reboot (Do NOT set initdefault to this)
  # 
  id:5:initdefault:
  ```

+ 运行级别

  | 运行级别 | 含义                                                         |
  | -------- | ------------------------------------------------------------ |
  | 0        | 关机                                                         |
  | 1        | 单用户模式，可以想像为windows的安全模式，主要用于系统修复（只启动最基本的程序，服务） |
  | 2        | 不完全的命令行模式，不含NFS（Network File System）服务（多用户，不联网） |
  | 3        | 完全的命令行模式，就是标准字符界面（多用户）                 |
  | 4        | 系统保留（不适用的）                                         |
  | 5        | 图形模式（xwindows）                                         |
  | 6        | 重启动                                                       |

##### centos7

+ 但是在centos7之后有了一个新的服务systemd取代了init

+ systemd 是 Linux 下一个与 SysV 和 LSB 初始化脚本兼容的系统和服务管理器。

+ 运行级别

  | 运行级别 | 含义              |
  | -------- | ----------------- |
  | 0        | shutdown.target   |
  | 1        | emergency.target  |
  | 2        | rescure.target    |
  | 3        | multi-user.target |
  | 4        | 无                |
  | 5        | graphical.target  |
  | 6        | 无                |

##### ubuntu

+ Ubuntu的默认开机的runlevel是2

+ Ubuntu、Debian系列与RedHat、CentOS启动级别含义有所区别

  | 运行级别 | 含义                                                   |
  | -------- | ------------------------------------------------------ |
  | 0        | 关机                                                   |
  | 1        | 单用户模式                                             |
  | 2        | 多用户模式，Full multi-user with display manager (GUI) |
  | 3        | 多用户模式，Full multi-user with display manager (GUI) |
  | 4        | 多用户模式，Full multi-user with display manager (GUI) |
  | 5        | 多用户模式，Full multi-user with display manager (GUI) |
  | 6        | 重启                                                   |

  2~5级是没有任何区别的

+ 运行级别配置文件

  vim /etc/init/rc-sysinit.conf

  ```shell
  # rc-sysinit - System V initialisation compatibility
  #
  # This task runs the old System V-style system initialisation scripts,
  # and enters the default runlevel when finished.
  
  description     "System V initialisation compatibility"
  author          "Scott James Remnant <scott@netsplit.com>"
  
  start on (filesystem and static-network-up) or failsafe-boot
  stop on runlevel
  
  # Default runlevel, this may be overriden on the kernel command-line
  # or by faking an old /etc/inittab entry
  env DEFAULT_RUNLEVEL=2
  
  emits runlevel
  ...
  ```

---

### 运行级别命令（centos6）

+ 查看运行级别

  runlevel

  输出：N 3

  含义：N：在进入3级别之前所处的级别，N代表null，即开机后直接进入3级别

+ 改变运行级别命令

  init 运行级别

---

### 系统默认运行级别（centos6）

+ 设置系统开机后直接进入的运行级别
  + vim /etc/inittab
  + id:3:initdefault:

---

### 设置运行级别（centos7）

systemctl [command] [unit.target]

+ command

  get-default:取得当前的target

  set-default:设置指定的target为默认的运行级别

  isolate:切换到指定的运行级别

  



