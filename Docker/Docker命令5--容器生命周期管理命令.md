# Docker命令5--容器生命周期管理命令

### docker create

+ 创建一个新的容器但不启动它

+ 语法

  ```bash
  docker create [OPTIONS] IMAG [COMMAND] [ARG...]
  ```

  ```bash
  Options:
        --add-host list                  Add a custom host-to-IP mapping (host:ip)
    -a, --attach list                    Attach to STDIN, STDOUT or STDERR
        --blkio-weight uint16            Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
        --blkio-weight-device list       Block IO weight (relative device weight) (default [])
        --cap-add list                   Add Linux capabilities
        --cap-drop list                  Drop Linux capabilities
        --cgroup-parent string           Optional parent cgroup for the container
        --cidfile string                 Write the container ID to the file
        --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
        --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
        --cpu-rt-period int              Limit CPU real-time period in microseconds
        --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
    -c, --cpu-shares int                 CPU shares (relative weight)
        --cpus decimal                   Number of CPUs
        --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
        --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
        --device list                    Add a host device to the container
        --device-cgroup-rule list        Add a rule to the cgroup allowed devices list
        --device-read-bps list           Limit read rate (bytes per second) from a device (default [])
        --device-read-iops list          Limit read rate (IO per second) from a device (default [])
        --device-write-bps list          Limit write rate (bytes per second) to a device (default [])
        --device-write-iops list         Limit write rate (IO per second) to a device (default [])
        --disable-content-trust          Skip image verification (default true)
        --dns list                       Set custom DNS servers
        --dns-option list                Set DNS options
        --dns-search list                Set custom DNS search domains
        --domainname string              Container NIS domain name
        --entrypoint string              Overwrite the default ENTRYPOINT of the image
    -e, --env list                       Set environment variables
        --env-file list                  Read in a file of environment variables
        --expose list                    Expose a port or a range of ports
        --gpus gpu-request               GPU devices to add to the container ('all' to pass all GPUs)
        --group-add list                 Add additional groups to join
        --health-cmd string              Command to run to check health
        --health-interval duration       Time between running the check (ms|s|m|h) (default 0s)
        --health-retries int             Consecutive failures needed to report unhealthy
        --health-start-period duration   Start period for the container to initialize before starting health-retries countdown
                                         (ms|s|m|h) (default 0s)
        --health-timeout duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)
        --help                           Print usage
    -h, --hostname string                Container host name
        --init                           Run an init inside the container that forwards signals and reaps processes
    -i, --interactive                    Keep STDIN open even if not attached
        --ip string                      IPv4 address (e.g., 172.30.100.104)
        --ip6 string                     IPv6 address (e.g., 2001:db8::33)
        --ipc string                     IPC mode to use
        --isolation string               Container isolation technology
        --kernel-memory bytes            Kernel memory limit
    -l, --label list                     Set meta data on a container
        --label-file list                Read in a line delimited file of labels
        --link list                      Add link to another container
        --link-local-ip list             Container IPv4/IPv6 link-local addresses
        --log-driver string              Logging driver for the container
        --log-opt list                   Log driver options
        --mac-address string             Container MAC address (e.g., 92:d0:c6:0a:29:33)
    -m, --memory bytes                   Memory limit
        --memory-reservation bytes       Memory soft limit
        --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable unlimited swap
        --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
        --mount mount                    Attach a filesystem mount to the container
        --name string                    Assign a name to the container
        --network network                Connect a container to a network
        --network-alias list             Add network-scoped alias for the container
        --no-healthcheck                 Disable any container-specified HEALTHCHECK
        --oom-kill-disable               Disable OOM Killer
        --oom-score-adj int              Tune host's OOM preferences (-1000 to 1000)
        --pid string                     PID namespace to use
        --pids-limit int                 Tune container pids limit (set -1 for unlimited)
        --platform string                Set platform if server is multi-platform capable
        --privileged                     Give extended privileges to this container
    -p, --publish list                   Publish a container's port(s) to the host
    -P, --publish-all                    Publish all exposed ports to random ports
        --read-only                      Mount the container's root filesystem as read only
        --restart string                 Restart policy to apply when a container exits (default "no")
        --rm                             Automatically remove the container when it exits
        --runtime string                 Runtime to use for this container
        --security-opt list              Security Options
        --shm-size bytes                 Size of /dev/shm
        --stop-signal string             Signal to stop a container (default "SIGTERM")
        --stop-timeout int               Timeout (in seconds) to stop a container
        --storage-opt list               Storage driver options for the container
        --sysctl map                     Sysctl options (default map[])
        --tmpfs list                     Mount a tmpfs directory
    -t, --tty                            Allocate a pseudo-TTY
        --ulimit ulimit                  Ulimit options (default [])
    -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
        --userns string                  User namespace to use
        --uts string                     UTS namespace to use
    -v, --volume list                    Bind mount a volume
        --volume-driver string           Optional volume driver for the container
        --volumes-from list              Mount volumes from the specified container(s)
    -w, --workdir string                 Working directory inside the container
  ```

