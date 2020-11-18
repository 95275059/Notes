# LinuxTips56--UbuntuCentOS更换镜像源

### Ubuntu

+ 参考：https://blog.csdn.net/sss_369/article/details/101715315

+ 16.04

  + 备份原始源文件

    ```bash
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
    ```

  + 修改源文件source.list

    + 更改文件权限

      ```bash
      sudo chmod 777 /etc/apt/sources.list
      ```

    + 更换内容

      ```bash
      sudo gedit /etc/apt/sources.list
      ```

      + 阿里源

        ```bash
        deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
        ```

      + 清华源

        ```bash
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
        ```

  + 更新源

    ```bash
    sudo apt-get update
    ```

+ 18.04
  + 备份原始源文件

    ```bash
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
    ```

  + 修改源文件source.list

    + 更改文件权限(大可不必)

      ```bash
      sudo chmod 777 /etc/apt/sources.list
      ```

    + 更换内容

      ```bash
      sudo vi /etc/apt/sources.list
      ```

      + 阿里源

        ```bash
        deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
        
        deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
        
        deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
        ```

      + 清华源

        ```bash
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
        
        deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
        
        deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
        ```
    
      + 163源
    
        ```bash
        deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
        
      deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
        
        deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
        
        deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
        
        deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
        
        deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
        
        deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
        
        deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
        
        deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
        ```
  
  + 更新源
  
    ```bash
    sudo apt-get update
    ```

---

### CentOS

+ 备份源文件

  ```bash
  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
  ```

+ 下载更改源

  + CentOS 5

    ```bash
    wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo
    ```

  + CentOS 6

    ```bash
    wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
    ```

  + CentOS 7

    ```bash
    wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
    ```

  + 注意：如果wget命令不生效，说明还没有安装wget工具，输入yum -y install wget 回车进行安装，或者使用

    ```bash
    curl -O http://mirrors.aliyun.com/repo/Centos-7.repo
    ```

  + 清空yum缓存并生成cache文件

    ```bash
    yum clean all
    yum makecache
    ```

  + 尝试更新系统(大可不必吧。。)

    ```bash
    yum -y update
    ```

    

