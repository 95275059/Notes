# Docker命令2--容器操作命令

### 列出容器

```bash
docker ps [OPTIONS]
```

+ [OPTIONS]

  | 选项     | 说明                         |
  | -------- | ---------------------------- |
  | -a       | 显示所有的容器，包括未运行的 |
  | -f       | 根据条件过滤显示的内容       |
  | --format | 指定返回值的模板文件         |
  | -l       | 显示最近创建的容器           |
  | -n       | 列出最近创建的n个容器        |
  | -q       | 静默模式，只显示容器编号     |
  | -s       | 显示总的文件大小             |

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

### 列出镜像

```bash
docker images [OPTIONS] [REPOSITORY[:TAG]]
```

+ [OPTIONS]

  | 选项                                                         | 说明                                                         |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | -a, --all<br>     --digests                                  | Show all images (default hides intermediate images)<br>Show digests |
  | -f, --filter filter <br/>     --format string<br/>     --no-trunc | Filter output based on conditions provided<br/>Pretty-print containers using a Go template<br>Don't truncate output |
  | -q, --quiet                                                  | Only display numeric IDs                                     |

+ 查看本地镜像列表

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker images
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  httpd               latest              3dd970e6b110        5 weeks ago         138MB
  ```

+ 列出本地镜像中REPOSITORY为httpd的镜像列表

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker images httpd
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  httpd               latest              3dd970e6b110        5 weeks ago         138MB
  ```









