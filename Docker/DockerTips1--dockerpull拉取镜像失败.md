# DockerTips1--dockerpull拉取镜像失败

### 拉取镜像过程速度慢或者不成功

+ 参考网址

  https://blog.csdn.net/qq_37823605/article/details/90666773

+ 原因

  使用的是国外镜像hub，下载速度慢

+ 解决方案：使用阿里云加速器，改用国内镜像

  https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors

  + 针对Docker客户端版本大于 1.10.0 的用户

  + 您可以通过修改daemon配置文件/etc/docker/daemon.json来使用加速器

  + ```bash
    sudo mkdir -p /etc/docker
    sudo tee /etc/docker/daemon.json <<-'EOF'
    {
      "registry-mirrors": ["https://b7a3l6tj.mirror.aliyuncs.com"]
    }
    EOF
    ```

  + ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

    

