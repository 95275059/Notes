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