# Docker命令1--服务管理

### docker服务器管理

```bash
systemctl status docker.service
```

```bash
systemctl restart docker.service
```

```bash
systemctl stop docker.service
```

```bash
systemctl disable/enable docker.service
```

### 重启docker服务器docker daemon

```bash
systemctl daemon-reload
systemctl restart docker.service
```



