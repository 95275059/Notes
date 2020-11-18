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

+ 实例1：从docker hub下载java最新版镜像

  ```bash
  docker pull java
  ```

+ 实例2：从docker hub下载REPOSITORY为java的所有镜像

  ```bash
  dockeer pull -a java
  ```


