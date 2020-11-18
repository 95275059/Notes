# Docker安装1--安装流程(Ubuntu)

### 参考网址

https://blog.csdn.net/qq_40423339/article/details/87885086

https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/

### 更换镜像源

更换为清华大学镜像源

+ vim /etc/apt/sources.list

  ```bash
  deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
  deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
  deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
  deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
  ```

### 删掉docker(如果安装过)

```bash
sudo apt-get remove docker docker-engine docker.io
```

### 更新源

```bash
sudo apt-get update
```

### 安装依赖

```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

### 信任Docker的GPG公钥

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

### 添加软件仓库

+ 对于 amd64 架构的计算机

  ```bash
  sudo add-apt-repository \
     "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian \
     $(lsb_release -cs) \
     stable"
  ```

+ 如果是树莓派或其它ARM架构计算机

  ```bash
  echo "deb [arch=armhf] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian \
       $(lsb_release -cs) stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list
  ```

### 安装

```bash
sudo apt-get update
sudo apt-get install docker-ce
```





