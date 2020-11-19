# DockerTips3--在本地上传私有镜像仓库时报错

### 报错：http: server gave HTTP response to HTTPS client

```bash
root@ubuntu16:~/Dockerfile/my-image# docker push 192.168.200.233:5000/95270422/ubuntu-with-vim:v2 
The push refers to repository [192.168.200.233:5000/95270422/ubuntu-with-vim]
Get https://192.168.200.233:5000/v2/: http: server gave HTTP response to HTTPS client
```

+ **原因**

  docker registry未采用https服务，而客户端docker使用https请求push所致

  **Docker自从1.3.X之后docker registry交互默认使用的是HTTPS，但是搭建私有镜像默认使用的是HTTP服务，所以与私有镜像仓库交互时出现以上错误。**

  ```bash
  root@ubuntu16:~/Dockerfile/my-image# docker -v
  Docker version 19.03.13, build 4484c46d9d
  ```

+ **解决方案**

  在docker server启动的时候，增加启动参数，默认使用HTTP访问

  + 在**docker客户端**进行修改，**让docker客户端以不安全的http请求访问docker registry**

    ```bash
     vim /etc/docker/daemon.json
    ```

    ```bash
    // 单个私服的写法
    {
        "registry-mirrors": ["http://f1361db2.m.daocloud.io"],
        "insecure-registries": ["registry的IP地址:端口号"]
    }
    // 多个私服的写法
    {
        "registry-mirrors": ["http://f1361db2.m.daocloud.io"],
        "insecure-registries": ["registry1的IP地址:端口号","registry2的IP地址:端口号"]
    }
    ```

    ```bash
    {
      "registry-mirrors": ["https://b7a3l6tj.mirror.aliyuncs.com"],
      "insecure-registries": ["192.168.200.233:5000"]
    }
    ```

  + 使配置生效

    ```bash
    systemctl daemon-reload
    ```

  + 重启docker

    ```bash
    systemctl restart docker
    ```

  

  