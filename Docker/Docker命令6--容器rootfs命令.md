# Docker命令6--容器rootfs命令

### docker commit

+ 从容器常见一个新的镜像

+ 语法

  ```bash
  docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
  ```

  + [OPTIONS]

    | 选项 | 说明                                                         |
    | ---- | ------------------------------------------------------------ |
    | -a   | 提交的镜像作者(e.g., "John Hannibal Smith <hannibal@a-team.com>") |
    | -c   | 使用Dockerfile指令来创建镜像                                 |
    | -m   | 提交时的说明文字                                             |
    | -p   | 在commit时，将容器暂停                                       |

+ 实例1：将容器silly_goldberg容器保存为镜像ubuntu-with-vi

  ```bash
  docker commit silly_goldberg ubuntu-with-vi
  ```

  + silly_goldberg：容器运行时被随机分配的名字，对应docker ps命令NAMES的值

+ 实例2：将容器a404c6c174a2 保存为新的镜像,并添加提交人信息和说明信息

  ```bash
  docker commit -a "runoob.com" -m "my apache" a404c6c174a2  mymysql:v1 
  ```

  + a404c6c174a2：容器运行时的容器ID，对应docker ps命令CONTAINER ID的值

---