---

### docker run

+ 创建一个新的容器并运行一个命令

+ 语法

  ```bash
  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
  ```

  + [OPTIONS]

    | 选项                               | 说明                                                         |
    | ---------------------------------- | ------------------------------------------------------------ |
    | -a stdin                           | 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项      |
    | -d                                 | 后台运行容器，并返回容器ID                                   |
    | -i                                 | 以交互模式运行容器，通常与 -t 同时使用                       |
    | -P                                 | 随机端口映射，容器内部端口**随机**映射到主机的端口           |
    | -p                                 | 指定端口映射，格式为：**主机(宿主)端口:容器端口**            |
    | -t                                 | 为容器重新分配一个伪输入终端，通常与 -i 同时使用             |
    | --name="nginx-lb"                  | 为容器指定一个名称                                           |
    | --dns 8.8.8.8                      | 指定容器使用的DNS服务器，默认和宿主一致                      |
    | --dns-search example.com           | 指定容器DNS搜索域名，默认和宿主一致                          |
    | -h "mars"                          | 指定容器的hostname                                           |
    | -e username="ritchie"              | 设置环境变量                                                 |
    | --env-file=[]                      | 从指定文件读入环境变量                                       |
    | --cpuset="0-2" or --cpuset="0,1,2" | 绑定容器到指定CPU运行                                        |
    | -m                                 | 设置容器使用内存最大值                                       |
    | --net="bridge"                     | 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型 |
    | --link=[]                          | 添加链接到另一个容器                                         |
    | --expose=[]                        | 开放一个端口或一组端口                                       |
    | --volume, -v                       | 绑定一个卷，**格式为：主机的本地目录：容器目录（本地目录的路径必须是绝对路径）** |
    | --restart                          | 设置容器重启策略，以决定在容器退出时Docker守护进程是否重启刚刚推出的容器<br>该选项通常只用于detached模式的容器<br>不能与--rm选项同时用。--restart选项适用于detached模式的容器，而--rm选项适用于foreground模式的容器。<br>no，默认策略，在容器退出时不重启容器<br>on-failure，在容器非正常退出时（退出状态非0），才会重启容器<br>on-failure:3，在容器非正常退出时才会重启容器，最多重启3次<br>always，在容器退出时总是重启容器<br>unless-stopped，在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器 |
    | --network network                  | 将容器连接到一个网络<br>--network=none<br>--network=host<br>--network=bridge   (default) |
    | --ip string                        | IPv4 address (e.g., 172.30.100.104)                          |
    
    

+ 实例1：使用docker镜像nginx:latest以后台模式启动一个容器,并将容器命名为mynginx

  ```bash
  docker run -d --name mynginx nginx:latest 
  ```

