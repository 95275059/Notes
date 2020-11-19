# Docker命令5--容器生命周期管理命令

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

