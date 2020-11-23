# Docker命令2--容器操作命令

### 列出容器

```bash
docker ps [OPTIONS]
```

+ [OPTIONS]

  | 选项                | 说明                                                         |
  | ------------------- | ------------------------------------------------------------ |
  | -a, --all           | 显示所有的容器，包括未运行的   Show all containers (default shows just running) |
  | -f, --filter filter | 根据条件过滤显示的内容   Filter output based on conditions provided |
  | --format string     | 指定返回值的模板文件   Pretty-print containers using a Go template |
  | -l, --lastest       | 显示最近创建的容器   Show the latest created container (includes all states) |
  | -n, --last int      | 列出最近创建的n个容器   Show n last created containers (includes all states) (default -1) |
  | -q, --quiet         | 静默模式，只显示容器编号   Only display numeric IDs          |
  | -s, --size          | 显示总的文件大小   Display total file sizes                  |
  | --no-trunc          | 不截断输出   Don't truncate output                           |

+ 列出所有在运行的容器信息

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker ps -a
  CONTAINER ID        IMAGE               COMMAND              CREATED             STATUS                     PORTS               NAMES
  dde6447a9551        httpd               "httpd-foreground"   25 minutes ago      Exited (0) 5 minutes ago                       gifted_visvesvaraya
  ```
  
+ **CONTAINER ID:** 容器 ID
  + **IMAGE:** 使用的镜像
  + **COMMAND:** 启动容器时运行的命令
  + **CREATED:** 容器的创建时间
  + **STATUS:** 容器状态
    + created（已创建）
    + restarting（重启中）
    + running（运行中）
    + removing（迁移中）
    + paused（暂停）
    + exited（停止）
    + dead（死亡）
  + **PORTS:** 容器的端口信息和使用的连接类型（tcp\udp）
  + **NAMES:** 自动分配的容器名称
  
+ 列出最近创建的5个容器信息

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker ps -n 5
  CONTAINER ID        IMAGE               COMMAND              CREATED             STATUS                     PORTS               NAMES
  dde6447a9551        httpd               "httpd-foreground"   26 minutes ago      Exited (0) 7 minutes ago                       gifted_visvesvaraya
  ```
  
+ 列出所有创建的容器ID

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker ps -a -q
  dde6447a9551
  ```

---

### 列出容器

```bash
docker container ls [OPTIONS]
```

+ [OPTIONS]

  | 选项                                          | 说明                                                         |
  | --------------------------------------------- | ------------------------------------------------------------ |
  | -a, --all                                     | Show all containers (default shows just running)             |
  | -f, --filter filter <br/>     --format string | Filter output based on conditions provided<br/>Pretty-print containers using a Go template |
  | -n, --last int                                | Show n last created containers (includes all states) (default -1) |
  | -l, --latest<br/>    --no-trunc               | Show the latest created container (includes all states)<br/>Don't truncate output |
  | -q, --quiet                                   | Only display numeric IDs                                     |
  | -s, --size                                    | Display total file sizes                                     |

---

### docker attach

+ 连接到正在**运行中**的容器

+ 直接进入容器启动命令的终端，不会启动新的进程

+ 语法

  ```bash
  docker attach [OPTIONS] CONTAINER
  ```

  + [OPTIONS]

    | 选项                 | 说明                                                     |
    | -------------------- | -------------------------------------------------------- |
    | --detach-keys string | Override the key sequence for detaching a container      |
    | --no-stdin           | Do not attach STDIN                                      |
    | --sig-proxy          | Proxy all received signals to the process (default true) |

  + CONTAINER

    容器的长ID 或者 短ID 或者 NAME（docker ps命令NAMES值）

+ 注

  要attach上去的容器必须正在运行，可以同时连接上同一个container来共享屏幕（与screen命令的attach类似）。

  官方文档中说attach后可以通过CTRL-C来detach，但实际上经过我的测试，如果container当前在运行bash，CTRL-C自然是当前行的输入，没有退出；如果container当前正在前台运行进程，如输出nginx的access.log日志，CTRL-C不仅会导致退出容器，而且还stop了。这不是我们想要的，detach的意思按理应该是脱离容器终端，但容器依然运行。好在attach是可以带上--sig-proxy=false来确保CTRL-D或CTRL-C不会关闭容器

---

### docker logs

+ 获取容器的日志

+ 语法

  ```bash
  docker logs [OPTIONS] CONTAINER
  ```

  + [OPTIONS]

    | 选项              | 说明                                                         |
    | ----------------- | ------------------------------------------------------------ |
    | -f, --follow      | 跟踪日志输出（与tail -f类似，能够持续打印输出）   Follow log output |
    | --sine string     | 显示某个开始时间的所有日志    Show logs since timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes) |
    | -t,  --timestamps | 显示时间戳   Show timestamps                                 |
    | --tail string     | 仅列出最新N条容器日志   Number of lines to show from the end of the logs (default "all") |
    | --details         | Show extra details provided to logs                          |
    | --until string    | Show logs before a timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes) |

+ 实例1：跟踪容器mynginx的日志输出

  ```bash
  docker logs -f mynginx
  ```

+ 实例2：查看容器mynginx从2020年11月23日后的最新10条日志

  ```bash
  docker logs --since="2020-11-23" --tail=10 mynginx
  ```

---

### docker rename

+ 重命名容器

+ 语法

  ```bash
  docker rename CONTAINER NEW_NAME
  ```

  











