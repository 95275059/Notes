# Docker命令3--镜像管理命令

### docker pull

+ 从镜像仓库中拉取或者更新镜像

+ 语法

  ```bash
  docker pull [OPTIONS] NAME[:TAG|@DIGEST]
  ```

  + [OPTIONS]

    | 选项                    | 说明                     |
    | ----------------------- | ------------------------ |
    | -a                      | 拉取所有tagged镜像       |
    | --disable-content-trust | 忽略镜像的校验，默认开启 |

  + NAME

    [registry-host] : [port]/[username]/xxx

    只有DockerHub上的镜像可以省略[registry-host] : [port]

+ 实例1：从docker hub下载java最新版镜像

  ```bash
  docker pull java
  ```

+ 实例2：从docker hub下载REPOSITORY为java的所有镜像

  ```bash
  dockeer pull -a java
  ```

+ 实例3：从私有仓库拉取镜像

  ```bash
  root@ubuntu16:~# docker pull 192.168.200.233:5000/95270422/ubuntu-with-vim:v2
  v2: Pulling from 95270422/ubuntu-with-vim
  Digest: sha256:efeeec9815ae807a93f9a5d3879691836cb909edea93ae9a1984031d547262bd
  Status: Downloaded newer image for 192.168.200.233:5000/95270422/ubuntu-with-vim:v2
  192.168.200.233:5000/95270422/ubuntu-with-vim:v2
  ```

---

### docker login/logout

+ docker login : 登录到一个Docker 镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub

+ docker logout : 登出一个Docker镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub

+ 语法

  + docker login

    ```bash
    docker login [OPTIONS] [SERVER]
    ```

  + docker logout

    ```bash
    docker logout [OPTIONS] [SERVER]
    ```

  + [OPTIONS]

    | 选项 | 说明         |
    | ---- | ------------ |
    | -u   | 登录的用户名 |
    | -p   | 登录的密码   |

+ 实例1：登陆到Docker Hub

  ```bash
  docker login -u 用户名 -p 密码
  ```

+ 实例2：登出Docker Hub

  ```bash
  docker logout
  ```

---

### docker push

+ 将本地的镜像上传到镜像仓库，要先登录到镜像仓库

+ 语法

  ```bash
  docker push [OPTIONS] NAME[:TAG]
  ```

  + [OPTIONS]

    | 选项                    | 说明                     |
    | ----------------------- | ------------------------ |
    | --disable-content-trust | 忽略镜像的校验，默认开启 |

+ 实例1：将本地镜像95270422/ubuntu-with-vim:v2上传到镜像仓库

  ```bash
  root@ubuntu16:~/Dockerfile/my-image# docker push 95270422/ubuntu-with-vim:v2
  ```

  + 上传速度太慢
  
+ 实例2：将本地镜像ubuntu-with-vim:v2上传到私有镜像仓库（192.168.200.233:5000）

  ```bash
  root@ubuntu16:~/Dockerfile/my-image# docker tag ubuntu-with-vim:v2 192.168.200.233:5000/95270422/ubuntu-with-vim:v2
  root@ubuntu16:~/Dockerfile/my-image# docker images 
  REPOSITORY                                      TAG                 IMAGE ID            CREATED             SIZE
  my-image                                        latest              07c569d6c316        5 hours ago         1.23MB
  95270422/ubuntu-with-vim                        v2                  68a54eeae724        9 hours ago         167MB
  ubuntu-with-vim-dockerfile-2                    latest              68a54eeae724        9 hours ago         167MB
  ubuntu-with-vim                                 latest              68a54eeae724        9 hours ago         167MB
  ubuntu-with-vim                                 v2                  68a54eeae724        9 hours ago         167MB
  192.168.200.233:5000/95270422/ubuntu-with-vim   v2                  68a54eeae724        9 hours ago         167MB
  httpd                                           latest              0a30f4c29d25        28 hours ago        138MB
  ubuntu-with-vim-dockerfile                      latest              801840732350        28 hours ago        167MB
  ubuntu-with-vim                                 v1                  801840732350        28 hours ago        167MB
  debian                                          latest              ef05c61d5112        39 hours ago        114MB
  ubuntu                                          latest              d70eaf7277ea        3 weeks ago         72.9MB
  busybox                                         latest              f0b02e9d092d        5 weeks ago         1.23MB
  centos                                          latest              0d120b6ccaa8        3 months ago        215MB
  registry                                        2                   2d4f4b5309b1        5 months ago        26.2MB
  hello-world                                     latest              bf756fb1ae65        10 months ago       13.3kB
  root@ubuntu16:~/Dockerfile/my-image# docker ps
  CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
  67d5908d8530        registry:2          "/entrypoint.sh /etc…"   7 minutes ago       Up 7 minutes        0.0.0.0:5000->5000/tcp   elegant_pare
  
  ```

  