+ 实例2：使用镜像nginx:latest以后台模式启动一个容器,并将容器的80端口映射到主机随机端口

  ```bash
  docker run -d -P nginx:latest
  ```

+ 实例3：使用镜像 nginx:latest，以后台模式启动一个容器,将容器的 80 端口映射到主机的 80 端口,主机的目录 /data 映射到容器的 /data。

  ```bash
  docker run -d -p 80:80 -v /data:/data nginx:latest
  ```

+ 实例4：使用镜像toolsapi:v8，以交互和后台的模式启动容器，挂载主机的本地目录 /usr/ToolsAPIDir 目录到容器的/ToolsAPIDir1 目录，同时指定主机的5005端口映射到容器的5004端口，并且运行tools_api.py文件

  ```bash
  docker run  -v /usr/ToolsAPIDir:/ToolsAPIDir1 -d -p 5005:5004 -it toolsapi:v8 python3 tools_api.py
  ```

  + python3 tools_api.py 启动api.py文件，这样可以不需要再Dockfile中指定 CMD命令，或者覆盖Dockfile中的CMD命令
  + 当启动的py文件中有bug时，可以在主机中更新py文件，然后重新运行 run 命令即可。这样就将环境和代码分离，镜像就是运行环境，运行环境只要不改变，就不用重新生成镜像。
    否则如果将py文件打包到镜像中的话，任何对代码的修改都必须重新生成镜像。 

---

### docker start

+ 启动一个或多个已经被停止的容器

+ docker start会保留容器的第一次启动时的所有参数

+ 以后台方式启动

+ 语法

  ```bash
  docker start [OPTIONS] CONTAINER [CONTAINER...]
  ```

  + [OPTIONS]

    | 选项                    | 说明                                                |
    | ----------------------- | --------------------------------------------------- |
    | -a, --attach            | Attach STDOUT/STDERR and forward signals            |
    | --checkpoint string     | Restore from this checkpoint                        |
    | --checkpoint-dir string | Use a custom checkpoint storage directory           |
    | --detach-keys string    | Override the key sequence for detaching a container |
    | -i, --interactive       | Attach container's STDIN                            |

---

### docker restart

+ 重启容器

+ 作用就是依次执行docker stop和docker start

+ 语法

  ```bash
  docker restart [OPTIONS] CONTAINER [CONTAINER...]
  ```


---

### docker stop 

+ 停止一个运行中的容器

+ 向容器在docker host中对应的进程发送一个SIGTERM信号

+ 语法

  ```bash
  docker stop [OPTIONS] CONTAINER [CONTAINER...]
  ```

  + [OPTIONS]

    | 选项           | 说明                                                    |
    | -------------- | ------------------------------------------------------- |
    | -t, --time int | Seconds to wait for stop before killing it (default 10) |

  + CONTAINER

    容器 长ID或者短ID或者名字(docker ps 命令的NAMES值)

+ 实例1：停止运行中的容器ubuntu

  ```bash
  docker stop ubuntu
  ```

---

### docker kill

+ 快速停止一个运行中的容器

+ 向容器在docker host中对应的进程发送一个SIGKILL信号

+ 语法

  ```bash
  docker kill [OPTIONS] CONTAINER [CONTAINER...]
  ```

  + [OPTIONS]

    | 选项                | 说明                                                         |
    | ------------------- | ------------------------------------------------------------ |
    | -s, --signal string | 想容器发送一个信号   Signal to send to the container (default "KILL") |

---

### docker pause

+ 暂停容器中的所有进程

+ 处于暂停状态的容器不会占用CPU资源，直到通过docker unpause恢复运行

+ 语法

  ```bash
  docker pause [OPTIONS] CONTAINER [CONTAINER...]
  ```

---

### docker unpause

+ 恢复容器中的所有进程

+ 语法

  ```bash
  docker unpause [OPTIONS] CONTAINER [CONTAINER...]
  ```

