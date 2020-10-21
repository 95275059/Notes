# Openstack笔记5--brctl命令

### 安装

+ CentOS

  ```bash
  yum install bridge-utils
  ```

+ Ubuntu

  ```bash
  apt-get install bridge-utils
  ```

### 命令

+ 查询网桥信息

  + 显示所有网桥信息

    ```bash
    brctl show
    ```

  + 显示某个网桥信息

    ```bash
    brctl show <bridge_name>
    ```

+ 

