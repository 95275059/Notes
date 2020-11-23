# Docker命令4--本地镜像管理命令

### docker images

+ 列出镜像

+ 语法

  ```bash
  docker images [OPTIONS] [REPOSITORY[:TAG]]
  ```

  + [OPTIONS]

    | 选项                                                         | 说明                                                         |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | -a, --all<br>     --digests                                  | Show all images (default hides intermediate images)<br>Show digests |
    | -f, --filter filter <br/>     --format string<br/>     --no-trunc | Filter output based on conditions provided<br/>Pretty-print containers using a Go template<br>Don't truncate output |
    | -q, --quiet                                                  | Only display numeric IDs                                     |
+ 实例1：查看本地镜像列表

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker images
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  httpd               latest              3dd970e6b110        5 weeks ago         138MB
  ```
  
+ 实例2：列出本地镜像中REPOSITORY为httpd的镜像列表

  ```bash
  cxy@ubuntu16:/etc/systemd/system/multi-user.target.wants$ sudo docker images httpd
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  httpd               latest              3dd970e6b110        5 weeks ago         138MB
  ```

---

### docker build

+ 使用Dockerfile创建镜像

+ 语法

  ```bash
  docker build [OPTIONS] PATH | URL | -
  ```

  + [OPTIONS]

    | 选项                    | 说明                                                         |
    | ----------------------- | ------------------------------------------------------------ |
    | --build-arg=[]          | 设置镜像创建时的变量                                         |
    | --cpu-shares            | 设置cpu使用权重                                              |
    | --cpu-period            | 限制CPU CFS周期                                              |
    | --cpu-quota             | 限制CPU CFS配额                                              |
    | --cpuset-cpus           | 指定使用的CPU id                                             |
    | --cpuset-mems           | 指定使用的内存 id                                            |
    | --disable-content-trust | 忽略校验，默认开启                                           |
    | -f                      | 指定要使用的Dockerfile路径                                   |
    | -force-rm               | 设置镜像过程中删除容器                                       |
    | -isolation              | 使用容器隔离技术                                             |
    | --label=[]              | 设置镜像使用的元数据                                         |
    | -m                      | 设置内存最大值                                               |
    | --memory-swap           | 设置swap的最大值为内存+swap,"-1"表示不限swap                 |
    | --no-cache              | 创建镜像的过程中不使用缓存                                   |
    | --pull                  | 尝试去更新镜像的新版本                                       |
    | --quiet,-q              | 安静模式，成功后只输出镜像ID                                 |
    | --rm                    | 设置镜像成功后删除中间容器                                   |
    | --shm-size              | 设置/dev/shm的大小，默认值是64M                              |
    | --ulimit                | ulimit配置                                                   |
    | --squash                | 将Dockerfile中所有的操作压缩为一层                           |
    | --tag, -t               | 镜像的名字及标签，通常name:tag或者name格式；可以在一次构建汇总为一个镜像设置多个标签 |
    | --network               | 默认default。在构建期间设置RUN指令的网络模式                 |

  + PATH

    指明build context的路径

    build context为镜像构建提供所需要的文件或目录

    Docker会将build context中所有文件发送给Docker daemon

    Docker默认会从build context中查找Dockerfile文件，也可以通过-f指定Dockerfile的位置

    Dockerfile中的ADD,COPY等命令可以将build context中的文件添加到镜像

    **注意不要把多余的文件放入build context，特别不要把/ , /usr, 作为build context，否则构建过程会相当缓慢甚至失败**

+ 实例1：使用当前目录的 Dockerfile 创建镜像，标签为 ubuntu-with-vim-dockerfile:v1

  ```bash
  docker build -t ubuntu-with-vim-dockerfile:v1 .
  ```

+ 实例2：使用URL github.com/creack/docker-firefox 的 Dockerfile 创建镜像

  ```bash
  docker build github.com/creack/docker-firefox 
  ```

+ 实例3：也可以通过 -f Dockerfile 文件的位置

  ```bash
  docker build -f /path/to/a/Dockerfile .
  ```

+ 实例4：在 Docker 守护进程执行 Dockerfile 中的指令前，首先会对 Dockerfile 进行语法检查，有语法错误时会返回

  ```bash
  $ docker build -t test/myapp .
  Sending build context to Docker daemon 2.048 kB
  Error response from daemon: Unknown instruction: RUNCMD
  ```

---

### docker history

+ 查看指定镜像的创建历史

+ 语法

  ```bash
  docker history [OPTIONS] IMAGE
  ```

  + [OPTIONS]

    | 选项       | 说明                                       |
    | ---------- | ------------------------------------------ |
    | -H         | 以可读的格式打印镜像大小和日期，默认为true |
    | --no-trunc | 显示完整的提交记录                         |
    | -q         | 仅列出提交记录ID                           |

+ 实例1：查看本地镜像ubuntu-with-vim-dockerfile的创建历史

  ```bash
  root@ubuntu16:~# docker history ubuntu-with-vim-dockerfile:latest 
  IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
  801840732350        19 hours ago        /bin/sh -c apt-get install -y vim               68.2MB              
  80a0540d7c67        19 hours ago        /bin/sh -c apt-get update                       26.1MB              
  2488a8b485f6        19 hours ago        /bin/sh -c apt-get clean                        0B                  
  c62c71526782        19 hours ago        /bin/sh -c sed -i s@/archive.ubuntu.com/@/mi…   2.74kB              
  d70eaf7277ea        3 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
  <missing>           3 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
  <missing>           3 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B                  
  <missing>           3 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B                
  <missing>           3 weeks ago         /bin/sh -c #(nop) ADD file:435d9776fdd3a1834…   72.9MB              
  ```

  + missing：表示无法获取IMAGE ID，通常从Docker Hub下载的镜像会有这个问题

---

### docker rmi

+ 删除本地一个或多个镜像

+ rmi只能删除host上的镜像，不会删除registry的镜像

+ 如果一个镜像对应了多个tag，只有当最后一个tag被删除时，镜像才被真正删除

+ 语法

  ```bash
  docker rmi [OPTIONS] IMAGE [IMAGE...]
  ```

  + [OPTIONS]

    | 选项       | 说明                             |
    | ---------- | -------------------------------- |
    | -f         | 强制删除                         |
    | --no-prune | 不移除该镜像的过程镜像，默认移除 |

+ 实例：强制删除本地镜像httpd

  ```bash
  root@ubuntu16:~/Dockerfile/ubuntu-with-vim-dockerfile-2# docker rmi -f httpd
  Untagged: httpd:latest
  Untagged: httpd@sha256:b82fb56847fcbcca9f8f162a3232acb4a302af96b1b2af1c4c3ac45ef0c9b968
  Deleted: sha256:3dd970e6b110c8cbcec63e05a91e3cefd23c76a780fcb78c33979153f044b2d4
  ```

---

### docker prune

+ 删除不再使用的docker镜像

+ 删除所有未被 tag 标记和未被容器使用的镜像

  ```bash
  docker image prune
  ```

+ 删除所有未被容器使用的镜像

  ```bash
  docker image prune -a
  ```

+ 删除所有停止运行的容器

  ```bash
  docker container prune
  ```

+ 删除所有未被挂载的卷

  ```bash
  docker volume prune
  ```

+ 删除所有网络

  ```bash
  docker network prunei
  ```

+ 删除docker所有资源

  ```bash
  docker system prune
  ```

  ```bash
  This will remove:
          - all stopped containers
          - all networks not used by at least one container
          - all dangling images
          - all dangling build cache
  ```

  删除停止的容器、删除所有未被容器使用的网络、删除所有none的镜像

---

### docker tag

+ 标记本地镜像，将其归入某一仓库

+ 语法

  ```bash
  docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
  ```

+ 实例：将本地镜像ubuntu-with-vim-dockerfile标记为 ubuntu-with-vim:v1

  ```bash
  root@ubuntu16:~/Dockerfile/my-image# docker images
  REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
  my-image                       latest              07c569d6c316        4 hours ago         1.23MB
  ubuntu-with-vim-dockerfile-2   latest              68a54eeae724        8 hours ago         167MB
  httpd                          latest              0a30f4c29d25        27 hours ago        138MB
  ubuntu-with-vim-dockerfile     latest              801840732350        27 hours ago        167MB
  debian                         latest              ef05c61d5112        38 hours ago        114MB
  ubuntu                         latest              d70eaf7277ea        3 weeks ago         72.9MB
  busybox                        latest              f0b02e9d092d        5 weeks ago         1.23MB
  centos                         latest              0d120b6ccaa8        3 months ago        215MB
  hello-world                    latest              bf756fb1ae65        10 months ago       13.3kB
  root@ubuntu16:~/Dockerfile/my-image# docker tag ubuntu-with-vim-dockerfile:latest ubuntu-with-vim:v1
  root@ubuntu16:~/Dockerfile/my-image# docker images
  REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
  my-image                       latest              07c569d6c316        4 hours ago         1.23MB
  ubuntu-with-vim-dockerfile-2   latest              68a54eeae724        8 hours ago         167MB
  httpd                          latest              0a30f4c29d25        27 hours ago        138MB
  ubuntu-with-vim-dockerfile     latest              801840732350        27 hours ago        167MB
  ubuntu-with-vim                v1                  801840732350        27 hours ago        167MB
  debian                         latest              ef05c61d5112        38 hours ago        114MB
  ubuntu                         latest              d70eaf7277ea        3 weeks ago         72.9MB
  busybox                        latest              f0b02e9d092d        5 weeks ago         1.23MB
  centos                         latest              0d120b6ccaa8        3 months ago        215MB
  hello-world                    latest              bf756fb1ae65        10 months ago       13.3kB
  root@ubuntu16:~/Dockerfile/my-image# docker tag ubuntu-with-vim-dockerfile-2:latest ubuntu-with-vim:v2
  root@ubuntu16:~/Dockerfile/my-image# docker images
  REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
  my-image                       latest              07c569d6c316        4 hours ago         1.23MB
  ubuntu-with-vim-dockerfile-2   latest              68a54eeae724        8 hours ago         167MB
  ubuntu-with-vim                v2                  68a54eeae724        8 hours ago         167MB
  httpd                          latest              0a30f4c29d25        27 hours ago        138MB
  ubuntu-with-vim-dockerfile     latest              801840732350        28 hours ago        167MB
  ubuntu-with-vim                v1                  801840732350        28 hours ago        167MB
  debian                         latest              ef05c61d5112        38 hours ago        114MB
  ubuntu                         latest              d70eaf7277ea        3 weeks ago         72.9MB
  busybox                        latest              f0b02e9d092d        5 weeks ago         1.23MB
  centos                         latest              0d120b6ccaa8        3 months ago        215MB
  hello-world                    latest              bf756fb1ae65        10 months ago       13.3kB
  root@ubuntu16:~/Dockerfile/my-image# docker tag ubuntu-with-vim-dockerfile-2 ubuntu-with-vim:latest
  root@ubuntu16:~/Dockerfile/my-image# docker images
  REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
  my-image                       latest              07c569d6c316        4 hours ago         1.23MB
  ubuntu-with-vim-dockerfile-2   latest              68a54eeae724        8 hours ago         167MB
  ubuntu-with-vim                latest              68a54eeae724        8 hours ago         167MB
  ubuntu-with-vim                v2                  68a54eeae724        8 hours ago         167MB
  httpd                          latest              0a30f4c29d25        27 hours ago        138MB
  ubuntu-with-vim-dockerfile     latest              801840732350        28 hours ago        167MB
  ubuntu-with-vim                v1                  801840732350        28 hours ago        167MB
  debian                         latest              ef05c61d5112        38 hours ago        114MB
  ubuntu                         latest              d70eaf7277ea        3 weeks ago         72.9MB
  busybox                        latest              f0b02e9d092d        5 weeks ago         1.23MB
  centos                         latest              0d120b6ccaa8        3 months ago        215MB
  hello-world                    latest              bf756fb1ae65        10 months ago       13.3kB
  ```

+ 实例2：将镜像ubuntu:15.10标记为 runoob/ubuntu:v3 镜像

  ```bash
  root@runoob:~# docker tag ubuntu:15.10 runoob/ubuntu:v3
  root@runoob:~# docker images   runoob/ubuntu:v3
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  runoob/ubuntu       v3                  4e3b13c8a266        3 months ago        136.3 MB
  ```

---