---

### docker exec

+ 在运行的容器中执行命令

+ 在容器中打开新的终端，可以启动新的进程

+ 语法

  ```bash
  docker exec [OPTIONS] CONTAINER COMMAND [ARG]
  ```

  + [OPTIONS]

    | 选项                                 | 说明                                                         |
    | ------------------------------------ | ------------------------------------------------------------ |
    | -e, --env list                       | Set environment variables                                    |
    | -d，--detach<br>--detach-keys string | 分离模式，在后台运行   Detached mode: run command in the background<br>Override the key sequence for detaching a container |
    | -i, --interactive                    | 即使没有附加也保持STDIN打开   Keep STDIN open even if not attached |
    | --privileged                         | Give extended privileges to the command                      |
    | -t, --tty                            | 分配一个伪终端    Allocate a pseudo-TTY                      |
    | -u, --user string                    | Username or UID (format: <name                               |
    | -w, --workdir string                 | Working directory inside the container                       |

+ 最常用方式

  ```bash
  docker exec -it CONTAINER bash|sh
  ```

+ 实例1：

  ```bash
  root@ubuntu16:~# docker run -d ubuntu /bin/bash -c "while true; do sleep 1;echo I_am_in_container;done"
  7dbfe192e04399dfe89438ee8628e2b880b73fe54a9210f6a228df616b463ab9
  root@ubuntu16:~# docker ps
  CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
  7dbfe192e043        ubuntu              "/bin/bash -c 'while…"   5 seconds ago       Up 4 seconds                                 infallible_hermann
  548af276a749        registry            "/entrypoint.sh /etc…"   4 days ago          Up 6 hours          0.0.0.0:5000->5000/tcp   docker-registry
  root@ubuntu16:~# docker exec -it 7dbfe192e043 bash
  root@7dbfe192e043:/# ps -elf
  F S UID         PID   PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
  4 S root          1      0  0  80   0 -   995 do_wai 12:40 ?        00:00:00 /bin/bash -c while true; do sleep 1;echo I_am_in_contai
  4 S root         42      0  0  80   0 -  1028 do_wai 12:40 pts/0    00:00:00 bash
  0 S root        153      1  0  80   0 -   628 hrtime 12:42 ?        00:00:00 sleep 1
  0 R root        154     42  0  80   0 -  1473 -      12:42 pts/0    00:00:00 ps -elf
  ```

+ 实例2：在容器 mynginx 中以交互模式执行容器内 /root/runoob.sh 脚本

  ```bash
  runoob@runoob:~$ docker exec -it mynginx /bin/sh /root/runoob.sh
  http://www.runoob.com/
  ```

+ 实例3：在容器 mynginx 中开启一个交互模式的终端

  ```bash
  runoob@runoob:~$ docker exec -i -t  mynginx /bin/bash
  root@b1a0703e41e7:/#
  ```

---

### docker rm

+ 删除一个或多个容器

+ 语法

  ```bash
  docker rm [OPTIONS] CONTAINER [CONTAINER...]
  ```

  + [OPTIONS]

    | 选项        | 说明                                                         |
    | ----------- | ------------------------------------------------------------ |
    | -f, --force | 通过SIGKILL信号强制删除一个运行中的容器   Force the removal of a running container (uses SIGKILL) |
    | -l, --link  | 移除容器间的网络连接，而非容器本身   Remove the specified link |
    | -v          | 删除与容器关联的卷   Remove anonymous volumes associated with the container |

+ 实例1：删除所有已经停止的容器

  ```bash
  docker rm -v $(docker ps -aq -f status=exited)
  ```

+ 实例2：移除容器 nginx01 对容器 db01 的连接，连接名 db

  ```bash
  docker rm -l db
  ```

+ 实例3：强制删除容器 db01、db02

  ```bash
  docker -f db01 db02
  ```

  

