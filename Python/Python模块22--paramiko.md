# Python模块22--paramiko

## 简介

+ paramiko是一个基于SSH用于连接远程服务器并执行相关操作（SSHClient和SFTPClinet,即一个是远程连接，一个是上传下载服务）

+ 使用该模块可以对远程服务器进行命令或文件操作
+ 远程连接方案
  + 基于用户名密码连接
  + 基于公钥秘钥连接

## 安装

```python
yum install pycrypto
yum install paramiko
```

## 使用

### SSHClient

#### 基于用户名密码连接

+ 只用SSHClient

  ```python
  import paramiko
  
  # 创建SSH对象
  ssh = paramiko.SSHClient()
  # 允许连接不在know_hosts文件中的主机
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  # 连接服务器
  ssh.connect(hostname='192.168.1.111', port=22, username='root', password='wanganwork@B416')
  # 执行命令
  stdin, stdout, stderr = ssh.exec_command('ls')
  # 获取命令结果
  result = stdout.read()
  print(result)
  print(result.split())
  # 关闭连接
  ssh.close()
  ```

+ 自己创建一个transport

  ```python
  import paramiko
  
  transport = paramiko.Transport(('192.168.1.111', 22))
  transport.connect(username='root', password='wanganwork@B416')
  ssh = paramiko.SSHClient()
  ssh._transport = transport
  stdin, stdout, stderr = ssh.exec_command('ls')
  result = stdout.read()
  print(result)
  print(result.split())
  transport.close()
  ```

#### 基于公钥秘钥连接

+ 只用SSHClient

  ```python
  import paramiko
  
  private_key = paramiko.RSAKey.from_private_key_file('C:/Users/CXY/.ssh/id_rsa')
  # 创建SSH对象
  ssh = paramiko.SSHClient()
  # 允许连接不在know_hosts文件中的主机
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  # 连接服务器
  ssh.connect(hostname='192.168.1.111', port=22, username='root', key=private_key)
  # 执行命令
  stdin, stdout, stderr = ssh.exec_command('ls')
  # 获取命令结果
  result = stdout.read()
  print(result)
  print(result.split())
  # 关闭连接
  ssh.close()
  ```

  没成功，没时间

+ 自己创建一个transport

  ````python
  import paramiko
    
  private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
  transport = paramiko.Transport(('192.168.1.111', 22))
  transport.connect(username='root', pkey=private_key)
  ssh = paramiko.SSHClient()
  ssh._transport = transport
  stdin, stdout, stderr = ssh.exec_command('df')
  result = stdout.read()
  print(result)
  print(result.split())
  transport.close()
  ````

  没测试，没时间

### SFTPClient

+ 基于用户名密码上传下载

  ```python
  import paramiko
  
  transport = paramiko.Transport(('192.168.1.111', 22))
  transport.connect(username='root', password='wanganwork@B416')
  
  sftp = paramiko.SFTPClient.from_transport(transport)
  # 将test.json 上传至服务器 /root/cxy/test.json
  sftp.put('test.json', '/root/cxy/test.json')
  # 将/root/admin-openrc 下载到本地 admin-openrc
  sftp.get('/root/admin-openrc', 'admin-openrc')
  transport.close()
  ```

+ 基于公钥秘钥上传下载

  ```python
  import paramiko
  
  private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
  
  transport = paramiko.Transport(('hostname', 22))
  transport.connect(username='GSuser', pkey=private_key )
  
  sftp = paramiko.SFTPClient.from_transport(transport)
  # 将location.py 上传至服务器 /tmp/test.py
  sftp.put('/tmp/location.py', '/tmp/test.py')
  # 将remove_path 下载到本地 local_path
  sftp.get('remove_path', 'local_path')
  
  transport.close()
  ```

  没测试，没时间

## demo

```python
class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接
 
    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport
 
    #下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)
 
    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)
 
    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print data.strip()   #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print err.strip()    #输出错误结果
            return err
 
    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()
```





