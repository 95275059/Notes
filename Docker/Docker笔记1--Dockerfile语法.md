# Docker笔记1--Dockerfile语法

```bash
#my dockerfile
FROM busybox
MAINTAINER "cxy 9527"
WORKDIR /testdir
RUN touch tmpfile1
COPY ["tmpfile2", "."]
ADD ["bunch.tar.gz", "."]
ENV WELCOME "You are in my container, welcome!"
```

+ Dockerfile支持以“#”开头的注释

+ 实操

  + build context : /root/Dockerfile/my-image

    ```bash
    root@ubuntu16:~/Dockerfile/my-image# ls
    bunch  bunch.tar.gz  Dockerfile  tmpfile2
    ```

    ```bash
    root@ubuntu16:~/Dockerfile/my-image# cat tmpfile2 
    tmpfile2 test cxy
    ```

    ```bash
    root@ubuntu16:~/Dockerfile/my-image# tar -xzvf bunch.tar.gz bunch
    bunch
    root@ubuntu16:~/Dockerfile/my-image# ls
    bunch  bunch.tar.gz  Dockerfile  tmpfile2
    root@ubuntu16:~/Dockerfile/my-image# cat bunch
    bunch.tar.gz test cxy
    ```

  + ```bash
    root@ubuntu16:~/Dockerfile/my-image# rm bunch
    ```

  + ```bash
    root@ubuntu16:~/Dockerfile/my-image# ls
    bunch  bunch.tar.gz  Dockerfile  tmpfile2
    ```

  + ```bash
    root@ubuntu16:~/Dockerfile/my-image# docker build -t my-image .
    Sending build context to Docker daemon  4.096kB
    Step 1/7 : FROM busybox
    latest: Pulling from library/busybox
    9758c28807f2: Pull complete 
    Digest: sha256:a9286defaba7b3a519d585ba0e37d0b2cbee74ebfe590960b0b1d6a5e97d1e1d
    Status: Downloaded newer image for busybox:latest
     ---> f0b02e9d092d
    Step 2/7 : MAINTAINER "cxy 9527"
     ---> Running in e9ca51f9e307
    Removing intermediate container e9ca51f9e307
     ---> 6133aa0ee743
    Step 3/7 : WORKDIR /testdir
     ---> Running in a592c4c995a8
    Removing intermediate container a592c4c995a8
     ---> f6e3a0ea6d4f
    Step 4/7 : RUN touch tmpfile1
     ---> Running in 260461751c9a
    Removing intermediate container 260461751c9a
     ---> 41cffa7167ea
    Step 5/7 : COPY ["tmpfile2", "."]
     ---> 34bd70689833
    Step 6/7 : ADD ["bunch.tar.gz", "."]
     ---> 84df37800605
    Step 7/7 : ENV WELCOME "You are in my container, welcome!"
     ---> Running in e29586b8982f
    Removing intermediate container e29586b8982f
     ---> 07c569d6c316
    Successfully built 07c569d6c316
    Successfully tagged my-image:latest
    ```

  + ```bash
    root@ubuntu16:~/Dockerfile/my-image# docker images
    REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
    my-image                       latest              07c569d6c316        4 minutes ago       1.23MB
    ubuntu-with-vim-dockerfile-2   latest              68a54eeae724        4 hours ago         167MB
    httpd                          latest              0a30f4c29d25        23 hours ago        138MB
    ubuntu-with-vim-dockerfile     latest              801840732350        23 hours ago        167MB
    debian                         latest              ef05c61d5112        34 hours ago        114MB
    ubuntu                         latest              d70eaf7277ea        3 weeks ago         72.9MB
    busybox                        latest              f0b02e9d092d        5 weeks ago         1.23MB
    centos                         latest              0d120b6ccaa8        3 months ago        215MB
    hello-world                    latest              bf756fb1ae65        10 months ago       13.3kB
    ```

  + ```bash
    root@ubuntu16:~/Dockerfile/my-image# docker run -it my-image
    /testdir # ls
    bunch     tmpfile1  tmpfile2
    /testdir # cat bunch 
    bunch.tar.gz test cxy
    /testdir # cat tmpfile2
    tmpfile2 test cxy
    /testdir # cat tmpfile1
    /testdir # echo $WELCOME
    You are in my container, welcome!
    ```

---

### FROM

+ 指定base镜像

+ 从零开始构建

  ```bash
  FROM scratch
  ```

+ 基于其他镜像

  ```bash
  FROM ubuntu
  ```

  后跟镜像的REPOSITORY名

---

### MAINTAINER

设置镜像的作者，可以是任意字符串

---

### RUN

在容器中运行指定的指令

---

### CMD

容器启动时运行指定的命令

Dockerfile中可以有多个CMD命令，但是只有最后一个生效

CMD可以被docker run之后的参数替换

---

### COPY

将文件从build context复制到镜像

COPY支持两种形式

+ ```bash
  COPY src dest
  ```

+ ```bash
  COPY ["src", "dest"]
  ```

  注意：src只能指定build context中的文件或目录

---

### ADD

与COPY类似，从build context复制文件到镜像

不同的是，如果src是归档文件（tar、zip、tgz、xz等），文件会被自动解压到dest

---

### ENV

设置环境变量，环境变量可被后面的指令使用

+ 例如

  ```bash
  ENV MY_VERSION 1.3
  RUN apt-get install -y mypackage=$MY_VERSION
  ```

---

### EXPOSE

指定容器中的进程会监听某个端口，Docker可以将该端口暴露出来

---

### VOLUME

将文件或目录声明为volume

---

### WORKDIR

为后面的RUN,CMD,ENTRYPOINT,ADD或COPY指令设置镜像中的当前工作目录

如果WORKDIR不存在，Docker会自动创建

---

### ENTRYPOINT

容器启动时运行指定的命令

Dockerfile中可以有多个ENTRYPOINT命令，但是只有最后一个生效

CMD或docker run之后的参数会被当做参数传递给ENTRYPOINT

---









